import sys,json; sys.path.insert(0,'/tmp/gen'); from common import page
from headers import LOGO
P='/mnt/user-data/outputs/artifacts/01ea5720-d0c8-4528-b8cc-76eb1693feae/project/'
c=json.load(open(P+'canvas.json'))
ARCH=[('DashboardPaid.dc.html',1440,3800,'Archive · Old paid dashboard'),('Request.dc.html',800,600,'Archive · Post a request'),('Item.dc.html',800,600,'Archive · Item'),('OwnerReports.dc.html',800,600,'Archive · Owner reports'),('OwnerWork.dc.html',800,600,'Archive · Owner work')]+[(f,800,400,'Unused · safe to delete') for f in ['FlowJourneys.dc.html','HomeMore.dc.html','HomeMore_p2.dc.html','HomeMore_p3.dc.html','HomeMore_p4.dc.html']]
_ay=0
for k,w,h,tt in ARCH:
    c['boards'][k]={'x':24000,'y':_ay,'w':w,'h':h,'title':tt}; _ay+=h+200
    if k not in c['order']: c['order'].append(k)
c['boards']['OwnerReferral.dc.html']['title']='14 · Referral program'
c['boards']['MonthReport.dc.html']['title']='11b · Monthly report'
T=lambda f: c['boards'][f]['title']
# columns = journeys; each: (name, who, color, [(desktop file, mobile board or None, one-liner)])
COLS=[
('A','Locals find and ask','Everyone','#2b59d9',[('Home.dc.html','MPublic','What locals know, AI recommends. A med spa page built from many sources, trending brands, how it works, the AI moment, the owner door, then the live homepage.'),('Join.dc.html','MPublic','Pick locals or owners.'),('Explore.dc.html','MExplore','Map plus what people are talking about.'),('ExploreSearch.dc.html','MExplore','Results for a search.'),('ExploreLumen.dc.html','MExplore','A place picked from the dropdown or map.'),('ExploreMe.dc.html','MExplore','Explore when signed in.'),('Me.dc.html','MLocals','A local\'s own profile.')]),
('B','Business profile','Everyone','#2b59d9',[('Main.dc.html','MProfile','The public page. Prototype bar switches 4 states.'),('Report.dc.html','MProfile','Suggest an edit or report the listing.'),('Photos.dc.html','MProfile','All photos.'),('History.dc.html','MProfile','Every change and who made it.')]),
('C','Posting and locals (storyboards)','Everyone','#2b59d9',[('Post.dc.html','MLocals','Post with no account. Optional reply alerts.'),('Thread.dc.html','MLocals','A single post with the owner answer.'),('Search.dc.html','MExplore','Search results page.'),('Types.dc.html','MExplore','Every category in a city.'),('BestOf.dc.html','MExplore','Ranked best-of page.'),('Book.dc.html','MProfile','Booking request, also sent to similar places.'),('Notify.dc.html','MLocals','Alerts and the Local expert badge.'),('Moderation.dc.html','MLocals','Reporting a post.')]),
('D','Owner finds us','Owner','#e5482d',[('Business.dc.html','MPublic','Marketing page. Plans and brand wall.'),('SignIn.dc.html','MPublic','Returning owners.')]),
('E','Claim and set up','Owner','#e5482d',[('Claim.dc.html','MClaim','Step 1. Business plus mobile number.'),('OTP.dc.html','MClaim','Step 2. Text code.'),('Setup.dc.html','MClaim','Step 3. Confirm info, 5 screens, no scrolling.'),('Verify.dc.html','MClaim','Step 4. Verify with Google.'),('ClaimIssue.dc.html',None,'What happens when a claim goes wrong.'),('AddBiz.dc.html',None,'Business is not listed yet.'),('Next.dc.html','MAudit','Free AI audit walkthrough, Kody on the left.'),('Audit.dc.html',None,'The full audit report.')]),
('F','Owner app, daily','Owner','#e5482d',[('OwnerHome.dc.html','MOwner','Dashboard. Verify, Kody, needs you, checklist.'),('Dashboard.dc.html','MOwner','My business: the page in owner view with edit pencils.'),('Edit.dc.html','MOwner','How editing and push-to-AI work.'),('OwnerInbox.dc.html','MOwner','Questions, bookings, suggested edits.')]),
('G','Premium','Owner, paid','#e5482d',[('OwnerPremium.dc.html','MOwner','Content calendar, AI Score, deliverables.'),('MonthReport.dc.html','MOwner','Monthly report.'),('OwnerNotes.dc.html','MAccount','Facts the owner tells AI.')]),
('H','Account and team','Owner','#e5482d',[('OwnerSettings.dc.html','MAccount','Settings.'),('OwnerTeam.dc.html','MAccount','Their team with access rules, and our team.'),('Invite.dc.html',None,'Accepting a team invite.'),('OwnerReferral.dc.html','MAccount','15% off per referral, stacks to free.'),('RefLanding.dc.html',None,'What a referred business sees.'),('OwnerHelp.dc.html','MAccount','Help center.'),('Emails.dc.html',None,'Emails owners receive.')]),
('I','Money','Owner','#237233',[('Upgrade.dc.html','MAccount','Pick a plan: Free, $500, $1,500, $3,000.'),('Checkout.dc.html','MAccount','Checkout.'),('Billing.dc.html','MAccount','Plan and billing.'),('AddLocation.dc.html',None,'Adding a second location.')]),
]
MB=[('MPublic','M1','Homepage, join, for business',6),('MExplore','M2','Explore and search',7),('MProfile','M3','Business profile',9),('MLocals','M4','Posting and locals',6),('MClaim','M5','Claim and set up',9),('MAudit','M6','Free AI audit',7),('MOwner','M7','Owner app',11),('MAccount','M8','Account, plans and billing',10)]
# ---- relayout canvas: one column per journey, mobile column last
GX=1640; x=GX
for L,name,who,col,items in COLS:
    y=0
    for f,_,_ in items:
        b=c['boards'][f]; b['x']=x; b['y']=y; y+=b['h']+200
    x+=GX
