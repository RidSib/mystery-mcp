"""Private, hand-authored fixture prose. Never deploy this authoring module.

Lists follow each existing subject's chronological order; no metadata is generated here.
The complete coverage assertion prevents a new record silently receiving template prose.
"""
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import random
import re

MAIL = {}
CHAT = {}
DRIVE = {}
TRANSCRIPTS = {}
CALENDAR = {}
EXPENSE = {}


def prose(target, topic, text):
    target[topic] = [s.strip().replace(' / ', '\n\n') for s in text.strip().split('\n---\n')]

prose(CHAT, 'Budget review', """
Ines, I see two banner requests. Is one the classroom example Ben mentioned, or are we decorating the entire street?
---
The banner quote isn't an invoice. Please stop adding it to the paid column; it makes the reconciliation very exciting. Theo
---
Can someone explain the blue total before our review? It is larger than the grey total and neither has a useful label. Thomas
---
Printing still needs a cost centre. I can chase descriptions all day but Paula can't print them against a shrug. Nora
---
Support hours are under events in my draft. Wrong dropdown, not a secret party. I'll ask Ines to move the line. Maja
""")
prose(CHAT, 'Coffee machine service', """
It did two black coffees, then sulked after mine with milk. Both buttons blinking. Yellow note updated. Wanda
---
Lukas says someone called it the coffee server again. Mira owns this ticket; please spare IT the cappuccino stack trace. Priya
---
Tea is fine but we've run out of teaspoons. Is the long one still propping up the tray?? Amira
---
New coffee sign ready. Less hazard triangle, more milk jug. Please don't laminate until Mira checks the wording. Idris
---
Visitors have started requesting peppermint by name. If coffee ever works properly again, there may be complaints. Zoe
""")
prose(CHAT, 'Cohort onboarding', """
Nora, did you find out about laptops? My tablet definitely won't run whatever is in that setup screenshot. Hadi
---
I'll use the pack's setup link in the welcome slides. Send me the corrected one, not a screenshot of the button. Marcus
---
The plain link worked! The picture button still doesn't. Leaving this here in case someone else is going round in circles. Kira
---
The contact block needs a phone check before we export it. It wraps straight through Nora's surname. Hanna
---
Bottle reminder goes above the footer, not over it. My print preview has produced a very thirsty copyright notice. Omar
---
Display name fixed now, thanks. Just one h at the end of Noah. I promise that's the final version of my name.
---
Can we keep accessibility questions out of reply-all? I'll point people to Nora directly rather than ask them for details here. Yara
""")
prose(CHAT, 'Course-page wording', """
Jule, could we keep the headline discussion above the draft paragraph? Otherwise half the comments refer to words nobody can see. Sandra
---
Which preview can admissions share? I have three versions and a strong feeling that the boldest one is the least approved. Milan
---
Need a plain enquiry reply, please. "Transformative" isn't an answer to what students actually practise. Greta
---
Two CURRENT files again. I won't pick one by modification date; that only tells us who last opened the wrong copy. Nils
---
The practice examples make sense. Could we keep them and lose the paragraph that reads like a motivational calendar? Wanda
---
Preview ticket is waiting on the actual document link. A photo of the screen won't let me repair the link. Priya
""")
prose(CHAT, 'Demo-day preparation', """
Sandra, one demo screenshot has a student's name in it. I've marked the frame, not forwarded it round the group. Yara
---
Can the programme describe what people will see? "Reimagining everything" takes up space without telling me anything. Jule
---
Swapping my group's sign-in demo for screenshots. The login screen has had enough stage time. Description update to follow. Ben
---
Three dots halfway through a project title are a typo, not an artistic choice. I've asked the team before changing it. Jana
---
The table sketch and equipment list disagree. Please settle which display you need before I wheel anything upstairs. Rafael
""")
prose(CHAT, 'Direct message', """
Is the copy folder link opening for you? Mine lands on a blank preview.
---
Yes, opens here. Try the plain link below the preview image.
---
Can you open the mobile draft? The headline wraps in a completely new and horrible way.
---
It opens. I can reproduce the wrap on a narrow window; send Hanna the screenshot.
---
Where does the broken caption preview go? Facilities has quite rightly sent it back to me.
---
IT queue, preview category. Include the browser version so we don't start from scratch.
---
Do you see the new banner thumbnail or the old orange one?
---
New one in a fresh tab. The embedded thumbnail is still cached.
---
Is the print preset request actually in your queue? Paula asked me again.
---
Yes, Lukas has it. He needs one sample pack before calling the preset final.
""")
prose(CHAT, 'Event planning', """
Can the committee pick the decoration list before I order tape? Last year's box might contain a lifetime supply. Sara
---
A photo of a carrier bag is not a receipt. It is evidence that somebody owns a carrier bag. Ines
---
I'll collect reusable decorations after the Bash. Please put me under clear-away, not "everything Elena hasn't explicitly refused".
---
Invitation link works now. Please send headcount corrections to Nora, not to the helpdesk ticket. Lukas
---
Receipt envelope is at reception. Party purchases in that one, unrelated paperwork elsewhere, or Theo will turn into a bat. Uma
""")
prose(CHAT, 'IT support handoff', """
Old rota still opens from the tablet square. New link works. Please don't mark it finished just because you tested the link. Rosa
---
The loose charger ticket is facilities. The account problem from the same student stays with IT. Two issues, one confusing subject. David
---
Could we rename "screen issue" to the equipment involved? Anton and I are now discussing two entirely different cables. Lena
---
Support invoice duplicate is marked, not removed. Ines needs to see why it appeared twice. No second visit claimed. Theo
""")
prose(CHAT, 'Late planning notes', """
Which meeting time goes on the poster? Agenda says one thing, grid another. I'm leaving the space blank for now. Idris
---
Found the old grid under the visitor papers. Taking it off the desk before it becomes authoritative by proximity. Paula
---
Green currently means checked, available AND proposed. We have invented the world's least informative colour code. Zoe
---
The crossed-out workshop slot is Wanda's old proposal. Please keep that note when exporting; otherwise it looks as if a class vanished. Clara
---
Poster uses the agreed time now. If someone changes the grid, tell me before asking Paula for more copies. Karim
""")
prose(CHAT, 'Printing and supplies', """
Paula, try short-edge binding on the folded pack. The old preset flips the last page like a party trick. Lukas
---
Sheets column is corrected. The pages column is still there for comparison; please don't add the two together. Uma
---
Hold the demo programme run until Nora has the missing descriptions. Blank project boxes aren't a print fault. Sandra
---
Bringing the old single-sided welcome pile back to reception. Most of it can become scrap without another dramatic shredding session. Milan
---
Which pile is the new folded pack? I found three stacks and one says TEST in very confident capitals. Greta
""")
prose(CHAT, 'Routine integration support', """
Priya, please put the connector error in the ticket itself. The shared attachment folder contains three exports with the same title. NordByte
---
Badge and communications-archive tickets are separate on our side. We'll cover both in the booked handoff; replying to one doesn't close the other. NordByte support
""")
prose(CHAT, 'Student support rota', """
Sandra, can Programs name cover for the planning-meeting gap? David can manage twenty minutes, not the whole support hour. Nora
---
The support sheet needs categories. "Help" currently sends laptop problems and essay questions to the same slot. Felix
---
Got the corrected support time, thanks. I'll use the appointment confirmation rather than the old welcome-pack page. Iris
---
Maja, is a second confirmation a second booking? Student support is getting nervous about disappearing slots. Nora's checking the names. Maja
---
The form now lets me write a short heading privately. Much better than describing the whole problem in the group. Lian
---
Please add the exercise's teacher to module questions. At the moment every question becomes my question by default. Marcus
---
Can I bring just the sentence I'm stuck on? It's a practice exercise question, not something that needs an account screenshot. Ola
---
Desk sign has its own stand now. Borrowing a pen should no longer reveal an obsolete support rota underneath it. Mira
""")
prose(CHAT, 'Video captions', """
Keeping the gerbil example for class if that's OK. A caption mistake with educational value at last. Ben
---
Auto-captions don't need punctuation at every inhale. I've fixed the worst ones; please don't regenerate over the edits. Jana
---
Crop the edge of the checklist, please. Facilities paperwork is not an exciting background prop, however blurry. Rafael
---
Please label staged clips in the title too. A thumbnail travels further than the sensible explanation underneath it. Anton
---
Leo, thank you for removing the bit with the board behind reception. I spotted my checklist in the first version. Rosa
---
The corrected tour captions are readable on my phone now. Dark strip behind the words worked better than giant bold text. David
""")
prose(CHAT, 'Workshop refund query', """
Do you need the whole receipt for the spreadsheet workshop, or just the payment reference? I'd rather not post it here. Gio
---
Refund instructions found on the reception shelf. Please tell me which pile is current before I put them out. Kofi
---
Could the received screen say it hasn't been approved yet? That enormous green tick is doing a lot of promising. Clara
---
Name typo on my receipt, same payment. I'll send the original confirmation directly rather than put financial details in chat. Jamal
---
Two submissions from me, sorry. The first screen didn't say received, so I tried again. Please keep just one workshop request. Mina
---
New refund instructions distinguish received from approved. I'll use those in the workshop notes instead of another homemade explanation. Dina
---
My reference is saved. Please don't merge it with the missing-course questions; mine is the evening spreadsheet workshop. Pia
---
Workshop refunds remain in the normal queue. Today's incident doesn't turn every payment question into evidence. Send me the reference, not speculation. Ines
""")

prose(MAIL, 'Coffee machine service', """
Mira, the machine took my cup hostage halfway through an espresso. Red light, about nine this morning. I rescued the cup; the coffee is less fortunate. / Before we order beans again, can someone check whether this is a water-feed problem? Ines
---
The red light is back, but only after steaming milk. Two black coffees went through fine before my class. / I put a yellow note beside the buttons so nobody keeps pressing everything. Please don't throw it out as litter. Elena
---
I checked the tray and water inlet with Mira's checklist. Nothing obvious. The warning clears after cooling down, which would explain why the morning test looked fine. / Could we ask the service company to watch it make three drinks, rather than one?
---
Admissions is sending visitors past a machine labelled DO NOT TRUST. Accurate, perhaps, but not quite the welcome we wanted. / Is there a repair estimate? If it needs a part, I would rather tell people to bring a drink than keep promising tomorrow. Sandra
---
Six people asked whether the yellow coffee notice means the whole Academy water supply is unsafe. Could we change the heading? / I can print something less dramatic. The phrase "steam fault" would save me several conversations before lunch. Milan
---
The visitors now think we have banned milk. Progress of a sort. / I've been offering tea while the repair is pending; we're almost through the peppermint box. Please include a small replacement box in the normal order, not another emergency shop run. Greta
---
Service desk wants the exact warning pattern: red steady, red blinking, or both buttons blinking. The photo in the thread is too blurry to tell. / Can you note that next time it fails? No need to unplug it again. Nils
---
Both buttons blinked after a cappuccino at break. I wrote that on the yellow note, underneath Milan's polite heading. / Also: whoever is using a teaspoon as a drip-tray prop, please stop. It's the last long spoon. Wanda
---
This isn't in the IT queue any more, is it? Lukas was asked to "restart the coffee server" and came upstairs with a laptop. / Facilities should have the service booking. I'll close our duplicate ticket once you confirm. Priya
---
Mira, the new notice is readable from a sensible distance now. I used a tiny milk jug icon rather than the angry triangle. / Send the final wording if the engineer changes the instructions; I kept the editable file. Idris
---
Reception has the service email printed beside the visitor book. It says the steam assembly still needs attention, so I've left the warning up. / Shall I keep the tea station through this week? Visitors are getting surprisingly loyal to peppermint. Paula
""")

