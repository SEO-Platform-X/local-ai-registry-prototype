import sys; sys.path.insert(0,'/tmp/gen'); from common import *
exec(open('/tmp/ed61.py').read().split("CL=['Claim'")[0])
TRI="url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='22' height='22' viewBox='0 0 22 22'%3E%3Cpath d='M11 3.5L19.5 18.5H2.5Z' fill='none' stroke='%238a8a8a' stroke-width='2.4' stroke-linejoin='round'/%3E%3C/svg%3E\") center / 100% 100% no-repeat"
CSS=r'''.wrapS{display:grid;grid-template-columns:240px 1fr 300px;gap:32px;padding:36px 40px 56px;align-items:start}
.stl{display:flex;flex-direction:column;gap:4px;position:sticky;top:20px}
.st{display:flex;align-items:center;gap:12px;padding:10px 12px;border-radius:12px;cursor:pointer;font-size:14px;font-weight:600;color:#6a6a6a}
.st.on{background:#ffffff;color:#222222;box-shadow:0 1px 4px rgba(0,0,0,0.08)}
.st .c{width:26px;height:26px;border-radius:50%;background:#ebebeb;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;flex-shrink:0}
.st.done .c{background:#237233;color:#ffffff}
.st.on .c{background:#222222;color:#ffffff}
.pane{background:#ffffff;border:1px solid #e6e6e6;border-radius:18px;padding:28px 30px;display:flex;flex-direction:column;gap:18px}
.pane h1{margin:0;font-size:26px;line-height:32px}
.fr{display:grid;grid-template-columns:150px 1fr auto;gap:14px;align-items:center;padding:14px 0;border-top:1px solid #f0f0f0}
.fr .k{font-size:13px;font-weight:600;color:#6a6a6a}
.fr .v{font-size:15px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.fr .v s{color:#a0a0a0;font-size:13px}
.acts{display:flex;gap:6px}
.chipb{display:inline-flex;align-items:center;height:32px;padding:0 12px;border-radius:16px;border:1px solid #dddddd;font-size:13px;font-weight:600;cursor:pointer;background:#ffffff}
.chipb.ok{background:#237233;border-color:#237233;color:#ffffff}
.chipb.no{background:#f1f1f1;color:#8a8a8a;border-color:#f1f1f1}
.kf{display:flex;flex-wrap:wrap;gap:10px}
.kc{display:inline-flex;align-items:center;gap:8px;height:44px;padding:0 16px;border-radius:22px;border:1px solid #dddddd;font-size:14px;font-weight:600;cursor:pointer;background:#ffffff}
.kc.on{border:2px solid #222222;background:#fff6f2}
.kc .n{width:20px;height:20px;border-radius:50%;background:#ff385c;color:#ffffff;font-size:11px;display:flex;align-items:center;justify-content:center}
.mk{position:relative;display:inline-block;width:11px;height:11px;flex-shrink:0}
.mk::after{content:"";position:absolute;inset:0}
.mk-site::after{inset:2px;background:#008a05;border-radius:50%}
.mk-vis::after{inset:2px;border:1.6px solid #e8740c;border-radius:50%}
.mk-ai::after{inset:0;background:'''+TRI+'''}
.side{display:flex;flex-direction:column;gap:14px;position:sticky;top:20px}
.card2{background:#ffffff;border:1px solid #e6e6e6;border-radius:16px;padding:18px 20px;display:flex;flex-direction:column;gap:10px}
.bar{height:6px;border-radius:3px;background:#ececec;overflow:hidden}.bar i{display:block;height:100%;background:#237233}
.fixb{display:flex;flex-direction:column;gap:8px;padding:0 0 16px}.finp{flex:1;height:42px;border:2px solid #13203a;border-radius:6px;background:#fff;display:flex;align-items:center;padding:0 12px;font-size:15px}
.kcount{display:block;font-size:13px;font-weight:700;color:#3d4658;margin:20px 0 14px}
.svg2{display:flex;flex-wrap:wrap;gap:12px}.sv2{display:inline-flex;align-items:center;gap:8px;height:48px;padding:0 18px;border-radius:9999px;border:1px solid #13203a;background:#fff;font-size:15px;font-weight:600;cursor:pointer}.sv2.off{border-color:#dcd5c7;color:#a0a0a0;text-decoration:line-through;background:#efeae0}.sv2.add{border-style:dashed;border-color:#8a93a3;color:#3d4658}
.addl{font-size:14px;font-weight:600;color:#222222;text-decoration:underline;cursor:pointer;align-self:flex-start}
'''
BODY=fhead(['Claim','Text code','Confirm info','Verify ownership'],3,'<a href="OwnerHome.dc.html" class="btn b-sm">Save and finish later</a>')+'''
<div class="wrapS"><div class="stl"><span class="mu" style="font-size: 11px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; padding: 0 12px 6px;">Confirm your info</span><sc-for list="{{steps}}" as="s" hint-placeholder-count="5"><span class="st {{s.cls}}" onClick="{{s.pick}}"><span class="c">{{s.n}}</span>{{s.t}}</span></sc-for></div>
<div class="pane"><span class="mu" style="font-size: 13px; font-weight: 600;">Step {{si1}} of 5</span><h1>{{h}}</h1><span style="font-size: 15px; line-height: 23px; color: #484848; margin-top: -8px;">{{sub}}</span>
<sc-if value="{{isSvc}}" hint-placeholder-val="{{ false }}"><span class="kcount">{{svcN}} services · tap anything you do not offer</span><div class="svg2"><sc-for list="{{svcs}}" as="c" hint-placeholder-count="10"><span class="sv2 {{c.cls}}" onClick="{{c.pick}}"><span class="mk mk-{{c.m}}"></span>{{c.t}}</span></sc-for><span class="sv2 add">+ Add a service</span></div></sc-if><sc-if value="{{isRows}}" hint-placeholder-val="{{ true }}"><div><sc-for list="{{rows}}" as="r" hint-placeholder-count="5"><div class="fr"><span class="k">{{r.k}}</span><span class="v"><span class="mk mk-{{r.m}}"></span>{{r.v}}<s style="display: {{r.od}};">{{r.o}}</s></span><span class="acts"><span class="chipb {{r.okc}}" onClick="{{r.ok}}">{{r.okl}}</span><span class="chipb {{r.fxc}}" onClick="{{r.fix}}">{{r.fxl}}</span><span class="chipb {{r.noc}}" onClick="{{r.no}}">{{r.nol}}</span></span></div><sc-if value="{{r.fixing}}" hint-placeholder-val="{{ false }}"><div class="fixb"><span class="mu" style="font-size: 12px;">Type the right {{r.kl}}. It shows as confirmed by you, and the old version goes into your change history.</span><span style="display: flex; gap: 8px;"><span class="finp">{{r.v}}</span><span class="chipb ok" onClick="{{r.save}}">Save</span><span class="chipb" onClick="{{r.fix}}">Cancel</span></span></div></sc-if></sc-for></div><span class="addl">{{addLbl}}</span></sc-if>
<sc-if value="{{isKnown}}" hint-placeholder-val="{{ false }}"><span style="font-size: 14px; font-weight: 700;">{{kCount}} of 3 picked</span><div class="kf"><sc-for list="{{known}}" as="k" hint-placeholder-count="10"><span class="kc {{k.cls}}" onClick="{{k.pick}}"><span class="n" style="display: {{k.nd}};">{{k.i}}</span>{{k.t}}</span></sc-for></div><span class="mu" style="font-size: 13px;">These show at the top of your page and are what AI will say you are known for.</span></sc-if>
<div style="display: flex; justify-content: space-between; align-items: center; padding-top: 10px; border-top: 1px solid #f0f0f0;"><span class="btn" onClick="{{back}}" style="visibility: {{backV}};">Back</span><sc-if value="{{notLast}}" hint-placeholder-val="{{ true }}"><span class="btn b-dark" onClick="{{next}}">Confirm and continue</span></sc-if><sc-if value="{{last}}" hint-placeholder-val="{{ false }}"><a href="OwnerHome.dc.html" class="btn b-coral">Finish and go to your dashboard</a></sc-if></div></div>
<div class="side"><div class="card2"><strong style="font-size: 15px;">{{doneN}} of 5 steps done</strong><span class="bar"><i style="width: {{pct}}%;"></i></span><span class="mu" style="font-size: 13px; line-height: 19px;">About 3 minutes. You can change anything later from your dashboard.</span></div>
<div class="card2"><strong style="font-size: 15px;">Rather do it together?</strong><span class="mu" style="font-size: 13px; line-height: 19px;">Kody walks through it with you in 30 minutes, on a video call.</span><a href="OwnerHome.dc.html" class="btn b-sm">Book 30 minutes with Kody</a></div>
<div class="card2"><strong style="font-size: 14px;">The marks</strong><span style="font-size: 13px; display: flex; align-items: center; gap: 8px;"><span class="mk mk-site"></span>Confirmed</span><span style="font-size: 13px; display: flex; align-items: center; gap: 8px;"><span class="mk mk-vis"></span>Visitor submitted</span><span style="font-size: 13px; display: flex; align-items: center; gap: 8px;"><span class="mk mk-ai"></span>AI guess, what AI engines say</span></div></div></div>'''
JS=r'''    const S = this.state || {};
    const si = S.si || 0, ok = S.ok || {}, no = S.no || {}, fx = S.fx, fixed = S.fixed || {}, kp = S.kp || ['Lip filler', 'Morpheus8'];
    const STEPS = [
      ['Basics', 'Is this right?', 'Name, address, phone and hours. AI gets these wrong most often.', [['Business name', 'Lumen Aesthetics', 'ai', 'LUMEN aesthetics'], ['Address', '9891 Irvine Center Dr, Suite 210, Irvine, CA 92618', 'site', ''], ['Phone', '(949) 555-0148', 'site', ''], ['Hours', 'Tue to Sat, 9 AM to 6 PM · Thu until 8 PM', 'ai', ''], ['Mondays', 'Closed', 'vis', '']], ''],
      ['Services', 'What do you offer?', 'Keep what you offer, remove what you do not.', [['Injectables', 'Botox', 'site', ''], ['Injectables', 'Lip filler', 'site', ''], ['Injectables', 'Dermal filler, cheeks and jaw', 'site', ''], ['Injectables', 'Filler dissolving', 'site', ''], ['Skin', 'Morpheus8, face', 'site', ''], ['Skin', 'Morpheus8 Body', 'site', ''], ['Skin', 'Microneedling', 'site', ''], ['Skin', 'Sculptra', 'site', ''], ['Laser', 'Laser hair removal', 'ai', ''], ['Medical', 'Skin checks', 'ai', '']], '+ Add a service'],
      ['Known for', 'Pick the 3 you want to be known for', 'Out of your services, which three should people and AI think of first?', [], ''],
      ['Team', 'Who works here?', 'Names, roles and a work email for each. Adding an email invites them, so they can finish setup, approve work and reply to people.', [['Owner', 'Dr. Priya Nair, MD · priya@lumenirvine.com', 'site', ''], ['Nurse injector', 'Nadia Rahimi, RN · add email', 'site', ''], ['Nurse injector', 'Jordan Lee, NP · add email', 'ai', ''], ['Front desk', 'Maya Ortiz · maya@lumenirvine.com', 'ai', ''], ['Marketing', 'Who handles your marketing? Add them and they get the approvals.', 'ai', '']], '+ Invite someone by email'],
      ['Links', 'Where else are you online?', 'Your website first, then the rest.', [['Website', 'lumenirvine.com', 'site', ''], ['Booking', 'lumenirvine.com/book', 'ai', ''], ['Instagram', 'instagram.com/lumenaesthetics', 'ai', ''], ['TikTok', 'tiktok.com/@lumenaesthetics', 'ai', ''], ['Facebook', 'facebook.com/lumenaestheticsirvine', 'ai', ''], ['Yelp', 'yelp.com/biz/lumen-aesthetics-irvine', 'site', '']], '+ Add a link']
    ];
    const cur = STEPS[si];
    const key = (i) => si + '-' + i;
    const rows = cur[3].map((r, i) => ({ k: r[0], v: r[1], m: ok[key(i)] ? 'site' : r[2], o: r[3], od: r[3] ? 'inline' : 'none', okc: ok[key(i)] ? 'ok' : '', kl: r[0].toLowerCase(), fixing: fx === key(i), fxc: fixed[key(i)] ? 'ok' : '', fxl: fixed[key(i)] ? 'Fixed' : 'Fix', fix: () => this.setState({ fx: fx === key(i) ? undefined : key(i) }), save: () => { const o = Object.assign({}, fixed); o[key(i)] = true; const k2 = Object.assign({}, ok); k2[key(i)] = true; this.setState({ fixed: o, ok: k2, fx: undefined }); }, okl: ok[key(i)] ? 'Confirmed' : 'Confirm', noc: no[key(i)] ? 'no' : '', nol: si === 1 || si === 3 ? (no[key(i)] ? 'Removed' : 'Not us') : (no[key(i)] ? 'Removed' : 'Not us'), ok: () => { const o = Object.assign({}, ok); o[key(i)] = !o[key(i)]; this.setState({ ok: o }); }, no: () => { const n = Object.assign({}, no); n[key(i)] = !n[key(i)]; this.setState({ no: n }); } }));
    const SV = STEPS[1][3].filter((r, i) => !no['1-' + i]).map(r => r[1]);
    const known = SV.map(t => { const idx = kp.indexOf(t); return { t, cls: idx >= 0 ? 'on' : '', i: String(idx + 1), nd: idx >= 0 ? 'flex' : 'none', pick: () => { let n = kp.slice(); if (idx >= 0) n.splice(idx, 1); else if (n.length < 3) n.push(t); this.setState({ kp: n }); } }; });
    const steps = STEPS.map((s, i) => ({ t: s[0], n: i < si ? '✓' : String(i + 1), cls: i < si ? 'done' : (i === si ? 'on' : ''), pick: () => this.setState({ si: i }) }));
    const svcs = STEPS[1][3].map((r, i) => ({ t: r[1], m: r[2], cls: no['1-' + i] ? 'off' : '', pick: () => { const n = Object.assign({}, no); n['1-' + i] = !n['1-' + i]; this.setState({ no: n }); } }));
    return { svcs, svcN: String(svcs.filter(x => !x.cls).length), isSvc: si === 1, steps, si1: String(si + 1), h: cur[1], sub: si === 1 ? 'Here is everything we found. Tap anything you do not offer, then continue.' : cur[2], rows, isRows: si !== 2 && si !== 1, isKnown: si === 2, known, kCount: String(kp.length), addLbl: cur[4],
      next: () => this.setState({ si: Math.min(si + 1, 4) }), back: () => this.setState({ si: Math.max(si - 1, 0) }), backV: si === 0 ? 'hidden' : 'visible', notLast: si < 4, last: si === 4, doneN: String(si), pct: String(si * 20) };'''
out=page('Confirm your info',CSS,BODY,JS).replace('background: #ffffff; position: relative;">','background: #f7f7f7; position: relative;">',1)
open(P+'Setup.dc.html','w').write(out); print('ok',out.count('\u2014'))
