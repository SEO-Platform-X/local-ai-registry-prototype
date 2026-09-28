import sys; sys.path.insert(0,'/tmp/gen'); from common import *
TRI="url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='22' height='22' viewBox='0 0 22 22'%3E%3Cpath d='M11 3.5L19.5 18.5H2.5Z' fill='none' stroke='%238a8a8a' stroke-width='2.4' stroke-linejoin='round'/%3E%3C/svg%3E\") center / 100% 100% no-repeat"
CSS='''.mk{position:relative;display:inline-block;width:11px;height:11px;margin:0 6px 1px 0;vertical-align:middle;flex-shrink:0}
.mk::after{content:"";position:absolute;inset:0}
.mk-site::after{inset:2px;background:#008a05;border-radius:50%}
.mk-vis::after{inset:2px;border:1.6px solid #e8740c;border-radius:50%}
.mk-ai::after{inset:0;background:'''+TRI+'''}
.stp{display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:10px;font-size:14px;cursor:pointer;color:#484848}
.stp.on{background:#f3f3f3;color:#222222;font-weight:600}
.stp .n{width:24px;height:24px;border-radius:50%;border:1.5px solid #c8c8c8;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;flex-shrink:0}
.stp.done .n{background:#237233;border-color:#237233;color:#ffffff}
.stp.on .n{border-color:#222222}
.row{display:grid;grid-template-columns:200px 1fr auto;gap:16px;align-items:center;padding:14px 0;border-top:1px solid #ebebeb}
.row:first-child{border-top:none}
.row .v{font-size:15px;display:flex;align-items:center}
.acts{display:flex;gap:6px}
.acts span{height:34px;padding:0 14px;border-radius:17px;border:1px solid #dddddd;display:inline-flex;align-items:center;font-size:13px;font-weight:600;cursor:pointer;background:#ffffff}
.acts span.ok{background:#237233;border-color:#237233;color:#ffffff}
.bar{height:8px;border-radius:4px;background:#ebebeb;overflow:hidden}
.bar i{display:block;height:100%;background:#237233}
'''
BODY=header('<span class="mu" style="font-size: 13px;">Lumen Aesthetics · Claimed by Dr. Priya Nair</span><a href="Dashboard.dc.html" class="btn b-sm" style="border-color: #dddddd;">Skip for now</a>')+'''
<div style="padding: 32px 120px 56px; display: grid; grid-template-columns: 280px 1fr 320px; gap: 32px; align-items: start;">
<div style="display: flex; flex-direction: column; gap: 4px; position: sticky; top: 20px;"><span class="mu" style="font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; padding: 0 12px 8px;">Confirm your page</span><sc-for list="{{steps}}" as="s" hint-placeholder-count="6"><span class="stp {{s.cls}}" onClick="{{s.pick}}"><span class="n">{{s.n}}</span><span style="display: flex; flex-direction: column; gap: 1px;"><span>{{s.t}}</span><span class="mu" style="font-size: 12px; font-weight: 400;">{{s.c}}</span></span></span></sc-for></div>
<div style="display: flex; flex-direction: column; gap: 18px;">
<div style="display: flex; flex-direction: column; gap: 6px;"><span class="mu" style="font-size: 13px; font-weight: 600;">Step {{cur.n}} of 6</span><h1 style="margin: 0; font-size: 30px; line-height: 36px; font-weight: 600;">{{cur.h}}</h1><span style="font-size: 15px; line-height: 23px; color: #484848;">{{cur.sub}}</span></div>
<sc-if value="{{notDone}}" hint-placeholder-val="{{ true }}">
<div class="card" style="padding: 8px 24px;"><sc-for list="{{cur.rows}}" as="r" hint-placeholder-count="6"><div class="row"><span style="font-size: 14px; color: #6a6a6a;">{{r.k}}</span><span class="v"><span class="mk mk-{{r.m}}"></span>{{r.v}}</span><span class="acts"><span class="ok">Confirm</span><span>Fix</span><span>Not us</span></span></div></sc-for></div>
<div style="display: flex; align-items: center; justify-content: space-between; gap: 16px;"><span class="sub">Confirmed facts turn into solid circles on your page right away. Anything you skip stays marked as an AI guess.</span><span class="btn b-dark" onClick="{{next}}">{{cur.btn}}</span></div>
</sc-if>
<sc-if value="{{done}}" hint-placeholder-val="{{ false }}">
<div class="card" style="padding: 28px; display: flex; flex-direction: column; gap: 14px; align-items: flex-start;"><span style="width: 52px; height: 52px; border-radius: 50%; background: #ddf1e1; color: #237233; display: flex; align-items: center; justify-content: center; font-size: 26px; font-weight: 700;">✓</span><h2 style="margin: 0; font-size: 24px; font-weight: 600;">Your record is confirmed</h2><span style="font-size: 15px; line-height: 23px; color: #484848;">Customers now see what you confirmed, marked with solid circles. AI engines will not see it right away: they keep repeating Yelp, Apple Maps and old listings until those agree with you. Your dashboard shows exactly where they still disagree.</span><div style="display: flex; gap: 10px;"><a href="Dashboard.dc.html" class="btn b-coral">Go to your dashboard</a><a href="Main.dc.html" class="btn">See your page</a></div></div>
</sc-if>
</div>
<div style="display: flex; flex-direction: column; gap: 14px; position: sticky; top: 20px;">
<div class="card" style="padding: 20px; display: flex; flex-direction: column; gap: 10px;"><strong style="font-size: 15px;">{{conf}} of 148 facts confirmed</strong><span class="bar"><i style="width: {{pct}}%;"></i></span><span class="sub">The core four, hours, contact, services and team, are what customers and AI rely on most. Finish those and the rest can wait.</span></div>
<div class="card" style="padding: 20px; display: flex; flex-direction: column; gap: 10px;"><strong style="font-size: 15px;">Rather do it together?</strong><span class="sub">Kody walks your whole page with you in 30 minutes, on a video call.</span><a href="Next.dc.html" class="btn b-sm">Book 30 minutes with Kody</a></div>
<div class="card" style="padding: 20px; display: flex; flex-direction: column; gap: 8px;"><strong style="font-size: 15px;">How to read the marks</strong><span style="font-size: 13px; display: flex; align-items: center;"><span class="mk mk-site"></span>Confirmed</span><span style="font-size: 13px; display: flex; align-items: center;"><span class="mk mk-vis"></span>Visitor submitted</span><span style="font-size: 13px; display: flex; align-items: center;"><span class="mk mk-ai"></span>AI guess, what AI engines say</span></div>
</div>
</div>'''
JS=r'''    const si = (this.state && this.state.si) || 0;
    const S = [
      ['Hours and contact', 'Is this how customers reach you?', 'These are what AI gets wrong most often. Right now ChatGPT says you are open Mondays.', [['Phone', '(949) 555-0192', 'site'], ['Website', 'lumenaesthetics.com', 'site'], ['Monday', 'Open 10 AM to 6 PM', 'ai'], ['Tuesday to Saturday', '9 AM to 7 PM', 'site'], ['Sunday', 'Closed', 'site'], ['Booking link', 'lumenaesthetics.com/book', 'ai']], 12],
      ['Services and prices', 'What do you offer, and what does it cost?', 'People ask AI about prices more than anything else. Confirm what you offer and at least a starting price.', [['Botox', '$12 per unit', 'site'], ['Dermal filler', '$780 per syringe', 'site'], ['Lip filler, half syringe', '$450', 'vis'], ['Morpheus8 Body', 'Not offered', 'ai'], ['Consultation', '$75, credited if you book', 'vis'], ['Laser hair removal', 'Offered', 'ai']], 34],
      ['Team', 'Who treats your customers?', 'Gemini says aestheticians do your injections. Confirm who actually does.', [['Dr. Priya Nair, MD', 'Owner and medical director', 'ai'], ['Nadia R., NP', 'Nurse practitioner, injector', 'site'], ['Jess T., RN', 'Registered nurse, injector and laser', 'site'], ['Aestheticians', '3, facials and peels only', 'ai'], ['Front desk', '2', 'vis']], 22],
      ['Policies', 'What should people know before they book?', 'Cancellation, deposits and age rules. Answering these here saves you phone calls.', [['Cancellation', '24 hours notice', 'vis'], ['Late cancel or no-show fee', '$50', 'vis'], ['Deposit to book', '$50', 'ai'], ['Minimum age', '18', 'ai'], ['Refunds', 'None on product used', 'ai']], 26],
      ['Links and socials', 'Where else can people find you?', 'AI guessed these from your posts. Confirming them ties your channels to your page.', [['Instagram', 'instagram.com/lumenaesthetics', 'ai'], ['TikTok', 'tiktok.com/@lumenaesthetics', 'ai'], ['Facebook', 'facebook.com/lumenaestheticsirvine', 'ai'], ['Yelp', 'yelp.com/biz/lumen-aesthetics-irvine', 'ai'], ['Before-and-after gallery', 'lumenaesthetics.com/results', 'site']], 30],
      ['Your story', 'What makes you different?', 'Only you can answer these. They are what AI quotes when it explains why to pick you.', [['Mission', 'Natural results that still look like you', 'site'], ['Founder story', 'Opened in 2016 by Dr. Nair', 'ai'], ['What makes you different', 'Says no when a treatment is not needed', 'ai'], ['Charity', 'Pink ribbon walk, Irvine', 'site']], 24]
    ];
    const done = si >= S.length;
    const cumul = [0]; S.forEach((x, i) => cumul.push(cumul[i] + x[4]));
    const conf = done ? 148 : cumul[si];
    const steps = S.map((x, i) => ({ n: i < si ? '✓' : String(i + 1), t: x[0], c: x[4] + ' facts', cls: i < si ? 'done' : (i === si ? 'on' : ''), pick: () => this.setState({ si: i }) }));
    const c = done ? S[S.length - 1] : S[si];
    const cur = { n: String(Math.min(si + 1, 6)), h: done ? 'All done' : c[1], sub: done ? 'Every section of your page is confirmed.' : c[2], rows: c[3].map(r => ({ k: r[0], v: r[1], m: r[2] })), btn: si === S.length - 1 ? 'Finish' : 'Confirm and continue' };
    return { steps, cur, done, notDone: !done, conf: String(conf), pct: String(Math.round(conf / 148 * 100)), next: () => this.setState({ si: si + 1 }) };'''
open(P+'Setup.dc.html','w').write(page('Confirm your page',CSS,BODY,JS))
print('ok')