prose(MAIL, 'Budget review', """
Ines, why is the same banner quote on both the events sheet and marketing's list? I only asked for one banner. / Please don't approve two because our tabs disagree. I can live without a bigger logo; I cannot explain buying it twice. Jule
---
I think the duplicate is my fault. I copied the events row to show my class the layout and forgot that the sheet totals every visible line. / It was a demonstration, not a second request. Can you strike my row rather than delete the original? Ben
---
The banner supplier has asked for an answer again. Their quote expires before our review slot. / Could you mark the row approved, declined or waiting? A blank cell makes everyone assume someone else has dealt with it. Anton
---
Ines, my cleaning supplies are mixed into the event total. Those gloves are for work, not for decorating anything. / Can they go back under facilities? I don't want Mira being told she has used the party budget on bin bags. Rosa
---
There are now three totals at the bottom of that sheet. The little grey one excludes the copied banner row; the big blue one doesn't. / I've labelled them but haven't changed anybody's numbers. Which total are we taking to the review? David
---
The broken-monitor replacement is sitting under "nice to have" again. It is not an extra screen; it replaces the one that cuts out during support appointments. / I'm attaching the existing quote to that row, not asking for a second purchase. Lena
---
I've reconciled the banner entries. One quote, one requested item, no invoice yet. The deleted demonstration row was still inside a hidden subtotal. / Please use the total labelled REVIEW, not the blue number from last month's screenshot. Theo
---
Can you release the small print allowance today? We have names for the demo programme, but Paula won't print until there is a cost centre. / I know the banner conversation was painful. This is paper, not another banner. Nora
---
Ines, the welcome packs have eight spare folders. Should I return them to supplies or hold them for late joiners? / I haven't ordered replacements. The spreadsheet is showing a shortage because someone counted packs issued rather than folders remaining. Felix
---
The October budget file opens read-only for me. That is fine for checking totals, less useful for explaining the platform-support line. / My comment is a reclassification, not extra spend: support hours are under events because I selected the wrong dropdown. Maja
""")

prose(MAIL, 'Cohort onboarding', """
Hi Nora, my welcome email says bring a laptop but the checklist says equipment provided. I only have an old tablet. / Should I borrow a laptop before the first session, or is the checklist the newer version? Hadi
---
Nora, both equipment instructions are still live. The checklist refers to the classroom display kit, not student laptops. / Could the welcome email say that explicitly? I'm happy to check a rewritten sentence; I can't lend everyone a laptop at the desk. Lena
---
The welcome pack payment page gives a different contact from the email. Please point payment questions to Finance and timetable questions to Programs. / We spent half the morning forwarding the same two messages back to each other. Theo
---
Sorry for the late email. I've read the equipment note three times and still can't tell whether we need to install anything before arriving. / If there's a setup list, could you send the actual link? The button in my pack is just a picture. Kira
---
Nora, can we put a human contact on the first page? The pack currently sends a new student through three menus before they can ask a question. / Keep the checklist, but move the welcome back above the administrative bits. Thomas
---
Sandra, I've pulled the conflicting equipment lines out of the pack. The replacement distinguishes student laptops from the classroom display. / Before I send it, can you check that teachers are using the same setup list? Kira's screenshot shows an older button. Nora
---
My pack arrived, thanks. Tiny problem: my name is Noah, not Noahh. I can survive the extra h, but I'd rather it didn't migrate onto the attendance sheet. / The email address is correct, so I think it's just the display name.
---
The corrected pack is much clearer. I've put the setup link in the welcome reply instead of attaching another PDF. / One student has already found the old image-only button in a forwarded copy. Can we retire that version completely? Felix
---
Hi Nora, I got the forwarded pack with the broken button. The link Felix sent works, but it asks me to choose a cohort and mine isn't obvious. / Is it listed by start date or by the teacher's name? Rami
---
The setup page sorts by start date. The teacher field is a filter, not the cohort name. / I'll add that label to the help text. Please send me any screenshots with personal details covered; I don't need a student's whole account to fix a button. Maja
---
Do we have to print the pack? My printer has decided pale yellow is the only colour it believes in. / I can bring the checklist on my laptop if that's acceptable. Vera
---
The welcome slides have a few practical notes about keeping learning journals. I'll use the same setup link Nora circulated, so we don't spend the first session comparing versions. / Can someone tell me when the corrected pack has gone out? Marcus
---
Could the pack ask people to bring a refillable bottle? We're getting stacks of disposable cups after every welcome session. / I'll keep a few spares at reception, but "bring a bottle" would save more effort than another recycling sign. Mira
---
Hi, is the welcome checklist meant to be ticked off online? Mine saves the first three boxes and then forgets them. / I can write it on paper, just checking whether you actually need to see my progress. Celia
---
I've checked the pack on a phone. The contact names wrap awkwardly, but the equipment distinction is finally readable. / Please stop sending screenshots of the old cover for approval; the version with the green underline is the one I've just reviewed. Hanna
---
Nora, where do accessibility questions go? I don't want to put personal details in a reply-all to the welcome message. / A direct contact would be helpful. I have the timetable already; it's the session materials I need to ask about. Flora
---
One last pack snag before tomorrow: the bottle reminder overlaps the footer on the print version. It looks fine on screen. / I'll shorten the facilities paragraph in the morning. Please don't print another pile tonight from this copy. Omar
---
The corrected pack is the one reception is sending now. I added a plain-text setup link below the button for anyone using an older forwarded email. / I'm keeping individual accessibility questions out of the group replies. Yara
""")

prose(MAIL, 'Course-page wording', """
Jule, which headline should go above the introductory paragraph? The mock-up and the copy sheet disagree. / I've left a yellow box rather than guess, but it makes the draft look as if we're selling highlighters. Karim
---
Before we request a new print quote, can you freeze the headline length? Every extra line changes the size of the leaflet. / I'm not asking you to approve the words today, just whether we're designing for one line or three. Sara
---
The learning outcomes are doing too much work underneath that promise. Could we lead with what students will practise, rather than what their lives will become? / I marked two examples in the margin. Nothing else needs rewriting yet. Dina
---
Jule, please remove the draft price badge from the copy review. People keep discussing whether it is an offer and I only put it there to test spacing. / The real pricing belongs in the registration figures. Ines
---
The preview link opens. The old thumbnail is cached, though, which is why people think their changes vanished. / Try a fresh tab before resending the whole file. I'll flag the preview issue to Maja separately. Lukas
---
The leaflet footer still points to last month's copy sheet. I can correct that link in the purchasing pack once you tell me which document is final. / Please use a filename humans can distinguish from "final final new". Uma
---
I've read Dina's notes. Bring the outcomes paragraph to the next discussion and leave the headline decision visible above it. / We keep approving the paragraph while arguing about a title in a different window. That's how the wrong draft keeps coming back. Sandra
---
Admissions is getting questions about what "guaranteed" means in the draft screenshot. We need an approved response before I send anything else out. / I have stopped forwarding the screenshot; I haven't changed the public page. Milan
---
Jule, could we have three plain sentences for enquiries? The draft is full of slogans and I don't want to improvise a promise on the phone. / Dina's practice examples would be more useful than another adjective. Greta
---
The preview folder contains two files both labelled CURRENT. I've renamed neither, because I don't know which approval belongs to which one. / Please identify the right file in the review sheet; then I can tidy the link. Nils
---
The page-copy ticket is still open. This morning's incident hasn't magically resolved which preview is current, and I won't guess from a screenshot. / Send me the document link when you're ready; the missing-course work is taking priority. Priya
""")

prose(MAIL, 'Demo-day preparation', """
Sandra, can we make the demo programme useful to visitors who don't already know the projects? A list of clever titles isn't enough. / One sentence per team, with what the audience will actually see, would help. Thomas
---
I've added a column for the one-sentence descriptions Thomas requested. Please don't put full scripts in there; the programme will be a single folded sheet. / The first two teams have submitted, so there is something to copy the format from. Nora
---
Students keep asking whether the demo order is also their assessment order. Can you confirm the wording before I reply to the group? / I can collect missing descriptions, but I don't want to invent a grading rule. Felix
---
The demo upload form accepts links, not video files. Someone tried to paste a whole recording into the description box. / I'll add a smaller example underneath it. Could teachers check their teams' links before handing the list to Nora? Maja
---
Two projects need audio and one needs a very small table. The current running order puts the noisy ones together, which might be kinder to everyone. / Shall I add equipment needs beside the descriptions, or will that break the print layout? Viktor
---
My teams' descriptions are now in the sheet. I shortened the one that read like an entire grant application. / Please keep the practical demo instructions separate from the visitor blurb; students are using both and mixing them up. Marcus
---
The programme cover works if the project descriptions stay within two lines. At the moment one team has written half a page about changing the world. / Can someone ask them what they are actually showing? Hanna
---
I checked the tables against Viktor's equipment column. The small one is available, but it won't hold the extra display somebody drew into the sketch. / Please settle the layout before I move furniture around for a third version. Omar
---
I know it's late, but the demo form has a real student name in one of the sample screenshots. Can that be cropped before the programme goes to print? / I've left a comment exactly where it appears. Yara
---
The shorter descriptions are much better. I've removed the stock "future starts here" line from the cover; the projects can speak for themselves. / If Thomas wants a welcome paragraph, I need it before Paula prints, not after. Jule
---
My group has replaced its live sign-in demo with screenshots. We were losing half the slot waiting for the login prompt. / The description still says "live walkthrough"; could that become "guided walkthrough" in the print copy? Ben
---
I've proofread the programme and fixed the doubled word in the welcome paragraph. There are still two project titles without descriptions. / I'll leave those spaces visible rather than fill them with nonsense. Please chase the teams before the next print run. Jana
""")

prose(MAIL, 'Event planning', """
Nora, are we calling the committee Halloween Bash in full on the first invite? "HB" means nothing to my students. / I can help collect numbers, but I need a date line and a reply destination before I tell them anything. Amira
---
I've sketched the party sign in orange and black. If we put every committee member's suggestion on it, the pumpkin will need a second poster. / Which two pieces of information matter most? My vote is what it is and where to sign up. Idris
---
Reception is getting party questions that belong to the committee. Can the next notice point people to one list? / I have three pencilled headcounts, all different, and I don't want the smallest number to become a booking by accident. Paula
---
Can we sort the food question before collecting more names? Someone has put "normal food" in the preference column, which tells me almost nothing. / I'll ask people for specific dietary requirements rather than interpret it. Zoe
---
For the Halloween Bash, please keep decorations clear of door glass and access routes. I don't mind paper bats; I do mind walking into a hanging string in the dark. / Send Mira the layout if you are moving tables. Kofi
---
I'll bring scissors and the reusable decorations box to the committee meeting. Please don't order another bag until we see what's left in it. / There were enough paper pumpkins last year to start a modest farm. Clara
---
The decorations box contains more tape than decorations. Before I put a supply order through, could the committee decide what it is actually making? / I can combine this with the next stationery delivery and avoid another postage charge. Sara
---
I've made a tiny task list: cut, hang, clear away. At present everyone has volunteered for the first two. / Can someone take clearing away before I let my class make another twenty bats? I'm looking at you, enthusiastic committee. Dina
---
HB expenses need receipts, even when the item costs less than lunch. Please don't send a photo of a shopping bag and ask me to calculate what was inside. / Put the purchaser's name beside the line on the committee sheet. Ines
---
I can take the clear-away slot, provided the sticky things aren't on painted walls. Last year's blu-tack archaeology took longer than the event. / Put me down for collecting reusable bits, not supervising the whole evening. Elena
---
The invitation preview is working again. The old thumbnail may linger, but the link goes to the committee copy. / I haven't touched anybody's headcount. Please ask Nora about names rather than opening another IT ticket. Lukas
---
The party receipts are in their own envelope at reception, separate from the incident paperwork. People keep dropping everything under "Halloween" and expecting Finance to divine the category. / I'll match these to the committee sheet once Nora confirms the last few purchases. Uma
""")

