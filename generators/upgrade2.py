import sys; sys.path.insert(0,'/tmp/gen'); from common import *
exec(open('/tmp/ed61.py').read().split("CL=['Claim'")[0])
CSS=r'''.wrapU{display:grid;grid-template-columns:1fr 340px;gap:28px;padding:32px 40px 56px;align-items:start}
.pc{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.pl{display:flex;flex-direction:column;gap:10px;padding:20px;border-radius:16px;border:1px solid #e3e3e3;background:#ffffff;cursor:pointer}
.pl.on{border:2px solid #222222;box-shadow:0 8px 24px rgba(0,0,0,0.08)}
.pl .nm{display:flex;justify-content:space-between;align-items:center;font-size:18px;font-weight:700}
.pl .pr{font-size:14px;color:#6a6a6a}
.pl .sc{font-size:13px;font-weight:700;color:#237233}
.pl ul{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:6px;font-size:13px;line-height:18px;color:#484848}
.pl li::before{content:"✓ ";color:#237233;font-weight:700}
.tag{display:inline-flex;align-items:center;height:22px;padding:0 9px;border-radius:11px;font-size:11px;font-weight:700}
.fx{display:flex;flex-direction:column;gap:0;border:1px solid #e6e6e6;border-radius:16px;background:#ffffff;overflow:hidden}
.fr2{display:grid;grid-template-columns:1fr 1fr 110px;gap:16px;align-items:center;padding:14px 18px;border-top:1px solid #f0f0f0;font-size:14px}
.fr2:first-child{border-top:none}
.fr2 .p{color:#c13515}
.fr2 .f{color:#1c5f2a;font-weight:600}
.lk{color:#8a8a8a;font-weight:600;font-size:12px}
.sum{display:flex;flex-direction:column;gap:14px;padding:22px;border-radius:18px;background:#ffffff;border:1px solid #e6e6e6;position:sticky;top:20px}
.sr{display:flex;justify-content:space-between;font-size:14px}
.sr b{font-size:15px}
'''
BODY=fhead(['Pick a plan','Checkout','Start'],1,'<a href="OwnerPremium.dc.html" class="btn b-sm">Back to Premium</a>')+'''<div class="wrapU"><div style="display: flex; flex-direction: column; gap: 22px;">
<div style="display: flex; flex-direction: column; gap: 6px;"><span class="mu" style="font-size: 13px; font-weight: 600;">Lumen Aesthetics · AI Score 58 today</span><h1 style="margin: 0; font-size: 32px; line-height: 38px;">Fix what AI gets wrong about Lumen</h1><span style="font-size: 15px; line-height: 23px; color: #484848; max-width: 760px;">Your page on Local AI Registry is the record. Each plan gets that record into more of the places ChatGPT, Gemini and Claude read, until they all say the same thing you do. Nothing goes out until you approve it.</span></div>
<div class="pc"><sc-for list="{{plans}}" as="p" hint-placeholder-count="4"><div class="pl {{p.cls}}" onClick="{{p.pick}}"><span class="nm">{{p.n}}<span class="tag" style="background: {{p.tbg}}; color: {{p.tfg}}; display: {{p.td}};">{{p.tg}}</span></span><span class="pr">{{p.pr}}</span><span style="font-size: 14px; font-weight: 600; line-height: 19px;">{{p.line}}</span><span class="sc">{{p.sc}}</span><ul><sc-for list="{{p.inc}}" as="i" hint-placeholder-count="4"><li>{{i}}</li></sc-for></ul></div></sc-for></div>
<div style="display: flex; flex-direction: column; gap: 10px;"><h2 style="margin: 0; font-size: 20px;">What {{selName}} fixes for Lumen</h2><span class="mu" style="font-size: 13px;">From your free AI Visibility Report</span><div class="fx"><sc-for list="{{fixes}}" as="f" hint-placeholder-count="7"><div class="fr2"><span class="p">{{f.p}}</span><span class="{{f.c}}">{{f.f}}</span><span class="lk">{{f.t}}</span></div></sc-for></div></div></div>
<div class="sum"><span class="mu" style="font-size: 12px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase;">Your plan</span><strong style="font-size: 22px;">{{selName}}</strong><div class="sr"><span class="mu">Price</span><b>{{selPrice}}</b></div><div class="sr"><span class="mu">Pieces of work in October</span><b>{{selCount}}</b></div><div class="sr"><span class="mu">AI Score today</span><b>58</b></div><div class="sr"><span class="mu">Projected by March</span><b style="color: #237233;">{{selScore}}</b></div>
<sc-if value="{{paid}}" hint-placeholder-val="{{ true }}"><a href="Checkout.dc.html" class="btn b-coral">Start {{selName}}</a></sc-if><sc-if value="{{free}}" hint-placeholder-val="{{ false }}"><a href="OwnerHome.dc.html" class="btn">Stay on Free</a></sc-if><a href="Next.dc.html" class="btn">Talk to Kody first</a>
<span class="mu" style="font-size: 12px; line-height: 17px;">No contract. Change or cancel any month. Projections come from similar businesses on the registry after 90 days and are not a guarantee.</span></div></div>'''
JS=r'''    const S = this.state || {}; const sel = S.sel === undefined ? 2 : S.sel;
    const P = [
      ['Free', 'Free', 'Your page and your AI Score', 'Stays at 58', ['Claim and edit your page', 'AI Score and prompts', 'Answer locals'], '', 0],
      ['Fix', '[price] / month', 'Get listed everywhere AI looks', 'About 63 by March', ['A directory submission every day', '31 directories in October'], '', 31],
      ['Trust', '[price] / month', 'Make every source agree, and answer for you', 'About 72 by March', ['Everything in Fix', 'Negative review disputes', 'Autopilot review replies and answers', 'Press releases', 'AI code on your photos', 'Google posts and optimization', 'Review link and velocity check'], 'Most picked', 57],
      ['Authority', '[price] / month', 'Own the answer in Irvine', 'About 80 by March', ['Everything in Trust', 'Technical and speed fixes', 'URL restructuring and topical map', 'Semantic content and entity mapping', 'Cannibalization fix', 'Articles and blogs', 'Your only, first and best story'], '', 69]];
    const plans = P.map((p, i) => ({ n: p[0], pr: p[1], line: p[2], sc: p[3], inc: p[4], tg: p[5], td: p[5] ? 'inline-flex' : 'none', tbg: '#e3f4e6', tfg: '#1c5f2a', cls: i === sel ? 'on' : '', pick: () => this.setState({ sel: i }) }));
    const F = [[1, 'Six listings disagree on your hours', 'Every directory gets the hours you confirmed'], [1, 'Missing from Bing Places, Nextdoor and 31 more', 'Listed on all of them in 31 days'], [2, '0 of 612 reviews answered', 'Every new review answered, in your voice'], [2, 'Gemini says aestheticians inject', 'Corrected at the source, then pushed to AI'], [2, '48 photos AI cannot read', 'All 51 photos tagged with what, where and who'], [3, 'No Irvine med spa owns "Morpheus8 Body"', 'Articles and pages that make it Lumen'], [3, 'Coastline shows up in 78% of answers', 'Close the gap with lists, press and entity mapping']];
    const TN = ['Free', 'Fix', 'Trust', 'Authority'];
    const fixes = F.map(f => ({ p: f[1], f: f[0] <= sel ? f[2] : 'Not in ' + TN[sel], c: f[0] <= sel ? 'f' : 'lk', t: f[0] <= sel ? 'Included' : 'In ' + TN[f[0]] }));
    const s = P[sel];
    return { plans, fixes, selName: s[0], selPrice: s[1], selCount: String(s[6]), selScore: ['58', '63', '72', '80'][sel], paid: sel > 0, free: sel === 0 };'''
out=page('Pick a plan',CSS,BODY,JS).replace('background: #ffffff; position: relative;">','background: #f7f7f7; position: relative;">',1)
open(P+'Upgrade.dc.html','w').write(out); print('ok',out.count('\u2014'))
