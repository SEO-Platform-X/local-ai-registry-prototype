import sys,json; sys.path.insert(0,'/tmp/gen'); from common import *
CSS_F='''.lane{display:flex;flex-direction:column;gap:14px}
.lh{display:flex;align-items:baseline;gap:12px}
.steps{display:flex;align-items:stretch;flex-wrap:wrap;row-gap:18px}
.st{width:214px;display:flex;flex-direction:column;gap:8px;padding:16px;border:1px solid #dddddd;border-radius:14px;background:#ffffff;text-decoration:none;color:#222222;box-sizing:border-box}
.st:hover{border-color:#222222;box-shadow:0 6px 20px rgba(0,0,0,0.08)}
.st.money{border-color:#f3b7c3;background:#fff7f9}
.sn{display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:50%;background:#222222;color:#ffffff;font-size:12px;font-weight:700}
.arr{width:30px;display:flex;align-items:center;justify-content:center;color:#b0b0b0;font-size:20px}
.sts{display:flex;flex-direction:column;gap:3px;font-size:12px;line-height:17px;color:#484848;margin:0;padding-left:16px}
.pr{display:flex;flex-direction:column;gap:6px;padding:16px 18px;border:1px solid #ebebeb;border-radius:12px}
'''
def step(n,title,who,desc,link,states=(),money=False):
    li=''.join(f'<li>{x}</li>' for x in states); ul=f'<ul class="sts">{li}</ul>' if states else ''
    return f'<a href="{link}" class="st{" money" if money else ""}"><span style="display: flex; align-items: center; justify-content: space-between;"><span class="sn">{n}</span><span class="mu" style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em;">{who}</span></span><strong style="font-size: 16px;">{title}</strong><span style="font-size: 13px; line-height: 19px; color: #484848;">{desc}</span>{ul}<span style="margin-top: auto; font-size: 13px; font-weight: 700; color: #ff385c;">Open</span></a>'
A='<span class="arr">→</span>'
def rows(items,per=5):
    return '\n'.join('<div class="steps">'+A.join(items[i:i+per])+'</div>' for i in range(0,len(items),per))
cons=[step(1,'Homepage','Everyone','Everyone starts here. Search a business name or a city.','Home.dc.html',['A business opens Explore with it selected','Why this is not Google or Yelp']),
      step(2,'Explore','Everyone','Map on the left shows where people are talking. Conversations on the right follow the map.','Explore.dc.html',['Location, search, type, when, status, from','Hot spots and neighborhood questions']),
      step(3,'Business profile','Everyone','Locals is the first tab. Post a question, tip or heads-up.','Main.dc.html',['Strip above the tabs','Report or suggest an edit']),
      step(4,'Suggest an edit, report','Everyone','How a visitor fixes a fact, with references and change history, and how an ownership dispute works.','Report.dc.html',['Hollow circle and a reference','Page locks during a dispute']),
      step(5,'Logged in','Consumer','Explore adds a For you tab: places you follow, questions you can help with, your impact.','ExploreMe.dc.html'),
      step(6,'Your profile','Consumer','Posts, answers, badges, and which of your tips AI now repeats.','Me.dc.html')]