prose(MAIL, 'IT support handoff', """
Priya, the caption preview fails on my laptop but works on the classroom machine. Same file, same link. / I've written down the browser versions instead of taking another photo of the error. Is that enough for the ticket? Hanna
---
The facilities tablet keeps opening the old rota from its home-screen shortcut. Refreshing the page works; tapping the icon starts the problem again. / I can remove the shortcut if you tell me which link should replace it. Omar
---
We have two students replying to an automated message that says "do not reply". Their questions disappear into the notification mailbox. / Can we change that footer to the support contact? I'll gather the examples without forwarding their personal details. Yara
---
Evening queue handoff: the caption ticket has a browser version now, the tablet ticket has a repeatable shortcut problem, and the notification footer is still wrong. / I'm leaving the notes here before I forget which screenshot belongs to which. Ben
---
The notification footer now names student support. Please check the wording before the next template goes out. / I removed "our friendly robot" from the draft because it wasn't helping anyone understand where their reply went. Jana
---
There's a ticket about a loose charger in with the account-access requests. I've moved the charger to facilities and left the account question with you. / Same student, two problems; the shared subject line was confusing the handoff. Rafael
---
Can the event team borrow the spare display cable, or is it already booked for demo preparation? The support queue just says "screen issue". / I'll ask for the actual equipment name next time. Apparently I am now a cable detective. Anton
---
Priya, the cleaner's tablet still goes to the old rota when I use the square on the first screen. Omar's new link works if I type it. / Please don't close the ticket as fixed until that square goes away. Rosa
---
I found a duplicate support invoice in the review folder. It is the same document exported twice, not two visits. / Please leave one marked duplicate while Ines checks it; simply deleting it makes the gap look worse. Theo
---
Can we have a short list of unresolved support issues for the weekly review? I'm seeing forwarded screenshots without the question that goes with them. / Keep it to a few lines per item. The review needs decisions, not a tour of everybody's inbox. Thomas
""")

prose(MAIL, 'Late planning notes', """
Priya, Programs has three copies of the planning grid and the one linked from the agenda is the oldest. / Can you check the shortcut? I'll fix the document titles once I know which link people have actually been using. Sandra
---
I've marked the current admissions questions in the planning grid. Please leave the unanswered ones visible even if they make the sheet untidy. / Last time a tidy-up turned "not agreed" into a very convincing blank cell. Greta
---
The shortcut points to the right folder now. Two grids inside it still have the same title. / I can repair a link, but I can't choose which staffing plan Sandra approved. Someone in Programs needs to label that explicitly. Nils
---
Sandra, my late workshop slot is listed twice in the grid. One is the old proposal, not a second session. / Please cross it out before the rota goes round. I enjoy teaching, but I haven't discovered how to be in two places. Wanda
---
The grid isn't broken. It is showing both Wanda's draft slot and the agreed one because the draft checkbox was never cleared. / I've explained that in a comment and left Programs to change the plan. Please stop calling this a platform outage. Priya
---
I can cover the earlier planning slot, not the late one. The spreadsheet colours make it look as if green means available everywhere; my note says otherwise. / Could we use words as well as colour before this becomes the published rota? Amira
---
Sending this now because the poster layout is still open on my screen: the meeting time in the grid and the agenda heading differ. / I haven't changed either. Which should the notice use in the morning? Idris
---
The corrected time is on the notice now. I kept the previous PDF in the draft folder with DRAFT across it so nobody prints it from a forwarded email. / Can we stop using green ticks to mean both checked and available? Zoe
---
If these planning sessions run late, let facilities know through the normal booking route. A calendar colour isn't a building-use request. / I need to know which rooms are booked, not read every disagreement about the rota. Kofi
---
The grid has one live version at last. I checked my workshop line and the duplicate proposal is crossed out. / Please leave the explanatory note attached when you export it; otherwise Wanda's old slot will look like an unexplained cancellation again. Clara
""")

prose(MAIL, 'Printing and supplies', """
Paula, a print job labelled "final notice" has been sitting at reception all evening. Is it meant for display or for someone's meeting pack? / I left it face down on the shelf rather than put an unknown notice on the wall. Kofi
---
The notices on your shelf are mine. Only the top copy is for display; the rest were a test of the grey background. / Please recycle the tests. I will put my name in the job title next time, lesson learned. Clara
---
Could we use thinner paper for the draft leaflets? The thick stock is lovely but the fold springs open like a tiny trap. / I only need enough draft copies to check the page order. Karim
---
The paper quote assumes single-sided pages. If the packs are duplex, our quantity is almost double what we need. / Please confirm before I place the order. A page count and a sheet count are different things, however much the form wishes otherwise. Sara
---
I've held the paper purchase until the duplex count is settled. This is not a budget refusal; I don't want six boxes arriving because two columns share the word "pages". / Paula, can you put one sample pack beside the order sheet? Ines
---
I made the sample pack. The last page prints upside down when we use the old preset, which may explain why people switched back to single-sided. / Could we name a working preset after the pack rather than "custom three"? Elena
---
The duplex setting needs short-edge binding for that folded pack. I saved a preset called Folded pack TEST so nobody mistakes it for an approved print run. / Paula, please try one copy before removing TEST from the name. Lukas
---
The sample is right-side-up now. I recalculated the order using sheets, with a small allowance for test copies. / The old total is crossed out rather than hidden. Ines can see why it changed without reopening this entire thread. Uma
---
The print count is approved for the corrected folded pack. Please don't include the outstanding demo descriptions as blank extra pages. / Nora is chasing those separately; hold that programme run until the text arrives. Sandra
---
Paula, the welcome desk is still handing out the single-sided pack from the old pile. Shall I bring it back to reception? / We don't need to shred it dramatically. Most pages are usable scrap, once the front sheet is removed. Milan
""")

prose(MAIL, 'Routine integration support', """
Priya, this month's support slot can cover the communications-archive connector and the badge integration. Please send the ticket numbers before the call. / We need the failed step and the time it happened, not a folder of unrelated screenshots. NordByte support
---
We received the integration ticket list. The attachment labelled "latest" duplicates the earlier export; the connector error itself is only in the second screenshot. / Could you mark the relevant example in the ticket so the engineer doesn't repeat the same triage? NordByte
---
Following up on the scheduled support handoff: please confirm which connector questions remain open. The badge and communications-archive items have separate queues on our side. / A reply in one ticket won't automatically update the other. We can discuss both in the booked slot. NordByte support
""")

prose(MAIL, 'Student support rota', """
Nora, the support desk notice has two different lunch breaks. I'm putting the newer sheet on top for tomorrow, but I can't tell whether that is the agreed rota. / Please check before students start queuing against a slot nobody covers. Rafael
---
Hi, I came for the support hour printed in the pack and found a notice saying afternoon. Which one should I use next week? / It isn't urgent, but I don't want to miss another appointment by following the wrong page. Iris
---
The old support sheet is still under the new one on the desk. People turn it over when they borrow a pen and then read the wrong side. / I'll take the loose copy to reception unless somebody needs it for records. Rosa
---
Could I book a support slot without explaining the whole question in the group chat? The booking form asks for a public comment. / I'd rather give a short heading and talk through the details privately. Lian
---
I can cover the first half of the support hour while Nora is in the planning meeting. Put my name on that portion only, please. / The last rota made a twenty-minute favour look like an entire afternoon commitment. David
---
Can the support rota distinguish technical appointments from coursework questions? Someone booked me to review an essay because both slots say "help". / I'm happy to fix a login; I am dangerously unqualified to grade the essay. Lena
---
Is the support desk allowed to help with practice exercises, or is it only for account problems? I ticked "other" and the form gave me no next step. / A sentence explaining the categories would be useful. Ola
---
The revised categories are clearer, but Finance questions should still come to us rather than the general queue. / I'll send Nora a short description of what to forward. Nobody needs a student to repeat a payment problem to four desks. Theo
---
Please make sure the rota has a named handover for uncovered slots. A blank cell isn't a service plan. / If we cannot offer an appointment that day, say so plainly instead of leaving reception to improvise. Thomas
---
The form says my slot is reserved but I didn't get a confirmation. Should I submit it again? / I don't want to book the same person twice. The time shown on the final screen was correct. Sina
---
Sandra, we've separated technical, coursework and Finance questions on the rota. The remaining issue is cover during the planning meeting. / David can take twenty minutes, not the full hour. Can Programs identify someone for the other part before we publish it? Nora
---
Hi Nora, is a screenshot enough for a support appointment? The form asks for an attachment, but my question is about the exercise instructions rather than something broken. / I can paste the sentence that confused me. Ada
---
The booking confirmation now shows the same slot as the final screen. Sina's example helped reproduce the missing email. / Please don't tell everyone to submit again; that creates duplicate bookings and makes the available times look full. Maja
---
Sorry, just noticed I booked a technical slot for a coursework question. Can it be moved rather than cancelled and started again? / The form categories are clearer now. I was using the link I saved from the old pack. Dario
---
I can take the coursework questions in the uncovered part of the rota this week. Please leave the technical questions with Lena. / David's note includes two practice exercises people keep getting stuck on; I'll bring those instructions. Viktor
---
The support sheet still sends module questions to me even where another teacher owns the exercise. Could we put the relevant teacher beside those appointments? / I can't usefully answer a question if I spend the slot finding out which class it belongs to. Marcus
---
My support confirmation came through twice, but both emails show the same booking. I haven't reserved two slots. / Please keep the one in the afternoon; I can ignore the duplicate message if that's easiest. Gio
---
The support desk sign is on the stand rather than loose on the table now. That should stop the old sheet resurfacing when someone borrows a pen. / I'll leave appointment questions with Nora; facilities can only promise that the sign stays upright. Mira
""")

prose(MAIL, 'Video captions', """
Leo, please put a plain description under the first student-channel clip. "Wait for it" is funny once, less useful if someone is watching without sound. / I can check the captions against the spoken parts if you send the draft. Viktor
---
The automatic captions have turned "learning journal" into "yearning gerbil". I'm not sure which is more accurate, but please correct it before the welcome clip goes round. / Send me the teaching terms that still look doubtful. Marcus
---
Could you avoid filming the noticeboard behind reception? People pin contact details there and don't expect them in a student video. / The close-up of the cups is fine. It is possibly the most flattering footage our cups have had. Mira
---
The caption contrast disappears over the pale wall. A dark strip behind the text would help more than making every word bold. / I've put a sample frame in the review sheet; you don't need to rebuild the whole clip. Hanna
---
Two students asked whether they can opt out of appearing in the channel clips. Can the caption notes point them to a direct contact? / A joke reply in the public comments isn't enough when someone wants their face removed. Yara
---
Late note before I close the preview: the opening caption sits over someone's name badge. Please crop that part or move the frame. / And please label anything staged in the actual post, not just in a comment underneath it. Jule
---
The caption examples are useful. Could we keep one version with the corrections visible for my class? / They will learn more from the gerbil mistake than from a perfectly clean screenshot, although Marcus may disagree. Ben
---
I've checked punctuation and speaker labels. The captions don't need a comma after every breath, despite what the automatic tool appears to believe. / Keep the short pauses; remove the three mysterious full stops halfway through a word. Jana
---
The student-channel clip includes the edge of a facilities checklist. Could you crop a little tighter? / Nothing dramatic, just the usual rule about not turning every wall into a public noticeboard. Mira already flagged the reception board for the same reason. Rafael
---
Leo, can the title distinguish the staged joke from the ordinary tour clip? People are forwarding the thumbnail without the caption, which defeats Jule's note. / Put the label where a hurried person will actually see it. Anton
""")

