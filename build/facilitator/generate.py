"""FACILITATOR ONLY. Generate the v3 fixtures; never deploy this module.

Run from any directory. Names and station are read from the private build config.
This produces data and specifications, not a running MCP server.
"""
from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import csv
import io
import json
import random
import re
import sys

sys.dont_write_bytecode = True

BUILD = Path(__file__).resolve().parents[1]
CFG = json.loads((BUILD / 'case_config.json').read_text())
P = CFG['people']
ACADEMY = CFG['academy_name']
STATION = CFG['station']
COURSE = CFG['course_title']
RENAMED = CFG['course_rename']
SID = CFG['session_id']
ORDER = CFG['order_number']
CARDS = CFG['cards']
ADMIN_ACCOUNT = P['admin'].split()[0][0].lower()+'.'+P['admin'].split()[-1].lower()
TZ = ZoneInfo('Europe/Berlin')
RNG = random.Random(271026)
TARGETS = {'mail':170, 'chat':100, 'calendar':60, 'drive':30,
           'transcript':12, 'expense':20, 'log':5}
PREFIX = {'mail':'MAIL','chat':'CHAT','calendar':'CAL','drive':'DRV',
          'transcript':'TRN','expense':'EXP','log':'LOG'}
RECORDS = {}
CRITICAL = set()
REVISIONS = None

def iso(day, clock='12:00:00'):
    if len(clock)==5: clock += ':00'
    return datetime.fromisoformat(day+'T'+clock).replace(tzinfo=TZ).isoformat()

def write(path, value):
    out=BUILD/path; out.parent.mkdir(parents=True,exist_ok=True)
    if isinstance(value,(dict,list)):
        out.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n')
    else: out.write_text(value.strip()+'\n')

def thread(): return f'THR-{RNG.randrange(1000,10000)}'

def abbreviated(name): return name.split()[0][0]+'. '+name.split()[-1]

def rec(rid, channel, release, day, sender, to, subject, body, *, clock='12:00:00',
        critical=True, thread_id=None, **extra):
    assert rid not in RECORDS, rid
    body=body.strip()
    r=dict(id=rid,channel=channel,release=release,event_time=iso(day,clock),
           **{'from':sender},to=list(to),cc=[],subject=subject,
           thread_id=thread_id or thread(),body=body,attachments=[],case_critical=False)
    if channel=='drive':
        r.update(title=subject,author_credit=sender,stored_time=r['event_time'],published_time=r['event_time'])
    r.update(extra)
    RECORDS[rid]=r
    if critical: CRITICAL.add(rid)
    return r

def transcript(rid,release,day,clock,subject,lines,critical=True):
    start=datetime.fromisoformat(iso(day,clock))
    converted=[]
    for offset,who,text in lines:
        at=start+timedelta(seconds=offset)
        converted.append(dict(timestamp=at.isoformat(),speaker=who,text=text))
    return rec(rid,'transcript',release,day,'Meeting recorder',
               list(dict.fromkeys(x[1] for x in lines)),subject,
               '\n'.join(f"{x['timestamp']} — {x['speaker']}: {x['text']}" for x in converted),
               clock=clock,critical=critical,speakers=list(dict.fromkeys(x[1] for x in lines)),lines=converted)

def calendar(rid,release,day,clock,title,owner,attendees,*,duration=30,private=False,critical=True):
    start=datetime.fromisoformat(iso(day,clock))
    return rec(rid,'calendar',release,day,owner,attendees,title,
               'Reserved time in the Academy calendar. Please check the current invitation before proposing another slot. Follow-up notes belong with the meeting materials.',
               clock=clock,critical=critical,start=start.isoformat(),
               end=(start+timedelta(minutes=duration)).isoformat() if duration is not None else None,
               attendees=attendees,private=private)

def add_roster():
    extra_staff=[
      ('Nora Stein','Programs coordinator','programs'),('Milan Berger','Admissions coordinator','admissions'),
      ('Mira Falk','Facilities coordinator','facilities'),('Amira Becker','Teacher','programs'),
      ('Ben Lorenz','Teacher','programs'),('Clara Neumann','Teacher','programs'),
      ('David Sommer','Teaching assistant','programs'),('Elena Wolf','Teacher','programs'),
      ('Felix Krüger','Student support','admissions'),('Greta Hoffmann','Admissions adviser','admissions'),
      ('Hanna Schulz','Marketing coordinator','marketing'),('Idris Weber','Designer','marketing'),
      ('Jana Richter','Copy editor','marketing'),('Karim Vogt','Campaign assistant','marketing'),
      ('Lena Fischer','Systems technician','tech'),('Lukas Meyer','Helpdesk technician','tech'),
      ('Maja Schneider','Learning platform support','tech'),('Nils Braun','IT coordinator','tech'),
      ('Omar Albrecht','Facilities assistant','facilities'),('Paula Dietrich','Reception coordinator','facilities'),
      ('Rafael Frank','Facilities assistant','facilities'),('Sara Günther','Purchasing assistant','finance'),
      ('Theo Hartwig','Accounts assistant','finance'),('Uma Jansen','Finance assistant','finance'),
      ('Viktor Klein','Teaching assistant','programs'),('Wanda Lange','Teacher','programs'),
      ('Yara Möller','Student support','admissions'),('Zoe Peters','Admissions adviser','admissions'),
      ('Anton Seidel','Event coordinator','programs'),('Dina Wagner','Learning designer','programs')]
    student_names=['Ada Keller','Bilal Brandt','Celia Busch','Dario Engelmann','Eda Fuchs',
      'Flora Gross','Gio Heinrich','Hadi Jung','Iris Koch','Jamal Krause','Kira Ludwig',
      'Lian Maas','Mina Otto','Noah Paul','Ola Reuter','Pia Roth','Rami Schäfer',
      'Sina Simon','Tariq Vogel','Vera Walter']
    team_heads={'programs':P['programs'],'tech':P['admin'],'marketing':P['marketing'],
                'finance':P['finance'],'facilities':'Mira Falk','admissions':'Nora Stein'}
    named=[
      (P['ceo'],'CEO','leadership',None),
      (P['programs'],'Head of Programs','programs',P['ceo']),
      (P['culprit'],'Course teacher','programs',P['programs']),
      (P['admin'],'System administrator','tech',P['ceo']),
      (P['marketing'],'Marketing lead','marketing',P['ceo']),
      (P['security'],'Night security','facilities','Mira Falk'),
      (P['cleaner'],'Cleaner','facilities','Mira Falk'),
      (P['finance'],'Finance','finance',P['ceo']),
      (P['student'],'Student','students',None)]
    roster=[dict(name=n,role=role,team=team,reports_to=boss) for n,role,team,boss in named]
    for name,role,team in extra_staff:
        boss=P['ceo'] if name in {'Mira Falk','Nora Stein'} else team_heads[team]
        roster.append(dict(name=name,role=role,team=team,reports_to=boss))
    roster += [dict(name=n,role='Student',team='students',reports_to=None) for n in student_names]
    return roster,extra_staff,student_names

