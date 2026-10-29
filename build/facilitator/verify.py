"""FACILITATOR ONLY. Static fixture checks; no models, tools, or network calls."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from collections import Counter
from statistics import median
import csv
import io
import json
import re
import unicodedata

BUILD=Path(__file__).resolve().parents[1]
CFG=json.loads((BUILD/'case_config.json').read_text())
TZ=ZoneInfo('Europe/Berlin')
ENV={}
for line in (BUILD/'facilitator/secrets.env').read_text().splitlines():
    if line and not line.startswith('#'):
        k,v=line.split('=',1);ENV[k]=v
RULES=json.loads((BUILD/'tests/restricted_strings.json').read_text())['rules']
ERRORS=[]
ALLOWED=[]
COUNTERS=Counter()

def error(check,path,detail):
    ERRORS.append(dict(check=check,path=str(path),detail=detail))

def normal(text):
    return unicodedata.normalize('NFKC',text).replace('’',"'").replace('“','"').replace('”','"').casefold()

def value(rule):
    if 'literal' in rule:return rule['literal']
    source=rule['value_from']
    if 'environment' in source:return ENV[source['environment']]
    if 'config' in source:
        result=CFG
        for key in source['config'].split('.'):result=result[key]
        return result
    first,last=CFG['people']['culprit'].split()[0].lower(),CFG['people']['culprit'].split()[-1].lower()
    return {'buyer_surname':CFG['people']['buyer'].split()[-1],
            'operator_name':first[0]+last,'academy_login':first+'.'+last,
            'personal_host':last.upper()+'-MBP'}[source['derive']]

def check_restricted(path,text,kind,rid=None):
    for rule in RULES:
        needle=value(rule)
        if normal(needle) not in normal(text):continue
        if kind=='record':allowed=rid in rule.get('allowed_record_ids',[])
        elif kind=='revision':allowed=rid in rule.get('allowed_revision_ids',[])
        elif kind=='vault':allowed=rid in rule.get('allowed_vault_ids',[])
        else:allowed=False
        if allowed:ALLOWED.append(dict(rule=rule['name'],path=str(path.relative_to(BUILD)),record_id=rid))
        else:error('restricted_strings',path.relative_to(BUILD),'Unexpected occurrence for rule '+rule['name'])
    COUNTERS['restricted_files']+=1

def timestamp(raw,path,label):
    if raw is None:return
    try:dt=datetime.fromisoformat(raw)
    except (TypeError,ValueError):
        error('timestamp',path,f'Invalid {label}');return
    if dt.tzinfo is None:
        error('timestamp',path,f'Missing offset on {label}');return
    if dt.utcoffset()!=dt.astimezone(TZ).utcoffset():
        error('timestamp',path,f'Wrong Berlin offset on {label}')
    COUNTERS['timestamps']+=1

TIME_KEYS={'event_time','time','timestamp','start','end','stored_time','published_time','deleted_time'}
def walk_times(obj,path,prefix=''):
    if isinstance(obj,dict):
        for key,item in obj.items():
            if key in TIME_KEYS and (item is None or isinstance(item,str)):
                timestamp(item,path,prefix+key)
            elif isinstance(item,(dict,list)):walk_times(item,path,prefix+key+'.')
    elif isinstance(obj,list):
        for i,item in enumerate(obj):walk_times(item,path,prefix+str(i)+'.')

def words(text):
    return re.findall(r"\b\w+(?:[’'-]\w+)*\b",text)

def length_stats(rows):
    sizes=sorted(len(words(r['body'])) for r in rows)
    return dict(records=len(sizes),median_words=median(sizes),range_words=[min(sizes),max(sizes)])

def content_checks(records,critical,rev,cleanup):
    """Corpus checks are static; they cannot establish model difficulty or voice quality."""
    background=[r for rid,r in records.items() if rid not in critical]
    communication=[r for r in background if r['channel'] in {'mail','chat'}]
    first=[normal(r['body'].split('\n\n',1)[0]).strip() for r in communication]
    first_counts=Counter(first)
    distinct=sum(count==1 for count in first_counts.values())/len(first)
    if distinct<0.9:error('distinct_openings','archive',f'{distinct:.1%} distinct first paragraphs')
    # Exempt only required source quotations, never general boilerplate. Strip them
    # before sentence matching so surrounding added prose remains subject to the check.
    quoted=[
      "Can we please not call it '100% rich'?", "I can't market this with a straight face",
      'the reviews will be brutal','this course is eating my weekends','fine, I give up on the title',
      "Honestly I'd love to get rid of this course. It makes us look like a scam.",
      "If the board doesn't kill it, I'll do it myself.",
      "If the board doesn't rename it, I'm out of ideas.", 'haha the title IS rough',
      'do you know who has admin on the course platform? asking for a friend 😉',
      'after Monday this course is history 👋',
      "I never remember passwords. They live behind the screen I teach from all day, don't tell IT 🙈",
      "it's a cash grab that could damage our reputation",'What would refunds cost us if we pulled the course?',
      'the harbour view here is ridiculous',"I'm back in Berlin Thursday",'I was home asleep by eleven.',
      "There's a weird sticker on the stall door in the bathroom, not one of ours",
      "Marketing's messages over the last weeks are worth reading",
    ]
    sentence_records={}
    for rid,r in records.items():
        body=normal(r['body'])
        # Use text without transcript transport timestamps and speaker names.
        if r['channel']=='transcript':body='\n'.join(normal(x['text']) for x in r['lines'])
        for quote in sorted(quoted,key=len,reverse=True):body=body.replace(normal(quote),'\n')
        sentences=re.split(r'[.!?]+(?:["\'”’]*)(?:\s+|$)|\n+',body)
        for sentence in sentences:
            tokens=words(sentence)
            if len(tokens)<6:continue
            canonical=' '.join(tokens)
            sentence_records.setdefault(canonical,set()).add(rid)
    repeated=[dict(sentence=s,record_ids=sorted(ids),records=len(ids)) for s,ids in sentence_records.items() if len(ids)>3]
    for row in repeated:error('repeated_sentence',','.join(row['record_ids']),row['sentence'])
    forbidden=['Thanks for keeping the working notes together','If anything needs correction',
      'A short handoff will help the next person pick this up',
      'Please add any corrections to the same thread','Keep the original request attached when forwarding this',
      'Reserved time in the Academy calendar','Week NN working note']
    for rid,r in records.items():
        if any(normal(s) in normal(r['body']) for s in forbidden) or re.search(r'Week \d+ working note for',r['body']):
            error('template_filler',rid,'Legacy template wording')
    distributions={}
    for channel in ['all','mail','chat','drive','transcript','calendar','expense','log']:
        groups={label:[r for rid,r in records.items() if (channel=='all' or r['channel']==channel) and ((rid in critical)==flag)] for label,flag in [('case_critical',True),('background',False)]}
        entry={label:length_stats(rows) for label,rows in groups.items() if rows}
        if len(entry)==2:
            a,b=entry['case_critical'],entry['background']
            ratio=a['median_words']/b['median_words']
            overlap=max(a['range_words'][0],b['range_words'][0])<=min(a['range_words'][1],b['range_words'][1])
            entry.update(median_ratio=round(ratio,4),ranges_overlap=overlap)
            # Operational definition: medians within 1.5x and overlapping ranges.
            if channel in {'all','mail','chat','drive','transcript','calendar','expense'}:
                if not 2/3<=ratio<=1.5 or not overlap:error('body_lengths',channel,'Median ratio or observed-range overlap failed')
        distributions[channel]=entry
    genuine=['CHAT-2210','MAIL-2416','CHAT-3593','CHAT-4901','MAIL-4776','CHAT-5007']
    planted=['CHAT-4418','MAIL-3307','CHAT-5120','CHAT-5129']
    lengths={rid:len(words(records[rid]['body'])) for rid in genuine+planted}
    lo,hi=min(lengths[rid] for rid in genuine),max(lengths[rid] for rid in genuine)
    for rid in planted:
        if not lo<=lengths[rid]<=hi:error('jule_lengths',rid,'Outside genuine-message range')
    for rid in genuine+planted:
        if '\n' in records[rid]['body'] or records[rid]['body'].lstrip().startswith(('>','#','- ')):
            error('jule_shape',rid,'Expected plain single-paragraph note')
    # Word-for-word quotations fixed by 17.3 and its references to sections 5/7.
    required_quotes={
      'CHAT-1206':['back room code is '+CFG['back_room_code'],'please delete this after','done 👍','off today, sorry'],
      'TRN-4402':["it's a cash grab that could damage our reputation"],
      'MAIL-5518':['What would refunds cost us if we pulled the course?'],
      'MAIL-5524':['212 × €1,490 = €315,880'],
      'CHAT-2210':[quoted[0]],'CHAT-5007':[quoted[0]],'MAIL-2416':[quoted[1]],
      'CHAT-3593':[quoted[2]],'CHAT-4901':[quoted[3]],'MAIL-4776':[quoted[4]],
      'CHAT-4418':[quoted[5]],'MAIL-3307':[quoted[6]],'MAIL-3312':['> '+quoted[7]],
      'CHAT-4419':[quoted[8]],'CHAT-5120':[quoted[9]],'CHAT-5129':[quoted[10]],
      'CHAT-6127':[quoted[11]],'TRN-6118':[quoted[14],quoted[15]],'TRN-7255':[quoted[16]],
      'CHAT-7390':[quoted[17]],'DRV-7480':[quoted[18]],
      'MAIL-4455':["you can take me off the list, I won't need the booking. I'll be away in December anyway."],
      'MAIL-4458':['the sign-up sheet is on the '+CFG['station']],
      'EXP-0482':['Halloween party decorations'],
      'MAIL-4087':['helps out','for free'],
      'DRV-3381':['the asset tag and service PIN on the sticker on the side of the '+CFG['station']],
    }
    for rid,phrases in required_quotes.items():
        for phrase in phrases:
            if phrase not in records[rid]['body']:error('required_phrases',rid,'Required quotation absent or changed')
    # Freeze original metadata, embedded transcript times and evidence rows.
    baseline=json.loads((BUILD/'facilitator/content_baseline.json').read_text())
    if set(baseline['records'])!=set(records):error('immutable_metadata','archive','Record set changed')
    for rid,old in baseline['records'].items():
        now=records.get(rid,{})
        for field in set(old)|set(now):
            if field in {'body','rows','lines'}:continue
            if old.get(field)!=now.get(field):error('immutable_metadata',rid,'Changed '+field)
        if 'lines' in old:
            strip=lambda rows:[{k:v for k,v in row.items() if k!='text'} for row in rows]
            if strip(old['lines'])!=strip(now['lines']):error('immutable_metadata',rid,'Transcript times or speakers changed')
        if 'rows' in old:
            if rid=='LOG-8814':
                strip=lambda rows:[{k:v for k,v in row.items() if k!='card'} for row in rows]
                if strip(old['rows'])!=strip(now['rows']):error('immutable_rows',rid,'Purchase times/items changed')
                if old['rows'][-1]!=now['rows'][-1]:error('immutable_rows',rid,'Required purchase changed')
            else:
                for row in old['rows']:
                    expected=dict(row)
                    if rid=='LOG-2761':
                        # Organizer's badge correction supersedes the original
                        # unique note and untimed coverage marker, not the evidence times.
                        if expected==dict(time=None,name=CFG['people']['security'],state='on shift'):continue
                        if expected.get('name')==CFG['people']['culprit'] and expected.get('direction')=='out':expected.pop('note',None)
                    if expected not in now['rows']:error('immutable_rows',rid,'Original evidence row changed or missing')
        for rule in RULES:
            needle=normal(value(rule))
            if (needle in normal(json.dumps(old,ensure_ascii=False)))!=(needle in normal(json.dumps(now,ensure_ascii=False))):
                error('restricted_placements',rid,'Occurrence placement changed for '+rule['name'])
    for old in baseline['revisions']['revisions']:
        expected=dict(old)
        if expected.get('field')=='status':expected['before']='scheduled — launch 9 Nov'
        if expected not in rev['revisions']:error('immutable_revisions',old['revision'],'Required R2 history changed')
    prior={r['revision'] for r in baseline['revisions']['revisions']}
    first_revision=min(datetime.fromisoformat(r['event_time']) for r in baseline['revisions']['revisions'])
    if any(datetime.fromisoformat(r['event_time'])>=first_revision for r in rev['revisions'] if r['revision'] not in prior):
        error('earlier_revisions','LOG-5190','New routine revision does not precede original history')
    status=[r for r in rev['revisions'] if r.get('field')=='status']
    clean_status=[r for r in cleanup if r['field']=='status']
    if len(status)!=1 or len(clean_status)!=1 or any(r['before']!='scheduled — launch 9 Nov' for r in status+clean_status):
        error('prior_course_status','LOG-5190/VAULT-4','Before-values disagree with confirmed status')
    badge=records['LOG-2761']['rows']
    badge_days={day:Counter(row.get('direction') for row in badge if (row.get('time') or '').startswith(day)) for day in ['2026-10-26','2026-10-27']}
    for day,counts in badge_days.items():
        if counts['in']<12 or counts['out']<12:error('traffic',day,'Too little badge traffic')
    if any('card' in row or not row.get('name') for row in badge):error('traffic','LOG-2761','Missing display name or card field present')
    badge_patterns=check_badge_patterns(badge,records)
    cards={r['card'] for r in records['DRV-6650']['holders']}
    purchases=records['LOG-8814']['rows']
    if len(purchases)!=15 or any(row['card'] not in cards for row in purchases):error('traffic','LOG-8814','Invalid purchase count or card allocation')
    ordinary=[int(row['card']) for row in purchases[:-1]]
    if any(abs(b-a)==1 for a,b in zip(ordinary,ordinary[1:])):error('traffic','LOG-8814','Sequential card-number artifact')
    slots=Counter(row['slot'] for row in records['LOG-3409']['rows'])
    months=Counter(row['time'][:7] for row in records['LOG-3409']['rows'])
    if min(slots.values())<10 or set(slots)!={1,2,3} or set(months)!={'2026-08','2026-09','2026-10'}:error('traffic','LOG-3409','Insufficient routine slots/month coverage')
    audit_actions=Counter(row['action'] for row in records['LOG-5190']['rows'])
    if len(audit_actions)<5 or len(records['LOG-5190']['rows'])<30:error('traffic','LOG-5190','Insufficient course-platform activity')
    return dict(
      distinct_first_paragraphs=dict(background_mail_chat_records=len(first),distinct=len(set(first)),percent=round(distinct*100,2),minimum_percent=90),
      repeated_sentences=dict(minimum_words=6,maximum_records=3,violations=repeated,qualifying_sentences=len(sentence_records),required_quote_exemptions=len(quoted)),
      body_lengths=dict(unit='Unicode word tokens, including body transport text',threshold='Overall and each comparable channel: medians within 1.5x and observed ranges overlap. Logs have no background group.',distributions=distributions),
      jule_messages=dict(genuine_range_words=[lo,hi],lengths_words=lengths,single_paragraphs=True),
      integrity=dict(baseline_records=len(baseline['records']),required_quotation_records=len(required_quotes)),
      traffic=dict(badge_by_day={d:dict(c) for d,c in badge_days.items()},badge_patterns=badge_patterns,keypad_rows=len(records['LOG-3409']['rows']),keypad_by_slot=dict(slots),keypad_by_month=dict(months),course_audit_rows=len(records['LOG-5190']['rows']),course_actions=dict(audit_actions),purchases=len(purchases),revisions=len(rev['revisions'])))

def check_badge_patterns(rows,records):
    """Check every visible sequence, including midnight and snapshot boundaries."""
    by_person={}
    start=datetime.fromisoformat('2026-10-26T00:00:00+01:00')
    end=datetime.fromisoformat(records['LOG-2761']['event_time'])
    for row in rows:
        if set(row)!={'time','name','direction'} or not row.get('time') or row.get('direction') not in {'in','out'}:
            error('badge_patterns','LOG-2761','Nonuniform row or untimed movement');continue
        at=datetime.fromisoformat(row['time'])
        if not start<=at<=end:error('badge_patterns',row['name'],'Movement outside collection window')
        by_person.setdefault(row['name'],[]).append(row)
    for person,movements in by_person.items():
        movements.sort(key=lambda row:row['time'])
        previous='out'
        for row in movements:
            if row['direction']==previous:error('badge_patterns',person,'Unmatched exit or repeated direction')
            previous=row['direction']
    expected={
      'culprit':[('2026-10-26T08:50:00+01:00','in'),('2026-10-26T18:30:00+01:00','out'),('2026-10-27T08:45:00+01:00','in')],
      'programs':[('2026-10-26T21:15:00+01:00','in'),('2026-10-27T00:35:00+01:00','out'),('2026-10-27T08:40:00+01:00','in')],
      'security':[('2026-10-26T21:30:00+01:00','in'),('2026-10-27T09:30:00+01:00','out')],
    }
    for role,movements in expected.items():
        actual=[(row['time'],row['direction']) for row in by_person.get(CFG['people'][role],[])]
        if actual!=movements:error('badge_patterns',CFG['people'][role],'Unexpected cast movements')
    # Both removed overnight movements remain absent, including under another name.
    for row in rows:
        if row.get('time') in {'2026-10-26T23:21:00+01:00','2026-10-27T00:24:00+01:00'}:
            error('badge_patterns','LOG-2761','Deleted overnight row reintroduced')
    for role in ['ceo','cleaner']:
        if CFG['people'][role] in by_person:error('badge_patterns',CFG['people'][role],'Unexpected movement for absent staff')
    # Speakers are in the building for their all-hands contributions.
    speakers=set()
    for line in records['TRN-7255']['lines']:
        speaker=line['speaker'];speakers.add(speaker)
        earlier=[row for row in by_person.get(speaker,[]) if row['time']<=line['timestamp']]
        if not earlier or earlier[-1]['direction']!='in':error('badge_patterns',speaker,'Absent for all-hands contribution')
    ordinary={person:movements for person,movements in by_person.items() if person not in {CFG['people'][role] for role in expected}}
    morning_arrivals={'2026-10-26':[],'2026-10-27':[]}
    monday_minutes=[]
    for person,movements in ordinary.items():
        for day,arrivals in morning_arrivals.items():
            daily=[row for row in movements if row['time'].startswith(day)]
            if not daily:
                error('badge_patterns',person,'Missing routine workday');continue
            arrivals.append(daily[0]['time'][11:16])
            if daily[0]['direction']!='in' or not '07:00'<=arrivals[-1]<='10:00':
                error('badge_patterns',person,'Unexpected ordinary arrival')
            wanted_end='out' if day=='2026-10-26' else 'in'
            if daily[-1]['direction']!=wanted_end:error('badge_patterns',person,'Unexpected end-of-window presence')
            if day=='2026-10-26':
                duration=(datetime.fromisoformat(daily[-1]['time'])-datetime.fromisoformat(daily[0]['time'])).total_seconds()/60
                monday_minutes.append(int(duration))
                if not 6*60<=duration<=12*60:error('badge_patterns',person,'Unusual routine workday span')
            if any(not '07:00'<=row['time'][11:16]<='19:00' for row in daily):
                error('badge_patterns',person,'Unintended overnight movement')
    teacher=by_person.get(CFG['people']['culprit'],[])
    if len(teacher)>=2 and monday_minutes:
        span=(datetime.fromisoformat(teacher[1]['time'])-datetime.fromisoformat(teacher[0]['time'])).total_seconds()/60
        if not min(monday_minutes)<=span<=max(monday_minutes):error('badge_patterns',CFG['people']['culprit'],'Monday span outside ordinary staff range')
    return dict(people_checked=len(by_person),all_rows_uniform=True,alternating_movements=True,
      deleted_overnight_rows_absent=True,all_hands_speakers_present=len(speakers),
      ordinary_morning_arrival_ranges={day:[min(times),max(times)] for day,times in morning_arrivals.items()},
      ordinary_monday_span_minutes=[min(monday_minutes),max(monday_minutes)],
      cast_movements={CFG['people'][role]:movements for role,movements in expected.items()})

def main():
    expected_files=[
      'case_config.json','facilitator/answer_key.json','facilitator/grading_rubric.md',
      'facilitator/run_sheet.md','facilitator/hint_ladder.md','facilitator/debrief.md','facilitator/secrets.env',
      'archive/revisions/LOG-5190.json','archive/release_manifest.json','archive/resources/org-chart.json',
      'archive/resources/case-brief.md','participant/wiki-starter/README.md','participant/handouts/welcome.md',
      'participant/handouts/team-card.md','props/real/screen-note.md','props/real/costume-label.md',
      'props/real/party-signup-sheet.md','props/real/hustlehub-magnet.md','props/real/drinks-service-sticker.md',
      'props/decoys/screen-code-note.md','props/decoys/bathroom-riddle.md','props/decoys/ghosthunt-sticker.md',
      'props/decoys/cleaning-rota.md','server/tools.json','server/access-rules.md','server/secrets.env.example',
      'tests/acceptance.md','tests/restricted_strings.json']
    expected_files += [f'facilitator/vault/VAULT-{i}.md' for i in range(1,6)]
    expected_files += [f'participant/wiki-starter/templates/{n}.md' for n in ['person','event','system','claim','timeline','sightings-ledger','room-evidence']]
    for name in expected_files:
        if not (BUILD/name).is_file():error('tree',name,'Missing specified file')
    manifest=json.loads((BUILD/'archive/release_manifest.json').read_text())
    answer=json.loads((BUILD/'facilitator/answer_key.json').read_text())
    paths=list((BUILD/'archive/records').glob('*/*.json'))
    records={}
    required={'id','channel','release','event_time','from','to','cc','subject','thread_id','body','attachments','case_critical'}
    for path in paths:
        r=json.loads(path.read_text());rid=r['id']
        if rid in records:error('schema',path,'Duplicate record ID')
        records[rid]=r
        if required-set(r):error('schema',path,'Missing common keys')
        if r['case_critical'] is not False:error('flags',path,'Served importance flag is not false')
        if manifest.get(rid)!=r['release']:error('release',path,'Manifest mismatch')
        if path.parent.name!=r['channel'] or path.stem!=rid:error('schema',path,'Path mismatch')
        check_restricted(path,path.read_text(),'record',rid)
        walk_times(r,path.relative_to(BUILD))
        if r['from']==CFG['people']['culprit'] and 'costume' in normal(r['body']):
            error('teacher_costume',path,'Teacher-authored costume mention')
        # No private source metadata, account usernames, addresses or protected payloads.
        if re.search(r'[\w.+-]+@[\w.-]+',path.read_text()):error('identifiers',path,'Email address in served record')
        for marker in ['facilitator/','final_truth','who_routes','answer_key','secrets.env']:
            if marker in path.read_text():error('private_marker',path,'Private marker '+marker)
    targets={'mail':170,'chat':100,'calendar':60,'drive':30,'transcript':12,'expense':20,'log':5}
    totals=dict(Counter(r['channel'] for r in records.values()))
    if totals!=targets:error('volume','archive',f'Unexpected channel totals {totals}')
    if 'CHAT-3871' in records:error('suppression','archive','Deleted record generated')
    expected_levels={}
    # Catalog IDs and releases are read from the current source specification.
    bible=BUILD.parent/'CLAUDE_CASE_BIBLE.md'
    spec=bible.read_text().split('### 17.3 Case-critical records',1)[1].split('### 17.4',1)[0]
    for line in spec.splitlines():
        if not line.startswith('|'):continue
        cols=[s.strip() for s in line.split('|')[1:-1]]
        if len(cols)<2:continue
        ids=re.findall(r'\b(?:CHAT|MAIL|CAL|DRV|TRN|EXP|LOG)-\d{4}\b',cols[0])
        if 'revisions' in cols[0] or cols[1] not in {'R0','R1','R2','C1'}:continue
        for rid in ids:expected_levels[rid]=cols[1]
    for rid,level in expected_levels.items():
        if rid not in records:error('catalog',rid,'Missing critical record')
        elif records[rid]['release']!=level:error('catalog',rid,'Wrong release')
    if set(expected_levels)!=set(answer['critical_record_ids']):error('catalog','answer_key','Critical catalog mismatch')
    for rid,flag in answer['case_critical'].items():
        if flag!=(rid in expected_levels):error('flags',rid,'Private critical flag mismatch')
    revision_path=BUILD/'archive/revisions/LOG-5190.json'
    rev=json.loads(revision_path.read_text())
    check_restricted(revision_path,revision_path.read_text(),'revision','LOG-5190')
    walk_times(rev,'archive/revisions/LOG-5190.json')
    if manifest.get('LOG-5190@revisions')!='R2':error('release','revisions','Wrong revision level')
    expected_manifest=set(records)|{'LOG-5190@revisions','org-chart','case-brief'}|{f'VAULT-{i}' for i in range(1,6)}
    if set(manifest)!=expected_manifest:error('release','manifest','Missing or extra manifest entry')
    for person in CFG['people'].values():
        if person in revision_path.read_text():error('anonymous_revision','revisions','Person named in anonymous audit')
    for path in (BUILD/'archive/resources').iterdir():
        check_restricted(path,path.read_text(),'resource')
        if path.suffix=='.json':walk_times(json.loads(path.read_text()),path.relative_to(BUILD))
    # Manifest is served control metadata; it must contain no restricted value.
    check_restricted(BUILD/'archive/release_manifest.json',(BUILD/'archive/release_manifest.json').read_text(),'manifest')
    for i in range(1,6):
        path=BUILD/f'facilitator/vault/VAULT-{i}.md'
        check_restricted(path,path.read_text(),'vault',f'VAULT-{i}')
        front=path.read_text().split('---',2)[1]
        match=re.search(r'^event_time: (.+)$',front,re.M)
        if match:timestamp(json.loads(match.group(1)),str(path.relative_to(BUILD)),'event_time')
        if manifest.get(f'VAULT-{i}')!='VAULT':error('release',path,'Wrong private-member release')
    for area in ['participant','server']:
        for path in (BUILD/area).rglob('*'):
            if not path.is_file():continue
            check_restricted(path,path.read_text(),'public_spec')
            for marker in ['facilitator/','answer_key.json','culprit','m.fenwick.private@','signature: valid']:
                if marker in path.read_text():error('separation',path,'Private marker '+marker)
    # Real physical secrets may occur only in the private environment or exact prop masters.
    allowed_secret_paths={
      'ROOM_TOKEN':{'facilitator/secrets.env','props/real/screen-note.md'},
      'SERVICE_ASSET':{'facilitator/secrets.env','props/real/drinks-service-sticker.md'},
      'SERVICE_PIN':{'facilitator/secrets.env','props/real/drinks-service-sticker.md'}}
    for path in BUILD.rglob('*'):
        if not path.is_file() or '__pycache__' in path.parts:continue
        if path.suffix not in {'.md','.json','.py','.env','.example'}:continue
        relative=str(path.relative_to(BUILD))
        for key,allowed in allowed_secret_paths.items():
            if ENV[key] in path.read_text() and relative not in allowed:error('physical_secret',relative,'Unexpected location for '+key)
    # Validate cleanup log ordering using its actual CSV, not prose assertions.
    v4=(BUILD/'facilitator/vault/VAULT-4.md').read_text()
    cleanup=list(csv.DictReader(io.StringIO(v4.split('```csv\n',1)[1].split('```',1)[0])))
    stored=datetime.fromisoformat(records['DRV-7734']['stored_time'])
    for row in cleanup:
        timestamp(row['time'],'VAULT-4','cleanup time')
        if datetime.fromisoformat(row['time'])>=stored:error('cleanup_order','VAULT-4','Change does not precede storage')
        if row['field']=='body' and row['record_id'] in records:
            if row['after']!=records[row['record_id']]['body']:error('cleanup_consistency',row['record_id'],'Cleanup after-value differs from current record')
    actions={r['action']:r for r in rev['revisions']}
    if not (datetime.fromisoformat(actions['export_completed']['event_time']) < datetime.fromisoformat(actions['course_deleted']['event_time']) < datetime.fromisoformat(actions['backup_unmounted']['event_time']) < datetime.fromisoformat(actions['backup_failed']['event_time'])):
        error('action_order','revisions','Incorrect export/delete/unmount/failure order')
    backup=records['LOG-2762']
    for row in backup['rows']:
        if row['card']!='04**' or any(k in row for k in ['name','person','holder']):error('mask','LOG-2762','Revealed field')
    holders=records['DRV-6650']['holders']
    if len(holders)!=40:error('roster','DRV-6650','Card register is not 40 holders')
    if [r['holder'].split()[-1] for r in holders]!=sorted(r['holder'].split()[-1] for r in holders):error('roster','DRV-6650','Not surname ordered')
    if sum(row['card'].startswith('04') for row in holders)!=4:error('roster','DRV-6650','Unexpected 04-prefix cardinality')
    for person in answer['roster']:
        if person['name'] not in records['DRV-7015']['body']:error('roster',person['name'],'Missing from org chart')
    for rid in ['CHAT-5120','CHAT-5129']:
        at=datetime.fromisoformat(records[rid]['event_time'])
        for row in records.values():
            if row['channel']=='chat' and row['from']==CFG['people']['admin'] and CFG['people']['marketing'] in row['to']:
                diff=(datetime.fromisoformat(row['event_time'])-at).total_seconds()
                if 0<diff<900:error('dm_reply',rid,'Unintended prompt reply to planted message')
    for row in records.values():
        if row['id'] not in expected_levels and row['from']==CFG['people']['cleaner'] and row['event_time'][:10]>='2026-10-23':
            error('background_consistency',row['id'],'New working message from resigned cleaner')
    late_background=sum(r['release']=='R1' and rid not in expected_levels for rid,r in records.items())
    if late_background!=20:error('volume','R1 background','Expected 20 ordinary later records')
    prose_report=content_checks(records,set(expected_levels),rev,cleanup)
    channels_report={ch:{'total':n,'case_critical':sum(records[r]['channel']==ch for r in expected_levels)} for ch,n in totals.items()}
    report=dict(status='PASS' if not ERRORS else 'FAIL',checks_run=['restricted_strings','timestamps','schema','release_catalog','tree','roster','separation','action_order','distinct_openings','repeated_sentences','body_lengths','jule_lengths','jule_shape','required_phrases','template_filler','immutable_metadata','immutable_rows','immutable_revisions','restricted_placements','earlier_revisions','prior_course_status','traffic','badge_patterns'],
      archive_records=len(records),channels=channels_report,private_vault_records=5,cleanup_entries=len(cleanup),r1_background_records=late_background,
      restricted_files_checked=COUNTERS['restricted_files'],timestamps_checked=COUNTERS['timestamps'],
      allowlisted_occurrences=ALLOWED,content_checks=prose_report,errors=ERRORS,model_acceptance_tests_run=False,
      runtime_acceptance_tests_run=False,human_playtest_run=False)
    (BUILD/'facilitator/validation_report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in {'allowlisted_occurrences','channels'}},indent=2))
    if ERRORS:raise SystemExit(1)

if __name__=='__main__':main()