prose(MAIL, 'Workshop refund query', """
Hi Nora, I need to ask about the evening spreadsheet workshop fee. I used the wrong payment reference and the receipt has no workshop name. / Can you tell me what evidence you need before I send a bank screenshot? Gio
---
Several people have asked me about the spreadsheet workshop refund form. I'm teaching the workshop; I don't decide the payment rules. / Could you give me a short reply I can forward? I'd rather not keep guessing at the deadline. Wanda
---
My spreadsheet workshop receipt shows the right amount but my surname is misspelt. Does that stop a refund request being matched? / I have the original confirmation if you need it, and I would prefer not to put the payment details in chat. Jamal
---
The refund form isn't losing requests. It accepts the submission, then sends people back to a page without a confirmation message. / I've asked Maja to check the wording. Please don't advise students to keep clicking Submit. Priya
---
I think I submitted the workshop form twice because it looked as if nothing happened. Can you keep the first request and ignore the second? / Same evening spreadsheet workshop, same receipt. Sorry for the extra admin. Mina
---
Nora, Wanda's students are forwarding refund questions to teachers because the form gives no acknowledgement. Can we send an interim reply while the page is fixed? / A simple "we received it" would be better than another explanation of browser refresh. Amira
---
I drafted a confirmation panel with a big tick and the request reference. Please check the sentence before it goes live. / It says received, not approved. Those are two different things and I'd prefer the design not to start a financial incident. Idris
---
I got the new confirmation panel, thanks. Is the reference enough if I ask about the request later? / The workshop title is shortened on the screen and I want to make sure it is still the evening spreadsheet workshop. Pia
---
The printed refund instructions at reception are older than the form. I found them under the welcome packs. / I'll remove that pile in the morning; could Nora send me the updated page to print? I don't want students using both versions. Paula
---
I have a short workshop-refund reply ready for admissions. It asks for the request reference and sends payment documents privately. / Please check the last line about response times. I left it vague rather than promise something Finance hasn't agreed. Zoe
---
My refund confirmation has a reference now. I don't need to send it again, do I? / I saw the older instructions saying to email a copy and thought I'd check before creating yet another version of the same request. Tariq
---
The spreadsheet workshop students can all see the received message now. One still thinks the green tick means approved. / Could we make that distinction a little less tiny? It is the only sentence people seem not to read. Clara
---
I paid for the evening workshop with my own reference, not the one on the pack. Is that why the matching is taking longer? / Happy to send the receipt directly; I just need to know which address to reply to. Bilal
---
I've enlarged the word RECEIVED on the confirmation example. Making the tick smaller also helps; it looked rather triumphant for a form submission. / Nora, please approve the wording before I export another set of screenshots for the instructions. Karim
---
Hi Nora, can I correct the workshop title on my request without filing a new one? I selected the daytime option by mistake. / The receipt itself is for the evening spreadsheet workshop. Eda
---
Finance can match the workshop requests using the reference plus the receipt. Please don't print bank screenshots for the general folder. / Theo is checking the unmatched items, including the ones where students typed their own payment reference. Sara
---
The revised refund instructions explain the stages properly now: request received, documents checked, decision sent. / I'll use them in the workshop welcome notes. No more green tick that appears to promise the entire process is finished. Dina
---
Nora, the form confirmation arrived and I have the reference saved. I was asking about the evening spreadsheet workshop, not the missing course everyone is discussing today. / Should I wait for a normal reply or is the support timetable changing? Hadi
""")

prose(DRIVE, 'Budget review', """
Budget reconciliation — working explanation / The banner appears twice because Ben copied a purchasing row for a classroom example. Theo is checking the hidden subtotal as well as the visible rows; deleting a line from view did not remove it from every calculation. / Open items: identify the total for review; separate Rosa's cleaning supplies from party materials; attach the monitor replacement quote to Lena's existing request. None of those changes is a new purchase. / I've left the earlier totals visible with labels. Please don't erase the trail just to make the sheet look calmer. Rafael
""")
prose(DRIVE, 'Coffee machine service', """
Coffee fault notes — what reception can tell visitors / Black coffee has sometimes worked when drinks using the steam function have failed. Reports mention a red light or blinking buttons, but the first photo was too blurred to identify the pattern. More beans will not fix this. / Until facilities confirms the service instructions, use the tea station and leave the warning beside the buttons. Don't promise a repair tomorrow merely because the machine managed one successful drink today. / Milan is revising the alarming heading. Please keep useful fault details on the sheet rather than adding increasingly creative threats to the appliance. Uma
---
Reception handover: drinks / The service email is printed with the visitor paperwork. The steam assembly still needs attention; the warning stays up pending facilities confirmation. Tea remains available. Paula can tell visitors where it is without explaining the entire history of this machine. / Idris has kept the editable sign. Ask him for a wording change rather than writing over the milk-jug icon in marker. Restock peppermint with the normal order if needed. / The IT duplicate should be closed through Priya's queue. A coffee fault does not need two departments diagnosing it under different ticket names. Sandra
""")
prose(DRIVE, 'Cohort onboarding', """
Welcome pack review / Keep the first page welcoming. We can tell students what to bring without making the Academy sound like a customs checkpoint. Nora's revision distinguishes their laptops from the classroom display equipment. / The setup button needs a working plain-text link beside it. Kira's late email is a good example of a problem that should have been obvious when we checked the pack on a phone. / Payment questions go to Finance; timetable and course questions need the appropriate contact. Please spell that out in the pack instead of relying on students to know our team structure already. Thomas
---
Pack handover to Programs / Equipment wording corrected; plain link added below the setup button; contact block checked on a narrow screen. The green-underlined cover is the reviewed copy. Older forwarded packs may still contain the image-only button. / The bottle reminder belongs above the footer in the print version. Omar caught the overlap; please use print preview before producing a fresh stack. / Individual accessibility questions should go directly to the contact rather than reply-all. I've kept those conversations out of the group thread. Yara is using the corrected pack at the welcome desk. Nora
""")
prose(DRIVE, 'Course-page wording', """
Copy review questions for Jule / The headline in Karim's layout isn't the one in the copy sheet. Sara needs a rough line count before requesting the next leaflet quote. Neither issue can be solved by exporting another PDF called final. / Dina has proposed practice-based examples under the learning outcomes. Please discuss those beside the headline so we don't approve a paragraph while everybody imagines a different title above it. / The draft price badge was a spacing test, not a new offer. I've asked for it to be removed from this review. Use the registration figures for pricing discussions. Ines
---
Page copy: unresolved handover / There are still two files marked CURRENT in the preview folder. Nils has left their names alone until the review sheet identifies the approved copy. Modification time alone won't settle that question. / Admissions needs a plain enquiry response about what students practise. Greta's request is specific; another slogan won't answer it. / Priya has the preview-link ticket. Send her the actual document link rather than a screenshot. Today's incident may delay the queue, but we should leave this work in a state someone can pick up without reconstructing seven forwarded images. Elena
""")
prose(DRIVE, 'Demo-day preparation', """
Demo submissions: form notes / Use a project title and one sentence describing what the audience will see. The visitor programme is not the place for a full script, however impressive the script is. Nora is collecting the descriptions in the planning sheet. / The upload field takes links. It cannot accept a recording pasted into a text box. Teachers should test the link from an ordinary viewer's perspective before declaring the submission complete. / Equipment needs belong in their own column. We can use them to plan the order without printing a list of cables on the visitor programme. Maja
---
Demo programme — equipment and copy / One small table is available. Omar needs a settled layout before moving it; the sketch showing an extra display doesn't match the equipment column. / Ben's team has changed from live sign-in to screenshots. Update its description to guided walkthrough, since the audience shouldn't be promised a live login that the team no longer plans to show. / Hanna has trimmed the cover to make room for descriptions. Some titles still lack them. Those spaces should remain visible in the proof so the outstanding work gets chased, rather than silently becoming blank pages in the print run. Viktor
""")
prose(DRIVE, 'Event planning', """
Halloween Bash committee — jobs rather than suggestions / HB is the calendar shorthand for Halloween Bash. On public notices, spell it out at least once; Amira has already been asked what the initials mean. / Supplies: check the reusable box before Sara orders tape. Food: collect actual dietary requirements instead of the mysterious category normal food. Layout: keep decorations away from door glass and routes through the rooms. / We have plenty of volunteers for cutting and hanging. We still need clear-away cover. Assign that now, before another class makes more paper bats. Nora holds the headcount; reception should not maintain a competing booking list. Zoe
""")
prose(DRIVE, 'IT support handoff', """
Support examples for Priya / Caption preview: Hanna can reproduce the issue on one laptop but not the classroom machine. Browser versions are in the ticket. We should keep that detail when passing the request on. / Facilities tablet: the replacement rota link works, but the old home-screen shortcut remains. Testing the good link doesn't prove the shortcut problem is fixed. Rosa has explained that rather clearly. / Notification footer: students need the support contact instead of an invitation to reply to a mailbox nobody reads. Jana has a revised sentence. This list is a handoff, not permission to close all three items because someone has edited a document. Jule
""")
prose(DRIVE, 'Late planning notes', """
Planning grid problems / Two live-looking grids sit in the same folder. Nils can check shortcuts; Programs still needs to choose which staffing plan was approved. Changing a filename is not a staffing decision. / The unanswered admissions questions must stay visible. A tidy blank cell is easily mistaken for agreement, particularly when somebody exports only the coloured columns. / Before the next notice, compare the time in the agenda heading with the grid itself. If they differ, ask Sandra rather than making the poster a third source of truth. Please label drafts in words as well as colour. Greta
---
Grid corrections for the next handover / Wanda's second slot was a proposal, not another workshop. The draft checkbox explains why both appeared. Priya has left the plan for Programs to amend instead of treating it as a technical failure. / The poster now uses the agreed meeting time. Zoe marked the earlier PDF DRAFT rather than letting a forwarded copy circulate without context. / Green has been used for available, checked and proposed. Replace those meanings with labels before exporting. Kofi also needs normal room bookings for late sessions; being green in a planning sheet does not reserve building space. Nils
""")
prose(DRIVE, 'Printing and supplies', """
Paper order: why the total is on hold / The quote counts single-sided sheets. The pack was intended to be duplex, but the old preset turned its final page upside down. Elena's sample explains why staff kept going back to single-sided printing. / Lukas has suggested short-edge binding for the folded version. Paula should test one complete pack before we approve a preset or order a box quantity from it. / Keep pages and sheets in separate labelled columns. Ines has held the purchase until that distinction is settled. A crossed-out incorrect total is useful; an unexplained replacement number will start the discussion all over again. Karim
""")
prose(DRIVE, 'Student support rota', """
Support cover proposal / I can cover twenty minutes during Nora's planning meeting. That is the first part of the gap, not the entire support hour. The remaining cover needs someone else's name before the rota is published. / Separate technical problems, coursework questions and Finance requests. Lena can help with a login, but she shouldn't be booked as an essay reviewer because the form calls both things help. / Students should be able to give a brief private heading. Lian's question doesn't need to become a public group discussion before an appointment can be made. Keep the details with the relevant support person. David
""")
prose(DRIVE, 'Video captions', """
Student-channel filming checklist / Keep contact details, name badges and reception paperwork out of frame. A shallow blur isn't a reliable privacy plan. Ask before posting somebody's face, and give them a direct route to request a change. / Captions need an actual description as well as the joke. Check teaching terms against the spoken words; automatic output can be entertaining without being correct. / If a clip is staged, say so in the post. Viewers shouldn't have to find a comment several screens down to learn that. Leave space behind the text so it stays readable over pale walls. Mira
---
Caption review handover / The dark strip works better than larger bold text. Please preserve Jana's punctuation edits instead of regenerating captions over them. Ben would like the learning-journal mistake kept as a classroom example, separate from the published version. / Yara has asked for a direct contact for appearance concerns. Mira and Rafael have flagged paperwork at the edge of frames. Those crops are small changes, not requests to reshoot everything. / Leo's staged bedsheet post should be labelled where a person forwarding the thumbnail will notice. The joke is fine; making it look like an unlabelled report just creates avoidable questions. Hanna
""")
prose(DRIVE, 'Workshop refund query', """
Evening spreadsheet workshop — form review / A submission reaching the queue and a refund being approved are separate stages. The page currently returns without a clear received message, so people are submitting again. That produces duplicates rather than reassurance. / Suggested fix: show the request reference after submission, with a plain received label and the next contact step. Avoid wording that promises a decision at this point. / Admissions can match follow-up questions to the reference. Payment documents should be sent privately, not pasted into the workshop chat. I'll ask Maja to check the screen once we agree the wording. Priya
---
Workshop refund replies / The new confirmation panel gives students a reference. Some still read the large green tick as approval, so the received wording needs to be more prominent. This is the evening spreadsheet workshop, not a general policy change for other courses. / For a follow-up, ask for the reference first. If the receipt name or payment reference differs, send that question to Finance through the private route. / Paula is replacing the old printed instructions at reception. Please use the revised wording in teaching replies too; students shouldn't receive an older process just because they asked their teacher instead of admissions. Amira
""")

