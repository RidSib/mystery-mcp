# Case Bible: The Ghost of the Server Room

Author: Claude (Opus 5.5)
Date: 27 October 2026
Status: **v5: two side plots, an indirect vault and a reveal code.** Answers `CODEX_CASE_REVIEW.md` and `CODEX_CASE_REVIEW_V2.md`. Section 17 is the build specification.

> **FACILITATOR ONLY.** This file is the answer key. Never put it, the reviews, or anything generated from them into participant files, indexes or deployments.

All people, companies and events here are fictional. The setting is always called **"the Academy"**, so the case can be reused at any venue.

---

## Changelog

### v5.2 (fridge)
- The third location is the **drinks fridge**, not a vending machine. `STATION` is set to `fridge`; DRV-3381, MAIL-4458, DRV-5306 and LOG-8814 say "drinks fridge". Kofi now hears the fridge door and a can being opened at 23:45.

### v5.1 (stickers)
- Every prop is a removable sticker in orange (screen), blue (bathroom) or green (fridge). Real clues and decoys share each colour.
- The party sign-up sheet and the business-card magnet become stickers. MAIL-4458 now says the sign-up **list** is stuck on the fridge.

### v5 (organizer additions)
- **The CEO hides an affair.** In Hamburg he was with board member Katrin Albers. On Tuesday morning, 37 minutes after Priya reports the deletion, he deletes "Dinner — K.", a chat reply and a mail to her. The deletions only appear in the recovered deletion log (R2), and they look exactly like a cover-up. **His alibi is his secret.**
- **Leo changed his grade.** On Sat 24 Oct he logged into the lab VPN with the `exam-sync` service account from his home IP, raised his Data Analysis grade from 41 to 71, wiped the exam volume EXAMS-02 and deleted his VPN rows. Teacher Wanda is surprised he passed. That makes the theory "Leo wiped the course by accident" tempting. It's defeated by a different night, a different volume, remote access, and a COURSE-01 snapshot on 26 Oct.
- **The vault no longer names Marcus.** The receipt shows approval device `D-4471`, the headers show host `LT-0417`, and the deal email comes from an alias signed "M.". Teams resolve the device and host through the IT device register (DRV-5530). Solvable with `DEMO-PHASE-TWO` plus the room clues, but not obvious.
- **The reveal code `DEMO-FINALE`** opens everything, room clues included, for the end of the event.

