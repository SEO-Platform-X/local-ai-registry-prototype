import sys; sys.path.insert(0,'/tmp/gen'); from common import *
# ---------------- REQUEST ----------------
CSS_R='''.fld{display:flex;flex-direction:column;gap:6px}
.fld label{font-size:13px;font-weight:700}
.inp{height:46px;border:1px solid #b0b0b0;border-radius:8px;padding:0 14px;font-family:inherit;font-size:15px;display:flex;align-items:center;background:#ffffff}
.chip{display:inline-flex;align-items:center;height:34px;padding:0 14px;border:1px solid #dddddd;border-radius:17px;font-size:13px;background:#ffffff}
.chip.on{border:2px solid #222222;padding:0 13px;font-weight:600}
.rsp{display:grid;grid-template-columns:1fr auto;gap:16px;padding:18px 20px;border:1px solid #dddddd;border-radius:14px;align-items:center}
.sc{display:inline-flex;align-items:center;height:22px;padding:0 8px;border-radius:11px;font-size:12px;font-weight:700;background:#ddf1e1;color:#237233}
'''
BODY_R=header('<a href="Home.dc.html" class="btn b-sm" style="border-color: #dddddd;">Back to results</a>')+'''
<div style="padding: 36px 120px 56px; display: grid; grid-template-columns: 1fr 420px; gap: 40px; align-items: start;">
<div style="display: flex; flex-direction: column; gap: 22px;">
<div style="display: flex; flex-direction: column; gap: 6px;"><span class="mu" style="font-size: 13px; font-weight: 600;">Post a request</span><h1 style="margin: 0; font-size: 32px; line-height: 38px; font-weight: 600;">Tell businesses what you want. They come to you.</h1><span style="font-size: 15px; line-height: 23px; color: #484848;">This is not an auction. Businesses reply with a real opening and a price range, and you choose on fit, reviews and AI Score, not just the lowest number.</span></div>
<sc-if value="{{notSent}}" hint-placeholder-val="{{ true }}">
<div class="card" style="padding: 24px; display: flex; flex-direction: column; gap: 18px;">
<div class="fld"><label>What do you want?</label><span class="inp">Lip filler, first time</span></div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;"><div class="fld"><label>Where</label><span class="inp">Irvine, within 10 miles</span></div><div class="fld"><label>When</label><span class="inp">Saturdays in October</span></div></div>
<div class="fld"><label>Budget</label><span class="inp">$400 to $700</span></div>
<div class="fld"><label>What matters to you</label><div style="display: flex; gap: 8px; flex-wrap: wrap;"><span class="chip on">Natural-looking</span><span class="chip on">A nurse or doctor injects</span><span class="chip on">Takes HSA</span><span class="chip">Free parking</span><span class="chip">Speaks Spanish</span><span class="chip">Can dissolve if needed</span></div></div>
<div class="fld"><label>Anything else</label><span class="inp" style="height: 80px; align-items: flex-start; padding-top: 12px; color: #6a6a6a;">I've never had filler. I want small and subtle.</span></div>
<div style="display: flex; align-items: center; justify-content: space-between; gap: 16px; padding-top: 4px;"><span class="sub" style="max-width: 420px;">Your name and contact stay hidden. Businesses only see the request. You choose who to reveal yourself to.</span><span class="btn b-coral" onClick="{{send}}">Send to 6 matching businesses</span></div>
</div>
</sc-if>
<sc-if value="{{sent}}" hint-placeholder-val="{{ false }}">
<div style="display: flex; flex-direction: column; gap: 12px;"><div style="display: flex; align-items: baseline; justify-content: space-between;"><h2 style="margin: 0; font-size: 22px; font-weight: 600;">3 replies so far</h2><span class="mu" style="font-size: 13px;">Sent 2 hours ago to 6 businesses · <span onClick="{{reset}}" style="text-decoration: underline; cursor: pointer;">Edit request</span></span></div>
<sc-for list="{{replies}}" as="r" hint-placeholder-count="3"><div class="rsp"><div style="display: flex; flex-direction: column; gap: 6px;"><span style="display: flex; align-items: center; gap: 10px;"><strong style="font-size: 17px;">{{r.n}}</strong><span class="sc" style="background: {{r.sbg}}; color: {{r.sc}};">AI {{r.s}}</span><span class="mu" style="font-size: 13px;">★ {{r.r}} · {{r.d}}</span></span><span style="font-size: 14px; line-height: 21px;">"{{r.msg}}"</span><span style="display: flex; gap: 16px; font-size: 13px; color: #484848; flex-wrap: wrap;"><span><strong>Opening:</strong> {{r.when}}</span><span><strong>Price:</strong> {{r.price}}</span><span><strong>Injector:</strong> {{r.who}}</span></span></div><div style="display: flex; flex-direction: column; gap: 8px;"><a href="{{r.href}}" class="btn b-dark b-sm">Choose and reveal me</a><a href="Main.dc.html" class="btn b-sm">See their page</a></div></div></sc-for>
<span class="sub">3 more businesses have seen it. Unclaimed businesses cannot reply until they claim their page.</span></div>
</sc-if>
</div>
<div style="display: flex; flex-direction: column; gap: 14px; position: sticky; top: 20px;">
<div class="card" style="padding: 20px; display: flex; flex-direction: column; gap: 10px;"><strong style="font-size: 15px;">Who sees your request</strong><span style="font-size: 14px; line-height: 21px; color: #484848;">6 med spas within 10 miles whose records match: they offer lip filler, a licensed nurse or doctor injects, and they take HSA.</span><span class="sub">Matching uses each business's verified record, not who pays the most.</span></div>
<div class="card" style="padding: 20px; display: flex; flex-direction: column; gap: 10px;"><strong style="font-size: 15px;">How it works</strong><ol style="margin: 0; padding-left: 18px; font-size: 14px; line-height: 22px; color: #484848;"><li>You post what you want. Nobody sees your name.</li><li>Matching businesses reply within a day with a real opening and a price range.</li><li>You pick one. Only then do they get your name and number.</li><li>Book through the registry and get cashback where it is on.</li></ol></div>
</div>
</div>'''
JS_R='''    const sent = !!(this.state && this.state.sent);
    const replies = [
      ['Lumen Aesthetics', 58, '4.9', '0.4 mi', "Most first-timers start with a half syringe. Nadia has Saturday Oct 10 at 11 AM. You can always add more later, but you can't take it back as easily.", 'Sat, Oct 10, 11 AM', '$450 half, $780 full', 'Nadia R., NP', 'Main.dc.html'],
      ['Spectrum Aesthetics MD', 81, '4.8', '0.9 mi', 'Dr. Chen does every first lip appointment. Saturday Oct 17 at 9 AM is open.', 'Sat, Oct 17, 9 AM', '$500 to $820', 'Dr. Alan Chen, MD', 'Main.dc.html'],
      ['Coastline MedSpa', 84, '4.8', '6.1 mi', 'We can do Saturday Oct 24. 20% cashback applies if you book through the registry.', 'Sat, Oct 24, 1 PM', '$600 to $850', 'Registered nurse', 'Main.dc.html']
    ].map(x => ({ n: x[0], s: String(x[1]), sbg: x[1] >= 75 ? '#ddf1e1' : '#fbe9e7', sc: x[1] >= 75 ? '#237233' : '#c13515', r: x[2], d: x[3], msg: x[4], when: x[5], price: x[6], who: x[7], href: x[8] }));
    return { sent, notSent: !sent, replies, send: () => this.setState({ sent: true }), reset: () => this.setState({ sent: false }) };'''