mx=x; y=0
for f,_,_,_ in MB:
    b=c['boards'][f+'.dc.html']; b['x']=mx; b['y']=y; y+=b['h']+300
order=['Flow.dc.html']+[f for _,_,_,_,it in COLS for f,_,_ in it]+[f+'.dc.html' for f,_,_,_ in MB]
c['order']=order+[o for o in c['order'] if o not in order]
# ---- page
CSS='''.fw{padding:44px 64px 56px;display:flex;flex-direction:column;gap:30px;background:#f3efe7;color:#13203a;font-family:Figtree,sans-serif}
.fh h1{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:64px;line-height:66px}.fh h1 em{color:#e5482d}
.fh p{margin:10px 0 0;font-size:17px;line-height:27px;color:#3d4658;max-width:900px}
.sec{display:flex;flex-direction:column;gap:16px}.sec h2{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:40px;line-height:44px}.sec .d{font-size:15px;line-height:23px;color:#3d4658;max-width:980px;margin:-6px 0 0}
.ey{font-size:11px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#5b6474}
.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.cd{background:#fff;border:1px solid #e4ded2;border-radius:10px;padding:18px 20px;display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:21px;color:#3d4658}.cd b{color:#13203a;font-size:15px}
.jr{display:grid;grid-template-columns:200px 1fr;gap:18px;padding:10px 0;border-top:1px solid #e4ded2}
.jl{display:flex;flex-direction:column;gap:4px}.jl .L{width:34px;height:34px;border-radius:50%;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:15px}
.jl b{font-size:16px}.jl span{font-size:12px;color:#5b6474}
.jsteps{display:flex;flex-wrap:wrap;gap:8px;align-items:stretch}
.js{display:flex;flex-direction:column;gap:3px;width:196px;padding:12px 14px;border-radius:8px;background:#fff;border:1px solid #e4ded2;text-decoration:none;color:#13203a;box-sizing:border-box}
.js:hover{border-color:#13203a}.js .t{font-size:13px;font-weight:700;line-height:18px}.js .s{font-size:12px;line-height:17px;color:#5b6474;flex:1}
.js .m{display:flex;gap:6px;margin-top:6px;align-items:center}.js .m a{margin:0 !important}.tag{display:inline-flex;align-items:center;gap:4px;height:22px;padding:0 8px;border-radius:11px;font-size:11px;font-weight:700;text-decoration:none}.tag.d{background:#13203a;color:#fff !important;font-size:11px !important;height:22px !important}.tag.mo{background:#f5e3cc;color:#13203a;border:1px solid #e6cfb2}
.mg{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.mc{display:flex;gap:14px;align-items:center;padding:16px;border-radius:10px;background:#fff;border:1px solid #e4ded2;text-decoration:none;color:#13203a}.mc:hover{border-color:#13203a}
.phn{width:40px;height:72px;border-radius:9px;border:3px solid #13203a;box-sizing:border-box;background:#f3efe7;flex-shrink:0;display:flex;flex-direction:column;justify-content:flex-end;padding:4px}.phn i{display:block;height:6px;border-radius:2px;background:#13203a}
.code{font-family:ui-monospace,Menlo,monospace;font-size:12.5px;line-height:20px;background:#13203a;color:#e6e9f0;border-radius:10px;padding:18px 20px;white-space:pre-wrap}
.lg{display:flex;gap:18px;flex-wrap:wrap;font-size:14px;align-items:center}
.sw{display:inline-block;width:22px;height:22px;border-radius:5px;vertical-align:-5px;margin-right:6px;border:1px solid rgba(0,0,0,0.1)}
table{border-collapse:collapse;width:100%;font-size:13px}td,th{text-align:left;padding:8px 10px;border-bottom:1px solid #ece6da;vertical-align:top}th{font-size:11px;letter-spacing:0.1em;text-transform:uppercase;color:#5b6474}
'''
def js(f,m,s): 
    mt=f'<a class="tag mo" href="{m}.dc.html">▯ Mobile {dict((a,b) for a,b,_,_ in MB)[m]}</a>' if m else ''
    return f'<div class="js"><a href="{f}" class="t" style="text-decoration: none; color: #13203a;">{T(f)}</a><span class="s">{s}</span><span class="m"><a class="tag d" href="{f}">▭ Desktop</a>{mt}</span></div>'