own=[step(1,'For business','Owner','Lands from an ad, a referral or Google. "Get your business into AI answers." · 20 sec','Business.dc.html',['Types their business in the hero']),
     step(2,'AI Visibility Report','Owner','Free, no login. What AI says, what it gets wrong, who it names instead. · 1 min','Audit.dc.html',['The hook: 38% visibility, 3 wrong facts']),
     step(3,'Claim','Owner','Email and phone. · 20 sec','Claim.dc.html'),
     step(4,'Text code','Owner','The page is theirs. · 15 sec','OTP.dc.html'),
     step(5,'Confirm info','Owner','Basics, services, 3 known-for, team, links. · 2 to 3 min, or save for later','Setup.dc.html'),
     step(6,'Dashboard','Owner','Setup tracker, verify with Google, Kody in the inbox.','OwnerHome.dc.html'),
     step(7,'Pick a plan','Owner','What each plan fixes for Lumen, from their own report. · 30 sec','Upgrade.dc.html',[],True),
     step(8,'Checkout','Owner','Card, done. · 1 min','Checkout.dc.html',[],True),
     step(9,'Premium','Owner','The first month is already on the calendar, waiting for approval.','OwnerPremium.dc.html',[],True),
     step(10,'Edit your page','Owner','Pencils on everything, tracked changes, push to AI.','Dashboard.dc.html'),
     step(11,'Inbox','Owner','Kickoff email from Steve, Kody\'s Calendly link.','OwnerInbox.dc.html'),
     step(12,'AI notes','Owner','Everything AI learned from your feedback.','OwnerNotes.dc.html',[],True)]
sales=[step(1,'Unclaimed page','Sales','Every unclaimed page is a prospect. Sales sends it with the audit.','Main.dc.html',['"Here is what ChatGPT says about you"']),
       step(2,'AI Visibility Report','Sales','The opener. No login needed to see it.','Audit.dc.html'),
       step(3,'Claim on the call','Sales','Owner claims while Kody is on the phone.','Claim.dc.html'),
       step(4,'Set up together','Sales','Kody books 30 minutes and confirms the page with them.','Next.dc.html'),
       step(5,'Straight to Premium','Sales','Paid on the call, the calendar is waiting in Premium.','OwnerPremium.dc.html',[],True)]