open(P+'Request.dc.html','w').write(page('Post a request',CSS_R,BODY_R,JS_R))

# ---------------- CHECKOUT ----------------
CSS_C='''.inp{height:46px;border:1px solid #b0b0b0;border-radius:8px;padding:0 14px;font-family:inherit;font-size:15px;display:flex;align-items:center;background:#ffffff;color:#222222}
.fld{display:flex;flex-direction:column;gap:6px}.fld label{font-size:13px;font-weight:700}
.seg{display:inline-flex;border:1px solid #dddddd;border-radius:22px;padding:3px}
.seg span{height:34px;padding:0 16px;border-radius:18px;display:inline-flex;align-items:center;font-size:13px;font-weight:600;cursor:pointer;color:#6a6a6a}
.seg span.on{background:#222222;color:#ffffff}
.row{display:flex;justify-content:space-between;gap:12px;font-size:14px;padding:6px 0}
.wk{display:grid;grid-template-columns:90px 1fr;gap:14px;padding:12px 0;border-top:1px solid #ebebeb;font-size:14px;line-height:21px}
'''
BODY_C=header('<a href="Upgrade.dc.html" class="btn b-sm" style="border-color: #dddddd;">Back to plans</a>')+'''
<sc-if value="{{notPaid}}" hint-placeholder-val="{{ true }}">
<div style="padding: 36px 120px 56px; display: grid; grid-template-columns: 1fr 420px; gap: 40px; align-items: start;">
<div style="display: flex; flex-direction: column; gap: 22px;">
<div style="display: flex; flex-direction: column; gap: 6px;"><span class="mu" style="font-size: 13px; font-weight: 600;">Lumen Aesthetics · Checkout</span><h1 style="margin: 0; font-size: 32px; line-height: 38px; font-weight: 600;">Start Tier 4 · Authority</h1><span style="font-size: 15px; line-height: 23px; color: #484848;">We do the work. You approve anything that goes out under your name. Cancel any month.</span></div>
<div style="display: flex; align-items: center; gap: 14px;"><span class="seg"><span class="{{mOn}}" onClick="{{pickM}}">Monthly</span><span class="{{aOn}}" onClick="{{pickA}}">Yearly, 2 months free</span></span></div>
<div class="card" style="padding: 24px; display: flex; flex-direction: column; gap: 16px;"><strong style="font-size: 16px;">Payment</strong>
<div class="fld"><label>Name on card</label><span class="inp">Priya Nair</span></div>
<div class="fld"><label>Card number</label><span class="inp">4417 •••• •••• ••••</span></div>
<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px;"><div class="fld"><label>Expires</label><span class="inp">08 / 29</span></div><div class="fld"><label>CVC</label><span class="inp">•••</span></div><div class="fld"><label>ZIP</label><span class="inp">92618</span></div></div>
<div class="fld"><label>Business name on invoices</label><span class="inp">Lumen Aesthetics Inc.</span></div></div>
<div class="card" style="padding: 20px 24px; display: flex; flex-direction: column; gap: 6px;"><strong style="font-size: 16px;">Connect so we can do the work</strong><span class="sub">You can do this now or from your dashboard.</span><div class="row"><span>Google Business Profile</span><span style="color: #237233; font-weight: 600;">Connected when you claimed</span></div><div class="row"><span>Instagram and Facebook</span><span style="font-weight: 600;">Connect</span></div><div class="row"><span>Your website</span><span style="font-weight: 600;">Connect or invite your web person</span></div></div>
</div>
<div class="card" style="padding: 24px; display: flex; flex-direction: column; gap: 14px; position: sticky; top: 20px;"><span class="eb" style="font-size: 11px; font-weight: 700; color: #6a6a6a; text-transform: uppercase; letter-spacing: 0.06em;">Order</span><strong style="font-size: 20px;">Tier 4 · Authority</strong><span class="sub">Everything in Tier 3, plus press, lists, articles, video and citation building. About 40 tasks a month.</span>
<div style="border-top: 1px solid #ebebeb; padding-top: 8px;"><div class="row"><span class="mu">Plan</span><strong>{{price}}</strong></div><div class="row"><span class="mu">Billed</span><strong>{{billed}}</strong></div><div class="row"><span class="mu">AI Score today</span><strong style="color: #c13515;">58</strong></div><div class="row"><span class="mu">Projected by December</span><strong style="color: #237233;">93</strong></div><div class="row"><span class="mu">First work goes out</span><strong>Oct 1, after you approve</strong></div></div>
<span class="btn b-coral" style="width: 100%; box-sizing: border-box;" onClick="{{pay}}">Start plan</span>
<span class="sub" style="font-size: 12px;">Projections come from similar businesses on the registry and are not a guarantee. Cancel any time before your next billing date.</span></div>
</div>
</sc-if>
<sc-if value="{{paid}}" hint-placeholder-val="{{ false }}">
<div style="padding: 48px 120px 64px; display: flex; flex-direction: column; align-items: center; gap: 22px;">
<span style="width: 64px; height: 64px; border-radius: 50%; background: #ddf1e1; color: #237233; display: flex; align-items: center; justify-content: center; font-size: 30px; font-weight: 700;">✓</span>
<h1 style="margin: 0; font-size: 34px; line-height: 40px; font-weight: 600; text-align: center;">You're on Tier 4, Dr. Nair</h1>
<span style="font-size: 16px; line-height: 24px; color: #484848; text-align: center; max-width: 620px;">Receipt sent to priya@lumenaesthetics.com. Here is what happens in your first month. Every item waits for your approval before it goes out.</span>
<div class="card" style="width: 720px; padding: 8px 24px 12px; display: flex; flex-direction: column;"><sc-for list="{{weeks}}" as="w" hint-placeholder-count="4"><div class="wk"><strong>{{w.w}}</strong><span>{{w.t}}</span></div></sc-for></div>
<div style="display: flex; gap: 12px;"><a href="Dashboard.dc.html" class="btn b-coral">Go to your dashboard</a><a href="Main.dc.html" class="btn">See your public page</a></div>
</div>
</sc-if>'''
JS_C='''    const paid = !!(this.state && this.state.paid), yr = !!(this.state && this.state.yr);
    const weeks = [['This week', 'Kody calls to walk your page with you. We connect your Google profile, Instagram and website, and run a baseline AI check.'], ['Week 1', 'We fix your hours and phone on Yelp, Apple Maps and Facebook, and draft your first Google posts and review replies for you to approve.'], ['Weeks 2 to 3', 'Schema and llms.txt on your website, all 40 directories synced, the first two articles and a press pitch.'], ['Week 4', 'Your first monthly report: AI Score, what AI now gets right, and what we do in November.']].map(x => ({ w: x[0], t: x[1] }));
    return { paid, notPaid: !paid, weeks, pay: () => this.setState({ paid: true }), mOn: yr ? '' : 'on', aOn: yr ? 'on' : '', pickM: () => this.setState({ yr: false }), pickA: () => this.setState({ yr: true }), price: yr ? '[price] / year' : '[price] / month', billed: yr ? 'Yearly' : 'Monthly' };'''