jour=''.join(f'<div class="jr"><div class="jl"><span class="L" style="background: {col};">{L}</span><b>{name}</b><span>{who} · column {L} on the canvas</span></div><div class="jsteps">{"".join(js(*i) for i in it)}</div></div>' for L,name,who,col,it in COLS)
mob=''.join(f'<a class="mc" href="{f}.dc.html"><span class="phn"><i></i></span><span style="display: flex; flex-direction: column; gap: 2px;"><span class="ey">{k} · {n} screens</span><b style="font-size: 16px;">{t}</b></span></a>' for f,k,t,n in MB)
PROMPT='''You are rebuilding Local AI Registry from a clickable design prototype.
The prototype is a set of HTML files, one per screen. Treat them as the
source of truth for layout, copy and behavior. Do not invent features.

Suggested stack (swap for ours if different): Next.js + TypeScript +
Tailwind. Mobile-first: build each page from its mobile board (M1 to M8)
first, then widen it to the matching desktop screen. Flow.dc.html lists
which mobile board goes with which desktop screen.

Before writing code, read these files in order and summarize them back:
  1. Flow.dc.html (this page: journeys, rules, tokens)
  2. Main.dc.html (business profile, 4 states)
  3. Setup.dc.html and MClaim.dc.html (claim flow)
  4. OwnerHome.dc.html and MOwner.dc.html (owner app)

Then build in this order, one PR each:
  1. Design tokens and base components (see the Tokens section)
  2. Public pages: Home, Explore, Search, Business profile
  3. Posting: post without an account, thread, alerts
  4. Claim flow: claim, text code, confirm info (5 screens), verify
  5. Owner app: dashboard, my business (edit), inbox
  6. Premium, plans, checkout, billing, team, referral
  7. Free AI audit walkthrough

Rules that are easy to get wrong are listed under "Product rules".
Ask me before changing any of them.'''
BODY=f'''<div class="fw">
<div class="fh"><span style="display: flex; align-items: center; gap: 10px;">{LOGO}<b style="font-size: 17px;">Local AI Registry</b><span class="ey" style="margin-left: 8px;">Prototype map · handoff</span></span><h1 style="margin-top: 18px;">Everything, in the order <em>people use it</em>.</h1><p>This is the start page. Every card below opens a screen. Desktop screens are laid out on the canvas in columns A to I, left to right, one column per journey. Mobile screens are in the last column, boards M1 to M8, with several phones per board.</p></div>

<div class="sec"><span class="ey">Start here</span><h2>How to read the canvas</h2><div class="g4">
<div class="cd"><b>Columns are journeys</b>Column A is locals finding things. Column I is money. Go top to bottom inside a column to follow a flow.</div>
<div class="cd"><b>Numbers are desktop screens</b>1 to 34, with letters for sub-screens (3b, 11c). "M" numbers are mobile boards.</div>
<div class="cd"><b>Dark bar on top = prototype control</b>Switches states, plans or steps so you can see every version. It is not part of the product. Do not build it.</div>
<div class="cd"><b>Storyboards</b>Boards with a grey "Storyboard" label show a flow as numbered frames instead of a working page.</div>
</div></div>

<div class="sec"><span class="ey">Journeys</span><h2>Every screen, desktop and mobile</h2><p class="d">Each card links to the desktop screen. The peach tag links to the mobile board that covers it. Screens with no peach tag are edge cases where mobile reuses a nearby screen.</p>{jour}</div>

<div class="sec"><span class="ey">Mobile</span><h2>Mobile boards</h2><p class="d">390 by 844, iPhone size. Build mobile first. Locals get a bottom tab bar (Explore, Search, Post, Alerts, Me). Owners get Home, Business, Inbox, Premium, More. Edits, booking, reports, approvals and booking with Kody open as bottom sheets.</p><div class="mg">{mob}</div></div>

<div class="sec"><span class="ey">For the builder</span><h2>Rebuilding this with Claude</h2><p class="d">Every screen is a single HTML file. Download the project from the artifact page (or ask Claude to read a board by its file name) and hand it the prompt below. Build one journey at a time, and compare each page side by side with its board before moving on.</p><div class="code">{PROMPT}</div></div>

<div class="sec"><span class="ey">Tokens</span><h2>Design system</h2><div class="g3">
<div class="cd"><b>Color</b><span><span class="sw" style="background: #f3efe7;"></span>Cream background #f3efe7</span><span><span class="sw" style="background: #13203a;"></span>Navy text and buttons #13203a</span><span><span class="sw" style="background: #e5482d;"></span>Red-orange accent #e5482d</span><span><span class="sw" style="background: #2b59d9;"></span>Blue links and data #2b59d9</span><span><span class="sw" style="background: #f5e3cc;"></span>Peach panels #f5e3cc</span><span><span class="sw" style="background: #237233;"></span>Green confirmed #237233</span></div>
<div class="cd"><b>Type</b><span>Headlines: Cormorant Garamond 500, big. 64 to 44px desktop, 46 to 34px mobile. One italic accent word in red-orange.</span><span>Body: Figtree. 15 to 17px desktop, 17px mobile. Never below 12px.</span></div>
<div class="cd"><b>Buttons and shapes</b><span>All buttons are pills. Primary: navy fill, white text. Secondary: white with navy outline. Red-orange only for Post and the main marketing CTA.</span><span>Cards: white, 1px #e4ded2 border, 8 to 14px radius. Tap targets 44px or more on mobile.</span></div>
</div></div>


<div class="sec"><span class="ey">Homepage</span><h2>Motion and assets: the live homepage stays as it is</h2><p class="d">The prototype homepage (board 1) shows the new hero, brand cards and Trending. Below them are two dashed placeholder blocks: "Insert current homepage sections here" and "Insert current footer here." Copy those parts straight from today's live homepage at localairegistry.com, with the same order, copy and animations. Do not redesign them.</p></div>
<div class="sec"><span class="ey">Do not break these</span><h2>Product rules</h2><table><tr><th style="width: 260px;">Rule</th><th>Detail</th></tr>
<tr><td><b>Marks on every fact</b></td><td><span style="color: #237233;">●</span> solid green = confirmed. <span style="color: #e8740c;">○</span> hollow orange = a visitor submitted it. <span style="color: #8a93a3;">△</span> grey triangle = AI guess. Shown next to every fact on the profile.</td></tr>
<tr><td><b>Posting needs nothing</b></td><td>No account, no code, no contact info to post. After posting, optionally ask for email or mobile, only to send reply alerts.</td></tr>
<tr><td><b>Owner edits</b></td><td>Pencil only on facts (services, prices, hours, description, details). Never on titles, Locals, Photos, References or measured data like Busy times. Changes show the old value crossed out to the owner only, plus "AI is still showing the old information" until it is pushed.</td></tr>
<tr><td><b>Claim flow</b></td><td>4 steps: claim, text code, confirm info (5 screens: basics, services, known for, team, links), verify. No screen scrolls. Kody and support visible on every step.</td></tr>
<tr><td><b>Plans</b></td><td>Free, Fix $500/mo, Trust $1,500/mo, Authority $3,000/mo. The owner header button always says "See plans".</td></tr>
<tr><td><b>Referral</b></td><td>15% off the referrer's plan per referred business that starts a plan, for as long as they stay. Stacks until free. The action is a booking link, not an in-app tracker.</td></tr>
<tr><td><b>OrbitBack</b></td><td>Separate company. Mentioned only once, as a card on the Referral page. No cashback anywhere else, including booking.</td></tr>
<tr><td><b>AI engines</b></td><td>Always "ChatGPT, Gemini and Claude". No answers written by Local AI Registry on business pages.</td></tr>
<tr><td><b>Writing</b></td><td>Plain language for non-technical owners. No em dashes anywhere.</td></tr></table></div>

<div class="sec"><span class="ey">Still open</span><h2>Placeholders to fill before launch</h2><div class="g3">
<div class="cd"><b>Links</b>Calendly for Kody and for OrbitBack. Badge image at localairegistry.com/badge/[slug].svg. /methodology and /developers pages.</div>
<div class="cd"><b>Data</b>Map is a drawing, needs a real map API. AI Score, audit numbers and plan forecasts are sample numbers. Yearly price is 12 times monthly, no discount set.</div>
<div class="cd"><b>Needs building behind the scenes</b>Checking whether the badge and schema are on the owner's site. Sending suggested edits to owners. The 21 brands on the homepage need real public pages.</div>
</div></div>
</div>'''
import re as _re
_inner=BODY[len('<div class="fw">'):BODY.rindex('</div>')]
_secs=_re.split(r'(?=<div class="sec">)',_inner)
head,secs=_secs[0],_secs[1:]
def _has(s,k): return k in s
parts=[('Flow.dc.html','0 · Start here: every screen',[s for s in secs if _has(s,'How to read the canvas') or _has(s,'Every screen, desktop and mobile')]),
       ('FlowBuild.dc.html','0b · Mobile, rebuilding with Claude, design system',[s for s in secs if _has(s,'Mobile boards') or _has(s,'Rebuilding this with Claude') or _has(s,'Design system')]),
       ('FlowRules.dc.html','0c · Homepage, product rules, open items',[s for s in secs if _has(s,'Motion and assets') or _has(s,'Product rules') or _has(s,'Placeholders to fill')])]