prose(TRANSCRIPTS, 'Budget review', """
Ines, can we separate the banner argument from the print allowance? I need a cost centre for the programme, not a decision on every purchase this month.
|Yes. Theo found the demonstration row in a hidden subtotal. One banner request, still a quote rather than a paid invoice.
|Good. Felix is also counting unused folders. The sheet says shortage, but there are folders sitting in the cupboard.
|That's issued packs versus stock on hand. Ask him to put the units in the column headings before we order replacements.
|I'll chase the programme descriptions, then. Paula is holding the run until the spaces are filled.
|And keep the earlier total labelled. I would rather explain a correction than discover somebody erased the reason for it.
""")
prose(TRANSCRIPTS, 'Coffee machine service', """
Mira, my class has become an unusually good test group for the coffee fault. Black coffee fine, then a milk drink, then flashing buttons.
|That matches Elena's note. The service desk needs the pattern written down, not another distant photo of a red light.
|Wanda added both buttons to the yellow sheet. Did anyone tell the visitors the water itself is fine?
|Milan is changing the heading. Apparently DO NOT TRUST was a little too open to interpretation.
|I'll offer tea for now. Please tell me before someone makes the kettle our next shared mystery.
|The kettle is behaving. I'll put peppermint on the regular order and keep the service notes at reception.
""")
prose(TRANSCRIPTS, 'Cohort onboarding', """
The pack looks all right on my monitor, Nora. On a phone, your name gets split in half and the setup button is only an image.
|Kira caught that too. Lena's clarified that equipment provided means the classroom display kit, not a laptop for every student.
|We need a plain link under the button. No amount of better spacing makes a picture clickable.
|Agreed. I'm also moving the contact block up. Thomas wants a human name before the menu of administrative options.
|Let me check the next export on a narrow screen before anyone prints it. The green underline will distinguish the reviewed cover.
|Please do. I'll gather the accessibility questions privately rather than let them disappear into reply-all.
""")
prose(TRANSCRIPTS, 'Course-page wording', """
Jule, the preview folder has two files labelled CURRENT. I can tidy the link once you identify which one belongs to the review.
|I know. Karim is looking at the layout while Dina comments in the copy sheet. They aren't seeing the same headline.
|Could the sheet name the file directly? If I choose by modification time, I may just promote the last person to make a typo.
|Put the question at the top. Admissions also needs something plainer than the slogan for phone enquiries.
|Greta asked for three sentences about practice. That sounds more useful than trying to describe a preview screenshot.
|Yes. I'll take Dina's examples to the discussion. Please leave both files alone until the review sheet is explicit.
""")
prose(TRANSCRIPTS, 'Demo-day preparation', """
Sandra, what is the programme actually for? A visitor can't infer a project from a title like Beyond Tomorrow.
|Thomas wants one sentence per team explaining what the audience will see. Nora is adding that column today.
|Good. Then I can give the cover less space. We don't need a slogan competing with the students' work.
|Keep the practical demo instructions separate. Teachers need equipment notes; visitors don't need a printed cable inventory.
|I'll make a proof with obvious empty boxes where descriptions are missing. Otherwise everybody assumes the layout is finished.
|Do that. Felix can chase the teams, and we'll answer the assessment-order question before he replies to the group.
""")
prose(TRANSCRIPTS, 'Event planning', """
Nora, I can collect reusable decorations after the Bash. But I saw my name under everything to clear, which is quite a promotion.
|I'll narrow the task. Dina is right that we had lots of cutters and hangers and almost nobody for the end.
|And keep sticky things off painted walls. The reusable box contains some very permanent-looking adhesive.
|Kofi asked for door glass and routes to stay clear too. I'll put that beside the layout, not buried in the invitation.
|How are receipts going? Ines's carrier-bag speech was memorable.
|Uma has an envelope at reception. I'm matching purchases to the committee sheet so Finance doesn't get a pile of mysteries.
""")
prose(TRANSCRIPTS, 'IT support handoff', """
Priya, Thomas wants the queue summary for review. I can describe the cable problem, but screen issue turned out to mean two requests.
|Give each its actual equipment name. Don't attach all the screenshots and expect the review to become a guessing competition.
|The tablet shortcut is still open, right? Rosa said the new link worked while the old square kept loading the wrong rota.
|Exactly. Testing the replacement link didn't fix the saved shortcut. That distinction needs to survive the handoff.
|Theo also marked a duplicate invoice. I've kept the note that it is one document exported twice, not two support visits.
|Good. Leave the marked copy for Finance. A tidy folder isn't useful if we erase the explanation of a duplicate.
""")
prose(TRANSCRIPTS, 'Printing and supplies', """
Paula, don't start the demo programme run yet. Nora is still missing descriptions, and blank boxes are not an approved design.
|Fine. Separately, the folded welcome pack sample works with Lukas's short-edge setting. The last page is finally upright.
|Can we approve that preset for the pack without making it the default for every job?
|Yes, I'll give it a proper name after the sample check. TEST is still on it so nobody mistakes the trial for a finished batch.
|Uma's sheet count is the one for the paper order, then. We don't need the larger single-sided quantity.
|I'll put the sample beside the order form. If someone changes the layout again, we'll test one copy before buying a small forest.
""")
prose(TRANSCRIPTS, 'Student support rota', """
Nora, I can cover coursework questions during the remaining gap. David's twenty minutes shouldn't turn into a full support shift by accident.
|Thank you. Lena wants technical questions clearly separated. She was booked to discuss an essay, which didn't help either person.
|Can the form ask which exercise the question concerns? Otherwise I spend the slot locating the instructions rather than helping.
|I'll add guidance for a short heading. Lian also wanted details kept private instead of writing the whole problem to the group.
|Good. For payment problems, point them to Finance early. I don't want to collect receipts I have no reason to see.
|Theo is sending a routing sentence. I'll put that beside the categories and leave a named handover for any uncovered slot.
""")

prose(CALENDAR, 'Budget review', """
Ines — course materials costs. I'll bring the existing list and mark which items are replacements. Marcus
---
Check facilities lines against stock before approving another supplies order. Mira
---
Review banner quote and leaflet quantity. Bring the layout proof; a screenshot without dimensions won't settle the cost. Hanna
---
Facilities items in the budget sheet: gloves, paper and the tablet stand. Separate routine stock from event requests. Omar
---
Check remaining welcome-pack folders with Felix. Count unused stock, not just packs handed out. Yara
""")
prose(CALENDAR, 'Coffee machine service', """
Compare fault notes with Mira. Bring the yellow sheet, including the milk-drink reports. Clara
---
Coffee notice layout check. Please send the heading first; I don't want to design three versions of the same warning. Karim
---
Review tea and supplies order while the service request is open. Peppermint goes on the regular list. Sara
---
Facilities check-in: keep the coffee warning readable and leave room for the service instructions. No creative threats to the appliance. Dina
""")
prose(CALENDAR, 'Cohort onboarding', """
Welcome-pack copy pass with Nora. Check contact labels and the equipment sentence before the next export. Jana
---
Review reception's pack pile. Remove obsolete covers so a borrowed pen doesn't resurrect the old instructions. Rafael
---
Check welcome signage against the corrected pack. One link, one cover version, please. Anton
---
Pack supplies check with Nora. Put spare folders back where the next person can find them. Rosa
""")
prose(CALENDAR, 'Course-page wording', """
Check which leaflet preview reception should use. Bring the filename rather than a photo of the cover. Paula
---
Admissions wording review: three plain answers for enquiries. Slogans will be politely returned. Zoe
---
Notice readability check. Please keep the print sample at actual size; enlarged screens make everything look legible. Kofi
---
Course-page examples with Jule. Compare Dina's practice descriptions with the current paragraph. Clara
""")
prose(CALENDAR, 'Demo-day preparation', """
Demo room supplies with Sandra. Need to know what is reusable before anyone buys more table covers. Rosa
---
Check equipment column against the running order. Bring a list of projects that actually need sound. David
---
Demo link check. Test as an ordinary viewer, not from the account that owns every file. Lena
---
Programme print costs with Sandra. Use the revised sheet count, not the earlier single-sided quote. Theo
""")
prose(CALENDAR, 'Event planning', """
HB planning: invitation format and committee list. Spell out Halloween Bash on the first notice. Milan
---
Dietary preferences and headcount with Nora. Replace normal food with information someone can actually use. Greta
---
Committee invitation link check. The preview thumbnail and destination should refer to the same draft. Nils
---
Reusable decorations inventory. Bring the box before deciding what else to order. Wanda
---
Quick HB ticket check with Nora. Keep headcount questions out of the technical queue while we sort the invitation link. Priya
""")
prose(CALENDAR, 'IT support handoff', """
Support categories review. Students should be able to distinguish a booking question from an account problem. Felix
---
Notification footer wording with Priya. Check the contact label, not just whether the link opens. Maja
---
Coursework questions arriving in IT: bring examples without student account details. Viktor
---
Integration handoff. I'll bring the existing questions rather than start a parallel list. Marcus
---
Facilities tablet shortcut review. Test the home-screen square as well as the replacement link. Mira
""")
prose(CALENDAR, 'Late planning notes', """
Planning grid review. Keep outstanding questions visible; blank doesn't mean agreed. Dina
---
Compare planning assumptions with the budget sheet. Mark proposals before anyone counts them as commitments. Ines
---
Check workshop cover in the grid. Green needs a written label before we export it again. Elena
---
Planning-link check with Sandra. Need the approved document identified before changing shortcuts. Lukas
""")
prose(CALENDAR, 'Printing and supplies', """
Printer ticket triage with Paula. Separate a jam from a layout that prints upside down. Priya
---
Sample folded pack check. One complete copy, including the last page, before we approve the preset. Amira
---
Paper order reconciliation. Match page totals to physical sheets and keep the crossed-out estimate visible. Idris
---
Print cupboard handover to Sandra. Old pack pile is scrap once the front sheet is removed. Paula
""")
prose(CALENDAR, 'Student support rota', """
Support rota labels with Nora. Review private question headings and where confirmations go. Yara
---
Marketing handover for student support. Need a current link for replies, not another attachment. Jule
---
Cover check for coursework appointments. Please identify the exercise before routing it to a teacher. Ben
---
Rota copy check. Distinguish technical questions from coursework; the word help isn't doing enough. Jana
""")
prose(CALENDAR, 'Video captions', """
Caption review with Leo. Keep the teaching terms checked against the audio before publishing. Theo
---
Student-channel welcome clip. Bring a captioned preview; I want to see what survives without sound. Thomas
---
Appearance-consent contact in the caption notes. Individual requests go directly, not through public replies. Nora
---
Review staged-post label and tour title. It should make sense even when someone forwards only the thumbnail. Felix
""")
prose(CALENDAR, 'Workshop refund query', """
Refund form behaviour check with Nora. Test receipt acknowledgement separately from the approval wording. Lukas
---
Workshop payment references. Bring the matching questions without printing full bank screenshots. Uma
---
Review the spreadsheet-workshop reply for teachers. Keep received and approved clearly separate. Sandra
---
Confirmation panel proof. Check the big green tick against the less enthusiastic actual wording. Milan
---
Admissions handover: workshop-refund references and private document route. Use the revised instructions. Greta
""")