open(P+'Checkout.dc.html','w').write(page('Checkout',CSS_C,BODY_C,JS_C))

# ---------------- FLOW OVERVIEW ----------------
CSS_F='''.lane{display:flex;flex-direction:column;gap:14px}
.lh{display:flex;align-items:baseline;gap:12px}
.steps{display:flex;gap:0;align-items:stretch;flex-wrap:wrap;row-gap:18px}
.st{width:228px;display:flex;flex-direction:column;gap:8px;padding:16px;border:1px solid #dddddd;border-radius:14px;background:#ffffff;text-decoration:none;color:#222222;box-sizing:border-box}
.st:hover{border-color:#222222;box-shadow:0 6px 20px rgba(0,0,0,0.08)}
.sn{display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:50%;background:#222222;color:#ffffff;font-size:12px;font-weight:700}
.arr{width:34px;display:flex;align-items:center;justify-content:center;color:#b0b0b0;font-size:20px}
.sts{display:flex;flex-direction:column;gap:3px;font-size:12px;line-height:17px;color:#484848;margin:0;padding-left:16px}
'''
def step(n,title,who,desc,link,states=()):
    li=''.join(f'<li>{x}</li>' for x in states)
    ul=f'<ul class="sts">{li}</ul>' if states else ''
    return f'<a href="{link}" class="st"><span style="display: flex; align-items: center; justify-content: space-between;"><span class="sn">{n}</span><span class="mu" style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em;">{who}</span></span><strong style="font-size: 16px;">{title}</strong><span style="font-size: 13px; line-height: 19px; color: #484848;">{desc}</span>{ul}<span style="margin-top: auto; font-size: 13px; font-weight: 700; color: #ff385c;">Open</span></a>'