NAV='<div style="display: flex; gap: 10px; flex-wrap: wrap;">'+''.join(f'<a href="{f}" style="height: 40px; padding: 0 16px; border-radius: 9999px; border: 1px solid #13203a; display: inline-flex; align-items: center; font-size: 14px; font-weight: 700; text-decoration: none; color: #13203a;">{t}</a>' for f,t,_ in parts)+'</div>'
H={'Flow.dc.html':2770,'FlowBuild.dc.html':1770,'FlowRules.dc.html':1890}
for i,(f,t,ss) in enumerate(parts):
    top=head if i==0 else f'<div class="fh"><span style="display: flex; align-items: center; gap: 10px;">{LOGO}<b style="font-size: 17px;">Local AI Registry</b><span class="ey" style="margin-left: 8px;">Prototype map · handoff</span></span><h1 style="margin-top: 18px; font-size: 52px; line-height: 56px;">{t.split(" · ",1)[1]}</h1></div>'
    body='<div class="fw">'+top+NAV+''.join(ss)+'</div>'
    open(P+f,'w').write(page('Local AI Registry: '+t,CSS,body,'    return {};'))
    b=c['boards'].get(f,{'w':1440,'is_interactive':True})
    b.update({'title':t,'x':0,'y':sum(H[p[0]]+200 for p in parts[:i]),'h':H[f],'w':1440})
    c['boards'][f]=b
c['order']=[p[0] for p in parts]+[o for o in c['order'] if o not in [p[0] for p in parts]]
c['title']='Local AI Registry: prototype'
json.dump(c,open(P+'canvas.json','w'))
print('ok')