BODY=header('<a href="Home.dc.html" class="btn b-sm" style="border-color: #dddddd;">Start at Home</a>')+f'''
<div style="padding: 36px 120px 56px; display: flex; flex-direction: column; gap: 32px;">
<div style="display: flex; flex-direction: column; gap: 8px; max-width: 920px;"><span class="mu" style="font-size: 13px; font-weight: 600;">For the team · September 2026</span><h1 style="margin: 0; font-size: 36px; line-height: 42px; font-weight: 700; letter-spacing: -0.01em;">Local AI Registry, end to end</h1><span style="font-size: 16px; line-height: 24px; color: #484848;"><strong>The angle:</strong> community. Everyone, owners included, starts on the homepage. AI can summarize what is online, but it cannot ask the neighbor who was there last Saturday. The root page is Reddit for local businesses, with a map, and every answer attaches to a real business and can become a checked fact. Every business already has a live page, built from what neighbors know. Nothing is gated. Owners claim for free, confirm their record, and only then do we sell the work of pushing it out to AI. Same as Yelp and LinkedIn: build the profile first, upgrade later, at the moment the owner feels the gap. Click any card to open that screen.</span></div>
<div class="lane"><div class="lh"><h2 style="margin: 0; font-size: 22px; font-weight: 600;">Consumer</h2><span class="sub">Free. Nobody pays to appear in answers.</span></div>{rows(cons)}</div>
<div class="lane"><div class="lh"><h2 style="margin: 0; font-size: 22px; font-weight: 600;">Owner, self-serve</h2><span class="sub">Pink cards are where money changes hands.</span></div>{rows(own)}</div>
<div class="lane"><div class="lh"><h2 style="margin: 0; font-size: 22px; font-weight: 600;">Owner, sales-led</h2><span class="sub">Sales can reach every business, claimed or not. Unclaimed pages are the prospect list.</span></div>{rows(sales)}</div>
<div class="card" style="padding: 22px 24px; display: flex; flex-direction: column; gap: 12px;"><h2 style="margin: 0; font-size: 20px; font-weight: 600;">Principles</h2><div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px;">
<div class="pr"><strong>Pages are always live</strong><span class="sub">Claiming changes who controls the page, not whether it exists.</span></div>
<div class="pr"><strong>Confirm before we push</strong><span class="sub">We never send AI guesses out under an owner's name. Work starts only on a confirmed record.</span></div>
<div class="pr"><strong>Upsell at the gap</strong><span class="sub">Every edit shows what AI still says. That moment, not a pricing page, is the pitch.</span></div>
<div class="pr"><strong>Every fact is marked</strong><span class="sub">Solid circle confirmed, hollow circle visitor submitted, hollow triangle what AI engines say.</span></div>
<div class="pr"><strong>Four profile states</strong><span class="sub">Unclaimed, claimed with nothing added, claimed and paid, and the owner view. Switch them with the dark bar on the profile.</span></div>
<div class="pr"><strong>Mock data</strong><span class="sub">Lumen Aesthetics and every business, person, price and number are invented for the prototype.</span></div>
</div></div>
</div>'''
open(P+'Flow.dc.html','w').write(page('Local AI Registry: end-to-end flow',CSS_F,BODY,'    return {};'))
c=json.load(open(P+'canvas.json'))
W=1560
L=[('Flow.dc.html','0 · Flow overview',0,0,1440,1900,False),
   ('Home.dc.html','1 · Homepage',W,0,1440,2520,True),('Explore.dc.html','2 · Explore',W,2640,1440,1000,False),('ExploreLumen.dc.html','2a · Explore, Lumen selected from search',W,3760,1440,1000,False),('ExploreMe.dc.html','2b · Explore, logged in',W,4880,1440,1000,False),('Me.dc.html','2c · Consumer profile',W,6000,1440,1200,True),('Request.dc.html','2d · Post a request',W,7320,1440,1100,False),
   ('Main.dc.html','3 · Business profile, 4 states',2*W,0,1440,3800,True),('Report.dc.html','3b · Suggest an edit, report this listing',2*W,3920,1440,1350,True),('History.dc.html','3d · Change history',2*W,6900,1440,1100,True),('Photos.dc.html','3c · All photos',2*W,5290,1440,1500,False),
   ('Business.dc.html','4 · For business',3*W,0,1440,3600,True),
   ('Claim.dc.html','5 · Claim',4*W,0,1440,900,False),('OTP.dc.html','6 · Code by text',4*W,1020,1440,900,False),('Setup.dc.html','7 · Confirm your info, 5 steps',4*W,2040,1440,1000,True),('Next.dc.html','7b · Set up with Kody',4*W,3260,1440,1000,False),
   ('OwnerHome.dc.html','8 · Dashboard: verify ownership',5*W,0,1440,1100,True),('Dashboard.dc.html','9 · Owner: edit your page',5*W,1220,1440,3800,True),('Edit.dc.html','9b · How editing works',5*W,5140,1440,700,True),
   ('OwnerInbox.dc.html','10 · Inbox',6*W,0,1440,900,True),('OwnerPremium.dc.html','11 · Premium',6*W,1020,1440,2600,True),('OwnerNotes.dc.html','12 · AI notes',6*W,4760,1440,900,True),
   ('OwnerSettings.dc.html','13 · Settings',7*W,0,1440,1700,True),('OwnerReferral.dc.html','14 · Referral and cashback',7*W,1820,1440,1000,True),('OwnerHelp.dc.html','15 · Help center',7*W,2940,1440,900,True),
   ('Audit.dc.html','16 · AI Visibility Report',8*W,0,1440,3200,True),('Upgrade.dc.html','17 · Pick a plan',8*W,3320,1440,1500,True),('Checkout.dc.html','18 · Checkout',8*W,4940,1440,1100,False)]
c['boards']={}
for f,tl,x,y,w,h,ex in L:
    b={'x':x,'y':y,'w':w,'h':h,'title':tl,'is_interactive':True}
    if ex: b['expand']='fill'
    c['boards'][f]=b
c['order']=[x[0] for x in L]; c['launch']={'view':'focused','file':'Flow.dc.html'}
json.dump(c,open(P+'canvas.json','w'))
print('ok')