A='<span class="arr">→</span>'
cons=[step(1,'Home','Consumer','Ask anything. Answer from verified records, map and list of matches.','Home.dc.html',['3 example questions','Map and list','Request fallback']),
      step(2,'Business profile','Consumer','The full record: every fact marked and sourced.','Main.dc.html',['7 tabs','References on every tab','AI tab: machine-readable page and code']),
      step(3,'Post a request','Consumer','Tell businesses what you want. Name hidden until you pick.','Request.dc.html',['Form','Replies from 3 businesses'])]
own=[step(1,'Unclaimed profile','Owner','Owner finds their page and sees what AI gets wrong.','Main.dc.html',['State 1 in the top bar']),
     step(2,'Claim','Owner','Free. Email or phone, matched to their Google listing.','Claim.dc.html'),
     step(3,'Verify','Owner','Code by text. Page is theirs.','OTP.dc.html'),
     step(4,'Book or audit','Owner','Book 30 minutes with Kody, or run the free AI audit.','Next.dc.html'),
     step(5,'AI Visibility Report','Owner','How often and how accurately AI mentions them, and who it names instead.','Audit.dc.html'),
     step(6,'Pick a plan','Owner','Three tiers. The calendar fills as the tier goes up.','Upgrade.dc.html',['Tier 2, 3, 4','Projected AI Score']),
     step(7,'Checkout','Owner','Pay, connect accounts, see the first month.','Checkout.dc.html',['Payment','Confirmation']),
     step(8,'Owner dashboard','Owner','Profile, Inbox and Professional tools. Settings under Me.','Dashboard.dc.html',['Profile with pencil edits','Inbox','AI visibility, calendar, approvals, reports'])]