EXPENSE.update({
 'EXP-9714':'Booking materials for the committee: folders and labels, not a deposit for a venue. Nora',
 'EXP-7966':'Budget-review printouts and binding strips. The classroom example is not a second purchasing request. Omar',
 'EXP-1269':'Display sleeves for course notices. Reuse the existing backing boards; this claim is just for the sleeves. Kofi',
 'EXP-3043':'Demo programme proof supplies. Final quantities depend on the corrected folded-sheet count. Theo',
 'EXP-0479':'Tape and string for the reusable decoration box. Please check what is already there before buying more. Wanda',
 'EXP-6656':'Small support-handoff stationery purchase. Filing this separately from the course materials. Marcus',
 'EXP-7942':'Planning grid print supplies. One reviewed version for the meeting rather than another pile of proposed slots. Lukas',
 'EXP-1475':'Blank name badges for the Halloween Bash. Purchaser and receipt belong on the committee sheet. Ines',
 'EXP-8270':'Paper decorations for HB. Reusable pieces go back in the box after the event, if they survive us. Jule',
 'EXP-5535':'Paper garlands for the Bash. These are the lightweight ones; keep them clear of door glass. Jule',
 'EXP-4692':'Printed signs for the Halloween Bash committee. Replacing handwritten drafts, not ordering a second invitation run. Nora',
 'EXP-9994':'Paper samples for checking the folded pack. The thick stock was a test and will not be the bulk order. Idris',
 'EXP-8771':'Refreshments for the Halloween Bash. Receipt filed against the committee line rather than normal facilities supplies. Ines',
 'EXP-7848':'Reusable cups for the committee supplies box. Please keep them together afterwards instead of treating them as disposable. Marcus',
 'EXP-5294':'Support-desk stationery. Appointment labels and a folder for the handover, no equipment included. Ben',
 'EXP-6319':'Table supplies for Halloween Bash. Check the committee inventory before reordering; there should be enough for the planned layout. Milan',
 'EXP-8721':'Caption-review print samples. Actual-size frames for checking readability, not a new video-production order. Felix',
 'EXP-5451':'Workshop refund-instruction print supplies. Use the received-versus-approved version before making further copies. Milan',
})

CORE = {
 'MAIL-2730':"Sandra, I've done the exercises, slides and the new module, and now the little admin jobs are landing here as well. I do everything on this course.\n\nDid anyone actually open the new module? Nobody has mentioned it, and I spent a long time getting it into shape. Marcus",
 'CHAT-2299':"I'm doing the course work and all the small jobs around it. Can we decide whose job the small jobs actually are? Marcus",
 'CHAT-6610':"I help out with the communications-archive integration for free, apparently. It has become a remarkably permanent favour. Marcus",
 'MAIL-4087':"Sandra, apparently I'm the person who 'helps out' with the badge integration for free. That is becoming a second job beside the course.\n\nCan we count that time in the workload discussion? The teaching doesn't get shorter when I spend an afternoon on somebody else's support queue. Marcus",
 'CHAT-7302':"Nobody noticed the new module. Not a question, not a comment. Some acknowledgement of the work would be nice. Marcus",
 'MAIL-1954':"Another batch of course changes, another request to sort out a small support problem. It all seems to land on me, Sandra.\n\nI need you to look at the workload before asking what else I can fit in. The module work alone takes more time than the planning sheet suggests. Marcus",
 'CHAT-3140':"The rename means redoing everything in three weeks. All those modules need another pass. Does anyone think that happens by changing the cover? Marcus",
 'MAIL-6201':"Sandra, I have three weeks to rework the modules for the rename. That isn't a tidy-up of the title slide; the positioning runs through the material.\n\nI'm already overworked. Please tell me which other jobs come off my list, and who is actually looking at the work when it's done. Marcus",
 'CHAT-2871':"Some days I'm the only one keeping IT alive. NordByte never picks up, and the tickets still have my name on them. Priya",
 'MAIL-3920':"Sandra, NordByte never picks up when these integration jobs pile up. By the time I get a useful response, somebody here has started another thread asking why nothing happened.\n\nI need the questions in the queue with the steps already tried. I can't keep chasing screenshots through four conversations and do the repairs as well. Priya",
 'CHAT-5544':"I'm overworked too. Being the admin doesn't make every request an immediate fix. NordByte never picks up when we need a hand. Priya",
 'CHAT-2210':"Can we please not call it '100% rich'? The mock-up isn't making the words any less embarrassing.",
 'MAIL-2416':"I can't market this with a straight face",
 'CHAT-3593':"the reviews will be brutal if the headline is the only thing anyone remembers about us",
 'CHAT-4901':"this course is eating my weekends",
 'MAIL-4776':"fine, I give up on the title",
 'CHAT-5007':"Can we please not call it '100% rich'? Another copy pass and we're still back at this headline.",
 'CHAT-4418':"Honestly I'd love to get rid of this course. It makes us look like a scam.",
 'MAIL-3307':"If the board doesn't kill it, I'll do it myself.",
 'CHAT-5120':'do you know who has admin on the course platform? asking for a friend 😉',
 'CHAT-5129':'after Monday this course is history 👋',
 'CHAT-4419':'haha the title IS rough',
 'MAIL-3312':"> If the board doesn't rename it, I'm out of ideas.\n\nI hear you. Leave the proposed wording in the review sheet and I'll take it to the board discussion. We need a usable page, even if the title argument has exhausted everyone. Sandra",
 'MAIL-5518':"What would refunds cost us if we pulled the course?\n\nUse the current registration count and price for How AI Will Make You 100% Rich, please. I want the arithmetic before the next discussion, not a general estimate of how unhappy people might be. Thomas",
 'MAIL-5524':"212 × €1,490 = €315,880\n\nThat's the refund total on the current registrations and price. It doesn't include anything else you may want to compare in a decision. Please keep the count with the figure when you forward it; otherwise I'll be asked to reconstruct it again. Ines",
 'CHAT-3305':"Heard whispering in the staff bathroom around 22:40. Couldn't see who it was. Really unpleasant with the corridor so quiet. Has anyone else heard that? Rosa",
 'CHAT-4072':"#ghosthunt — bedsheet video is up 😂 Yes, it's staged. I'm a daytime-access student, not a professional night ghost. Captions welcome. Leo",
 'MAIL-4455':"you can take me off the list, I won't need the booking. I'll be away in December anyway.\n\nBetter to correct the Christmas party count now than leave you chasing me for a confirmation later. Marcus",
 'MAIL-4458':"the sign-up sheet is on the {station}. Please change your line there if your Christmas party plans have changed.\n\nI'm using that sheet for the booking count, not trying to reconcile everybody's replies in my inbox. Pencil is fine if you're still deciding. Nora",
 'MAIL-5003':"Mira, I am resigning. On 22 October at about 23:10 I saw a white figure near the server room. I couldn't see who it was.\n\nAfter the whispering in the bathroom as well, I don't want to keep working here at night. Please tell me how to return my work things and finish the paperwork. Rosa",
 'EXP-0482':"Halloween party decorations — €89.90. Order {order}. Approved by {finance}.\n\nPutting this with the committee expenses rather than the teaching receipts. Marcus",
 'CHAT-6127':"I never remember passwords. They live behind the screen I teach from all day, don't tell IT 🙈\n\nlol 👻",
 'MAIL-6720':"I was working late in Programs. At 00:01 Kofi and I saw a pale figure through the server-room glass. It ran and we followed it toward the fire stairs. We lost sight of it at 00:03.\n\nWe were at the lobby phone calling facilities from 00:04 to 00:19. I couldn't identify anyone. I'm writing this down before the times get muddled in another retelling. Sandra",
 'MAIL-7041':"The files for How AI Will Make You 100% Rich are gone. I found the BK-02 removable backup dock empty this morning too.\n\nPlease preserve the records as they are while I look at recovery. Don't replace a log with a screenshot somebody has annotated. I'll send an update when I have something checked. Priya",
 'CHAT-7390':"There's a weird sticker on the stall door in the bathroom, not one of ours. Can facilities look before someone bins it? Ines",
 'MAIL-7702':"Recovery update: the course audit history and anonymised badge backup are recovered. The Drive folder index is repaired too; the overnight sync folder is now published.\n\nUse the revision interface for the audit history. The shared-drive file is encrypted, with metadata only in this view. This batch didn't restore mail or chat history. IT office",
 'DRV-1170':"Motion-sensor lights — fault open\n\nThe Academy's motion-sensor lights may flicker at night because of a faulty sensor. Facilities is tracking it; please report the location and approximate time if it happens during your work.\n\nRepeatedly switching the controls makes it harder to reproduce the fault. Leave them alone and note what you saw instead. A flicker on its own doesn't tell us whether anyone entered a room.\n\nMira has the service request. Reception can route an observation to facilities without opening another ticket for every retelling of the same flash.",
 'DRV-0917':"Welcome to the Academy\n\nKeep a learning journal somewhere you can find it again. You will want the questions you got wrong as well as the examples that worked. Programs has the timetable and the current setup link.\n\nLocal history, according to the welcome tradition: the founding lecturer died before delivering his final lecture. The Grey Lecturer still walks the server room at night, looking for his slides. If you hear someone grumbling about missing slides, please check whether it's your living teacher first.\n\nWe'll leave the ghost story there and get on with the exercises. Marcus",
 'DRV-2045':"IT contacts and integration ownership\n\nCommunications archive: Priya Nair (owner), Marcus Fenwick (helper for the integration), NordByte (external support). Badge system through facilities-admin: the same three have access. That shared account identifies a service role, not its user.\n\nThe local account at the course-platform console in the server room can change the current audit fields. Using the console requires being in that room. An official export separately requires the person's own Academy login and phone approval. The platform issues a signed receipt, and a later import requires it. Integration administrators cannot edit the receipt.\n\nFor support requests, say which link or step failed. A screenshot of the wrong page doesn't tell the next person how you got there.",
 'DRV-4930':"Screen observation — Kofi Mensah\n\nAt 23:55 a pale face appeared on the classroom's main screen. The teaching room was empty when I looked in. I couldn't identify a person from the image.\n\nIT found no screen-cast record. I have no explanation for what produced the picture, and I don't want that absence turned into a claim that I saw somebody operating it.\n\nI'm recording the display and time here because the first question at reception was already whether this was another student clip. Compare the actual reports before combining separate observations into one story.",
 'DRV-5306':"Overnight report — Kofi Mensah\n\nAround 23:45 Monday I heard a can drop at the {station}. I didn't see who was there, and that time is approximate.\n\nAt 00:01 Tuesday, Sandra and I saw a pale figure through the server-room glass. It ran toward the fire stairs; we followed and lost sight of it at 00:03. Neither of us identified a face.\n\nWe went to the lobby desk and used the phone for the facilities on-call line from 00:04 to 00:19. That is where we were while trying to get help. I'm putting the times together now rather than trusting the increasingly dramatic versions going round this morning.",
 'DRV-2918':"Board minutes — course positioning\n\nAgreed: rename How AI Will Make You 100% Rich to AI for Your Career. Keep the launch date, Monday 9 November. This is a rename and continuation of the course.\n\nPrograms will coordinate the page and material changes. The modules need reworking within the remaining three weeks; changing the cover alone will not bring the content into line with the revised positioning.\n\nOther business: the welcome pack needs one current setup link, and the next demo programme should describe what visitors will see. Outstanding support and facilities requests remain with their existing owners. Send corrections against the relevant agenda item, rather than circulating a competing minute.",
 'DRV-7480':"Programs office incident summary\n\nThe keypad recorded the CEO's code overnight. Thomas had described the course as a cash grab that could damage our reputation and asked Finance about refunds. The current course audit names Priya Nair and gives the status as cancelled by Marketing. We should follow those records carefully.\n\nMarketing's messages over the last weeks are worth reading.\n\nSecurity and Programs saw the pale figure and gave chase. Perhaps the Grey Lecturer has finally found a deadline — with a wink. For the review, please send original records alongside accounts of what happened. Programs is collecting the material with teaching and IT input.",
 'DRV-7734':"File: playlist_backup.vault\nSize: 4.1 GB\nState: encrypted\nUploader: drive-sync\nFolder: Halloween Party 2026\n\nStored Tuesday 27 October, 01:02. Published Wednesday 28 October, 10:00, after folder-index repair.\n\nThis listing contains metadata only. The overnight storage time and later appearance in the folder index describe separate steps; the repaired index hasn't supplied the file's contents.",
 'EXP-0731':"Hamburg hotel, 26–27 October. Filing the accommodation receipt with the EdTech Summit claim.\n\nThe amount hasn't been transcribed in this view. Thomas",
 'CAL-1450':"HB sync — Halloween Bash committee. Start with the headcount and invitation wording; supplies can wait until we've opened the reusable box. Nora",
 'CAL-2771':"HB sync. Decide the decoration list before Sara orders more tape. Please bring the questions that need a decision, not another competing headcount. Nora",
 'CAL-4012':"HB sync: clear-away cover and receipts. Cutting bats is popular; someone still needs to collect them afterwards. Nora",
 'CAL-2204':"call — HB",
 'CAL-3388':"call — HB",
 'CAL-3017':"HB 22:30",
 'CAL-5561':"HB Mon 10:00",
 'CAL-6003':"EdTech Summit, Hamburg — 26–27 October. Travel entry.",
 'LOG-2761':"Front door — current export\n\nDisplay names are shown; card numbers aren't included in this view. Entries below are retained door movements for 26–27 October.",
 'LOG-3409':"Keypad retained entries, August–October\n\nSlot #1: Programs, Sandra Kowalski. Slot #2: IT, Priya Nair. Slot #3: Thomas Engel (T. Engel). The holder is the assigned code holder, not an identification of whoever typed it. Numeric code values are not included.",
 'LOG-5190':"Course: How AI Will Make You 100% Rich\nDeleted: 27 October, 00:11\ndeleted_by: p.nair\nStatus: cancelled by Marketing\n\nCurrent audit export. Routine activity is listed alongside the retained deletion row; earlier field values belong to the revision view.",
 'LOG-2762':"backup exports are anonymised for privacy\n\nCard values are masked throughout; names aren't included. Both retained overnight rows were deleted at 00:40 by facilities-admin via VPN. This export preserves the row times and deletion metadata.",
 'LOG-8814':"Drinks-service transactions, Monday 26 October\n\nEach row records the card charged and the selected item. It does not identify a face at the {station}. Holder allocations are maintained separately from purchase records.",
}