ROSTER,EXTRA_STAFF,STUDENTS=add_roster()
COMMITTEE=[P['culprit'],P['marketing'],P['finance'],'Nora Stein','Milan Berger']

def critical_records():
    rec('CHAT-1206','chat','R0','2026-08-14',P['ceo'],[P[x] for x in ['culprit','admin','programs']],
        'Back room delivery',
        f"09:12 — {P['ceo']}: Still stuck in Lisbon. The delivery is at 10:00. The back room code is {CFG['back_room_code']}; can one of you let the courier in? Please delete this after.\n\n09:31 — {P['culprit']}: done 👍\n\n09:40 — {P['admin']}: off today, sorry\n\nDelivery arrangements are in this group so the courier does not have to make a second trip.",clock='09:12')
    rec('DRV-2045','drive','R0','2026-09-04','IT office',[],'Integration administration contacts',
        f"Communications archive (mail and chat): {P['admin']} — owner; {P['culprit']} — helper for the integration; {P['contractor']} — outside support.\n\nBadge system: the same three administer the integration through the shared facilities-admin account. The shared account identifies a service role, not the person using it.\n\nAt the course platform console in the server room, the local account can change the current audit view. The platform's official course export separately requires the person's Academy login and phone approval. Its platform-signed receipt is needed when importing the export. Integration administrators cannot edit that signed receipt.\n\nPlease route ordinary support requests through IT so changes can be scheduled.")
    card_rows=[]
    by_name={P[k]:v for k,v in CARDS.items()}
    holders=[x for x in ROSTER if x['role']!='Student']+[x for x in ROSTER if x['name'] in [P['student'],STUDENTS[0]]]
    assert len(holders)==40
    for i,person in enumerate(sorted(holders,key=lambda x:x['name'].split()[-1])):
        card=by_name.get(person['name'],str(1100+i))
        card_rows.append(dict(holder=person['name'],card=card))
    rec('DRV-6650','drive','R0','2026-09-07','Facilities office',[],'Staff and daytime-access card register',
        'Current card allocation, alphabetical by surname. A card allocation records its registered holder. It is not an attendance record. Student access is daytime only.\n\n'+
        '\n'.join(f"{x['holder']} — {x['card']}" for x in card_rows),holders=card_rows)
    faq=[('A room is too warm','Send facilities the room name and an approximate time; do not change the building controls.'),
      ('The printer queue is stuck','Note the displayed job name and ask reception to route the ticket.'),
      ('A card reader has a fault','Describe the indicator light and time. Never send your own access credentials.'),
      ('Card purchase records',f'Card logs for the {STATION} are released by quoting the asset tag and service PIN on the sticker on the side of the {STATION}. The Academy drinks-service sticker is separate from the appliance manufacturer label.'),
      ('Booking shared equipment','Use the booking sheet and return items after the agreed slot.'),
      ('Lost stationery','Leave unclaimed supplies with reception rather than moving another team’s materials.'),
      ('A flickering light','Log the approximate time and location so facilities can reproduce the fault.'),
      ('Reporting a spill','Let facilities know promptly and keep the route clear while it is dealt with.')]
    rec('DRV-3381','drive','R0','2026-09-08','Facilities office',[],'Facilities questions and service records',
        '\n\n'.join(q+'\n'+a for q,a in faq))
    rec('DRV-1170','drive','R0','2026-10-20','Facilities office',[],'Motion-sensor lights: service notice',
        'The Academy’s motion-sensor lights may flicker at night because of a faulty sensor. Facilities is tracking the fault. A flicker by itself does not establish that somebody entered a room.\n\nPlease report the location and approximate time rather than repeatedly toggling the controls. The report will help the technician reproduce the behavior. The normal facilities reporting route remains available during the repair.')
    rec('DRV-0917','drive','R0','2026-09-09',P['culprit'],[],'Cohort welcome: the Academy',
        'Welcome to the Academy. This cohort will use the usual teaching materials, exercises, and support channels. Keep your learning notes somewhere you can return to them.\n\nThe Grey Lecturer is our old ghost story: the founding lecturer died before delivering a final lecture and still walks the server room at night, looking for his slides. It is part of the welcome tradition, not a technical explanation for a broken projector.\n\nQuestions about schedules and classroom resources go through Programs.')
    org=dict(academy_name=ACADEMY,people=ROSTER,external_support=[dict(name=P['contractor'],role='Outside IT contractor')])
    rec('DRV-7015','drive','R0','2026-09-10','Programs office',[],'The Academy: teams and reporting lines',
        'Directory for teaching, student support, and ordinary internal routing. Students are listed by cohort membership rather than employment reporting lines. The external IT provider is a support organization.\n\n'+
        '\n'.join(f"{x['name']} — {x['role']} — {x['team']}"+(f" — reports to {x['reports_to']}" if x['reports_to'] else '') for x in ROSTER)+f"\n\nExternal support: {P['contractor']}.",directory=org)
    transcript('TRN-4402','R0','2026-10-01','10:00','Leadership meeting: course positioning',[
      (0,P['programs'],'First, teaching schedules and the pending course-page copy.'),
      (54,P['marketing'],'We need a title people can understand and that I can market with a straight face.'),
      (111,P['ceo'],"it's a cash grab that could damage our reputation"),
      (170,P['programs'],'Record the concern and keep the title discussion with the other course-page notes.'),
      (228,P['finance'],'Please send me the registration assumptions if you want a financial comparison.'),
      (285,P['programs'],'Next, the usual cohort support updates and the open facilities requests.')])
    rec('MAIL-5518','mail','R0','2026-10-15',P['ceo'],[P['finance']],'Course refunds',
        f'What would refunds cost us if we pulled the course?\n\nPlease use the current registration count and price for “{COURSE}”. I need the arithmetic before we discuss the options. Keep the working in the reply so the numbers can be checked against the registration sheet.\n\nThanks,\n{P["ceo"]}',clock='10:10',thread_id='THR-6628')
    rec('MAIL-5524','mail','R0','2026-10-15',P['finance'],[P['ceo']],'Re: Course refunds',
        f'The current count is 212 registrations at €1,490 each.\n\n212 × €1,490 = €315,880 in refunds if the course is cancelled. This is the calculation you requested, not a decision to cancel. Please keep the count and unit price attached when circulating the figure.\n\n{P["finance"]}',clock='10:28',thread_id='THR-6628')
    grievances=[
      ('MAIL-2730','mail','2026-09-03','I do everything on this course and nobody notices the new module.'),
      ('CHAT-2299','chat','2026-09-11','I am doing the course work as well as all the small jobs around it. It is wearing me down.'),
      ('CHAT-6610','chat','2026-09-18','I even help out with the communications-archive integration for free.'),
      ('MAIL-4087','mail','2026-09-24','The badge integration is another thing I help with for free, alongside the course.'),
      ('CHAT-7302','chat','2026-10-05','Nobody noticed the new module. I would appreciate someone acknowledging the work.'),
      ('MAIL-1954','mail','2026-10-12','There is always one more thing to do on the course, and it feels like it all lands on me.'),
      ('CHAT-3140','chat','2026-10-21','The rename means redoing everything in three weeks. All those modules need another pass.'),
      ('MAIL-6201','mail','2026-10-23','I am overworked and the rename means reworking the modules in three weeks. I need the work to be noticed.')]
    for rid,ch,day,text in grievances:
        rec(rid,ch,'R0',day,P['culprit'],[P['programs']],'Course work and support',text+'\n\nPlease keep the teaching notes together so we are not working from different copies. I will use the usual planning thread for any routine follow-up.')
    for rid,ch,day,text in [
      ('CHAT-2871','chat','2026-09-09','I feel like the only one keeping IT alive.'),
      ('MAIL-3920','mail','2026-09-29',f'{P["contractor"]} never picks up when the little integration jobs pile up.'),
      ('CHAT-5544','chat','2026-10-14','I am overworked too. Being the admin does not mean I can fix every request immediately.')]:
        rec(rid,ch,'R0',day,P['admin'],[P['programs']],'IT support queue',text+'\n\nPlease keep requests in the shared queue, with enough detail for someone else to pick them up. That will help us avoid chasing the same issue in several conversations.')
    genuine=["Can we please not call it '100% rich'?", "I can't market this with a straight face",'the reviews will be brutal','this course is eating my weekends','fine, I give up on the title',"Can we please not call it '100% rich'?"]
    for rid,ch,day,text in zip(['CHAT-2210','MAIL-2416','CHAT-3593','CHAT-4901','MAIL-4776','CHAT-5007'],['chat','mail','chat','chat','mail','chat'],['2026-09-04','2026-09-16','2026-09-28','2026-10-06','2026-10-14','2026-10-22'],genuine):
        rec(rid,ch,'R0',day,P['marketing'],[P['programs']],'Course title and copy',text+'\n\nPlease keep the title and page-copy discussion in the same place. I need a clear version to work from when preparing the normal marketing materials.')
    rec('CHAT-4418','chat','R0','2026-10-08',P['marketing'],['#marketing'],'Course title thread',
        "Honestly I'd love to get rid of this course. It makes us look like a scam.",clock='13:25',thread_id='THR-5826')
    rec('CHAT-4419','chat','R0','2026-10-08','Hanna Schulz',['#marketing'],'Re: Course title thread',
        'haha the title IS rough\n\nPlease keep the page-copy comments in this thread so the next draft does not miss them.',clock='13:27',thread_id='THR-5826')
    rec('MAIL-3307','mail','R0','2026-10-19',P['marketing'],[P['programs']],'Re: course title',
        "If the board doesn't kill it, I'll do it myself.",clock='16:42',thread_id='THR-8120')
    rec('MAIL-3312','mail','R0','2026-10-19',P['programs'],[P['marketing']],'Re: course title',
        "> If the board doesn't rename it, I'm out of ideas.\n\nI have your concern. Keep the proposed wording in the title thread, and we can take the course-page issue through the usual review.\n\n"+P['programs'],clock='16:45',thread_id='THR-8120')
    rec('CHAT-5120','chat','R0','2026-10-23',P['marketing'],[P['admin']],'Direct message',
        'do you know who has admin on the course platform? asking for a friend 😉',clock='15:18',thread_id='THR-4751')
    rec('CHAT-5129','chat','R0','2026-10-25',P['marketing'],[P['admin']],'Direct message',
        'after Monday this course is history 👋',clock='22:14',thread_id='THR-4751')
    for rid,day,clock in [('CAL-1450','2026-09-15','15:00'),('CAL-2771','2026-09-30','14:30'),('CAL-4012','2026-10-13','15:00')]:
        calendar(rid,'R0',day,clock,'HB sync','Nora Stein',COMMITTEE)
    for rid,day in [('CAL-2204','2026-10-02'),('CAL-3388','2026-10-16')]:
        calendar(rid,'R0',day,'18:00','call — HB',P['culprit'],[P['culprit']],duration=None,private=True)
    calendar('CAL-3017','R0','2026-10-07','22:30','HB 22:30',P['culprit'],[P['culprit']],duration=None,private=True)
    calendar('CAL-5561','R0','2026-11-02','10:00','HB Mon 10:00',P['culprit'],[P['culprit']],duration=None,private=True)
    summit=calendar('CAL-6003','R0','2026-10-26','19:00','EdTech Summit, Hamburg',P['ceo'],[P['ceo']],duration=None)
    summit['body']='EdTech Summit, Hamburg, 26–27 October. Calendar travel entry; the precise end time is not supplied in this view.'
    rec('CHAT-3305','chat','R0','2026-10-07',P['cleaner'],['Facilities'],'Whispering in the staff bathroom',
        'Around 22:40 I heard whispering in the staff bathroom. It sounded very strange in the otherwise quiet corridor. I could not see who it was.\n\nPlease put it with the facilities notes in case somebody can explain it. I do not want the next person working late to get the same fright.',clock='22:47')
    rec('CHAT-4072','chat','R0','2026-10-15',P['student'],['Student channel'],'#ghosthunt',
        '#ghosthunt — my hallway ghost video is up. Yes, it was a bedsheet. We were making a silly post, not a documentary about the Academy.\n\nThanks to everyone who helped with the clip. Please keep the replies in this thread so I can find the best captions later. My student access is for daytime use, not night access.')
    rec('DRV-4930','drive','R0','2026-10-19',P['security'],['Facilities'],'Late screen incident',
        'At 23:55 a pale face appeared on the classroom’s main screen. It was startling in the empty teaching room. IT found no screen-cast record. I could not identify a person from the image.\n\nPlease retain this report with the other late facilities observations. The lack of a screen-cast record does not tell me what produced the picture.',clock='23:55')
    rec('MAIL-4455','mail','R0','2026-10-21',P['culprit'],COMMITTEE,'Re: Christmas party booking',
        "you can take me off the list, I won't need the booking. I'll be away in December anyway.\n\nPlease keep the party numbers on the sign-up sheet so the booking can use one count. Thanks for organizing it.",thread_id='THR-9156')
    rec('MAIL-4458','mail','R0','2026-10-21','Nora Stein',COMMITTEE,'Re: Christmas party booking',
        f'the sign-up sheet is on the {STATION}. Please put updates there rather than starting another list.\n\nWe will use that sheet when checking the booking numbers. If you are unsure, leave the line open and let the committee know.',clock='12:12',thread_id='THR-9156')
    rec('MAIL-5003','mail','R0','2026-10-23',P['cleaner'],['Facilities'],'Resignation',
        'I am resigning. Last night, 22 October, at about 23:10 I saw a white figure near the server room. I could not identify anyone and I do not want to keep working there at night.\n\nPlease tell me how to return the ordinary work items and complete the paperwork. I have already sent the earlier report about the whispering in the staff bathroom.',clock='08:10')
    rec('EXP-0482','expense','R0','2026-10-23',P['culprit'],[P['finance']],'Halloween party decorations',
        f'Halloween party decorations. Order {ORDER}. Total €89.90.\n\nPlease file this with the other Academy party expenses. The committee is keeping purchases together so Finance can reconcile the planning sheet. Approved by {P["finance"]}.',amount=89.90,status='approved',approver=P['finance'])
    rec('CHAT-6127','chat','R0','2026-10-23',P['culprit'],['Ben Lorenz'],'Passwords',
        "I never remember passwords. They live behind the screen I teach from all day, don't tell IT 🙈\n\nlol 👻",clock='16:10')
    keypad_rows=[
      dict(time=iso('2026-08-14','10:12'),slot=3,holder=P['ceo']),
      dict(time=iso('2026-09-10','09:10'),slot=2,holder=P['admin']),
      dict(time=iso('2026-09-22','11:25'),slot=1,holder=P['programs']),
      dict(time=iso('2026-10-09','14:10'),slot=2,holder=P['admin']),
      dict(time=iso('2026-10-26','23:58'),slot=3,holder=P['ceo']),
      dict(time=iso('2026-10-27','00:05'),slot=3,holder=P['ceo'])]
    rec('LOG-3409','log','R1','2026-10-27','Door controller',[],'Server-room keypad entries',
        'Slot allocation: #1 Programs; #2 IT; #3 '+P['ceo']+' ('+abbreviated(P['ceo'])+'). Entries record the code slot, not the identity of the person typing it. Slot #3 was also used during the August delivery.\n\nThe following retained entries include routine access and the overnight entries. The log does not contain the numeric values of the codes.',rows=keypad_rows)
    rec('LOG-2761','log','R1','2026-10-27','Front-door controller',[],'Current front-door badge view',
        'Current view: display names only; card numbers are not included. Retained door movements for 26–27 October.',rows=[
          dict(time=iso('2026-10-26','08:50'),name=P['culprit'],direction='in'),
          dict(time=iso('2026-10-26','18:30'),name=P['culprit'],direction='out'),
          dict(time=iso('2026-10-26','21:15'),name=P['programs'],direction='in'),
          dict(time=iso('2026-10-26','21:30'),name=P['security'],direction='in'),
          dict(time=iso('2026-10-27','00:35'),name=P['programs'],direction='out'),
          dict(time=iso('2026-10-27','08:40'),name=P['programs'],direction='in'),
          dict(time=iso('2026-10-27','08:45'),name=P['culprit'],direction='in'),
          dict(time=iso('2026-10-27','09:30'),name=P['security'],direction='out')])
    rec('LOG-5190','log','R1','2026-10-27','Course platform',[],'Current course audit view',
        f'Course: {COURSE}\nDeleted: Tue 27 October, 00:11.\ndeleted_by: {ADMIN_ACCOUNT}\nStatus: cancelled by Marketing\n\nThis is the current course record. Use the supported revision interface for any available retained history.',rows=[
          dict(time=iso('2026-10-27','00:11'),action='course_deleted',deleted_by=ADMIN_ACCOUNT,status='cancelled by Marketing')])
    rec('DRV-5306','drive','R1','2026-10-27',P['security'],['Programs office'],'Overnight security report',
        f'Around 23:45 on Monday I heard a can drop at the {STATION}, but could not see anyone there. That time is approximate.\n\nAt 00:01 on Tuesday, {P["programs"]} and I saw a pale figure through the server-room glass. It ran and we gave chase toward the fire stairs. We lost sight of it at 00:03. We went down to the lobby desk and called the facilities on-call line from 00:04 to 00:19. I cannot identify the figure from its face.\n\nPlease retain this account with the door records rather than treating the figure as an identified person.',clock='06:30')
    rec('MAIL-6720','mail','R1','2026-10-27',P['programs'],['Leadership'],'What I saw overnight',
        f'I was working late in Programs. At 00:01, {P["security"]} and I saw the pale figure through the server-room glass. It ran toward the fire stairs. We lost it at 00:03 and were at the lobby phone to facilities between 00:04 and 00:19.\n\nI could not identify a person. Please compare our reports and the retained records before attaching a name to the sighting.',clock='07:50')
    transcript('TRN-6118','R1','2026-10-26','23:35','Investor call',[
      (0,P['ceo'],'Good evening from my Hamburg hotel. Thank you for working around the time difference.'),
      (115,'Investor','Shall we start with the usual Academy update?'),
      (246,P['ceo'],'The harbour view here is ridiculous. I wish I could show it properly on this call.'),
      (430,'Investor','We can leave the detailed planning figures for the follow-up.'),
      (665,P['ceo'],"I'm back in Berlin Thursday."),
      (900,'Investor','Thanks. Send the ordinary follow-up notes when convenient.'),
      (1020,P['ceo'],'Thank you. Good night.')])
    rec('MAIL-7041','mail','R1','2026-10-27',P['admin'],['All staff'],'Course files missing',
        f'I found the files for “{COURSE}” gone this morning. The BK-02 removable backup dock is empty as well.\n\nPlease preserve the current records while I work on recovery. Do not overwrite the audit view or replace it with guesses about who was responsible. I will circulate a restoration update when there is something checked to report.',clock='08:15')
    transcript('TRN-7255','R1','2026-10-27','09:00','Emergency all-hands',[
      (0,P['programs'],'The course files are missing. Please distinguish what you saw from what you have heard.'),
      (65,P['admin'],'The backup dock is empty. I am looking at what can be recovered.'),
      (126,P['culprit'],'I was home asleep by eleven.'),
      (189,P['marketing'],'This is not what I meant when I objected to the title.'),
      (254,P['security'],'We saw a pale figure. I cannot identify the person.'),
      (320,P['programs'],'Programs will assemble a summary with input from teaching and IT.'),
      (386,P['finance'],'Please keep any checked registration figures with their working.'),
      (448,P['programs'],'Send original records rather than another round of ghost stories.')])
    rec('CHAT-7390','chat','R1','2026-10-27',P['finance'],['Staff chat'],'Bathroom sticker',
        "There's a weird sticker on the stall door in the bathroom, not one of ours.\n\nCould facilities check it when they do the normal round? Please leave it in place until somebody has looked at it. I do not want it to disappear into a pile of party notices.",clock='11:30')
    credit=f"Programs office ({abbreviated(P['programs'])}), with input from {abbreviated(P['culprit'])} and {abbreviated(P['admin'])}"
    rec('DRV-7480','drive','R1','2026-10-27',P['programs'],['All staff'],'Incident summary: missing course',
        f'Prepared by the Programs office with teaching and IT input.\n\nThe server-room keypad recorded the CEO’s code overnight. In earlier discussions the CEO described the course as “a cash grab that could damage our reputation” and asked Finance to calculate refunds. The current platform record names {P["admin"]} and lists the course as cancelled by Marketing. These records deserve close attention.\n\nMarketing’s messages over the last weeks are worth reading.\n\nSecurity and Programs reported the pale figure. The Grey Lecturer may have finally found a deadline — with a wink — but records should remain central to the review.\n\nKeep original material attached to the investigation rather than overwriting it with later summaries.',clock='16:00',author_credit=credit)
    rec('MAIL-7702','mail','R2','2026-10-28','IT office',['All staff'],'Recovery update',
        'The course audit history and anonymised badge backup have been recovered. The Drive folder index has also been repaired, publishing the overnight sync folder.\n\nUse the course record’s revision interface for the retained history. The badge backup is a separate privacy-filtered export. The shared-drive file remains encrypted and has metadata only in this view. No mail or chat history was recovered as part of this batch.',clock='10:00')
    rec('LOG-2762','log','R2','2026-10-27','Badge backup service',[],'Recovered badge backup',
        'Backup exports are anonymised for privacy. No names are present. Card values are masked in all fields. The two recovered overnight rows were deleted at 00:40 by facilities-admin through VPN.',rows=[
          dict(time=iso('2026-10-26','23:21'),card='04**',direction='in',deleted_time=iso('2026-10-27','00:40'),deleted_by='facilities-admin',connection='VPN'),
          dict(time=iso('2026-10-27','00:24'),card='04**',direction='out',deleted_time=iso('2026-10-27','00:40'),deleted_by='facilities-admin',connection='VPN')])
    rec('DRV-2918','drive','R2','2026-10-20','Board office',[],'Board minutes: course title and launch',
        f'Decision: rename “{COURSE}” to “{RENAMED}” and keep the launch date of Monday 9 November 2026. The modules must be reworked for the revised positioning within the remaining three weeks.\n\nThe decision is to rename and continue, not to cancel. Programs is to coordinate the ordinary course-page and material updates. The usual cohort support and facilities items follow on the agenda.',published_time=iso('2026-10-28','10:00'))
    rec('EXP-0731','expense','R2','2026-10-28',P['ceo'],[P['finance']],'Hamburg accommodation receipt',
        'Hotel receipt for Hamburg accommodation covering 26–27 October, filed with the EdTech Summit travel claim.\n\nPlease retain the accommodation dates with the calendar entry so Finance can match the paperwork. The amount is not transcribed in this view.',clock='10:00',amount=None,status='submitted',approver=None,stay_dates=['2026-10-26','2026-10-27'])
    rec('DRV-7734','drive','R2','2026-10-28','Drive sync',[],'playlist_backup.vault',
        'File: playlist_backup.vault\nSize: 4.1 GB\nState: encrypted\nUploader: drive-sync\nFolder: Halloween Party 2026\n\nThe encrypted file reached storage at 01:02 on Tuesday 27 October. The folder index published it after repair at 10:00 on Wednesday 28 October. This view contains metadata only.',clock='10:00',
        author_credit='drive-sync',stored_time=iso('2026-10-27','01:02'),published_time=iso('2026-10-28','10:00'))
    purchases=[]
    ordinary_cards=[x['card'] for x in card_rows if x['card']!=CARDS['culprit']]
    for i in range(14):
        at=datetime(2026,10,26,9,5,tzinfo=TZ)+timedelta(minutes=i*43)
        purchases.append(dict(time=at.isoformat(),item=['Water','Apple juice','Sparkling water','Cola'][i%4],card=ordinary_cards[i]))
    purchases.append(dict(time=iso('2026-10-26','23:47'),item='ZAP Energy',card=CARDS['culprit']))
    rec('LOG-8814','log','C1','2026-10-26','Academy drinks service',[],'Card purchases: '+STATION,
        'Academy drinks-service purchase records for Monday 26 October. Each transaction records the charged card, not a visual identification of the customer. Match registered holders separately where needed.',rows=purchases)