def rows(items,per):
    out=[]
    for i in range(0,len(items),per):
        chunk=items[i:i+per]; out.append('<div class="steps">'+A.join(chunk)+'</div>')
    return '\n'.join(out)
BODY_F=header('<a href="Home.dc.html" class="btn b-sm" style="border-color: #dddddd;">Start at Home</a>')+f'''
<div style="padding: 36px 120px 56px; display: flex; flex-direction: column; gap: 34px;">
<div style="display: flex; flex-direction: column; gap: 8px; max-width: 900px;"><span class="mu" style="font-size: 13px; font-weight: 600;">For the team · September 2026</span><h1 style="margin: 0; font-size: 36px; line-height: 42px; font-weight: 700; letter-spacing: -0.01em;">Local AI Registry, end to end</h1><span style="font-size: 16px; line-height: 24px; color: #484848;">Two paths through the same record. Consumers ask, compare and request. Owners claim, see what AI gets wrong, pay us to fix it, and approve the work. Click any card to open that screen. Every screen links to the next one.</span></div>
<div class="lane"><div class="lh"><h2 style="margin: 0; font-size: 22px; font-weight: 600;">Consumer path</h2><span class="sub">Free. Nobody pays to appear in answers.</span></div>{rows(cons,5)}</div>
<div class="lane"><div class="lh"><h2 style="margin: 0; font-size: 22px; font-weight: 600;">Owner path</h2><span class="sub">Claim is free. Revenue starts at step 7.</span></div>{rows(own,5)}</div>
<div class="card" style="padding: 22px 24px; display: flex; flex-direction: column; gap: 10px;"><h2 style="margin: 0; font-size: 20px; font-weight: 600;">The profile page has four states</h2><span class="sub">Switch them with the dark bar at the top of the profile screen.</span>
<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px;">
<div class="card" style="padding: 14px 16px; display: flex; flex-direction: column; gap: 4px;"><strong>1 · Unclaimed</strong><span class="sub">What we found. Owner seats empty, claim prompts, AI guesses everywhere.</span></div>
<div class="card" style="padding: 14px 16px; display: flex; flex-direction: column; gap: 4px;"><strong>2 · Claimed, nothing added</strong><span class="sub">Owner verified, but nothing confirmed yet.</span></div>
<div class="card" style="padding: 14px 16px; display: flex; flex-direction: column; gap: 4px;"><strong>3 · Claimed and paid</strong><span class="sub">Everything unlocked, owner answers questions, cashback live.</span></div>
<div class="card" style="padding: 14px 16px; display: flex; flex-direction: column; gap: 4px;"><strong>4 · Owner view</strong><span class="sub">The dashboard. Edits show the old value crossed out, with Push it to AI.</span></div>
</div></div>
<div class="card" style="padding: 22px 24px; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 20px;">
<div style="display: flex; flex-direction: column; gap: 6px;"><strong>Every fact is marked</strong><span class="sub">Solid circle: confirmed from a known source. Hollow circle: visitor submitted, dated. Hollow triangle: what AI engines say, unconfirmed.</span></div>
<div style="display: flex; flex-direction: column; gap: 6px;"><strong>Where the money is</strong><span class="sub">Owners pay for Tiers 2 to 4, where we do the AI visibility work. Cashback on bookings. Requests route demand to claimed businesses.</span></div>
<div style="display: flex; flex-direction: column; gap: 6px;"><strong>Mock data</strong><span class="sub">Lumen Aesthetics and every business, person, price and number here are invented for the prototype.</span></div>
</div>
</div>'''
open(P+'Flow.dc.html','w').write(page('Local AI Registry: end-to-end flow',CSS_F,BODY_F,'    return {};'))
print('ok')