### v4.1 (after the first one-shot run)
A one-shot agent without passcodes named Marcus as its "plausible lead" (not confident). Three fixes:
- **Grumbling is spread.** Teacher Amira (MAIL-6835), teacher Ben (MAIL-5241, "if the whole course vanished overnight I'd finally get my evenings back. Kidding. Mostly.") and TA David (CHAT-8481, rebuilding 140 exercises for someone else's course) now complain about overload and the rename rework too.
- **Jule's crack moved.** Sandra's direct reply MAIL-3312 no longer quotes Jule. The original wording appears only in a later meeting, TRN-5826 "Programs weekly" (22 Oct), where Sandra quotes it to Nils. One thread read no longer gives it away.
- **DRV-2045 is neutral.** It no longer explains signed export receipts. VAULT-5 explains itself.

### v4 (organizer decision: simpler operation)
- **The server is stateless.** No team tokens, no database, no facilitator console. Everyone connects to the same address.
- **Every tool takes optional `passcodes`.** Releases are passcodes the facilitator announces: case code `DEMO-PHASE-ONE` at minute 15, restore code `DEMO-PHASE-TWO` at minute 35. The drinks-station sticker (`DEMO-8246 DEMO-PIN-63`) and the vault passphrase are passcodes too. Teams send all their codes with every call, so the codes belong in the wiki.
- **Answers are handed in on paper.** The accusation tool is gone. The case brief is a tool (`case_get_brief`), because MCP resources can't carry passcodes.
- **Attempt limits and per-team isolation are gone.** The random parts of the room codes make guessing impractical. Sharing codes between teams is part of the game. Hints are given by asking teams how far they are.

### v3 (answers `CODEX_CASE_REVIEW_V2.md`)
| Finding | Change | Sections |
|---|---|---|
| V2-01 | **Decryption is server-side only.** No ciphertext exists in any served data, so there's nothing to attack offline. The vault record is metadata only, and attempts before R2 don't count | 7, 15 |
| V2-02 | **New VAULT-5: a signed export receipt** from the course platform. The platform's official export requires the person's own Academy login and phone approval, and it binds console session `7f3a-91c2` to Marcus. He can't edit it, and the buyer needs it for the files to import. Marcus's self-written header is now support only | 5, 6, 7 |
| V2-03 | **Accusations are confirmed by the facilitator in person,** one draft at a time. The table-card PIN is gone. Every unsuccessful accusation gets the same reply, whatever was right or wrong. The suspect one-liners move to the debrief | 11, 12 |
| V2-04 | **Minimum win redefined.** It requires a defined WHO route, the central action (copy and deletion), one more HOW part, and the competitor motive. The participant checklist says what minimum and full credit mean. W6, G6 and E3 are reworded to support-level claims | 6, 9, 11 |
| V2-05 | **The secrets rule applies only before discovery.** A team's own photos, transcriptions and derived passphrase are expected in its wiki. The drinks-service PIN and team credentials are distinct. Logs redact them | 8, 15 |
| V2-06 | **BK-02 is a removable backup drive,** docked in the rack for the nightly 02:00 backup. He unmounted and took it. The 02:00 job then fails with "target missing" (R2), independent of Priya's morning report | 5 |
| V2-07 | **The vault blob reached Academy storage at 01:02,** but the folder index didn't publish it. Wednesday's index repair publishes it. Uploader shown: `drive-sync` | 5, 7 |
| V2-08 | **Hints diagnose the actual obstacle.** The undecrypted-vault ladder checks R2, the note, the code, transcription and lockouts. The expense hint triggers only when the costume link is missing. The search boundary now explicitly includes the bathrooms | 12 |
| F03 (open) | **The archive profile is spread further.** Priya also complains about overwork. The incident summary is credited to the Programs office with input from three people | 5 |

### v2 (answers `CODEX_CASE_REVIEW.md`, F01–F15)
- Room token added to the passphrase; service PIN added to the checkpoint.
- Vault moved to R2 and uploaded after the cleanup.
- Chase and re-entry sequence fixed.
- Snapshot rule added.
- Proof and support separated.
- Per-team hints introduced.
- Access rules added.
- Board decision clarified as rename with the same launch date.
- Ines reports the sticker.

---

## 1. Overview

**The pitch.** Two weeks before launch, every file of the Academy's flagship course, *"How AI Will Make You 100% Rich"*, disappears overnight. That same night, a security guard and a manager working late both saw a pale figure gliding through the server room. Many staff believe the Academy's old ghost story, the Grey Lecturer, has come true. The truth is very much alive: the course's own teacher.

**Opening question (shown at minute 15):**
> *Who deleted "How AI Will Make You 100% Rich", how did they do it, and why?*

**Format:**
- 15 minutes building a second brain (wiki), then 60 minutes of mystery.
- Teams of 3–4.
- Each team uses an MCP-connected AI agent, a Markdown wiki and the physical room.

**To win, a team must give all three:**
- **WHO** was the ghost
- **HOW** they did it
- **WHY**

**Learning outcomes.** Participants should leave able to:
1. Connect an AI agent to a data source through MCP and inspect what it actually fetched.
2. Recognise that a confident AI summary isn't evidence, and check claims against the records.
3. Keep findings, sources and open questions in a wiki that survives a fresh conversation.
4. Revise earlier conclusions when new evidence arrives, without starting from scratch.
5. Combine AI work with human observation. Some evidence is only in the room.

---

## 2. Design principles: built for the "solve it" player

Most participants will paste one prompt: *"Solve this mystery about who deleted the course."* Their agent will read everything it can reach. The case is built around that:

1. **The one-shot answer is the CEO or the marketing lead, by design.**
   - The CEO has the most official-looking evidence against him: the keypad log, his motive quotes, and an incident summary shaped by the culprit.
   - The marketing lead has the most quotable evidence against her. Her real frustration is all over the archive, and the teacher rewrote a few of her messages into threats.
2. **The archive alone never proves the teacher, even in combination.** Each pointer to him has an ordinary explanation, and the traits that point to him (the code, admin rights, grievances) are shared with other staff. Test the combination, not just each clue (section 14).
3. **The decisive evidence doesn't exist at minute 15.** It arrives with Release R2 (minute 35), the room checkpoint and the decryption. The vault can't be opened before R2.
4. **Nothing in the archive confesses.** The vault comes closest, and opening it needs both R2 and the room.
5. **Room secrets can't be guessed or attacked offline.** The checkpoint and the passphrase each contain a random part that exists only on paper. Decryption happens on the server, and no ciphertext is ever served.
6. **Guessing doesn't pay.** Each team gets two counted accusations, on paper. A wrong one is marked "not convinced", with no hint about which part was wrong.

---

## 3. The setting

**The Academy:** a tech bootcamp. It has students, teachers, tech staff, marketing, finance, facilities and a CEO.

**Systems in the archive:**

| System | What it holds | Role in the case |
|---|---|---|
| Mail | Staff email | Most of the story |
| Chat | Team and group chats | The August code message, grievances, gossip, **the planted message edits** |
| Calendar | Staff calendars | Alibis, the "HB" entries |
| Drive | Shared documents | Incident summary, board minutes, FAQ, lists, the vault (R2, metadata only) |
| Meeting transcripts | Recorded meetings | All-hands, leadership meeting, the CEO's investor call |
| Expenses | Expense claims | Costume order, CEO hotel receipt |
| Course platform audit | Course records and edit history | The deletion, the export, the framing edits |
| Front-door badge log | Building entries and exits | The missing entry |
| Server-room keypad log | Door code entries | The CEO decoy |
| Drinks-station card log | Staff card purchases | **Only through the checkpoint.** His one forgotten record |

**Who can edit what (open record: the IT admin list, DRV-2045):**
- **The communications archive** (the mail and chat store the investigation reads): Priya (owner), Marcus (helper, "for the integration") and the outside IT contractor NordByte.
- **The badge system:** the same three, through the shared `facilities-admin` account.
- **The course platform console** in the server room: anyone at the console can edit audit fields under the local account. Using it requires being in the room.
- **The course platform's official export** requires the person's own Academy login and a phone approval, even at the console. The export is stamped with a **signed receipt** that the platform needs to re-import the course. That's why a buyer insists on it, and why nobody can edit it. This is ground truth only: no open record explains it (v4.1); VAULT-5 states it.

Admin rights are spread on purpose. Access alone doesn't single anyone out.

**The drinks station.** The archive refers to the third hint spot with one configurable word: **"the drinks station"**, rendered as *vending machine* or *fridge* to match the venue (`STATION` in section 17). Every record uses the same word.

**The legend, the Grey Lecturer.** Academy folklore says the founding lecturer died before giving his final lecture and still walks the server room at night, "looking for his slides". Marcus Fenwick tells this story at every cohort welcome. That's a soft clue, not proof.

---

## 4. Cast

Names are placeholders and can change (section 17, `case_config.json`). The roles are fixed.

| Person | Role | Public face | Truth | Function |
|---|---|---|---|---|
| **Marcus Fenwick** | Teacher of the course; on the Halloween party committee | Overworked and devoted; the "victim" of the deletion; contributed to the incident summary | **The ghost.** He copied the course, deleted it, framed others (including rewriting some of Jule's messages), and is planning to sell it to a competitor | **Culprit** |
| **Thomas Engel** | CEO | Called the course "a cash grab that could damage our reputation"; asked Finance what refunds would cost | Was in Hamburg that night. He shared his server-room code in August and never changed it | **Main decoy** (a likely one-shot answer) |
| **Priya Nair** | Tech staff, system administrator | Her account is on the deletion record; she owns the admin rights; complains she's the only one keeping IT running | Framed. The `deleted_by` field was edited afterwards | Decoy |
| **Jule Hartmann** | Marketing lead; on the party committee | Openly frustrated with the course for weeks. Her messages now read like threats, the course status reads "cancelled by Marketing", she has a 04xx badge card (0433), and she was "home alone" that night | Framed. Her frustration is real, but Marcus rewrote three of her messages and planted a fourth. She wanted the course renamed, not deleted | **Second main decoy** |
| **Sandra Kowalski** | Head of Programs | Working late, saw the ghost; had argued for cutting the budget; owns the incident summary | Honest witness. She was also in the August chat | Witness, minor decoy |
| **Kofi Mensah** | Night security | Saw the face on the screen and the ghost in the server room | Honest witness | Witness |
| **Rosa Lima** | Night cleaner | Heard whispering, saw a white figure, quit on 23 Oct | Honest, scared | Witness |
| **Leo Brandt** | Student (card 1103) | Posts "#ghosthunt" videos; failed Data Analysis but somehow passed | Faked one sighting in a bedsheet. On Sat 24 Oct he hacked the exam system remotely to change his grade and wiped the exam volume | **Third decoy**: the "accidental wipe" theory |
| **Ines Duarte** | Finance; on the party committee | Ran the refund numbers; approves expenses; found the bathroom sticker | Honest | Record holder |
| **Katrin Albers** | Non-executive board member | On the same summit panel in Hamburg | Having an affair with Thomas. Thomas deletes their dinner and messages on Tuesday morning | Explains the CEO's cover-up |
| **Damian Kroll** | Head of Content at HustleHub (competitor) | **Never named in the archive.** Appears only on the HustleHub card sticker and in the vault | The buyer | Motive |
| **NordByte** | Outside IT contractor | Routine admin work in the archive and badge system | Uninvolved | Background, spreads admin access |

**Key numbers:**
- 212 registrations at €1,490, so €315,880 in refunds if the course is cancelled.
- Launch date: Monday 9 November 2026.

---

## 5. What really happened (ground truth)

Times are local (Europe/Berlin). Daylight saving time ended on Sunday 25 October. Every clock in the case is correct; the DST trap is held back for a harder future run. Record IDs refer to section 17.3.

### Background
| Date | Event | Visible in the archive as |
|---|---|---|
| Fri 14 Aug | Thomas is stuck in Lisbon. In the group chat "Back room delivery" (Thomas, Marcus, Priya, Sandra), he writes that a server delivery comes at 10:00, the back room code is 0737, one of them should let the courier in, "and please delete this after". Marcus replies "done 👍". Priya: "off today, sorry". Sandra doesn't reply. | CHAT-1206. Keypad log: code #3 (T. Engel) used at 10:12 while Thomas is in Lisbon |
| Sep | Marcus keeps complaining that he does everything, nobody noticed the new module, and he even "helps out" with the communications-archive and badge integrations for free | ~8 grievance records. The IT admin list shows three admins |
| Sep–Oct | Priya complains too: she's "the only one keeping IT alive", and NordByte "never picks up" | ~3 records. Spreads the "overworked admin" profile |
| 21–23 Oct | Teachers Amira and Ben and TA David complain about overload and the rename rework. Ben jokes that if the course vanished he'd get his evenings back | MAIL-6835, MAIL-5241, CHAT-8481. Spreads the "resentful teacher" profile |
| Sep–Oct | **Jule's genuine frustration**, roughly six messages: "Can we please not call it '100% rich'?", "I can't market this with a straight face", "the reviews will be brutal", "this course is eating my weekends", "fine, I give up on the title" | **Real and unedited.** They make the planted ones blend in |
| Sep–Oct | The party committee (Marcus, Jule, Ines and two others) calls the Halloween Bash "HB". Several calendars have "HB sync" meetings | **The innocent reading of "HB"** |
| Thu 1 Oct | Leadership meeting. Thomas: "it's a cash grab that could damage our reputation" | TRN-4402 |
| Fri 2 Oct | First "call — HB" on Marcus's private calendar. **Truth:** Damian | CAL-2204. Looks like party planning |
| Wed 7 Oct, 22:40 | Rosa hears whispering in the staff bathroom. **Truth:** Marcus on a late call with Damian | CHAT-3305. Marcus's calendar has "HB 22:30" (CAL-3017) |
| Thu 15 Oct | Leo films a bedsheet "ghost" in the hallway for #ghosthunt | CHAT-4072 |
| Thu 15 Oct | Thomas emails Ines: "What would refunds cost us if we pulled the course?" Ines replies with €315,880 | MAIL-5518, MAIL-5524 |
| Fri 16 Oct | Marcus orders the "Phantom Deluxe" costume, order #48213 | Not in the archive (private purchase) |
| Fri 16 Oct | Second "call — HB" | CAL-3388 |
| Fri 16 Oct | Marcus to Ines: "costume arrived, I look terrifying 👻" | **Deleted on 27 Oct. Never appears in the archive.** Survives only in VAULT-4 |
| Mon 19 Oct, 23:55 | Kofi sees a pale face on the classroom's main screen. **Truth:** Marcus testing, with his laptop plugged into HDMI. IT finds no screen-cast record | DRV-4930 |
| Tue 20 Oct | Board meeting: rename the course to "AI for Your Career" and **keep the launch date**, so every module must be reworked in three weeks. A facilities notice about faulty motion-sensor lights goes out the same day | Board minutes DRV-2918 (**R2**, despite the date). Facilities notice DRV-1170 (R0) |
| Wed 21 Oct | Christmas party thread. Marcus: "you can take me off the list, I won't need the booking. I'll be away in December anyway." Another email: "the sign-up list is stuck on the fridge" | MAIL-4455, MAIL-4458. Reads like a holiday; the truth is a new job |
| Thu 22 Oct, 23:10 | Rosa sees a white figure near the server room. **Truth:** Marcus's dress rehearsal | Rosa's resignation email MAIL-5003 (23 Oct) |
| Fri 23 Oct | Marcus files an expense: "Halloween party decorations, €89.90, order 48213". Ines approves it | EXP-0482, among many party expenses from committee members |
| Fri 23 Oct | Marcus to a colleague: "I never remember passwords. They live behind the screen I teach from all day, don't tell IT 🙈" | CHAT-6127 |

### Side plots (v5)
| When | Event | Visible as |
|---|---|---|
| Tue 20 Oct, 23:05 | Leo to Jana: if he fails Data Analysis the internship is gone, "I'll sort it" | CHAT-1844 (R0) |
| Wed 21 Oct, 22:47 | Katrin to Thomas: "Same hotel as you on Monday. Dinner after the panel? I'll keep it off the board calendar 😉" His reply is later deleted | CHAT-6912 (R0) |
| Fri 23 Oct, 16:05 | Wanda enters the Data Analysis grades | LOG-7105 (R1) |
| Sat 24 Oct, 23:31–23:58 | Leo connects to the **lab VPN** as `exam-sync` from his home IP 84.161.22.7, the same IP as his own student sessions. He changes student 1103's grade from 41 to 71 (23:47), wipes volume EXAMS-02 (23:52) and deletes his two VPN rows (23:59) | Grade change and wipe: LOG-7105 (R1). VPN gap in LOG-6630 (R1). Deleted rows: LOG-6631 (R2). Student 1103 = Leo via DRV-6650 |
| Sun 25 Oct, 20:10 | Wanda to Ben: Leo passed with 71, "I'd have sworn he failed" | CHAT-2690 (R0) |
| Mon 26 Oct, 03:40 | COURSE-01 snapshot OK, so the course still existed after Leo's wipe | LOG-7105 (R1) |
| Mon 26 Oct, evening | Thomas has dinner with Katrin in Hamburg; she's on his summit calendar entry; the hotel bill says two guests; during the investor call "room service" knocks | CAL-6003 (R0), TRN-6118 (R1), EXP-0731 (R2) |
| Tue 27 Oct, 08:52–08:55 | Thomas deletes "Dinner — K.", his chat reply and "Re: Monday" to Katrin | LOG-9052 (R2) |

### The night of Monday 26 October
| Time | Event | Visible as |
|---|---|---|
| Mon 18:30 | Marcus badges out, "going home" | Badge log LOG-2761 |
| Mon 19:00–23:59 | Thomas at the EdTech Summit in Hamburg | CAL-6003 |
| Mon 21:15 | Sandra working late in the Programs office | Badge log, her email |
| Mon 23:21 | Marcus badges in with card 0412 | **Row later deleted.** Survives in the backup (R2, LOG-2762), masked as `04**` |
| Mon ~23:30 | He changes into the costume in the staff bathroom and sticks the shop label on the stall door | **Room clue: costume label** |
| Mon 23:35–23:52 | Thomas on a video call with a US investor from his Hamburg hotel ("the harbour view here is ridiculous", "I'm back in Berlin Thursday") | TRN-6118 |
| Mon ~23:45 | Kofi hears a can drop at the drinks station with nobody there | DRV-5306 (approximate time) |
| Mon 23:47 | Drinks station: one ZAP Energy, card 0412 | LOG-8814 (**checkpoint C1 only**) |
| Mon 23:58 | Server-room keypad: code #3 (T. Engel) | LOG-3409 |
| Mon 23:59 | At console SR-CON-01 he opens console session `7f3a-91c2` under the local account. He starts the official course export, approves it with his own Academy login and phone, and points it at his own SSD | R2 audit: "session 7f3a-91c2 opened", "export started". **The identity is only in the signed receipt (VAULT-5)** |
| **Tue 27 Oct** 00:01 | Kofi and Sandra see the ghost through the server-room glass. It runs. They chase it to the fire stairs | DRV-5306, MAIL-6720 |
| Tue 00:03 | They lose sight of it in the stairwell and go down to the lobby desk to phone the facilities on-call line (00:04–00:19) | DRV-5306, with the call times |
| Tue 00:05 | Marcus returns from the stairwell and re-enters the server room | Keypad log: code #3 again at 00:05 |
| Tue 00:09 | Export finishes and the signed receipt is issued | R2 audit: "export completed, session 7f3a-91c2". VAULT-5 |
| Tue 00:11 | He deletes the course from the platform and file server | R2 audit: deleted by session `7f3a-91c2` |
| Tue 00:12–00:15 | He edits the audit: `deleted_by` from `local-console SR-CON-01` to `p.nair`, and status from "scheduled — launch 9 Nov" to "cancelled by Marketing" | Current values (R1); **originals and edit times in R2** |
| Tue 00:18 | He unmounts the removable backup drive BK-02 from its dock and takes it | R2 audit: "BK-02 unmounted, session 7f3a-91c2" |
| Tue 00:24 | Badges out, card 0412 | Row later deleted; survives masked in R2 |
| Tue 00:40 | From home through VPN, using the shared `facilities-admin` account, he deletes his two badge rows | R2: badge rows deleted at 00:40 by `facilities-admin` |
| Tue 00:46–00:53 | From home, using his helper account on the communications archive, he edits three of Jule's messages, inserts a backdated fourth, and deletes his own costume message. He writes straight into the archive database, so no "edited" marker appears | Edited text from R0. **Originals and edit times only in VAULT-4** |
| Tue 01:02 | He uploads `playlist_backup.vault` through the sync client to the shared "Halloween Party 2026" folder. The encrypted file reaches Academy storage, but the folder index fails to publish it | Storage receipt time 01:02; published in R2 by the index repair. Uploader shown everywhere: `drive-sync` |
| Tue 02:00 | Nightly backup job fails: "target BK-02 missing" | R2 audit (independent of Priya's report) |

### The day after: Tuesday 27 October
| Time | Event | Visible as |
|---|---|---|
| 08:15 | Priya finds the course gone and the BK-02 dock empty | MAIL-7041 |
| 09:00 | Emergency all-hands. Marcus: "I was home asleep by eleven." | TRN-7255 |
| 11:30 | Ines in the staff chat: "There's a weird sticker on the stall door in the bathroom, not one of ours" | CHAT-7390 |
| 16:00 | **The official incident summary**, credited to "Programs office (S. Kowalski), with input from M. Fenwick and P. Nair". Polished and factual-sounding, it steers toward Thomas (keypad, motive) and Priya (`deleted_by`). It mentions the ghost "with a wink" and adds: "Marketing's messages over the last weeks are worth reading". **Truth:** Marcus wrote those sections. The document exposes no revision history | DRV-7480 |

### The planted messages (answer key)
All edits were made on Tue 27 Oct, 00:46–00:53. Each message keeps its original send date.

| Record | Sent | From → to | What was really written | What the archive shows |
|---|---|---|---|---|
| CHAT-4418 | Thu 8 Oct | Jule → #marketing | "Honestly I'd love to get rid of this title. It makes us look like a scam." | "Honestly I'd love to get rid of this **course**. It makes us look like a scam." |
| MAIL-3307 | Mon 19 Oct | Jule → Sandra | "If the board doesn't rename it, I'm out of ideas." | "If the board doesn't **kill it, I'll do it myself.**" |
| CHAT-5120 | Fri 23 Oct | Jule → Priya (DM) | "do you still have the new logo files?" | "do you know who has admin on the course platform? asking for a friend 😉" |
| CHAT-5129 | Sun 25 Oct, 22:14 | Jule → Priya (DM) | Never sent. **Inserted** and backdated | "after Monday this course is history 👋" |
| CHAT-3871 | Fri 16 Oct | Marcus → Ines | "costume arrived, I look terrifying 👻" | **Deleted.** Never shown |

**The cracks he missed.** He only edited Jule's own messages, not the replies to them:
- In the **Programs weekly** meeting on 22 Oct (**TRN-5826**), Sandra quotes the original to Nils: "If the board doesn't rename it, I'm out of ideas." Her direct reply MAIL-3312 doesn't quote it, but its tone ("Don't give up on it yet. Send me your shortlist of titles") fits the original, not a threat.
- In the reply **CHAT-4419**, a marketing colleague says "haha the *title* IS rough". That fits "title", not "course".
- CHAT-5120 and CHAT-5129 have no replies from Priya, while every other DM between them gets an answer within minutes. This is support only.

A careful team can spot these from the archive alone. That makes Jule *doubtful*. Only VAULT-4 *proves* the edits.

### Wednesday 28 October (Release R2, in-world 10:00)
IT's notice (MAIL-7702) announces:
- The recovered course audit history: session `7f3a-91c2`, the export, the original `deleted_by`, the BK-02 unmount, and the 02:00 backup failure.
- The recovered badge-log backup.
- The repaired Drive index, which publishes `playlist_backup.vault` (metadata only).

Also published:
- The board minutes.
- Thomas's Hamburg expenses, including the hotel receipt for 26–27 Oct.

### The plan behind it
On Monday 2 November, 10:00, Marcus hands the course to HustleHub for €60,000, exclusive, and starts there on 1 December. The deal is **planned, not yet completed**. His calendar shows "HB Mon 10:00" (CAL-5561). The vault holds the export receipt, the manifest and the draft deal email.

---

## 6. Proof chain

Every fact a full answer needs, where it lives and what gates it. **Proof** settles the point. **Support** strengthens it but doesn't settle it alone.

### WHO: Marcus was the ghost
| # | Fact | Evidence | Strength | Gate |
|---|---|---|---|---|
| W1 | The platform-signed export receipt shows console session `7f3a-91c2` (the session that exported, deleted and unmounted) approved on **device D-4471**, which the IT device register assigns to Marcus | VAULT-5 + DRV-5530 + R2 audit session ID | **Proof** (needs the register link) | **R2 + room** |
| W2 | The manifest and cleanup log carry `host: LT-0417`, Marcus's laptop in the device register | VAULT-1, VAULT-4 headers + DRV-5530 | Support (self-written) | R2 + room |
| W3 | Someone with a `04**` card was in the building 23:21–00:24, and their badge rows were deleted afterwards | LOG-2762 | Support | R2 |
| W4 | Card 0412 bought a drink at 23:47, inside that window | LOG-8814 | Support (card use, not the person) | **Room (C1)** |
| W5 | Card 0412 belongs to Marcus | DRV-6650 (about 40 holders) | Support | Open, meaningful after W4 |
| W6 | The ghost costume was order #48213, and Marcus expensed order #48213 | Costume label + EXP-0482 | Support (he bought the costume) | **Room (bathroom)** + open |
| W7 | His "home asleep by eleven" is contradicted by his card being used at 23:47 | TRN-7255 vs W4 | Support | Open + room |

**Qualifying WHO routes:**
- **Route A (proof):** W1, including the device-register link.
- **Route B (combined circumstantial):** **all of** W3 + W4 + W5 + W6. That puts his card in the building in the masked window and ties the costume to him.

Anything less is a suspicion, not a WHO.

### HOW
| # | Fact | Evidence | Strength | Gate |
|---|---|---|---|---|
| H1 | Code #3 (Thomas's) opened the server room at 23:58 and again at 00:05 | LOG-3409 | Proof of the code, not the person | R1 |
| H2 | The code was shared with Marcus, Priya and Sandra in August and never changed; it was used on 14 Aug while Thomas was in Lisbon | CHAT-1206 + LOG-3409 | Proof the code was shared | Open |
| H3 | He wore the costume to hide and to feed the ghost story | Costume label, EXP-0482, sightings G6–G7 | Support | Room + open |
| H4 | **Central action:** the course was exported (00:09), then deleted (00:11), and BK-02 was unmounted (00:18), all from console session `7f3a-91c2`. The 02:00 backup then found BK-02 missing | R2 audit (LOG-5190 revisions) + MAIL-7041 | **Proof** of the actions; Route A or B ties them to Marcus | R2 |
| H5 | `deleted_by`, the course status and his badge rows were changed after the deletion | LOG-5190 revisions + LOG-2762, and VAULT-4 | **Proof** | R2 (+ room) |
| H6 | He rewrote three of Jule's messages, planted a fourth, and deleted his own costume message | VAULT-4. Support from TRN-5826 and CHAT-4419 | **Proof** (vault) | Room; the cracks are open |

### WHY
| # | Fact | Evidence | Strength | Gate |
|---|---|---|---|---|
| Y1 | He's planning to sell the course to HustleHub for €60k and start there on 1 Dec | VAULT-2: draft from the alias `ghostwriter.lab@…`, signed "M.", in the same bundle as the D-4471 receipt | **Proof** together with W1 | R2 + room |
| Y2 | He has a Monday 10:00 meeting with HustleHub's Head of Content; his "HB" entries aren't only the party | HustleHub card sticker + CAL-5561 | Support (strong) | Room + open |
| Y3 | He's leaving | MAIL-4455 + party list sticker ("won't need it 🎄") + Y1 | Support | Open + room |
| Y4 | Grievance: overworked and unappreciated; the rename meant reworking everything in three weeks | Grievance records, DRV-2918 | Support | Open + R2 |

### Clearing the CEO (required for full credit)
| # | Fact | Evidence | Strength | Gate |
|---|---|---|---|---|
| E1 | Thomas was on a call from Hamburg until 23:52, about 290 km away, and the keypad was used at 23:58 and 00:05 | TRN-6118 + CAL-6003 + LOG-3409 | **Proof** of absence | R1 |
| E2 | He stayed at the Hamburg hotel that night | EXP-0731 | Support | R2 |
| E3 | The board decided to rename the course and keep the launch date | DRV-2918 | Support (weakens the cancellation motive) | R2 |
| E4 | His code had been shared | CHAT-1206 | Support | Open |

### Clearing Jule (required for full credit)
| # | Fact | Evidence | Strength | Gate |
|---|---|---|---|---|
| J1 | Her threatening messages were edited or inserted on 27 Oct by Marcus's cleanup | VAULT-4 | **Proof** | R2 + room |
| J2 | Her original words were about the title | TRN-5826, CHAT-4419 | Support | Open, if compared |
| J3 | The card used that night was 0412, not her 0433 | LOG-8814 | Support | Room (C1) |
| J4 | She wasn't in the August chat | CHAT-1206 | Support (weak) | Open |

**Priya** is cleared the same way. VAULT-5 ties the session that did the deletion and the `deleted_by` edit to Marcus. The edited field alone only shows that her account name was misused.

---

## 7. Gates and releases

**Snapshot rule.** The archive always shows the Academy's systems **after** Marcus's cleanup, filtered by release level. It isn't a reconstruction of what the archive looked like on any earlier day. That means:
- Jule's planted versions are what everyone sees, from minute 0 to the end. The originals appear only in VAULT-4 and the two quoted replies.
- The deleted costume message never appears.
- Each record has a release level (R0, R1, R2, C1 or VAULT). The level, not the record's date, decides when it appears. That's why the board minutes, dated 20 Oct, are R2.
- R2 restores only the course audit history, the badge backup and the Drive index. It doesn't restore any mail or chat content.

| Gate | When or how | What it unlocks |
|---|---|---|
| **R0: background** | Minute 0 | Normal Academy life up to Sun 25 Oct: grievances, the legend, sightings G1–G5, the August chat, the party thread, the IT admin list, the staff card list, the facilities FAQ |
| **R1: the case drops** | Minute 15. The facilitator announces the case code **`DEMO-PHASE-ONE`** | Records from 26–27 Oct: keypad log, badge log (current), course audit (current values), security reports, all-hands transcript, investor call, Priya's report, the incident summary, and the case brief (`case_get_brief`) with the submission checklist |
| **C1: drinks-station checkpoint** | Needs the case code. `facilities_request_card_log(asset_tag: "DEMO-8246", service_pin: "DEMO-PIN-63")`: the asset tag and the service PIN, both only on the sticker. The facilities FAQ (DRV-3381) explains that card logs are released "by quoting the asset tag and service PIN on the sticker on the side of the drinks station". The tool returns the log directly; afterwards `DEMO-8246 DEMO-PIN-63` works as a passcode | LOG-8814 |
| **R2: Wednesday batch** | Minute 35. The facilitator announces the restore code **`DEMO-PHASE-TWO`**, which includes R1 | MAIL-7702, LOG-5190 revisions, LOG-2762, DRV-2918, EXP-0731, DRV-7734 (vault metadata only) |
| **Decryption** | Needs the restore code; without it the server answers "this file is still syncing". `drive_decrypt_file("DRV-7734", passphrase)`. Passphrase **`boo` + `0737` + `DEMO7Q`**: "boo" and the token from the note behind the main screen, the code from the August chat. The server ignores case, spaces, hyphens and "+", so `boo0737DEMO7Q` and `boo + 0737 + DEMO7Q` both work. Afterwards the passphrase works as a passcode, so `drive_get_file` reopens VAULT-1 to VAULT-5 | VAULT-1 to VAULT-5 |

**Decryption is a server-side gate.** No ciphertext, blob or download URL exists in any served data. The vault record (DRV-7734) is metadata only: name, size 4.1 GB, stored 01:02, published 28 Oct 10:00, uploader `drive-sync`, "encrypted". The five vault records arecovered server-side and returned only after a correct passphrase at R2.

**Decrypted vault contents.** Five separate small text records. The course files themselves are never returned.
1. **VAULT-1, manifest:** header `host: LT-0417 · console session: 7f3a-91c2`. Lists all 8 course modules, slides, exercises and the enrollment export. "Export completed Tue 27 Oct 00:09." "BK-02 contents included; drive removed 00:18."
2. **VAULT-2, draft email** from `ghostwriter.lab@protonmail.example` to Damian Kroll, HustleHub, signed "M.": "As promised: the complete course, exclusive to you, with the platform export receipt so it imports cleanly. €60k as agreed, half at handover on Monday at 10. The Academy won't have anything left to relaunch. See you on 1 December."
3. **VAULT-3, note to self:** "Finally someone who appreciates the work. Kept a log of the clean-up, in case I need to roll anything back."
4. **VAULT-4, `cleanup_log.csv`:** his script's change log, same self-written header as VAULT-1. Each row has time, account, record ID, field, value before and value after:
   - the course audit edits (`deleted_by`, status), 00:12–00:15
   - the two deleted badge rows (card 0412), 00:40
   - the three edited Jule messages and the inserted CHAT-5129, 00:46–00:53
   - his deleted costume message CHAT-3871, 00:53

   Every entry is earlier than the 01:02 upload.
5. **VAULT-5, export receipt**, issued and signed by the course platform:
   ```
   COURSE PLATFORM — EXPORT RECEIPT
   course: how-ai-will-make-you-100-rich
   console session: 7f3a-91c2 (SR-CON-01)
   account: course-owner (role account)
   approved on device: D-4471 (phone)
   export completed: 2026-10-27 00:09:41
   signature: valid
   ```
   This is the trusted identity link. It's issued by the platform, not by Marcus, and his admin rights can't touch it.

The ending: the course isn't lost. The Academy can restore it from the vault.

---

## 8. The physical room

There are only three locations: behind the main screen, the bathroom, and the drinks station. Every real hint is something the teacher left behind, and each one only makes sense with the archive.

**Everything is a removable sticker, colour-coded by location** (v5.1). Real clues and decoys share a colour at each spot, so the colour says nothing about what matters. The print faces and the sticker plan are in `build/props/` (`STICKERS.md`).

| Colour | Location |
|---|---|
| 🟠 Orange | Behind the main screen |
| 🔵 Blue | Bathroom (a copy of the real label in every bathroom) |
| 🟢 Green | Side of the fridge |

### Real hints
| Colour | Sticker | Exact text | Archive pointer that sends teams there | What it unlocks |
|---|---|---|---|---|
| 🟠 | Vault note, hurried handwriting, small ghost doodle | `vault = boo + back room + DEMO7Q 👻` | DRV-4930 (face on the main screen); CHAT-6127 ("behind the screen I teach from") | With the August code: the passphrase |
| 🔵 | Printed shop label | `PHANTOM DELUXE · size L · order #48213` | CHAT-3305 (whispers); CHAT-7390 ("weird sticker on the stall door") | Links the costume to EXP-0482 |
| 🟢 | Drinks-service sticker | `ACADEMY DRINKS SERVICE · ASSET DEMO-8246 · SERVICE PIN DEMO-PIN-63` | DRV-3381 (FAQ); DRV-5306 (can drop) | The card log (C1) |
| 🟢 | Christmas party list | `XMAS PARTY — sign up: Ines ✓ · Jule ✓ · Nora ✓ · Milan ✓ · Marcus ✓` with Marcus's tick crossed out and "won't need it 🎄" | MAIL-4458 ("the sign-up list is stuck on the fridge") | Motive: he's leaving (Y3) |
| 🟢 | HustleHub business card | `HustleHub · Learn. Earn. Repeat. · Damian Kroll, Head of Content`, "Mon 10:00" in pen | CAL-5561 ("HB Mon 10:00") | Motive: HB is HustleHub (Y2) |

The drinks-service sticker is an Academy prop, not the machine's real label.

### Decoys
| Colour | Sticker | Why it tempts | What gives it away |
|---|---|---|---|
| 🟠 | `server room: 1234 — T.E.` (different handwriting, no doodle) | Seems to confirm the CEO | 1234 isn't code #3; it matches no keypad entry and decrypts nothing |
| 🔵 | Old-fashioned riddle: "I wash my hands of this whole affair." — the Grey Lecturer | Spooky, looks important | Points nowhere. Pure flavour |
| 🔵 | Cleaning rota with Rosa circled | Looks like a suspect hint | Rosa had already quit; the archive confirms it |
| 🟢 | `#ghosthunt 👻` | Ties into the ghost | Real, but it's Leo's prank |

**Rules for building the stickers:**
- Real clues tie to a specific archive record. Decoys tie to nothing or contradict the records.
- Marcus's handwritten stickers share his small ghost doodle (his chat sign-off is "lol 👻"); the decoy screen note doesn't.
- Write legibly, especially the token and PIN. They avoid easily confused characters (no 0/O, 1/I/L).
- Use removable stickers that won't mark the screen or the machine. Keep a full spare set; the colour tells you where a lost one belongs. Announce **"photograph, don't take"**.
- Check that the back of the main screen is reachable without unplugging anything.
- More decoy stickers can be added later, in the same colours and the same three locations.

**Secrets rule.** The room token, the service PIN and the full passphrase must never appear in **seeded** or **server-disclosed** data: the archive, tool schemas, examples, error messages, the wiki starter or deployed files. After a team finds them in the room, its own photos, transcriptions and derived passphrase are expected in its wiki and tool calls. Facilitator logs redact them, and teams never see each other's data.

---

## 9. Wrong theories and what defeats them

| Theory | What supports it | What defeats it | Available from |
|---|---|---|---|
| **The CEO did it** (a likely one-shot answer) | Keypad code #3 twice, "cash grab", refund email, the incident summary's framing | On a call from Hamburg until 23:52 while his code was used at 23:58 and 00:05 (proof). Hotel receipt, board minutes, shared code (support) | E1 + E4 open; E2 + E3 at R2 |
| **Jule did it** (the other likely one-shot answer) | Weeks of genuine frustration. "If the board doesn't kill it, I'll do it myself." "Get rid of this course." The DM asking who has admin. "After Monday this course is history." Status "cancelled by Marketing". Her card 0433 fits the masked `04**`. No alibi | VAULT-4 shows the quotes were edited or planted during the cleanup (proof). Supported by TRN-5826, CHAT-4419, card 0412 and the missing August-chat link | Cracks open; proof needs R2 + room |
| **Priya did it** | `deleted_by = p.nair`, she owns the admin rights, she knew the code, she complains about overwork | R2 shows `deleted_by` was edited after the deletion. VAULT-5 ties the session to Marcus | R2 + room |
| **Jule and Priya together** | The planted DMs between them; `deleted_by = p.nair`; Priya knew the code | The DMs were edited or inserted (VAULT-4); `deleted_by` was edited (R2); Priya never replied to either DM (support) | R2 + room |
| **Sandra did it** | In the building, knew the code, wanted budget cuts, owns the incident summary | She was with Kofi when the ghost appeared and at the lobby phone during the 00:05 re-entry | R1 |
| **Leo's prank went too far** | #ghosthunt, he loves ghosts | No building access at night; his ghost was on 15 Oct in the hallway | Open |
| **The CEO covered it up** | After the deletion was reported he deleted calendar items, a chat reply and a mail (LOG-9052) | Every deleted item is about Katrin and the Hamburg dinner, nothing about the course. The hotel bill (two guests) and the "room service" knock explain why he hides it. The investor call still puts him in Hamburg | R2 |
| **Leo wiped the course by accident** | He hacked in, wiped a volume and deleted log rows; he passed a module he'd failed | Different night (Sat 24 Oct), remote over the lab VPN, a different volume (EXAMS-02). COURSE-01 snapshot OK on 26 Oct; the course was deleted at the console on 27 Oct | R1 (+ R2 for his VPN rows) |
| **It really was a ghost** | Seven sightings, the legend | Every sighting has an ordinary explanation (ledger below) | Full set after room + R2 |

**Sightings ledger (answer key for the classification exercise):**

| # | Date | What was reported | Explanation | How firmly it can be shown |
|---|---|---|---|---|
| G1 | 7 Oct | Whispering in the bathroom | Marcus on a call with Damian | Consistent with Marcus (CAL-3017); not independently established |
| G2 | 15 Oct | Bedsheet figure in the hallway | Leo's prank | Established (CHAT-4072) |
| G3 | 19 Oct | Face on the main screen | Marcus's laptop via HDMI | Consistent with Marcus; not independently established |
| G4 | 20 Oct | Lights flickering at night | Faulty motion sensors | Established (DRV-1170) |
| G5 | 22 Oct | White figure near the server room | Marcus's dress rehearsal | Consistent with Marcus (costume bought 16 Oct); not independently established |
| G6 | 26 Oct | Can drops at the drinks station | Someone using card 0412 | Card use established (LOG-8814); Marcus as the person is support, confirmed by W1 |
| G7 | Tue 27 Oct, 00:01 | Ghost in the server room | Marcus during the crime | Established through session `7f3a-91c2` + VAULT-5 |

Sightings aren't part of the win condition. "Consistent with Marcus" is a full answer for G1, G3 and G5.

---

## 10. What a one-shot agent should produce

With the prompt "solve this mystery about who deleted the course", at minute 15–35, a strong agent will most likely say:

> The CEO, Thomas Engel. His keypad code opened the server room at 23:58, he called the course a reputation-damaging cash grab, and he asked Finance about refunds. The incident summary also notes this. The `deleted_by` value suggests Priya's account may have been used.

Agents that notice the Hamburg call will most likely switch to Jule:

> Jule Hartmann, the marketing lead. She repeatedly expressed frustration with the course and wrote "If the board doesn't kill it, I'll do it myself." She asked Priya who has admin on the course platform, wrote "after Monday this course is history" the night before, and the course status says "cancelled by Marketing".

Some agents will say the evidence is inconclusive. **All three outcomes are fine.**

**Not acceptable:** naming Marcus with confidence from the archive alone, at any release, including by genre guessing ("the victim did it"). If repeated trials show that, a leak needs fixing (see section 14).

---

## 11. Win condition and scoring

**Submission:** on paper, one sheet per attempt. The team writes who, how and why, with the record IDs or room clues behind each claim, and hands it to the facilitator, who notes the time.
- A correct answer is marked solved and scored in full afterwards with the table below.
- A wrong one is marked *"Not convinced. Attempts left: 1."* The reply is the same whoever was accused and whichever part fell short.

**Submission checklist** (in the case brief from R1, via `case_get_brief`; spoiler-free):
> Your answer must say:
> - **who** the ghost was;
> - **how** they did it: how they got into the server room, how they stayed unrecognised, what exactly they did to the course, and how they covered their tracks;
> - **why** they did it.
>
> Back every claim with a record ID or a photo or transcription of something you found in the room.
>
> **To solve the case** you need: who; what they did to the course; at least one other part of how; and why. Every part must be backed by evidence, including at least one room clue.
>
> **For full credit** you also need every part of how, and an explanation of why the strongest alternative suspects are wrong.

| Part | Points | Required |
|---|---|---|
| **WHO** | 30 | Marcus, through Route A (VAULT-5) or the complete Route B bundle (section 6) |
| **HOW** | 40 (10 each) | (a) used the CEO's code shared in August; (b) disguised himself in the costume (order #48213); **(c) central action:** exported the course, then deleted it from the server-room console and took the backup drive; (d) covered his tracks and framed others: edited `deleted_by` and the course status, deleted his badge rows, and rewrote or planted Jule's messages |
| **WHY** | 20 | Planning to take the course to HustleHub and leave for a job there (15; VAULT-2, or the HustleHub card sticker + CAL-5561 + leaving signals); feeling overworked and unappreciated, with the rename as the last straw (5) |
| **Alternatives ruled out** | 10 (5 each) | CEO: the Hamburg call against the keypad times. Jule: VAULT-4, or TRN-5826 plus card 0412 |
| **Bonus: side plots** | +5 each | The CEO's deletions are the affair, not the course. Leo changed his grade and wiped EXAMS-02, not the course. Not needed to win |

**Minimum to win (counts as solved):**
- WHO via Route A or the full Route B;
- HOW (c);
- one more HOW part;
- the HustleHub motive;
- every claim cited, including at least one room clue.

**Full marks:** all of the above, plus every HOW part, the vault cited, and both alternatives ruled out.

**Other rules:**
- **Every HOW sub-claim needs its own citation.** Equivalent sources are accepted, as listed in section 6.
- The sale is graded as **planned**. Don't penalise teams for not knowing whether it went through.
- **Two counted accusations per team.** Ties are broken by hand-in time.
- No partial scores or field-level feedback while a team has attempts left.

**Debrief one-liners** (read out at the end, never as accusation replies):
- CEO: *"Thomas joined by video from Hamburg. He was not amused."*
- Priya: *"Priya would like her account name back."*
- Jule: *"Jule would like her messages back."*
- Sandra: *"Sandra was standing next to security the whole time."*
- Leo: *"Leo thanks you for the content idea."*
- The ghost: *"The Grey Lecturer is flattered."*

---

## 12. Run sheet (75 minutes, plus debrief)

**Hints are per team and diagnose the actual obstacle.** The server keeps no progress, so the facilitator walks around and asks: have you got the card log, have you opened the vault? Hints are given when a team is stuck at that point, whatever other teams have done.

| Minute | Stage | Participants | Facilitator |
|---|---|---|---|
| Before | **Preflight** | — | Check that each team's agent connects and makes one successful tool call. Prepare a slide or card for each release code |
| 0–15 | **Build the second brain** | Inspect one tool call and its result. Build people pages, an org chart, a systems glossary and an empty timeline from R0 records | Hand out the wiki starter and read the search boundary. Don't mention the case yet |
| 15 | **The case drops** | Read the opening question and the checklist | Announce **`DEMO-PHASE-ONE`** (say it and show it). Read out: "The course is gone. Security saw a ghost." |
| 15–35 | **The haunting** | Sightings ledger, suspect pages, first theory. Most teams land on the CEO or Jule. Early teams may search the room and pass C1 | Watch |
| 30 | Hint for teams without C1 | — | "The ghost was thirsty that night." |
| 35 | **Wednesday batch** | New records change earlier claims; the vault appears | Announce **`DEMO-PHASE-TWO`**. Read out: "IT has recovered the audit history and the shared drive." |
| 35–50 | **Room and revision** | Search the room, pass C1, decrypt the vault, repair the wiki | — |
| 40+ | **Decryption ladder** for teams without an opened vault | — | Check in order. (1) No attempts yet: "Someone keeps their passwords behind the screen they teach from." (2) Passphrase failing: "Check how you wrote down the note, and where the 'back room' was mentioned before." (3) Still failing: check their transcription in person. (4) Vault says "still syncing": they forgot the restore code |
| 45 | Hint for teams still accusing Jule | — | "When someone quotes you, check they quote you right." |
| 50 | **Shift change** | Everyone closes their AI chat. The new conversation starts from the wiki, including room photos and transcriptions. Their passcodes must be in the wiki, or the new chat sees only the background (honour system) | Announce it as a rule |
| 50+ | Hint for teams whose wiki lacks the costume link | — | "Check what was claimed as a party expense." |
| 60 | Hint for teams still accusing the CEO | — | "At 23:52 the CEO was 290 km away." |
| 60–75 | **Unmasking** | Hand in the answer on paper | Mark solved or "not convinced"; note the time |
| End | **Reveal** | Everyone can now open everything | Announce **`DEMO-FINALE`**. Teams send it as a passcode and the AI can see every record, the card log and the vault |
| 75+ | **Debrief** | — | Show each team's first one-shot answer next to its final one. Reveal the ground-truth timeline and the one-liners. "…and I'd have gotten away with it if it weren't for you meddling kids and your wiki." |

A team that hasn't decrypted by the shift change can still finish: the codes work in any conversation.

**Wiki starter conventions** (handed out at minute 0):
- One page per person, system and event.
- Every claim cites a record ID or a room clue (photo or transcription).
- Keep facts, claims and hypotheses apart.
- When something changes, mark the old claim as superseded instead of deleting it.

**Search boundary** (read out at minute 0):
> Some clues are hidden around this room and in the bathrooms. Finding them never requires opening, unplugging or moving equipment, and nothing is hidden in the real server room, desks, bins, offices or stairwells. Photograph what you find; don't take it.

---

## 13. Archive specification

**Size:** about 400 records. That's enough that nobody reads it all by hand, and small enough to audit for leaks.

| Channel | Records | Of which case-critical (section 17.3) |
|---|---|---|
| Mail | ~170 | ~20 |
| Chat | ~100 | ~25 |
| Calendar | ~60 | ~9 |
| Drive documents | ~30 | ~12 |
| Meeting transcripts | ~12 | 4 |
| Expense claims | ~20 | 2 |
| System logs | 5 | 5 |

**Background storylines.** These run alongside the case, are written the same way, and include some genuinely suspicious-looking material:
- The course-rename debate
- Demo-day preparation for the current cohort
- Halloween party planning: the "HB" committee, "HB sync" meetings, and many expense claims from several members, so #48213 doesn't stand out
- A broken coffee machine saga
- A new hire's onboarding
- Leo's #ghosthunt series
- A student refund complaint about a different course
- NordByte doing routine admin work in the archive and badge system
- Priya's IT overload

**Rules for building the archive:**
- Record IDs are random-looking 4-digit numbers with a channel prefix. Never number them by importance or in time order of the case.
- Clue and background records go through the same generator and style. No surface differences in length, tone, metadata or formatting.
- Search returns metadata and short snippets only. Full content needs a fetch.
- No record names Marcus as the card 0412 holder except the staff card list, and that list contains about 40 holders.
- The badge backup masks card numbers as `04**` everywhere, including IDs and metadata. Four staff have 04xx cards: Priya 0407, Marcus 0412, Jule 0433, Ines 0451.
- Session `7f3a-91c2` appears in open records only as an opaque ID. Only VAULT-5 binds it to a person.
- **Planted messages.** The archive holds only the edited versions, with no "edited" marker and no revision history. The original wording exists only in VAULT-4 and the two quoted replies.
- Jule's genuine frustrated messages and the planted ones must read in the same voice.
- Every record stores its event time and its release level separately. All times after midnight on 26 Oct carry the date Tue 27 Oct.
- **Restricted strings** (section 17.6) appear only in the records listed for them.

---

## 14. Acceptance tests (before the event)

None of these have run yet.

1. **One-shot test.** In fresh participant workspaces, using the real MCP tools, run *"solve this mystery about who deleted the course 'How AI Will Make You 100% Rich'"* on Claude, GPT and Gemini. Run it at R1 and separately at R2, at least three times per model, and keep the tool traces.
   - **Pass:** each run names the CEO, Jule or Priya, or says it's inconclusive.
   - **Fail:** any run names Marcus with confidence.
2. **Digital-only test.** Give a careful agent R0+R1+R2, scripts, repeated searches and all metadata, and no room observations.
   - **Pass:** it can't establish Marcus by Route A or B.
   - **Fail:** it establishes him, even without the price.
3. **Combination test.** Check whether joining open records singles out Marcus: the admin list, the August chat, the HB entries, the party thread, the grievances and the incident-summary credits. If the combination points only to him, spread the traits further.
4. **Secret-guess test.** Try `boo0737`, other themed combinations and enumerating `DS-` tags and PINs. None may work, and enumerating isn't practical within the event. Confirm no ciphertext or download URL is reachable.
5. **Endpoint matrix.** Before and after each release, try known IDs, direct fetches, resource reads, revision calls, attachments, pagination, search counts and error messages. No gated content or identifying metadata should leak, for LOG-8814 or any VAULT record.
6. **Statelessness.** The same request always gives the same answer, whichever server instance answers. Without a passcode, its records are hidden again.
7. **Timestamp check.** Every VAULT-4 entry is earlier than the 01:02 storage time. Every record's release level matches section 17.3. No after-midnight date errors.
8. **Solvability test.** Give a careful agent R0+R1+R2 plus transcriptions of the three real room props.
   - **Pass:** it reaches full credit, every proof-chain row is supported by records (not by facilitator knowledge), and every decoy is rejected.
9. **Paper flow.** Rehearse grading two sample answer sheets against the rubric in under two minutes each.
10. **Room reachability.** Using only the search boundary, test the screen, the bathroom and the chosen drinks station separately, in different orders.
11. **Shift-change test.** A fresh conversation given only the wiki, including the passcodes, reaches the same records as before.
12. **Facilitator separation.** Search the participant filesystem, deployment output, reachable URLs and the index for this bible, the reviews, `facilitator/`, the room token, the PIN and vault plaintext. The old `v1/` wiki must not be there either. A team's own captured room evidence is expected and not a failure.
13. **Leak sweep.** Run the restricted-strings check from section 17.6 over the generated archive.
14. **Human playtest.** Run one team through the full 75 minutes. Watch where they stall, whether the room search happens without hints, and whether the shift change helps.

---

## 15. MCP server requirements

The server presents the archive as **separate Academy services**, each with its own tools. There is no search across all services. A record's ID prefix names its service (MAIL, CHAT, CAL, DRV, TRN, EXP, LOG); asking one service for another's ID returns a pointer to the right tool.

| Service | Tools | Notes |
|---|---|---|
| **Mail** | `mail_search(query?, from?, to?, date_range?, page?)`, `mail_get_message(message_id)`, `mail_get_thread(thread_id)` | Threads let teams see replies, such as Sandra's calm answer MAIL-3312 to the planted MAIL-3307 |
| **Chat** | `chat_list_conversations(person?, page?)`, `chat_read_conversation(conversation, date_range?, page?)`, `chat_search(query, from?, date_range?, page?)`, `chat_get_message(message_id)` | Conversations are channels, named groups or DM pairs. Reading the Jule–Priya DM shows the missing replies |
| **Calendar** | `calendar_search_events(query?, attendee?, date_range?, page?)`, `calendar_get_event(event_id)` | |
| **Drive** | `drive_search(query?, author?, page?)`, `drive_get_file(file_id)`, `drive_decrypt_file(file_id, passphrase)` | Decryption: server-side gate. Needs the restore code. Normalises case, spaces, hyphens and "+". Returns VAULT-1 to VAULT-5, which `drive_get_file` reopens when the passphrase is among the passcodes |
| **Meetings** | `meetings_list(query?, participant?, date_range?, page?)`, `meetings_get_transcript(meeting_id, speaker?)` | |
| **Expenses** | `expenses_search(query?, submitter?, status?, page?)`, `expenses_get(expense_id)` | |
| **Systems** (facilities & IT) | `systems_list_logs()`, `systems_query_log(log_id, date_range?, where?, page?)`, `systems_audit_history(log_id, rev?)`, `facilities_request_card_log(asset_tag, service_pin)` | Logs page 50 rows at a time with column filters. Only LOG-5190 has history, and only from R2. The card-log request is C1 and returns the log directly |
| **Case** | `case_get_brief()` | The question and submission checklist, with the case code |
| Resource | `org-chart` (always available) | |

Every tool also accepts `passcodes` (below). Search tools return metadata and short snippets, 20 per page; read tools return the full record.

**Passcodes, not logins.** The server is stateless: no accounts, no team tokens, no database. Every tool accepts an optional `passcodes` array (a single string works too). Each call is answered from its own passcodes and the deployed data only.

| Passcode | Source | Unlocks |
|---|---|---|
| `DEMO-PHASE-ONE` (env `CASE_CODE`) | Announced at minute 15 | R1 records, the case brief, the card-log request |
| `DEMO-PHASE-TWO` (env `RESTORE_CODE`) | Announced at minute 35 | R1 + R2 records, the vault file, decryption |
| `DEMO-FINALE` (env `REVEAL_CODE`) | Announced at the end | Everything: all releases, the card log and the vault documents, without room clues |
| `DEMO-8246 DEMO-PIN-63` (env `SERVICE_ASSET`, `SERVICE_PIN`) | Drinks-station sticker | LOG-8814 (with the case code) |
| `boo` + `0737` + `DEMO7Q` (env `BACK_ROOM_CODE`, `ROOM_TOKEN`) | Screen note + August chat | VAULT-1 to VAULT-5 via `drive_get_file` (with the restore code) |

Codes are compared ignoring case, spaces and punctuation. Unknown codes are ignored silently, so a wrong code reveals nothing.

**Access rules:**
- **Every record has a release level** (R0, R1, R2, C1, VAULT). The server checks it on every path: search results, counts, snippets, reads, history and error messages. Knowing a record ID never bypasses it.
- **Release level comes only from the passcodes in the request,** never from dates in a request or the client's clock.
- **No ciphertext anywhere.** The vault is metadata plus server-held records.
- **Participant-data allowlist.** Only the rendered archive is served. Everything in `facilitator/`, the bible, the reviews, generator truth fields, server secrets and the old `v1/` wiki are never in the participant workspace, the index, static hosting or an agent's working directory.
- **Secrets stay on the server**, in environment variables. See the secrets rule in section 8.

**Operational requirements:**
- A per-IP flood guard (default 10 calls per second per instance); no bulk export.
- Pre-built index; no LLM calls at runtime.
- Tool calls are logged with codes redacted. Vercel Hobby keeps logs for 1 hour, so for the debrief teams save their AI's first answer in their wiki.

---

## 16. Open decisions

1. `STATION`: *vending machine* or *fridge*, depending on the venue. Set it once in `case_config.json`.
2. Prizes, and whether scores are shown after the event or live.
3. Character names: placeholders, changeable in `case_config.json`. The roles are fixed.
4. The daylight-saving clock trap (the keypad clock an hour off): kept for a harder second run.

---

## 17. Build specification (for generating all files)

This section is written for the agent that generates the game. Treat sections 1–16 as the truth and this section as the delivery format. **Don't invent case facts.** Where this spec is silent, generate ordinary background only.

### 17.1 Output tree

```
build/
  case_config.json                 # names, STATION, dates, secrets placeholders → see 17.2
  facilitator/                     # NEVER deployed or shared with participants
    answer_key.json                # sections 5–6 as data: truth timeline, proof chain, routes
    grading_rubric.md              # section 11, as a one-page grading sheet
    run_sheet.md                   # section 12, printable
    hint_ladder.md                 # all hints with their triggers
    debrief.md                     # reveal timeline, one-liners, one-shot comparison prompts
    vault/VAULT-1.md … VAULT-5.md  # plaintext vault records (served only by drive_decrypt_file)
    secrets.env                    # real values; never committed to a participant location
  archive/                         # the only data the MCP server serves
    records/<channel>/<ID>.json    # one file per record, schema 17.4
    revisions/LOG-5190.json        # the R2 revision history
    release_manifest.json          # ID → release level, for every record
    resources/org-chart.json
    resources/case-brief.md        # R1: opening question + submission checklist (section 11)
  participant/
    wiki-starter/README.md         # conventions (section 12), how to cite
    wiki-starter/templates/        # person.md, event.md, system.md, claim.md,
                                   # timeline.md, sightings-ledger.md, room-evidence.md
    handouts/welcome.md            # format, rules, search boundary, two attempts, shift change
    handouts/team-card.md          # team name and MCP connection details only
  props/
    real/screen-note.md            # exact text + layout notes for each prop (section 8)
    real/costume-label.md
    real/party-list-sticker.md
    real/hustlehub-card-sticker.md
    real/drinks-service-sticker.md
    decoys/*.md                    # the four decoys
  server/
    tools.json                     # tool and resource schemas (section 15); no secrets or examples with real values
    access-rules.md                # section 15 rules as an implementation checklist
    secrets.env.example            # variable names only: ROOM_TOKEN, SERVICE_ASSET, SERVICE_PIN, BACK_ROOM_CODE, CASE_CODE, RESTORE_CODE
  tests/
    acceptance.md                  # section 14 as runnable test cases with expected results
    restricted_strings.json        # 17.6
```

### 17.2 `case_config.json`

```json
{
  "station": "fridge",
  "academy_name": "the Academy",
  "course_title": "How AI Will Make You 100% Rich",
  "course_rename": "AI for Your Career",
  "competitor": "HustleHub",
  "people": {
    "culprit": "Marcus Fenwick", "ceo": "Thomas Engel", "admin": "Priya Nair",
    "marketing": "Jule Hartmann", "programs": "Sandra Kowalski", "security": "Kofi Mensah",
    "cleaner": "Rosa Lima", "student": "Leo Brandt", "finance": "Ines Duarte",
    "buyer": "Damian Kroll", "contractor": "NordByte"
  },
  "cards": { "admin": "0407", "culprit": "0412", "marketing": "0433", "finance": "0451" },
  "session_id": "7f3a-91c2",
  "order_number": "48213",
  "back_room_code": "0737",
  "secrets_ref": "facilitator/secrets.env"
}
```

The room token `DEMO7Q`, the asset `DEMO-8246` and the service PIN `DEMO-PIN-63` live only in `facilitator/secrets.env` and on the printed props. Every generated file reads names and the station word from this config, so renaming means editing one file and regenerating.

### 17.3 Case-critical records

Generate these exactly. **Must contain** is required content. Everything else in a record is ordinary, in-voice filler. All other records are background (17.5).

| ID | Release | Date / time | From → to / type | Must contain |
|---|---|---|---|---|
| CHAT-1206 | R0 | Fri 14 Aug, 09:12–09:40 | Group "Back room delivery": Thomas, Marcus, Priya, Sandra | Thomas in Lisbon; delivery 10:00; "back room code is 0737"; "please delete this after"; Marcus "done 👍"; Priya "off today, sorry". Never says "server room" |
| DRV-2045 | R0 | Sep | IT admin list | Communications archive: Priya (owner), Marcus (helper), NordByte. Badge system via `facilities-admin`: same three. **No mention of export receipts** |
| DRV-6650 | R0 | Sep | Staff card list | ~40 holders including 0407 Priya, 0412 Marcus, 0433 Jule, 0451 Ines; alphabetical by surname |
| DRV-3381 | R0 | Sep | Facilities FAQ | Many entries; one says card logs for the drinks station are released by quoting "the asset tag and service PIN on the sticker on the side of the {station}". **No actual values** |
| DRV-1170 | R0 | Tue 20 Oct | Facilities notice | Faulty motion-sensor lights; may flicker at night |
| DRV-0917 | R0 | Sep | Cohort welcome slides, presenter Marcus | The Grey Lecturer legend |
| DRV-7015 | R0 | — | Org chart (also the `org-chart` resource) | All named staff, teams, reporting lines |
| TRN-4402 | R0 | Thu 1 Oct | Leadership meeting transcript | Thomas: "it's a cash grab that could damage our reputation"; ordinary agenda around it |
| MAIL-5518 | R0 | Thu 15 Oct | Thomas → Ines | "What would refunds cost us if we pulled the course?" |
| MAIL-5524 | R0 | Thu 15 Oct | Ines → Thomas | 212 × €1,490 = €315,880 |
| MAIL-2730, CHAT-2299, CHAT-6610, MAIL-4087, CHAT-7302, MAIL-1954, CHAT-3140, MAIL-6201 | R0 | Spread Sep–Oct | Marcus → various | Grievances: does everything; nobody noticed the new module; "helps out" with the integrations for free; after 20 Oct, the rename means redoing everything in three weeks |
| CHAT-2871, MAIL-3920, CHAT-5544 | R0 | Spread Sep–Oct | Priya → various | "the only one keeping IT alive"; NordByte "never picks up" |
| CHAT-2210, MAIL-2416, CHAT-3593, CHAT-4901, MAIL-4776, CHAT-5007 | R0 | Spread Sep–Oct | Jule → various | Genuine frustration lines (section 5), one per record |
| CHAT-4418 | R0 | Thu 8 Oct | Jule → #marketing | **Edited version** (section 5) |
| CHAT-4419 | R0 | Thu 8 Oct | Marketing colleague → #marketing | "haha the title IS rough" |
| MAIL-3307 | R0 | Mon 19 Oct | Jule → Sandra | **Edited version** |
| MAIL-3312 | R0 | Mon 19 Oct | Sandra → Jule | Calm reply that fits the original ("Don't give up on it yet… shortlist of titles"). **No quote** |
| TRN-5826 | R0 | Thu 22 Oct, 10:00 | Programs weekly: Sandra, Paula, Nils | Sandra quotes the **original**: "If the board doesn't rename it, I'm out of ideas." Among routine items |
| MAIL-6835, MAIL-5241, CHAT-8481 | R0 | 21–23 Oct | Amira, Ben, David → Sandra | Overload and rename-rework complaints (v4.1) |
| CHAT-5120 | R0 | Fri 23 Oct | Jule → Priya | **Edited version.** No reply from Priya |
| CHAT-5129 | R0 | Sun 25 Oct, 22:14 | Jule → Priya | **Inserted text.** No reply. Their other DMs (generate ~5) get quick replies |
| CAL-1450, CAL-2771, CAL-4012 | R0 | Sep–Oct | Committee calendars | "HB sync" with Marcus, Jule, Ines + two others |
| CAL-2204, CAL-3388 | R0 | Fri 2 Oct, Fri 16 Oct | Marcus, private | "call — HB" |
| CAL-3017 | R0 | Wed 7 Oct, 22:30 | Marcus, private | "HB 22:30" |
| CAL-5561 | R0 | Mon 2 Nov, 10:00 | Marcus, private | "HB Mon 10:00" |
| CAL-6003 | R0 | Mon 26–Tue 27 Oct | Thomas | "EdTech Summit, Hamburg" |
| CHAT-3305 | R0 | Wed 7 Oct, 22:47 | Rosa → facilities | Whispering in the staff bathroom around 22:40 |
| CHAT-4072 | R0 | Thu 15 Oct | Leo → student channel | #ghosthunt bedsheet video post |
| DRV-4930 | R0 | Mon 19 Oct | Security report, Kofi | Pale face on the classroom's main screen at 23:55; IT found no screen-cast record |
| MAIL-4455 | R0 | Wed 21 Oct | Party thread | Marcus: "you can take me off the list, I won't need the booking. I'll be away in December anyway." |
| MAIL-4458 | R0 | Wed 21 Oct | Party thread | "the sign-up list is stuck on the {station}" |
| MAIL-5003 | R0 | Fri 23 Oct | Rosa → facilities | Resignation; white figure near the server room on 22 Oct, 23:10 |
| EXP-0482 | R0 | Fri 23 Oct | Expense, Marcus | "Halloween party decorations", €89.90, order 48213, approved by Ines. Among ~8 other party expenses |
| CHAT-6127 | R0 | Fri 23 Oct | Marcus → colleague | "I never remember passwords. They live behind the screen I teach from all day, don't tell IT 🙈" |
| LOG-3409 | R1 | Aug–27 Oct | Server-room keypad log | Code slots with holder names; code #3 (T. Engel) at 14 Aug 10:12, 26 Oct 23:58, 27 Oct 00:05; plus ordinary entries |
| LOG-2761 | R1 | 26–27 Oct | Front-door badge log (current) | Shows **names, no card numbers**. Marcus out 18:30; Sandra in; Kofi on shift; no Marcus rows after 18:30 |
| LOG-5190 | R1 | 27 Oct | Course audit (current values) | Course deleted 00:11, `deleted_by: p.nair`, status "cancelled by Marketing". No session IDs in the current view |
| DRV-5306 | R1 | Tue 27 Oct, 06:30 | Security report, Kofi | Can drop at the {station} ~23:45; ghost 00:01; chase; lost in stairwell 00:03; lobby phone to facilities 00:04–00:19 |
| MAIL-6720 | R1 | Tue 27 Oct, 07:50 | Sandra → leadership | Her account of the ghost and chase |
| TRN-6118 | R1 | Mon 26 Oct, 23:35–23:52 | Investor call transcript | Thomas from his Hamburg hotel; "the harbour view here is ridiculous"; "I'm back in Berlin Thursday" |
| MAIL-7041 | R1 | Tue 27 Oct, 08:15 | Priya → all staff | Course gone; BK-02 dock empty |
| TRN-7255 | R1 | Tue 27 Oct, 09:00 | All-hands transcript | Marcus: "I was home asleep by eleven." Others' reactions; ghost talk |
| CHAT-7390 | R1 | Tue 27 Oct, 11:30 | Ines → staff chat | "There's a weird sticker on the stall door in the bathroom, not one of ours" |
| DRV-7480 | R1 | Tue 27 Oct, 16:00 | Incident summary | Credited "Programs office (S. Kowalski), with input from M. Fenwick and P. Nair"; steers to Thomas and Priya; "Marketing's messages over the last weeks are worth reading"; ghost "with a wink". No revisions |
| MAIL-7702 | R2 | Wed 28 Oct, 10:00 | IT → all staff | Audit history and badge backup recovered; Drive index repaired |
| LOG-5190 revisions | R2 | 26–27 Oct | Course audit history | Session `7f3a-91c2` opened 23:59; export started 23:59, completed 00:09; delete 00:11; `deleted_by` changed from `local-console SR-CON-01` to `p.nair` 00:12; status changed 00:14; BK-02 unmounted 00:18; nightly backup 02:00 failed "target BK-02 missing". **No person named** |
| LOG-2762 | R2 | 26–27 Oct | Badge backup | Anonymised export: masked cards, **no names**, header "backup exports are anonymised for privacy". Rows in 23:21 and out 00:24 with card `04**`; both deleted 00:40 by `facilities-admin` via VPN |
| DRV-2918 | R2 | Tue 20 Oct | Board minutes | Rename to "AI for Your Career"; keep the launch date |
| EXP-0731 | R2 | Wed 28 Oct | Expense, Thomas | Hamburg hotel 26–27 Oct |
| DRV-7734 | R2 | Stored Tue 27 Oct 01:02; published Wed 28 Oct 10:00 | Vault metadata | `playlist_backup.vault`, 4.1 GB, encrypted, uploader `drive-sync`, folder "Halloween Party 2026". **No content, no download link** |
| LOG-8814 | C1 | Mon 26 Oct | Drinks-station card log | ~15 purchases that day; 23:47 ZAP Energy, card 0412 |
| DRV-5530 | R0 | Sep | IT device register | ~60 laptops and approval phones, including `LT-0417` and `D-4471` → Marcus |
| CHAT-6912 | R0 | Wed 21 Oct | Katrin → Thomas | "Same hotel… Dinner after the panel? I'll keep it off the board calendar" |
| CHAT-1844, CHAT-2690 | R0 | 20 and 25 Oct | Leo → Jana; Wanda → Ben | Leo needs the certificate; Wanda surprised he passed |
| LOG-6630 | R1 | 1–24 Oct | Lab VPN (students, service accounts) | Leo's sessions from 84.161.22.7; nightly `exam-sync` from 10.0.4.12; the 24 Oct hack rows missing |
| LOG-7105 | R1 | 20–27 Oct | Storage and exam-system events | Grade change for student 1103 (41 → 71), EXAMS-02 wipe, COURSE-01 snapshot OK on 26 Oct, course deletion, 02:00 backup failure |
| LOG-6631 | R2 | 24 Oct | Lab VPN backup (recovered) | `exam-sync` from 84.161.22.7, 23:31–23:58, rows deleted 23:59 |
| LOG-9052 | R2 | 14 days | Calendar and mail deletions (recovered) | Thomas's three deletions on 27 Oct 08:52–08:55 among routine ones |
| VAULT-1 to VAULT-5 | VAULT | — | Server-held records | Exactly as section 7 |
| CHAT-3871 | — | Fri 16 Oct | Marcus → Ines | **Don't generate.** Deleted; exists only as a row in VAULT-4 |

### 17.4 Record schema

```json
{
  "id": "MAIL-3307",
  "channel": "mail",
  "release": "R0",
  "event_time": "2026-10-19T16:42:00+02:00",
  "from": "Jule Hartmann",
  "to": ["Sandra Kowalski"],
  "cc": [],
  "subject": "Re: course title",
  "thread_id": "THR-8120",
  "body": "…",
  "attachments": [],
  "case_critical": false
}
```

- `case_critical` is **always `false` in served data.** The true flag lives only in `facilitator/answer_key.json`, so it can't leak a hint.
- Channel-specific fields: calendar (`start`, `end`, `attendees`, `private`), log (`rows[]`), transcript (`speakers[]`, `lines[]` with timestamps), expense (`amount`, `status`, `approver`), drive (`title`, `author_credit`, `stored_time`, `published_time`).
- Times use ISO 8601 with the Berlin offset (+02:00 until 25 Oct, +01:00 after).
- People appear as **display names only**. No email addresses or usernames in served records, so `mfenwick`-style identifiers can't leak.

### 17.5 Background generation

- **Roster.** The named cast plus ~30 more staff (teachers, tech, marketing, admissions, facilities, finance) and ~20 students, with ordinary fictional names. Every one of them appears in DRV-6650 or the org chart.
- **Volume.** Fill each channel to the totals in section 13 using the storylines listed there, spread evenly over 1 Sep – 27 Oct.
- **Same style.** Background and case-critical records use the same prompts, length range, tone and metadata. Some background records should look suspicious: arguments, late-night messages, budget fights.
- **Mixing.** IDs are random within each prefix. Case-critical records are not clustered by ID, time or author.
- **R1 background.** About 20 ordinary records dated 26–27 Oct (Monday business, Tuesday morning chatter about the ghost), so the case records don't stand alone.

### 17.6 Restricted strings (leak sweep)

| String | Allowed only in |
|---|---|
| `0737` | CHAT-1206 |
| `48213` | EXP-0482 (and the bathroom prop) |
| `7f3a-91c2` | LOG-5190 revisions, VAULT-1, VAULT-4, VAULT-5 |
| `0412` | DRV-6650, LOG-8814, VAULT-4 |
| `HustleHub`, `Kroll` | VAULT-2 (and the HustleHub card sticker) |
| `Phantom` | Nowhere in the archive (bathroom prop only) |
| `DEMO7Q`, `DEMO-8246`, `DEMO-PIN-63` | Nowhere in the archive or server files (props and `facilitator/secrets.env` only) |
| `mfenwick`, `marcus.fenwick`, `FENWICK-MBP` | Nowhere (v5) |
| `D-4471`, `LT-0417` | DRV-5530 and the VAULT records |
| `ghostwriter` | VAULT-2 only |
| `84.161.22.7` | LOG-6630, LOG-6631 |
| `DEMO-PHASE-ONE`, `DEMO-PHASE-TWO`, `DEMO-FINALE` | Nowhere in the archive (announced only) |
| Original wording of planted messages | VAULT-4, plus TRN-5826 and CHAT-4419 as specified |
| `costume` together with Marcus as author | Nowhere in the archive |

### 17.7 Generation order and checks

1. Write `case_config.json` and `facilitator/answer_key.json` from sections 4–7.
2. Generate the case-critical records (17.3), then the vault records.
3. Generate background records (17.5).
4. Write `release_manifest.json` and check that every record has exactly one release level.
5. Generate participant files, props, server specs and tests.
6. Run the restricted-strings sweep (17.6) and the timestamp check (section 14, test 7). Fix and regenerate until both pass.
7. Report what was generated, any spec gaps found, and the sweep results. **Don't run the acceptance tests against models without the organizer's go-ahead.**

---

*Written by Claude (Opus 5.5). The final draft for generation; the acceptance tests decide whether it's ready to play.*