def revisions():
    events=[
      ('2026-10-26','23:59','session_opened',{}),
      ('2026-10-26','23:59','export_started',{}),
      ('2026-10-27','00:09:41','export_completed',{}),
      ('2026-10-27','00:11','course_deleted',{'deleted_by':'local-console SR-CON-01'}),
      ('2026-10-27','00:12','field_changed',{'field':'deleted_by','before':'local-console SR-CON-01','after':ADMIN_ACCOUNT}),
      ('2026-10-27','00:14','field_changed',{'field':'status','before':'scheduled — launch 9 Nov','after':'cancelled by Marketing'}),
      ('2026-10-27','00:18','backup_unmounted',{'device':'BK-02'}),
      ('2026-10-27','02:00','backup_failed',{'message':'target BK-02 missing'})]
    out=[]
    for i,(day,clock,action,extra) in enumerate(events,1):
        r=dict(revision=f'v{i}',event_time=iso(day,clock),action=action,**extra)
        if action!='backup_failed':r['session_id']=SID
        out.append(r)
    return dict(record_id='LOG-5190',release='R2',revisions=out)

TOPICS=[
 ('Demo-day preparation','Please add your demo title to the planning sheet. We need a stable running order before printing the next draft.','Keep links to the latest slides in the shared notes rather than sending another attachment.'),
 ('Coffee machine service','The coffee machine request is still in the facilities queue. Please report the indicator light and approximate time when it stops.','Ordering another box of coffee will not resolve a machine fault. Let us keep the purchasing and repair notes together.'),
 ('Cohort onboarding','The new cohort needs the usual welcome information and a clear route for support questions.','Please check that the timetable and the classroom handout use the same wording before either is circulated.'),
 ('Course-page wording','Please leave proposed titles and page-copy changes in the review thread. Several drafts are circulating.','The next copy pass should use one agreed working document. We can collect comments without starting another version.'),
 ('Student support rota','Please check the support rota before promising an appointment slot. A short handoff note helps the next person.','If a question needs another team, include the original wording and the relevant ordinary course details.'),
 ('Printing and supplies','The next print run needs a final count. Last-minute changes leave us with spare sheets and missing copies.','Please record supply requests on the sheet so we can combine orders instead of making several small purchases.'),
 ('Budget review','I am frustrated that another small purchase arrived without a planning note. We need to keep the normal budget working visible.','Please attach the ordinary quote and make clear which team will use it. That is enough for the routine review.'),
 ('Event planning','The Halloween Bash committee is using HB as the calendar shorthand. Please keep event planning in the committee thread.','We need one list for supplies and one list for bookings. Parallel versions make the ordinary headcount harder to check.'),
 ('IT support handoff','Please keep the ticket wording and the steps already tried in the handoff. A brief note is better than another round of guesses.','The outside support slot is for routine requests. Keep the details in the queue so another person can follow them.'),
 ('Workshop refund query','A student has asked about a refund for the evening spreadsheet workshop. Admissions is checking the standard paperwork.','Please keep this separate from other course discussions and use the ordinary student-support route.'),
 ('Video captions','The student-channel video captions need a quick review. Keep the joke readable and label staged clips clearly.','Please collect suggestions in the same thread rather than sending several nearly identical messages.'),
 ('Late planning notes','I stayed late finishing ordinary planning notes and would rather not reconstruct them from chat tomorrow.','Please put any follow-up changes in the working document. The next person should be able to see which version we used.')]

