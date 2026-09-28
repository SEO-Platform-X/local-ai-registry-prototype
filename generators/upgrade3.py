import sys; sys.path.insert(0,'/tmp/gen'); from common import *
exec(open('/tmp/ed61.py').read().split("CL=['Claim'")[0])
DATA=open('/tmp/gen/premdata.js').read()
CSS=r'''.wrapU{display:grid;grid-template-columns:1fr 320px;gap:24px;padding:28px 40px 48px;align-items:start}
.ptabs{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.ptabs > div{display:flex;flex-direction:column;gap:4px;padding:14px 16px;border-radius:14px;border:1px solid #e3e3e3;background:#ffffff;cursor:pointer}
.ptabs > div.on{border:2px solid #222222}
.ptabs strong{font-size:17px}
.ptabs span{font-size:12px;color:#6a6a6a}
.cal{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));border-top:1px solid #ebebeb;border-left:1px solid #ebebeb;background:#ffffff;border-radius:12px;overflow:hidden}
.cal .h{padding:8px;font-size:11px;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:#6a6a6a;border-right:1px solid #ebebeb;border-bottom:1px solid #ebebeb;background:#fafafa}
.cal .c{min-height:92px;padding:6px;border-right:1px solid #ebebeb;border-bottom:1px solid #ebebeb;display:flex;flex-direction:column;gap:3px;box-sizing:border-box}
.cal .c.off{background:#fafafa}
.cal .n{font-size:12px;font-weight:600;color:#6a6a6a}
.ev{display:block;padding:2px 6px;border-radius:5px;font-size:10px;line-height:14px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:#ffffff}
.leg{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:12px;color:#484848}
.leg i{display:inline-block;width:10px;height:10px;border-radius:3px;margin-right:5px;vertical-align:-1px}
.sum{display:flex;flex-direction:column;gap:12px;padding:22px;border-radius:18px;background:#ffffff;border:1px solid #e6e6e6;position:sticky;top:20px}
.sr{display:flex;justify-content:space-between;font-size:14px}
.inc{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:5px;font-size:13px;color:#484848}
.inc li::before{content:"✓ ";color:#237233;font-weight:700}
'''
BODY=fhead(['Pick a plan','Checkout','Start'],1,'<a href="OwnerPremium.dc.html" class="btn b-sm">Back to Premium</a>')+'''<div class="wrapU"><div style="display: flex; flex-direction: column; gap: 16px;">
<div style="display: flex; flex-direction: column; gap: 4px;"><span class="mu" style="font-size: 13px; font-weight: 600;">Lumen Aesthetics · AI Score 58 today</span><h1 style="margin: 0; font-size: 30px;">Pick a plan. Watch October fill up.</h1><span style="font-size: 14px; color: #484848;">Every piece below gets your Local AI Registry record into a place AI reads. Grey pieces are in higher plans. Nothing goes out until you approve it.</span></div>
<div class="ptabs"><sc-for list="{{plans}}" as="p" hint-placeholder-count="4"><div class="{{p.cls}}" onClick="{{p.pick}}"><strong>{{p.n}} <span style="font-weight: 500; color: #3d4658;">{{p.pr}}</span></strong><span>{{p.c}} pieces in October · AI Score {{p.sc}}</span></div></sc-for></div>
<div class="cal"><sc-for list="{{dow}}" as="d" hint-placeholder-count="7"><span class="h">{{d}}</span></sc-for><sc-for list="{{cal}}" as="c" hint-placeholder-count="35"><div class="c {{c.cls}}"><span class="n">{{c.n}}</span><sc-for list="{{c.ev}}" as="e" hint-placeholder-count="2"><span class="ev" style="background: {{e.c}};">{{e.t}}</span></sc-for></div></sc-for></div>
<div class="leg"><sc-for list="{{leg}}" as="l" hint-placeholder-count="10"><span style="opacity: {{l.o}};"><i style="background: {{l.c}};"></i>{{l.n}}</span></sc-for></div></div>
<div class="sum"><span class="mu" style="font-size: 12px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase;">Your plan</span><strong style="font-size: 24px;">{{selName}}</strong><div class="sr"><span class="mu">Price</span><b>{{selPr}}</b></div><div class="sr"><span class="mu">Pieces in October</span><b>{{selCount}}</b></div><div class="sr"><span class="mu">AI Score today</span><b>58</b></div><div class="sr"><span class="mu">Projected by March</span><b style="color: #237233;">{{selScore}}</b></div><ul class="inc"><sc-for list="{{inc}}" as="i" hint-placeholder-count="6"><li>{{i}}</li></sc-for></ul>
<sc-if value="{{paid}}" hint-placeholder-val="{{ true }}"><a href="Checkout.dc.html" class="btn b-coral">Start {{selName}}</a></sc-if><sc-if value="{{free}}" hint-placeholder-val="{{ false }}"><a href="OwnerHome.dc.html" class="btn">Stay on Free</a></sc-if><a href="Next.dc.html" class="btn">Talk to Kody first</a><span class="mu" style="font-size: 12px; line-height: 17px;">No contract. Change or cancel any month. Projections come from similar businesses on the registry and are not a guarantee.</span></div></div>'''
JS='    const S = this.state || {}; const sel = S.sel === undefined ? 2 : S.sel;\n'+DATA+r'''    const TN = ['Free', 'Fix', 'Trust', 'Authority'];
    const inTier = t => IT.filter(x => TC[x.k][3] <= t);
    const PR = ['Free', '$500/mo', '$1,500/mo', '$3,000/mo']; const plans = TN.map((n, i) => ({ n, pr: PR[i], c: String(i === 0 ? 0 : inTier(i).length), sc: ['58', '63', '72', '80'][i], cls: i === sel ? 'on' : '', pick: () => this.setState({ sel: i }) }));
    const its = sel === 0 ? [] : inTier(sel);
    const cal = Array.from({ length: 35 }, (_, i) => { const n = i - 3; const inM = n >= 1 && n <= 31; if (!inM) return { n: '', cls: 'off', ev: [] }; const day = IT.filter(x => x.d === n).sort((a, b) => TC[a.k][3] - TC[b.k][3]); const inc = day.filter(x => TC[x.k][3] <= sel), lk = day.filter(x => TC[x.k][3] > sel); const ev = inc.slice(0, 4).map(x => ({ t: TC[x.k][1], c: TC[x.k][2], o: '1' })); const room = Math.max(0, 5 - ev.length); lk.slice(0, room).forEach(x => ev.push({ t: '🔒 ' + TC[x.k][1], c: '#c9c3b6', o: '1' })); const more = day.length - ev.length; if (more > 0) ev.push({ t: '+' + more + ' more', c: '#8a8a8a', o: '1' }); return { n: String(n), cls: '', ev }; });
    const leg = TY.map(y => ({ n: (y[3] > sel ? '🔒 ' : '') + y[1], c: y[3] > sel ? '#c9c3b6' : y[2], o: y[3] > sel ? '0.55' : '1' }));
    const INC = [['Your page, AI Score and prompts', 'No work'], ['A directory submission every day'], ['Everything in Fix', 'Negative review disputes', 'Autopilot review replies and answers', 'Press releases', 'AI code on your photos', 'Google posts and optimization', 'Review link and velocity check'], ['Everything in Trust', 'Technical and speed fixes', 'URL restructuring and topical map', 'Semantic content and entity mapping', 'Cannibalization fix', 'Articles and blogs', 'Your only, first and best story']];
    return { plans, cal, leg, dow: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], inc: INC[sel], selName: TN[sel], selPr: ['Free', '$500 / month', '$1,500 / month', '$3,000 / month'][sel], selCount: String(its.length), selScore: ['58', '63', '72', '80'][sel], paid: sel > 0, free: sel === 0 };'''
out=page('Pick a plan',CSS,BODY,JS).replace('background: #ffffff; position: relative;">','background: #f7f7f7; position: relative;">',1)
open(P+'Upgrade.dc.html','w').write(out); print('ok')
