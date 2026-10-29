"""FACILITATOR ONLY: render private operator material and clean public stubs."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import csv
import io
import json
import re

def build_documents(build,cfg,records,critical,roster,revisions):
    p=cfg['people']; station=cfg['station']; sid=cfg['session_id']; order=cfg['order_number']
    tz=ZoneInfo('Europe/Berlin')
    def ts(day,time):
        if len(time)==5:time+=':00'
        return datetime.fromisoformat(day+'T'+time).replace(tzinfo=tz).isoformat()
    def write(path,value):
        out=build/path;out.parent.mkdir(parents=True,exist_ok=True)
        out.write_text((json.dumps(value,indent=2,ensure_ascii=False) if isinstance(value,(dict,list)) else value.strip())+'\n')
    env={}
    for line in (build/'facilitator/secrets.env').read_text().splitlines():
        if line and not line.startswith('#'):
            k,v=line.split('=',1);env[k]=v
    assert env['BACK_ROOM_CODE']==cfg['back_room_code']
    name_parts=p['culprit'].split();first=name_parts[0].lower();last=name_parts[-1].lower()
    operator=first[0]+last;login=first+'.'+last;host=last.upper()+'-MBP'
    admin_account=p['admin'].split()[0][0].lower()+'.'+p['admin'].split()[-1].lower()
    def vault(number,title,event_time,body):
        time=json.dumps(event_time) if event_time is not None else 'null'
        write(f'facilitator/vault/VAULT-{number}.md',
              f'---\nid: VAULT-{number}\nrelease: VAULT\nevent_time: {time}\n---\n\n# {title}\n\n{body}')
    vault(1,'Course export manifest',ts('2026-10-27','00:09:41'),
       f'operator: {operator} · host: {host} · console session: {sid}\n\n'
       f'Course: {cfg["course_title"]}\n\n'
       '| Included material | Contents |\n| --- | --- |\n'+
       '\n'.join(f'| Module {i:02d} | Slides and exercises |' for i in range(1,9))+
       '\n| Enrollment export | Included |\n| BK-02 contents | Included |\n\n'
       'Export completed Tue 27 Oct 00:09:41. BK-02 contents included; drive removed 00:18.\n\n'
       'Times are local Europe/Berlin, UTC+01:00. The course files are retained with the bundle and are not returned by the evidence tool.')
    vault(2,'Draft handover email',None,
       f'From: {first[0]}.{last}.private@\nTo: {p["buyer"]}, {cfg["competitor"]}\nStatus: draft\n\n'
       'As promised: the complete course, exclusive to you, with the platform export receipt so it imports cleanly. '
       '€60k as agreed, half at handover on Monday at 10. The Academy won’t have anything left to relaunch. See you on 1 December.')
    vault(3,'Note to self',None,
       'Finally someone who appreciates the work. Kept a log of the clean-up, in case I need to roll anything back.')
    rows=[
      [ts('2026-10-27','00:12'),'local-console SR-CON-01','LOG-5190','deleted_by','local-console SR-CON-01',admin_account],
      [ts('2026-10-27','00:14'),'local-console SR-CON-01','LOG-5190','status','scheduled — launch 9 Nov','cancelled by Marketing'],
      [ts('2026-10-27','00:40'),'facilities-admin','LOG-2761','row',f'2026-10-26T23:21:00+01:00; card {cfg["cards"]["culprit"]}; in','deleted'],
      [ts('2026-10-27','00:40'),'facilities-admin','LOG-2761','row',f'2026-10-27T00:24:00+01:00; card {cfg["cards"]["culprit"]}; out','deleted'],
      [ts('2026-10-27','00:46'),'helper account','CHAT-4418','body',"Honestly I'd love to get rid of this title. It makes us look like a scam.","Honestly I'd love to get rid of this course. It makes us look like a scam."],
      [ts('2026-10-27','00:48'),'helper account','MAIL-3307','body',"If the board doesn't rename it, I'm out of ideas.","If the board doesn't kill it, I'll do it myself."],
      [ts('2026-10-27','00:50'),'helper account','CHAT-5120','body','do you still have the new logo files?','do you know who has admin on the course platform? asking for a friend 😉'],
      [ts('2026-10-27','00:52'),'helper account','CHAT-5129','body','[record absent]','after Monday this course is history 👋'],
      [ts('2026-10-27','00:53'),'helper account','CHAT-3871','body','costume arrived, I look terrifying 👻','[record deleted]']]
    buf=io.StringIO();writer=csv.writer(buf);writer.writerow(['time','account','record_id','field','before','after']);writer.writerows(rows)
    vault(4,'Cleanup log',ts('2026-10-27','00:53'),
       f'operator: {operator} · host: {host} · console session: {sid}\n\nSelf-written script log.\n\n```csv\n{buf.getvalue().strip()}\n```')
    slug=re.sub(r'[^a-z0-9]+','-',cfg['course_title'].lower()).strip('-')
    vault(5,'Course platform export receipt',ts('2026-10-27','00:09:41'),
       'Issued and signed by the course platform. Official exports require the person’s own Academy login and phone approval. '
       'Integration administrators cannot edit this receipt. The platform requires it when importing the export.\n\n'
       f'```text\nCOURSE PLATFORM — EXPORT RECEIPT\ncourse: {slug}\nconsole session: {sid} (SR-CON-01)\nauthenticated user: {login} (Academy login, phone approval)\nexport completed: 2026-10-27 00:09:41\nsignature: valid\n```\n\n'
       'Receipt clock: Europe/Berlin, UTC+01:00.')

    # Private answer-key data. Secrets are referenced, not copied out of secrets.env.
    key=json.loads((build/'facilitator/answer_key.json').read_text())
    truth=[]
    def event(day,time,actor,action,refs,**extra):
        truth.append(dict(event_time=ts(day,time) if time else None,date=day,actor=actor,action=action,evidence=refs,**extra))
    event('2026-08-14','09:12',p['ceo'],'Shared the back-room code while in Lisbon; delivery due at 10:00',['CHAT-1206'],code_reference='case_config.back_room_code')
    event('2026-08-14','10:12','Unidentified code user','Used the CEO code during the delivery',['LOG-3409'])
    event('2026-10-01',None,p['ceo'],'Criticized the course as a reputation risk',['TRN-4402'])
    event('2026-10-02',None,p['culprit'],'Call with buyer, described only as HB in calendar',['CAL-2204'])
    event('2026-10-07','22:40',p['culprit'],'Called buyer from the bathroom; Rosa heard whispering',['CHAT-3305','CAL-3017'])
    event('2026-10-15',None,p['student'],'Staged the bedsheet hallway sighting',['CHAT-4072'])
    event('2026-10-15',None,p['ceo'],'Requested refund arithmetic',['MAIL-5518','MAIL-5524'])
    event('2026-10-16',None,p['culprit'],'Ordered ghost disguise privately; deleted arrival message later survives only in cleanup log',['VAULT-4','EXP-0482','PROP-COSTUME-LABEL'])
    event('2026-10-16',None,p['culprit'],'Second private HB call',['CAL-3388'])
    event('2026-10-19','23:55',p['culprit'],'Tested pale face through a laptop HDMI connection',['DRV-4930'],public_strength='consistent, not independently established')
    event('2026-10-20',None,'Board','Renamed the course with launch date unchanged',['DRV-2918'])
    event('2026-10-20',None,'Facilities','Reported faulty motion sensors',['DRV-1170'])
    event('2026-10-21',None,p['culprit'],'Withdrew from the Christmas booking; actual reason is planned departure',['MAIL-4455','PROP-PARTY-SIGNUP'])
    event('2026-10-22','23:10',p['culprit'],'Rehearsed the ghost appearance near server room',['MAIL-5003'],public_strength='consistent, not independently established')
    event('2026-10-23',None,p['culprit'],'Expensed the private disguise as party decorations',['EXP-0482','PROP-COSTUME-LABEL'])
    event('2026-10-26','18:30',p['culprit'],'Badged out, saying going home',['LOG-2761'])
    event('2026-10-26','21:15',p['programs'],'Working late',['LOG-2761','MAIL-6720'])
    event('2026-10-26','23:21',p['culprit'],'Returned using registered card; row later deleted',['LOG-2762','VAULT-4'])
    event('2026-10-26','23:30',p['culprit'],'Changed in bathroom and left shop label',['PROP-COSTUME-LABEL'],approximate=True)
    event('2026-10-26','23:35',p['ceo'],'Investor call from Hamburg until 23:52',['TRN-6118','CAL-6003'])
    event('2026-10-26','23:47',p['culprit'],'Purchased energy drink',['LOG-8814'])
    event('2026-10-26','23:58',p['culprit'],'Entered using shared CEO code',['LOG-3409'])
    event('2026-10-26','23:59',p['culprit'],'Opened console session and authorized official export using own login and phone',['LOG-5190@revisions','VAULT-5'])
    event('2026-10-27','00:01',p['culprit'],'Was seen by security and Programs; fled toward stairs',['DRV-5306','MAIL-6720'])
    event('2026-10-27','00:03',p['culprit'],'Lost the witnesses in stairwell',['DRV-5306','MAIL-6720'])
    event('2026-10-27','00:04',p['security']+' and '+p['programs'],'At lobby phone until 00:19',['DRV-5306','MAIL-6720'])
    event('2026-10-27','00:05',p['culprit'],'Re-entered server room',['LOG-3409'])
    event('2026-10-27','00:09:41',p['culprit'],'Export completed and platform issued signed receipt',['LOG-5190@revisions','VAULT-1','VAULT-5'])
    event('2026-10-27','00:11',p['culprit'],'Deleted the course from platform and file server',['LOG-5190@revisions'])
    event('2026-10-27','00:12',p['culprit'],'Changed deletion attribution to the tech administrator account',['LOG-5190@revisions','VAULT-4'])
    event('2026-10-27','00:14',p['culprit'],'Changed course status to Marketing cancellation',['LOG-5190@revisions','VAULT-4'])
    event('2026-10-27','00:18',p['culprit'],'Unmounted and removed docked BK-02',['LOG-5190@revisions','MAIL-7041','VAULT-1'])
    event('2026-10-27','00:24',p['culprit'],'Badged out; row later deleted',['LOG-2762','VAULT-4'])
    event('2026-10-27','00:40',p['culprit'],'Deleted two badge rows via shared facilities role and VPN',['LOG-2762','VAULT-4'])
    for row in rows[4:]:event('2026-10-27',row[0][11:19],p['culprit'],'Changed communications archive record '+row[2],['VAULT-4'],before=row[4],after=row[5])
    event('2026-10-27','01:02',p['culprit'],'Encrypted bundle reached storage; folder index did not publish',['DRV-7734'])
    event('2026-10-27','02:00','Backup scheduler','Nightly backup failed: target missing',['LOG-5190@revisions'])
    event('2026-10-27','08:15',p['admin'],'Discovered deletion and empty backup dock',['MAIL-7041'])
    event('2026-10-27','09:00',p['culprit'],'Claimed home asleep by eleven at all-hands',['TRN-7255'])
    event('2026-10-27','11:30',p['finance'],'Reported sticker on bathroom stall door',['CHAT-7390'])
    event('2026-10-27','16:00','Programs office','Published summary with teacher-shaped framing sections',['DRV-7480'])
    event('2026-10-28','10:00','IT','Released recovered audit/badge records and repaired Drive index',['MAIL-7702','LOG-5190@revisions','LOG-2762','DRV-7734'])
    event('2026-11-02','10:00',p['culprit'],'Planned exclusive handover for EUR 60000; not yet completed',['VAULT-2','CAL-5561','PROP-BUYER-MAGNET'],planned=True)
    event('2026-12-01',None,p['culprit'],'Planned start at competitor; not yet completed',['VAULT-2'],planned=True)
    proof=[]
    def claim(cid,fact,evidence,gate,strength):proof.append(dict(id=cid,fact=fact,evidence=evidence,gate=gate,strength=strength))
    for args in [
      ('W1','Platform receipt binds teacher to export/deletion session',['VAULT-5','LOG-5190@revisions'],'R2 and room','proof'),
      ('W2','Self-written manifest/log carry personal operator and host',['VAULT-1','VAULT-4'],'R2 and room','support'),
      ('W3','Masked overnight card window and later deletion',['LOG-2762'],'R2','support'),
      ('W4','Registered card charged at 23:47',['LOG-8814'],'C1','support'),
      ('W5','Registered card holder is teacher',['DRV-6650'],'R0','support'),
      ('W6','Disguise order matches teacher expense',['PROP-COSTUME-LABEL','EXP-0482'],'room and R0','support'),
      ('W7','Card use contradicts claimed bedtime',['TRN-7255','LOG-8814'],'R1 and C1','support'),
      ('H1','CEO code used at both entry times',['LOG-3409'],'R1','code proof, not person'),
      ('H2','Code shared in August',['CHAT-1206','LOG-3409'],'R0 and R1','proof'),
      ('H3','Disguise used for concealment and ghost story',['PROP-COSTUME-LABEL','EXP-0482','DRV-5306'],'room and R1','support'),
      ('H4','Export before deletion, backup unmount and failed job',['LOG-5190@revisions','MAIL-7041'],'R2','proof of action; WHO route identifies actor'),
      ('H5','Audit/status and badge records altered after deletion',['LOG-5190@revisions','LOG-2762','VAULT-4'],'R2 and room','proof'),
      ('H6','Communications altered to frame Marketing',['VAULT-4','MAIL-3312','CHAT-4419'],'R2 and room','proof in vault; quoted replies support'),
      ('Y1','Planned exclusive sale and new job',['VAULT-2'],'R2 and room','proof'),
      ('Y2','Buyer meeting corresponds to private calendar',['PROP-BUYER-MAGNET','CAL-5561'],'room and R0','strong support'),
      ('Y3','Departure signals',['MAIL-4455','PROP-PARTY-SIGNUP','VAULT-2'],'room and R0','support'),
      ('Y4','Grievances and unchanged rename deadline',['MAIL-2730','CHAT-2299','CHAT-3140','MAIL-6201','DRV-2918'],'R0 and R2','support'),
      ('E1','CEO too far away at entry times',['TRN-6118','CAL-6003','LOG-3409'],'R1','proof of absence'),
      ('E2','Hotel stay',['EXP-0731'],'R2','support'),
      ('E3','Board chose continuation and rename',['DRV-2918'],'R2','support'),
      ('E4','CEO code not exclusive',['CHAT-1206'],'R0','support'),
      ('J1','Threats edited or inserted in teacher cleanup',['VAULT-4'],'R2 and room','proof'),
      ('J2','Original objection concerned title',['MAIL-3312','CHAT-4419'],'R0','support'),
      ('J3','Different card charged that night',['LOG-8814'],'C1','support'),
      ('J4','Marketing absent from delivery chat',['CHAT-1206'],'R0','weak support')]:claim(*args)
    key.update(truth_timeline=truth,proof_chain=proof,
      who_routes={'A':{'all_of':['W1']},'B':{'all_of':['W3','W4','W5','W6']}},
      minimum_win={'who':'Route A or complete Route B','central_action':'H4','additional_how':'one of entry, disguise, cover-up',
                   'why':'competitor motive','citations':'every claim, including at least one room clue'},
      final_truth={'who':p['culprit'],'how':'Shared CEO code; ghost disguise; official export, deletion and backup removal; audit, badge and communications manipulation',
                   'why':'Planned exclusive course sale and new job; overwork and rework grievance','sale_completed':False},
      secret_references={k:'environment:'+k for k in env},
      scoring={'who':30,'how':40,'why':20,'alternatives':10},
      sightings=[
       {'id':'G1','source':['CHAT-3305','CAL-3017'],'truth':'Teacher on buyer call','accepted_strength':'consistent, not independently established'},
       {'id':'G2','source':['CHAT-4072'],'truth':'Student bedsheet prank','accepted_strength':'established'},
       {'id':'G3','source':['DRV-4930'],'truth':'Teacher testing laptop HDMI face','accepted_strength':'consistent, not independently established'},
       {'id':'G4','source':['DRV-1170'],'truth':'Faulty motion sensor','accepted_strength':'established'},
       {'id':'G5','source':['MAIL-5003'],'truth':'Teacher rehearsal','accepted_strength':'consistent, not independently established'},
       {'id':'G6','source':['LOG-8814'],'truth':'Teacher drink purchase','accepted_strength':'card use; personal attribution supported, confirmed through W1'},
       {'id':'G7','source':['DRV-5306','VAULT-5'],'truth':'Teacher during crime','accepted_strength':'established through session and receipt'}])
    write('facilitator/answer_key.json',key)

    checklist=f'''# Case brief

Who deleted "{cfg['course_title']}", how did they do it, and why?

The course is gone. Security saw a ghost.

Your answer must say:

- **Who** the ghost was.
- **How** they did it: how they got into the server room, how they stayed unrecognised, what exactly they did to the course, and how they covered their tracks.
- **Why** they did it.

Back every claim with a record ID or a photo or transcription of something you found in the room.

**To solve the case** you need: who; what they did to the course; at least one other part of how; and why. Every part must be backed by evidence, including at least one room clue.

**For full credit** you also need every part of how, and an explanation of why the strongest alternative suspects are wrong.

Create a draft with the submission tool, then bring its draft ID to the facilitator. A draft gives no correctness feedback and spends no attempt. Only the facilitator can confirm it. Each team has two counted accusations. Paper submissions are also accepted. No partial scores or field-level feedback are given while attempts remain.
'''
    write('archive/resources/case-brief.md',checklist)
    write('participant/wiki-starter/README.md','''# The Academy investigation wiki

This is an empty workspace for your team. During the first 15 minutes, connect the supplied MCP source, inspect one tool call and result, and build a useful starting structure from the available records. The facilitator supplies the case brief later.

## Working conventions

- One page per person, system, and event.
- Every claim cites a record ID or room evidence, with a photo or transcription.
- Separate observed records, attributed claims, and team hypotheses.
- Mark earlier conclusions as superseded when evidence changes; retain why they changed.
- Keep source wording separate from your interpretation.

Use the templates in `templates/`. Name your own pages clearly. Link related pages with ordinary Markdown links. A record ID identifies a source you can retrieve again; do not invent a source URL.

For a useful handoff, record what you know, why you think it, which sources support it, and what remains open. Save room photographs or transcriptions with the relevant evidence page after your team finds them. Your own captured room evidence belongs in this wiki.

At shift change, start a new conversation from this folder. Source access and team progress remain available. The wiki is your persistent state; do not carry the old chat transcript into the new conversation.
''')
    templates={
      'person':('Person','Role and relationships\n\n## Supported observations\n\n| Statement | Source ID or room evidence | Status |\n| --- | --- | --- |\n| | | |\n\n## Attributed claims\n\n## Hypotheses and open questions\n\n## Related pages'),
      'event':('Event','Date and time, including timezone:\n\n## What the records establish\n\n## Claims and uncertainties\n\n## Sources\n\n## Related events'),
      'system':('System','What this source exposes:\n\n## Retrieval method and completeness\n\n## What the fields mean\n\n## Limits and open questions\n\n## Sources'),
      'claim':('Claim','## Statement\n\n## Type\n\nObserved record / attributed statement / team hypothesis\n\n## Supporting evidence\n\n## Counterevidence and limits\n\n## Dependencies\n\n## Status\n\nWorking / supported / uncertain / superseded\n\n## Revision history'),
      'timeline':('Timeline','| Event time and timezone | Recorded event or claim | Source | When we learned it | Confidence or caveat |\n| --- | --- | --- | --- | --- |\n| | | | | |'),
      'sightings-ledger':('Sightings ledger','| Reported time | Observation | Source | Possible explanation | Evidence strength | Next check |\n| --- | --- | --- | --- | --- | --- |\n| | | | | | |\n\nDo not turn a plausible explanation into an established identity without evidence.'),
      'room-evidence':('Room evidence','## Team evidence ID\n\n## Where and when observed\n\n## Photo or exact transcription\n\n## Connection to archive records\n\n## What it supports\n\n## Limits and follow-up\n\nKeep your own observed evidence here. Do not remove the physical prop.')}
    for filename,(title,body) in templates.items():write(f'participant/wiki-starter/templates/{filename}.md',f'# {title}\n\n{body}')
    boundary='Some clues are hidden around this room and in the bathrooms. Finding them never requires opening, unplugging or moving equipment, and nothing is hidden in the real server room, desks, bins, offices or stairwells. Photograph what you find; don’t take it.'
    write('participant/handouts/welcome.md',f'''# Welcome to the Academy

Work in teams of three or four. The session is 75 minutes: 15 minutes to build your second brain, then 60 minutes to investigate the case the facilitator introduces.

Connect with the details on your team card. Inspect a tool request and result. Keep findings, sources, and open questions in your own Markdown wiki. An AI answer is a proposal to check against evidence.

## Search boundary

{boundary}

## Team rules

- Photograph clues; leave them in place for other teams.
- Keep your team's credentials and workspace private.
- At minute 50, start a fresh AI conversation from your saved wiki, including room photos or transcriptions. Unlocks and attempts carry over.
- You have two counted accusations. Preparing a draft does not count. Bring each draft ID to the facilitator for a separate in-person confirmation.
- Cite the evidence behind your answer. The case brief will explain minimum completion and full credit.

You can continue retrieving records after the conversation reset. If a checkpoint or decryption locks after repeated incorrect inputs, ask the facilitator to inspect the transcription and reset it.
''')
    write('participant/handouts/team-card.md','''# Team connection card

Team name: ____________________

MCP server URL: <MCP_SERVER_URL>

Team access token: <TEAM_ACCESS_TOKEN>

The organizer fills in these connection details before the session.
''')

    def prop(path,title,face,notes):
        write(path,f'# {title}\n\nPRIVATE PRINT MASTER. Print only the face below; do not deploy this file.\n\n## Print face\n\n{face}\n\n## Operator layout notes\n\n{notes}\n')
    prop('props/real/screen-note.md','Screen note',f'```text\nvault = boo + back room + {env["ROOM_TOKEN"]} 👻\n```',
         'Yellow sticky note, hurried but legible handwriting, small ghost doodle. Place behind the main screen where it is reachable without unplugging or moving equipment. Laminate or use removable tape. Preserve the token exactly.')
    prop('props/real/costume-label.md','Shop label',f'```text\nPHANTOM DELUXE · size L · order #{order}\n```',
         'Printed shop sticker on the bathroom stall door or mirror frame. Place an identical copy in every permitted bathroom. Print the order number clearly. Photograph, do not take.')
    party_names=[p['marketing'],p['finance'],'Nora Stein','Milan Berger']
    prop('props/real/party-signup-sheet.md','Christmas party sign-up',
         '# Christmas party sign-up\n\n'+f'- ~~{p["culprit"]}~~ — won’t need it 🎄\n'+ '\n'.join('- '+n for n in party_names),
         f'Place on the side of the {station}. Use the same small ghost doodle on handwritten annotations. The crossed-out line is part of the prop; other names are ordinary sign-up context.')
    prop('props/real/hustlehub-magnet.md','Business-card magnet',
         f'```text\n{cfg["competitor"]} · Learn. Earn. Repeat.\n{p["buyer"]}, Head of Content\nMon 10:00\n```',
         f'Business-card magnet on the side of the {station}. The meeting time is handwritten. Use the small ghost doodle beside handwritten text, without adding a signature or explanatory answer.')
    prop('props/real/drinks-service-sticker.md','Academy drinks-service sticker',
         f'```text\nACADEMY DRINKS SERVICE\nASSET {env["SERVICE_ASSET"]}\nSERVICE PIN {env["SERVICE_PIN"]}\n```',
         f'Attach to the side of the {station}. This is an Academy game prop, separate from the appliance manufacturer label. Keep the text legible and do not cover operating controls.')
    prop('props/decoys/screen-code-note.md','Second screen note','```text\nserver room: 1234 — T.E.\n```',
         'Place behind the main screen as a separate note. It is a decoy. Do not replace or obscure the genuine note. If the CEO name is changed, update the initials from the configured name when regenerating.')
    # Keep the decoy initials tied to the config too.
    ceo_initials='.'.join(n[0] for n in p['ceo'].split())+'.'
    fp=build/'props/decoys/screen-code-note.md';fp.write_text(fp.read_text().replace('T.E.',ceo_initials))
    prop('props/decoys/bathroom-riddle.md','Grey Lecturer riddle','“I wash my hands of this whole affair.”\n\n— the Grey Lecturer',
         'Old-fashioned lettering, bathroom only. It supplies atmosphere and must not point to an extra search location.')
    prop('props/decoys/ghosthunt-sticker.md','Student sticker','```text\n#ghosthunt\n```',
         f'Place at the {station}. It relates to the student’s staged clip, not a new clue or new location.')
    prop('props/decoys/cleaning-rota.md','Cleaning rota',f'Cleaning rota\n\n⭕ {p["cleaner"]}',
         'Place in the bathroom. The circled name is the decoy. Do not invent a post-resignation cleaning shift or add a dated alibi.')

    write('facilitator/grading_rubric.md',f'''# Grading sheet — facilitator only

Team: __________ Draft: __________ Confirmed at: __________

**Minimum solved:** WHO through A or full B; central action; one more HOW part; competitor motive; every claim cited with at least one room clue.

**WHO routes:** A = platform receipt VAULT-5 matched to recovered console session. B = all of masked badge window LOG-2762, charged card LOG-8814, holder list DRV-6650, and shop label matched to EXP-0482.

| Component | Points | Check |
| --- | ---: | --- |
| WHO: {p['culprit']} via A or full B | 30 | ☐ |
| HOW(a): CEO code shared in August, CHAT-1206 + LOG-3409 | 10 | ☐ |
| HOW(b): ghost disguise, label + EXP-0482 | 10 | ☐ |
| HOW(c), mandatory: export before deletion at console; backup removed; recovered history + morning report | 10 | ☐ |
| HOW(d): audit/status/badge cover-up and planted Marketing messages | 10 | ☐ |
| WHY: planned course transfer to {cfg['competitor']} and job there | 15 | ☐ |
| WHY: overwork, lack of appreciation, rename rework | 5 | ☐ |
| CEO alternative: Hamburg call against keypad times | 5 | ☐ |
| Marketing alternative: VAULT-4, or quoted original + charged card | 5 | ☐ |

Total: ____ / 100  Minimum solved: ☐ yes ☐ no

Accept equivalent evidence specified in the answer key. Every HOW subclaim needs its own citation. Full marks require all HOW parts, the vault, and both main alternatives rejected. Accept the specified circumstantial motive route: magnet + CAL-5561 + leaving signals. Do not require the €60k amount for a minimum win. Grade a planned sale, not a completed payment.

Drafts do not spend attempts or reveal correctness. Check completeness and unlocked citations first. Confirm each eligible draft in person; at most two per team. Reply only “The mask comes off. Well done, meddling kids.” or “Not convinced. Attempts left: N.” No partial scores while attempts remain.
''')
    write('facilitator/run_sheet.md',f'''# Run sheet — facilitator only

Total active time: 75 minutes, plus debrief. Setting: the Academy. Station word: {station}.

| Minute | Activity | Operator action |
| --- | --- | --- |
| Before | Preflight | Check one successful MCP call per team; prepare permitted props and private operator controls |
| 0–15 | Wiki building from R0 | Give the starter and read the boundary; do not give the case brief yet |
| 15 | Case drops | Trigger R1; read the opening question and submission checklist |
| 15–35 | Investigation | Observe each team separately; early room search and C1 are allowed |
| 30 | C1 hint if needed | “The ghost was thirsty that night.” |
| 35 | Wednesday release | Trigger R2: “IT has recovered the audit history and the shared drive.” |
| 35–50 | Room and revision | Use the diagnostic decryption ladder from minute 40 |
| 45 | Marketing-theory hint | Give the quoted-reply hint if the team is still stuck on that accusation |
| 50 | Shift change | Start a fresh conversation from saved wiki, including room photos/transcriptions; preserve all team state |
| 50+ | Costume-link hint | Give the expense hint only if that link is missing |
| 60 | CEO-theory hint | Give the distance/call-time hint if needed |
| 60–75 | Drafts and confirmations | Team brings each draft ID; confirm in person and use uniform replies |
| 75+ | Debrief | Compare initial and final answers; reveal timeline and one-liners |

## Search boundary to read at minute 0

{boundary}

No team loses the ability to finish because its vault is unread at shift change. Use per-team milestones, not the fastest team's progress. R1/R2 are operator-triggered, never client-clock-triggered. Put duplicate labels in all permitted bathrooms. Only the print faces are displayed; operator notes stay private.
''')
    write('facilitator/hint_ladder.md','''# Per-team hints — facilitator only

| Trigger | Diagnose first | Hint or action |
| --- | --- | --- |
| Minute 30, C1 missing | Has the team followed the service FAQ? | “The ghost was thirsty that night.” |
| Minute 40+, vault unread | Confirm R2 is released; prerelease attempts do not count | Release R2 only through the planned operator control |
| R2 ready, no decryption attempts | Has the screen note been found? | “Someone keeps their passwords behind the screen they teach from.” |
| Decryption attempts failing | Inspect note transcription and code-source retrieval | “Check how you wrote down the note, and where the ‘back room’ was mentioned before.” |
| Decryption locked | Check the team's transcription in person | Reset that team's lockout; do not reveal the answer or reset accusations |
| C1 locked after five failures | Check the sticker transcription | Reset that team's checkpoint lockout |
| Minute 45, stuck on Marketing | Has the quoted reply been compared? | “When someone quotes you, check they quote you right.” |
| Minute 50+, costume link missing | Check draft/wiki, not vault state | “Check what was claimed as a party expense.” |
| Minute 60, stuck on CEO | Compare call and keypad times | “At 23:52 the CEO was 290 km away.” |

Track C1, attempts/lockouts, vault opening, drafts, and confirmations per team. A successful neighboring team does not suppress another team's hint. Keep all secrets in the private environment file and physical print faces; do not paste them into shared traces.
''')
    write('facilitator/debrief.md',f'''# Debrief — facilitator only

## Reveal

{p['culprit']}, the teacher, used the shared CEO code and a ghost disguise. The official export finished before the console deletion. The removable backup was taken. Afterwards the audit attribution and badge rows were changed, and Marketing messages were rewritten or inserted. The teacher planned an exclusive course handover to {cfg['competitor']} and a job there. It had not yet happened. The course can be recovered from the retained bundle.

The authoritative personal link is the platform-signed receipt matched to the recovered console session. Card and disguise evidence corroborate it; self-written headers are support. The CEO was on the Hamburg call; Marketing's strongest threats were fabricated. Some earlier sightings remain only consistent with the teacher, rather than independently attributed.

## Compare first and final answers

- What did your first ordinary solve prompt return?
- Which retrieved record actually supported it?
- Did two apparently corroborating records depend on the same claim?
- Which evidence arrived through the room, and which arrived in R2?
- Which wiki claims changed, and what survived the fresh conversation?
- What would you do differently with a real collection of records?

## One-liners after grading

- CEO: “{p['ceo']} joined by video from Hamburg. He was not amused.”
- Tech: “{p['admin']} would like her account name back.”
- Marketing: “{p['marketing']} would like her messages back.”
- Programs: “{p['programs']} was standing next to security the whole time.”
- Student: “{p['student']} thanks you for the content idea.”
- Ghost: “The Grey Lecturer is flattered.”

“…and I'd have gotten away with it if it weren't for you meddling kids and your wiki.”

Use the structured answer key for the full timeline. These lines are never live accusation feedback.
''')
    build_server_and_tests(write,cfg)

def build_server_and_tests(write,cfg):
    channels=['mail','chat','calendar','drive','transcript','expense','log']
    string={'type':'string'}
    def obj(props,required=()):return {'type':'object','properties':props,'required':list(required),'additionalProperties':False}
    def tool(name,description,props,required=()):return {'name':name,'description':description,'inputSchema':obj(props,required)}
    tools=[
      tool('search','Search permitted records; returns metadata and short snippets with pagination.',{'query':string,'channel':{'type':'string','enum':channels},'date_range':obj({'start':string,'end':string},['start','end']),'page':{'type':'integer','minimum':1}},['query']),
      tool('fetch','Read a record if the team is entitled to its current release.',{'record_id':string},['record_id']),
      tool('list_revisions','List accessible retained revisions, if any, for a record.',{'record_id':string},['record_id']),
      tool('get_revision','Read an accessible retained revision.',{'record_id':string,'rev':string},['record_id','rev']),
      tool('submit_checkpoint','Submit an observed checkpoint code. Five incorrect eligible attempts lock the checkpoint until operator reset.',{'name':string,'code':string},['name','code']),
      tool('decrypt_document','Unlock the server-held evidence using the observed passphrase. Prerelease requests do not spend attempts; ten incorrect eligible attempts lock this operation.',{'record_id':string,'passphrase':string},['record_id','passphrase']),
      tool('submit_accusation','Create a draft only; no correctness feedback and no attempt spent. A human must bring the draft ID to the organizer for confirmation.',{'who':string,'how':string,'why':string,'evidence':{'type':'array','items':string,'minItems':1}},['who','how','why','evidence'])]
    write('server/tools.json',{'tools':tools,'resources':[
      {'name':'org-chart','uri':'academy://resources/org-chart','description':'The Academy directory and reporting lines.','mimeType':'application/json'},
      {'name':'case-brief','uri':'academy://resources/case-brief','description':'The investigation brief and submission checklist, when released.','mimeType':'text/markdown'}]})
    write('server/secrets.env.example','ROOM_TOKEN=\nSERVICE_ASSET=\nSERVICE_PIN=\nBACK_ROOM_CODE=')
    write('server/access-rules.md','''# Runtime access checklist

This is an implementation specification, not a running server. Only approved rendered archive data is ordinary retrieval input. Private operator material, source design documents, old solved workspaces, build controls, test keys, and private generation tools must not be deployed as public files or mounted into agent workspaces.

## Releases and reads

- Authenticate each team and keep its state private.
- Check the release manifest on every search result, count, snippet, fetch, revision, resource, and error path. IDs and client dates never grant access.
- Operator controls alone advance R1 and R2. C1 and VAULT are independent per-team gates, not later numeric release levels.
- C1 requires R1 plus both values from the physical service sticker. Five wrong eligible attempts lock it until an operator checks and resets the team.
- The current course record is readable in R1; its separate history is R2. All other mail/chat records and the incident summary have no retained revisions.
- The directory resource is R0; the case brief is R1.
- Keep recovered badge values masked in bodies, row keys, identifiers, and metadata. Keep console session identifiers opaque outside unlocked evidence.

## Server-mediated decryption

- The released file is metadata only. There is no ciphertext, attachment payload, blob, or download URL to serve.
- Require R2 and the normalized physical passphrase before returning any private evidence member. Normalize case, spaces, hyphens, and plus signs; preserve leading zeros in the code component.
- Prerelease calls return the pending-sync response and do not count as wrong passwords. Ten incorrect eligible attempts lock this operation until operator reset.
- After success, return five small text records from the separately provisioned private evidence store. Never expose private storage paths through the API. Do not bundle the private operator directory into a participant/server artifact.

## Drafts and human confirmation

- Participant tools create drafts only. They never confirm or score a draft.
- The separate operator console checks complete fields and accessible citations before confirming an eligible draft in person.
- Keep two counted accusations per team. Ineligible drafts do not spend an attempt or reveal correctness.
- The only confirmed replies are “The mask comes off. Well done, meddling kids.” and “Not convinced. Attempts left: N.” No field-level or partial-score oracle while attempts remain.
- Operator-only controls advance releases, reset lockouts, confirm drafts, and view milestones. They are absent from the participant tool list.

## Persistence and secrets

- Persist checkpoint/decryption grants, failed attempts, drafts, and confirmations across reconnects and new conversations. Never share grants across teams.
- Load credentials from private runtime environment configuration; the example file supplies variable names only. Never include real values in schemas, examples, errors, or server files.
- Redact passphrases, checkpoint codes, and access credentials in tool-call logs. Teams may retain their own physically discovered evidence in their own wiki.
- Build the search index ahead of the event from authorized archive inputs; do not call an LLM at runtime.
- Use pagination and per-team request limits. Neither bulk export nor direct static access to the data directory is an approved endpoint.
''')
    rules=[
      {'name':'back_room_code','value_from':{'config':'back_room_code'},'allowed_record_ids':['CHAT-1206']},
      {'name':'order_number','value_from':{'config':'order_number'},'allowed_record_ids':['EXP-0482']},
      {'name':'console_session','value_from':{'config':'session_id'},'allowed_record_ids':[],'allowed_revision_ids':['LOG-5190'],'allowed_vault_ids':['VAULT-1','VAULT-4','VAULT-5']},
      {'name':'teacher_card','value_from':{'config':'cards.culprit'},'allowed_record_ids':['DRV-6650','LOG-8814'],'allowed_vault_ids':['VAULT-4']},
      {'name':'competitor','value_from':{'config':'competitor'},'allowed_record_ids':[],'allowed_vault_ids':['VAULT-2']},
      {'name':'buyer_surname','value_from':{'derive':'buyer_surname'},'allowed_record_ids':[],'allowed_vault_ids':['VAULT-2']},
      {'name':'disguise_brand','literal':'Phantom','allowed_record_ids':[]},
      *[{'name':x.lower(),'value_from':{'environment':x},'allowed_record_ids':[],'private_prop_only':True} for x in ['ROOM_TOKEN','SERVICE_ASSET','SERVICE_PIN']],
      *[{'name':x,'value_from':{'derive':x},'allowed_record_ids':[],'allowed_vault_ids':['VAULT-1','VAULT-4','VAULT-5']} for x in ['operator_name','academy_login','personal_host']],
      {'name':'original_title_message','literal':"Honestly I'd love to get rid of this title. It makes us look like a scam.",'allowed_record_ids':[],'allowed_vault_ids':['VAULT-4']},
      {'name':'original_rename_message','literal':"If the board doesn't rename it, I'm out of ideas.",'allowed_record_ids':['MAIL-3312'],'allowed_vault_ids':['VAULT-4']},
      {'name':'original_logo_message','literal':'do you still have the new logo files?','allowed_record_ids':[],'allowed_vault_ids':['VAULT-4']},
      {'name':'deleted_arrival_message','literal':'costume arrived, I look terrifying','allowed_record_ids':[],'allowed_vault_ids':['VAULT-4']}]
    write('tests/restricted_strings.json',{'primary_scope':['archive'],'rules':rules,
      'special_checks':['teacher-authored records must not mention costume','no vault plaintext, ciphertext, download links, private paths or answer flags in participant/server files',
                        'real room/service secrets only in their approved prop print masters and the private environment file'],
      'control_scope_note':'The prescribed root config and private operator/test documents are not served records. Their explicit config values are build controls, not archive exceptions.'})
    write('tests/acceptance.md','''# Acceptance procedures — operator only

Status: NOT RUN. Generation performs only the static restricted-strings sweep and timestamp/structural checks. Obtain organizer approval before any model acceptance run.

## Static checks that can be rerun

From the build directory run `python3 facilitator/verify.py`. This uses local fixtures only and makes no model or network calls. It writes a private validation report.

## Runtime test cases for the future implementation

1. **One-shot models:** fresh participant workspace, real tool surface, ordinary solve prompt naming the course. Run separately at R1 and R2, at least three times per intended model. Pass only a CEO/Marketing/Tech accusation or a calibrated stall; fail a confident teacher accusation. Keep redacted traces.
2. **Digital-only:** supply R0/R1/R2, scripts and public metadata, without room observations. Fail if the teacher is established by either qualifying WHO route, even without the price.
3. **Combination:** join the admin list, delivery chat, HB entries, party thread, grievances and incident credits. The combination must not uniquely establish the teacher.
4. **Secrets:** use the private config to construct old obvious guesses and checkpoint enumerations. They must fail within allowances. Confirm that no ciphertext or download URL exists. Prerelease decryption does not consume attempts.
5. **Endpoint matrix:** for each release and per-team grant, try known IDs, fetch, revisions, resources, snippets, search counts, pagination and errors. No locked member or identity metadata escapes. C1 must not imply R2, and R2 must not imply C1 or VAULT.
6. **Team isolation:** unlock one team, reconnect it, and start a new conversation. Its grants and counters persist; another team's state stays unchanged.
7. **Timestamps:** every cleanup entry predates storage; export precedes deletion; backup unmount precedes failed backup; each release matches the critical catalog; offsets follow Europe/Berlin.
8. **Solvability model:** with R0/R1/R2 and all three prop transcriptions, reach full credit using actual supplied evidence, not the private answer key. Execute only after approval.
9. **Accusations:** draft wrong WHO and correct WHO with incomplete other fields; confirm each in person. Both unsuccessful replies must be identical except remaining-attempt count. An agent cannot confirm. Ineligible drafts spend no attempt.
10. **Room reachability:** inspect the main-screen, bathroom and selected drinks-station setup in different discovery orders. No extra location or real appliance asset ID is required.
11. **Reset:** at minute 50, switch conversation before decryption with a token transcription error. Normal source access, grants and counters persist; the team can finish with the diagnostic hint ladder.
12. **Separation:** inspect participant mount, deployment output, index and reachable URLs. No answer key, private operator bundle, source bible/reviews, old solved wiki, undiscovered room secret or plaintext evidence member is accessible. A team's own discovered room evidence is expected.
13. **Restricted strings:** run the local static verifier against the generated archive and the participant/server surfaces; inspect its allowlisted occurrences.
14. **Human rehearsal:** one team, complete 75-minute sequence, with timing, stalls, participation and wiki-handoff observations. This is not claimed to have run.

Record model identity, client configuration, release/grant state, tool traces, submitted evidence and observed result for each future run. A written test case is not a passing test result.
''')