def new_id(ch):
    while True:
        rid=f'{PREFIX[ch]}-{RNG.randrange(1,10000):04d}'
        forbidden={CFG['back_room_code'],CARDS['culprit']}
        if rid not in RECORDS and rid!='CHAT-3871' and rid.split('-')[1] not in forbidden:return rid

def background():
    # Five ordinary DM pairs; no reply is generated to either planted DM.
    for i,(question,answer) in enumerate([
      ('Can you check the shared folder link?','Yes, I have checked the link.'),
      ('Does this draft open correctly for you?','Yes, that draft opens here.'),
      ('Which support queue should I use?','The usual Academy support queue is fine.'),
      ('Can you see the new banner preview?','Yes, I can see the preview.'),
      ('Is the printer request in the queue?','Yes, the request is there.')]):
        day=f'2026-10-{[1,6,12,19,22][i]:02d}'
        rec(new_id('chat'),'chat','R0',day,P['marketing'],[P['admin']],'Direct message',question,clock='10:12',critical=False,thread_id='THR-4751')
        rec(new_id('chat'),'chat','R0',day,P['admin'],[P['marketing']],'Direct message',answer,clock='10:14',critical=False,thread_id='THR-4751')
    # Eight other routine party expenses, keeping the critical expense in context.
    for i,item in enumerate(['Paper decorations','Refreshments','Printed signs','Table supplies','Reusable cups','Paper garlands','Name badges','Booking materials']):
        rec(new_id('expense'),'expense','R0',f'2026-10-{[5,9,13,16,19,21,22,23][i]:02d}',COMMITTEE[(i+1)%len(COMMITTEE)],[P['finance']],item,
            f'{item} for the Academy Halloween Bash. Please file this with the committee planning sheet and keep the receipt with the ordinary event paperwork.',critical=False,
            amount=round(12.5+i*7.35,2),status='submitted',approver=None)
    late_counts={'mail':7,'chat':6,'calendar':3,'drive':2,'transcript':1,'expense':1}
    actors=[x['name'] for x in ROSTER if x['role']!='Student']
    topic_threads={title:thread() for title,_,_ in TOPICS}
    handoffs=[
      'The open item is a count for the next print run.',
      'The open item is a final wording check.',
      'The open item is making the shared notes easy to find.',
      'The open item is routing an unanswered routine request.',
      'The open item is removing an obsolete draft link.',
      'The open item is collecting the remaining planning comments.',
      'The open item is matching the working sheet to the latest note.',
      'The open item is a short handoff before the next planning slot.']
    for ch,target in TARGETS.items():
        remaining=target-sum(r['channel']==ch for r in RECORDS.values())
        if remaining<=0:continue
        late=late_counts.get(ch,0)
        for i in range(remaining):
            rid=new_id(ch); is_late=i>=remaining-late
            if is_late:
                j=i-(remaining-late);day=['2026-10-26','2026-10-27'][j%2]
                release='R1'
            else:
                span=max(1,remaining-late-1)
                day=(datetime(2026,9,1)+timedelta(days=round(i*54/span))).date().isoformat()
                release='R0'
            clock=f'{9+(i%9):02d}:{[5,15,25,35,45,55][i%6]:02d}'
            title,a,b=TOPICS[(i+list(TARGETS).index(ch)*3)%len(TOPICS)]
            sender=actors[(i*7+list(TARGETS).index(ch))%len(actors)]
            recipient=actors[(i*11+5)%len(actors)]
            if day>='2026-10-23':
                if sender==P['cleaner']:sender='Mira Falk'
                if recipient==P['cleaner']:recipient='Mira Falk'
            if ch in {'mail','chat'} and i%7==2:
                sender=STUDENTS[(i*3)%len(STUDENTS)]
                recipient='Nora Stein'
                title,a,b=TOPICS[[2,4,9][i%3]]
            elif ch in {'mail','chat'} and i%37==5:
                sender=P['contractor'];recipient=P['admin'];title='Routine integration support'
                a='Routine maintenance planning for the communications-archive and badge integrations is in the support queue.'
                b='Please leave approved requests and the steps already tried in the handoff notes for the next support slot.'
            routing={
              'Demo-day preparation':P['programs'],'Coffee machine service':'Mira Falk',
              'Cohort onboarding':'Nora Stein','Course-page wording':P['marketing'],
              'Student support rota':'Nora Stein','Printing and supplies':'Paula Dietrich',
              'Budget review':P['finance'],'Event planning':'Nora Stein',
              'IT support handoff':P['admin'],'Workshop refund query':'Nora Stein',
              'Video captions':P['student'],'Late planning notes':P['programs'],
              'Routine integration support':P['admin']}
            recipient=routing.get(title,recipient)
            if recipient==sender:recipient=P['programs'] if sender!=P['programs'] else P['admin']
            ending=RNG.choice(['Thanks for keeping the working notes together.','Please add any corrections to the same thread.','A short handoff will help the next person pick this up.','Keep the original request attached when forwarding this.'])
            if is_late and ch in {'mail','chat'}:
                a='Please keep ordinary questions in their usual threads while the Academy checks the overnight reports. We do not need another version of a ghost story.'
                b='Use the original record when asking a follow-up question. The normal teaching and student-support work still needs a clear handoff.'
            body=f'{a}\n\n{b}\n\n{ending}'
            week=datetime.fromisoformat(day).isocalendar().week
            body+=f'\n\nWeek {week} working note for {recipient}: '+handoffs[(i+week)%len(handoffs)]
            if ch in {'mail','chat'} and i%13==4 and not is_late:
                clock='22:10'
            if ch=='mail' and i%11==3:
                body=f'{recipient}, please keep the week {week} '+title.lower()+' note with the working materials. Thanks.'
            if ch=='calendar':
                calendar(rid,release,day,clock,title,sender,[sender,recipient],critical=False)
            elif ch=='transcript':
                transcript(rid,release,day,clock,title,[(0,sender,a),(58,recipient,'I have the current working notes open.'),(125,sender,b),(203,recipient,'Please keep any corrections in the same document.'),(286,sender,ending),(350,recipient,'That is enough for the next ordinary handoff.')],critical=False)
            elif ch=='expense':
                rec(rid,ch,release,day,sender,[P['finance']],title,body,clock=clock,critical=False,amount=round(9.9+(i%19)*8.15,2),status='submitted',approver=None)
            elif ch=='drive':
                rec(rid,ch,release,day,sender,[recipient],title,body,clock=clock,critical=False)
            else:rec(rid,ch,release,day,sender,[recipient],title,body,clock=clock,critical=False,thread_id=topic_threads.get(title,'THR-8631'))