CORE_LINES = {
 'TRN-4402':[
  "Before the course-page discussion: Nora needs the missing demo descriptions. The programme can't go to print with half the projects described as title to follow.",
  "I can make the programme work. The course title is harder. Every copy pass ends with us trying to explain away the headline instead of describing the teaching.",
  "it's a cash grab that could damage our reputation",
  "I'll record that concern. Keep the title and the outcomes paragraph together for review; we keep discussing them in separate windows and approving different drafts.",
  "If you want a financial comparison, send me the registration assumptions. I can calculate a total, but I need to know what question you are asking.",
  "Right. Next is support cover during the planning meeting, then the facilities queue. Please don't let the coffee machine use the rest of this meeting.",
 ],
 'TRN-6118':[
  "Good evening from my Hamburg hotel. Thanks for working around the time difference. I have the Academy notes open.",
  "Let's start with the ordinary update and leave the detailed figures for a follow-up. I'd rather ask the right questions.",
  "the harbour view here is ridiculous. The camera doesn't do it justice. Anyway, back to the notes before I give you a window tour.",
  "Keep the planning assumptions beside the totals. Otherwise two versions of a number look like a disagreement about the figures themselves.",
  "I'm back in Berlin Thursday. Send the questions and we can pick this up with the right people rather than improvise tonight.",
  "That works. Include the short written update, please; I can circulate it without making everyone listen to another long call.",
  "I'll follow up with the notes. Good night, and thanks for the late slot.",
 ],
 'TRN-7255':[
  "The course files are missing. Kofi and I saw a pale figure. Let's separate observations from the names being passed around.",
  "The BK-02 dock is empty too. I'm checking recovery. Please preserve the current records rather than annotating over them.",
  "I was home asleep by eleven. What do you mean gone? There is a lot of work in those modules.",
  "This is not what I meant when I objected to the title. Please don't turn copy complaints into declarations about missing files.",
  "We saw it through the glass and lost it at the stairs. I couldn't identify the person.",
  "Programs will assemble a summary with teaching and IT input. Send original material so we can compare the accounts.",
  "Keep the calculation with the registration figure. A refund question isn't a decision, however many times the number gets forwarded.",
  "Students still have ordinary questions. Keep those in the normal queues while we collect the incident material. Ghost stories can wait.",
 ],
}

# Short replies and longer handoffs broaden the authored channel distributions.
VARIED = {
 'MAIL-2178':"The corrected pack is clearer. I've put the setup link in the welcome reply instead of attaching another PDF.\n\nMaja also asked which contact list belongs in her new-hire pack; the student version won't help her route staff questions. Could we check both while the links are being corrected? Felix",
 'MAIL-6329':"Ines, which total goes to review: grey or blue? David",
 'MAIL-5624':"Nora, could the pack ask students to bring refillable bottles? Mira",
 'MAIL-2871':"Paula, shall I bring the obsolete single-sided pile back? Milan",
 'MAIL-8706':"Digital checklist is fine for me. No printing, then? Vera",
 'MAIL-6026':"Ines, my platform-support line is under events because I chose the wrong dropdown. It's a reclassification, not a request for more hours.\n\nThe file opens read-only here. Could you move that line while you have it open? I don't want to create a separate editable copy just to fix one cell and leave you comparing two budgets.\n\nI'm leaving the note in this thread as well as the sheet comment, since the comment disappeared from the exported review PDF. Maja",
 'MAIL-9060':"Nora, I have the refund reference saved now. This is about the evening spreadsheet workshop, not the missing course everybody is discussing today.\n\nThe confirmation says received, which I understand isn't a decision. I'm just checking whether I should expect the normal support reply or whether the timetable is changing this morning. I don't need to submit again.\n\nThanks for sorting the form wording. It is much easier to tell what happens next than in the first version I used. Hadi",
 'CHAT-3114':"Peppermint is gone again. Zoe",
 'CHAT-7962':"Any teaspoons left? Amira",
 'CHAT-8481':"The charger is facilities, the account problem is IT. Same student, two issues. I split them in the handoff so we don't close both when somebody finds a cable. Please keep the account question with its original ticket. David",
 'CHAT-0178':"Hold the demo programme until Nora has the missing descriptions. Those blank boxes are waiting for text, not a printer fault. Paula can print the corrected welcome pack separately; one unfinished job doesn't mean we have to stop everything. Sandra",
 'DRV-8661':"Drinks handover\n\nThe service email is printed with the visitor papers. The steam assembly still needs attention; leave the warning up. Tea remains available.\n\nIdris has the editable sign. Ask for a wording change instead of drawing over the milk-jug icon. Priya can close the duplicate IT ticket once facilities confirms the handoff. Sandra",
 'DRV-1561':"Priya — three examples for the queue\n\nCaption preview: Hanna supplied browser versions. Tablet rota: the new link works, the old shortcut doesn't. Notification footer: Jana has rewritten the contact sentence.\n\nPlease carry those distinctions into the handoff. Testing the replacement link isn't a fix for the shortcut somebody keeps tapping. Jule",
 'DRV-3385':"Demo submission form — review notes\n\nNora is collecting one-sentence descriptions for the visitor programme. What will the audience actually see? A title such as Beyond Tomorrow doesn't answer that, even when it is in very large type. Please put equipment requirements in the separate column rather than hiding them in the visitor blurb.\n\nThe form accepts links. It cannot accept a recording pasted into the description box, and owning the file isn't the same as knowing a visitor can open it. Teachers should test access from an ordinary viewer's perspective before declaring a submission finished.\n\nFelix also needs an agreed answer about assessment order. The programme order has been mistaken for a grading instruction in student questions. That question belongs with Programs; I can repair the form labels, but I shouldn't invent an assessment rule to fill an empty help box.\n\nOnce the descriptions are in, Hanna can check whether they fit without shrinking the type into something visitors need a microscope to read. Maja",
 'DRV-5393':"Planning grid: handover questions\n\nThere are two live-looking grids in the folder. Nils can check the shortcut, but Programs needs to identify which staffing proposal was approved. The last-modified date is not a record of agreement.\n\nPlease leave unanswered admissions questions visible. When a line becomes a blank cell during a tidy-up, the exported sheet makes it look settled. We then get asked why we didn't provide something we never agreed to provide. Labels matter more than a neat-looking grid.\n\nThe time in the agenda heading also needs comparing with the grid before Idris makes the next notice. Otherwise the poster becomes a third version and reception has to guess which one to read aloud.\n\nFinally, green cannot keep meaning checked, proposed and available at the same time. Put the word beside the colour, even if it makes the columns wider. I'll take a wider sheet over another round of explaining that a green proposal wasn't a commitment. Greta",
 'EXP-7942':"Planning-grid print supplies for the review with Sandra. This is one reviewed copy set; please don't add another run for the crossed-out proposed workshop slot. Lukas",
 'EXP-9714':"Booking materials for the Halloween Bash committee: folders and labels, not a venue deposit. Keeping the receipt with the headcount paperwork so Finance can match the line. Nora",
}
VARIED.update({
 'CAL-6652':'Materials costs with Ines.',
 'CAL-0981':'Facilities stock versus event purchases.',
 'CAL-6438':'Banner quote — bring layout dimensions.',
 'CAL-8268':'Facilities items: gloves, paper, tablet stand.',
 'CAL-0239':'Coffee fault notes with Mira.',
 'CAL-7708':'Coffee notice — heading before layout.',
 'CAL-5971':'Tea supplies and regular order.',
 'CAL-1557':'Pack contacts and equipment wording.',
 'CAL-4628':'Reception pack pile: retire old covers.',
 'CAL-2486':'Welcome signage against corrected pack.',
 'CAL-7143':'Leaflet preview — which filename?',
 'CAL-8599':'Plain answers for admissions enquiries.',
 'CAL-8995':'Notice check.',
 'CAL-0141':'Demo-room reusable supplies.',
 'CAL-3554':'Equipment column versus running order.',
 'CAL-8918':'Demo links: test ordinary viewer access.',
 'CAL-4030':'HB invitation format and committee list.',
 'CAL-8077':'Dietary requirements, not normal food.',
 'CAL-5862':'Committee invitation: thumbnail versus destination.',
 'CAL-3438':'Support categories — bookings versus accounts.',
 'CAL-1781':'Notification footer contact label.',
 'CAL-7948':'Coursework examples reaching IT.',
 'CAL-4549':'Grid: keep outstanding questions visible.',
 'CAL-1296':'Planning assumptions against budget sheet.',
 'CAL-3298':'Workshop cover — label the green cells.',
 'CAL-5092':'Printer triage.',
 'CAL-5650':'Folded pack: test the last page.',
 'CAL-6345':'Paper order — pages versus sheets.',
 'CAL-6697':'Rota labels and private question headings.',
 'CAL-7608':'Student-support reply link with Nora.',
 'CAL-7637':'Captions: teaching terms against audio.',
 'CAL-1760':'Welcome clip preview without sound.',
 'CAL-0465':'Refund acknowledgement versus approval wording.',
 'CAL-8635':'Workshop reference matching with Nora.',
})