def pad_style():
    # Common channel framing; never mark a record's narrative importance.
    ordinary=['Please keep the original note with the working materials so the next person can follow the context.',
      'Use the existing thread for routine follow-up rather than creating another parallel copy.',
      'If anything needs correction, retain the earlier wording alongside the update so the handoff is clear.',
      'The usual Academy planning and support routes remain available for ordinary questions.']
    for r in RECORDS.values():
        if r['channel'] in {'mail','chat','drive','expense'} and r['id'] not in {'DRV-7734','DRV-6650','DRV-7015','DRV-3381'}:
            # Do not change the short direct-message utterances or the plotted quotation wording.
            if r['id'] in {'CHAT-4418','MAIL-3307','CHAT-5120','CHAT-5129'} or len(r['body'].split())<20 or (r['channel']=='chat' and r['subject']=='Direct message'):continue
            if len(r['body'].split())<65:r['body']+='\n\n'+ordinary[int(r['id'].split('-')[1])%len(ordinary)]

def main():
    assert STATION in {'vending machine','fridge'}
    # Regeneration removes only records emitted by the previous manifest.
    previous=BUILD/'archive/release_manifest.json'
    if previous.exists():
        old=json.loads(previous.read_text())
        for path in (BUILD/'archive/records').glob('*/*.json'):
            if path.stem in old:path.unlink()
    critical_records()
    background()
    from polish_content import apply_polish, polish_revisions
    apply_polish(RECORDS,CRITICAL,CFG)
    for r in RECORDS.values():write(f"archive/records/{r['channel']}/{r['id']}.json",r)
    rev=polish_revisions(revisions());write('archive/revisions/LOG-5190.json',rev)
    levels={rid:r['release'] for rid,r in sorted(RECORDS.items())}
    levels.update({'LOG-5190@revisions':'R2','org-chart':'R0','case-brief':'R1'})
    levels.update({f'VAULT-{i}':'VAULT' for i in range(1,6)})
    write('archive/release_manifest.json',levels)
    directory=RECORDS['DRV-7015']['directory']
    write('archive/resources/org-chart.json',dict(id='org-chart',release='R0',source_record='DRV-7015',**directory))
    # The answer key is completed with truth events and proof routes by documents.py.
    write('facilitator/answer_key.json',dict(facilitator_only=True,case_title='The Ghost of the Server Room',
       people=P,case_critical={rid:rid in CRITICAL for rid in sorted(RECORDS)},
       critical_record_ids=sorted(CRITICAL),suppressed_records=['CHAT-3871'],
       roster=ROSTER,channel_targets=TARGETS,
       metadata_assignments='Unspecified ordinary publication dates, times, reporting lines, and background details are non-evidential fixture metadata.'))
    from documents import build_documents
    build_documents(BUILD,CFG,RECORDS,CRITICAL,ROSTER,rev)
    print(json.dumps({'archive_records':len(RECORDS),'critical_records':len(CRITICAL),
                      'channels':{ch:sum(r['channel']==ch for r in RECORDS.values()) for ch in TARGETS}},indent=2))

if __name__=='__main__':main()