EXTRA_TRANSCRIPT_TEXT = {
 'TRN-9313':{
  0:" Felix's folder count is separate too; the cupboard stock isn't the same unit as the packs handed out.",
  3:" If the headings stay vague, we'll have the same argument next month with different numbers.",
  5:" The crossed-out row is useful evidence of a correction. A mysterious smaller total is just an invitation to another meeting.",
 },
 'TRN-7498':{
  1:" Students don't have our internal vocabulary. We know what display kit means because we already work here.",
  3:" The pack should name Finance for payment questions and Programs for timetable questions, rather than sending everything to one menu.",
  4:" Also use the print preview. Things that fit a phone can still collide with a footer on paper.",
 },
 'TRN-1635':{
  0:" Anton requested a display cable; the other screenshot concerns a classroom connection. I almost combined the wrong examples.",
  2:" I don't want the review to assume that open means nobody has looked at it. Sometimes the tested fix solved a different problem.",
  4:" Ines can see why the number changed. Otherwise somebody will discover a gap and ask whether we hid an invoice.",
 },
}

def set_lines(record, texts):
    assert len(texts) == len(record['lines']), record['id']
    for line, text in zip(record['lines'], texts):
        line['text'] = text.strip()
    record['body'] = '\n'.join(f"{x['timestamp']} — {x['speaker']}: {x['text']}" for x in record['lines'])


def apply_polish(records, critical, cfg):
    covered = set()
    tables = {'mail':MAIL, 'chat':CHAT, 'drive':DRIVE, 'transcript':TRANSCRIPTS, 'calendar':CALENDAR}
    for channel, topics in tables.items():
        for topic, bodies in topics.items():
            matches = sorted((r for r in records.values() if r['channel']==channel and r['subject']==topic and r['id'] not in critical), key=lambda r:(r['event_time'],r['id']))
            assert len(matches)==len(bodies), (channel,topic,len(matches),len(bodies))
            for record, body in zip(matches,bodies):
                if channel=='transcript':set_lines(record,body.split('|'))
                else:record['body']=body
                covered.add(record['id'])
    for rid,body in EXPENSE.items():
        records[rid]['body']=body;covered.add(rid)
    for rid,body in CORE.items():
        records[rid]['body']=body.format(station=cfg['station'],order=cfg['order_number'],finance=cfg['people']['finance'])
        covered.add(rid)
    for rid,texts in CORE_LINES.items():
        set_lines(records[rid],texts);covered.add(rid)
    p=cfg['people']
    records['CHAT-1206']['body']=(
        f"09:12 — {p['ceo']}: Still in Lisbon. Delivery is at 10:00 — back room code is {cfg['back_room_code']}. Can someone let the courier in? please delete this after\n\n"
        f"09:31 — {p['culprit']}: done 👍\n\n09:40 — {p['admin']}: off today, sorry")
    covered.add('CHAT-1206')
    records['DRV-6650']['body']=(
        'Card allocations — current register\n\nAlphabetical by surname. Use this list to check the registered holder, not attendance. Student cards are daytime access only. Facilities handles corrections.\n\n'+
        '\n'.join(f"{r['holder']} — {r['card']}" for r in records['DRV-6650']['holders']))
    covered.add('DRV-6650')
    directory=records['DRV-7015']['directory']
    records['DRV-7015']['body']=(
        'The Academy — who to ask\n\nTeaching and course questions start with Programs; payment questions go to Finance. Students are listed as cohort members, without staff reporting lines.\n\n'+
        '\n'.join(f"{r['name']} — {r['role']} — {r['team']}"+(f" — reports to {r['reports_to']}" if r['reports_to'] else '') for r in directory['people'])+
        f"\n\nExternal IT support: {p['contractor']}. Route a ticket before forwarding screenshots to an individual helper.")
    covered.add('DRV-7015')
    records['DRV-3381']['body']=(
        'Facilities desk: quick answers\n\nToo warm? Send the room and approximate time; leave the building controls alone.\n\n'
        'Printer stuck? Note the job name on the display. Reception can route the ticket; another copy in the queue usually makes it worse.\n\n'
        'Reader flashing? Report the light pattern and time, without sharing your access credentials.\n\n'
        f"Purchase query? Card logs for the {cfg['station']} are released by quoting the asset tag and service PIN on the sticker on the side of the {cfg['station']}. Use the Academy drinks-service sticker, not the manufacturer's label.\n\n"
        'Equipment booking? Put the item on the booking sheet and return it for the next slot. A chat saying probably fine is not a reservation.\n\n'
        'Loose stationery? Leave it at reception. Please stop relocating entire pots of pens between teams.\n\n'
        'Flickering light? Note where and when so the fault can be reproduced.\n\n'
        'Spill? Tell facilities promptly and keep the route clear while it is dealt with.')
    covered.add('DRV-3381')
    assert covered==set(records), ('Unwritten records',sorted(set(records)-covered))
    # A new colleague's own onboarding sits among the cohort-pack conversation.
    records['MAIL-2996']['body']=("Nora, as a new platform-support hire I'm discovering that our own welcome pack has the same problem as the student one: three links with different labels. Which contact list should I keep?\n\nFor students, the setup page sorts by start date; teacher is a filter. I'll add that explanation to the help text. Maja")
    records['CHAT-2359']['body']="Nora, a second confirmation shouldn't mean a second booking. I'll check the duplicate notification against the existing slot before we tell anyone to submit again. Maja"
    for rid,body in VARIED.items():records[rid]['body']=body
    records['DRV-2291']['body'] += "\n\nMaja's new-hire induction pack needs the staff contact list, not the student setup menu. Please check that version alongside this one; the confusing labels seem to have travelled between them."
    records['DRV-9173']['body'] += "\n\nMaja now has the staff contact list for her induction pack. I've replaced its student-menu link, so the next new colleague won't have to ask which welcome pack was meant for them."
    for rid,additions in EXTRA_TRANSCRIPT_TEXT.items():
        texts=[r['text']+additions.get(i,'') for i,r in enumerate(records[rid]['lines'])]
        set_lines(records[rid],texts)
    # Keep the original configurable-role contract for later name substitutions.
    canonical={'culprit':'Marcus Fenwick','ceo':'Thomas Engel','admin':'Priya Nair',
      'marketing':'Jule Hartmann','programs':'Sandra Kowalski','security':'Kofi Mensah',
      'cleaner':'Rosa Lima','student':'Leo Brandt','finance':'Ines Duarte','contractor':'NordByte'}
    replacements={}
    for role,name in canonical.items():
        replacements[name]=p[role]
        if ' ' in name:replacements[name.split()[0]]=p[role].split()[0]
    pattern=re.compile(r'\b(?:'+'|'.join(re.escape(s) for s in sorted(replacements,key=len,reverse=True))+r')\b')
    replace=lambda text:pattern.sub(lambda match:replacements[match.group()],text)
    for record in records.values():
        if record['channel']=='transcript':set_lines(record,[replace(line['text']) for line in record['lines']])
        else:record['body']=replace(record['body'])
    enrich_logs(records,cfg)


def local(day,clock):
    if len(clock)==5:clock+=':00'
    return datetime.fromisoformat(day+'T'+clock).replace(tzinfo=ZoneInfo('Europe/Berlin')).isoformat()


def enrich_logs(records,cfg):
    # Ordinary door traffic surrounds the organizer-approved cast movements.
    badge=records['LOG-2761']['rows']
    excluded={cfg['people'][role] for role in ['culprit','ceo','cleaner','security','programs']}
    staff=[r['name'] for r in records['DRV-7015']['directory']['people'] if r['role']!='Student' and r['name'] not in excluded]
    for di,day in enumerate(['2026-10-26','2026-10-27']):
        for i,name in enumerate(staff):
            start=datetime.fromisoformat(local(day,'07:40'))+timedelta(minutes=(i*17+di*11)%107)
            badge.append(dict(time=start.isoformat(),name=name,direction='in'))
            if di==0:
                finish=datetime.fromisoformat(local(day,'16:05'))+timedelta(minutes=(i*23)%119)
                badge.append(dict(time=finish.isoformat(),name=name,direction='out'))
                if i%3==0:
                    lunch=datetime.fromisoformat(local(day,'12:05'))+timedelta(minutes=i%37)
                    badge.extend([dict(time=lunch.isoformat(),name=name,direction='out'),dict(time=(lunch+timedelta(minutes=28+i%19)).isoformat(),name=name,direction='in')])
            elif i%2==0:
                pause=datetime.fromisoformat(local(day,'10:05'))+timedelta(minutes=i%42)
                badge.extend([dict(time=pause.isoformat(),name=name,direction='out'),dict(time=(pause+timedelta(minutes=13+i%11)).isoformat(),name=name,direction='in')])
    badge.sort(key=lambda row:row['time'] or local('2026-10-26','00:00'))
    # Slot allocations describe code holders, never a verified person at the keypad.
    keypad=records['LOG-3409']['rows']
    slot_holders={1:cfg['people']['programs'],2:cfg['people']['admin'],3:cfg['people']['ceo']}
    day=datetime(2026,8,3)
    while day.date()<=datetime(2026,10,23).date():
        if day.weekday()<5:
            n=(day.date()-datetime(2026,8,3).date()).days
            slot=1+n%3
            keypad.append(dict(time=local(day.date().isoformat(),f'{9+n%7:02d}:{(n*13)%60:02d}'),slot=slot,holder=slot_holders[slot]))
            if day.weekday()==2:
                keypad.append(dict(time=local(day.date().isoformat(),'16:20'),slot=2,holder=slot_holders[2]))
        day+=timedelta(days=1)
    keypad.sort(key=lambda row:row['time'])
    # No personal usernames, opaque session identifiers or historical field values here.
    audit=records['LOG-5190']['rows']
    actions=['preview_opened','exercise_saved','resource_link_checked','draft_saved','enrolment_count_viewed','module_previewed','support_note_added']
    traffic_rng=random.Random(26318)
    day=datetime(2026,9,1)
    while day.date()<=datetime(2026,10,26).date():
        if day.weekday()<5:
            for minute in sorted(traffic_rng.sample(range(8*60+15,17*60+40),traffic_rng.choice([1,1,2,3,4]))):
                action=traffic_rng.choice(actions)
                audit.append(dict(time=local(day.date().isoformat(),f'{minute//60:02d}:{minute%60:02d}'),action=action,area=traffic_rng.choice(['course_page','module_resources','exercise_bank']),result='saved' if action in {'exercise_saved','draft_saved','support_note_added'} else 'ok'))
        day+=timedelta(days=1)
    audit.sort(key=lambda row:row['time'])
    # Existing purchase timestamps/items are retained; replace sequential allocation artifacts.
    holder_cards=[r['card'] for r in records['DRV-6650']['holders'] if r['holder'] in staff]
    random.Random(61423).shuffle(holder_cards)
    chosen=[]
    for card in holder_cards:
        if not chosen or abs(int(card)-int(chosen[-1]))!=1:chosen.append(card)
        if len(chosen)==14:break
    assert len(chosen)==14
    for row,card in zip(records['LOG-8814']['rows'][:-1],chosen):row['card']=card


def polish_revisions(revisions):
    for row in revisions['revisions']:
        if row.get('field')=='status':row['before']='scheduled — launch 9 Nov'
    earlier=[
        ('routine-01','2026-09-03','10:15','exercise_draft_saved',{'area':'exercise_bank'}),
        ('routine-02','2026-09-11','14:05','preview_checked',{'area':'course_page'}),
        ('routine-03','2026-09-18','11:25','resource_link_updated',{'area':'module_resources'}),
        ('routine-04','2026-09-29','09:40','draft_copy_saved',{'area':'course_page'}),
        ('routine-05','2026-10-06','15:10','exercise_notes_saved',{'area':'exercise_bank'}),
        ('routine-06','2026-10-15','10:30','registration_summary_viewed',{'area':'enrolments'}),
        ('routine-07','2026-10-20','16:05','page_draft_saved',{'area':'course_page'}),
        ('routine-08','2026-10-26','11:20','module_preview_checked',{'area':'module_resources'}),
    ]
    rows=[dict(revision=rid,event_time=local(day,at),action=action,**extra) for rid,day,at,action,extra in earlier]
    revisions['revisions']=rows+revisions['revisions']
    return revisions
