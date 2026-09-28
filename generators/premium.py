CSS += r'''.prem{display:grid;grid-template-columns:300px 1fr;gap:24px;align-items:start}
.tiers{display:inline-flex;padding:4px;border-radius:14px;background:#efefef;gap:2px}
.tiers span{display:inline-flex;flex-direction:column;align-items:flex-start;justify-content:center;height:48px;padding:0 16px;border-radius:11px;cursor:pointer;font-size:14px;font-weight:700;color:#484848;min-width:120px;box-sizing:border-box}
.tiers span i{font-style:normal;font-size:11px;font-weight:600;color:#8a8a8a}
.tiers span.on{background:#ffffff;color:#222222;box-shadow:0 1px 4px rgba(0,0,0,0.12)}
.tiers span.cur i{color:#237233}
.mcal2{display:grid;grid-template-columns:repeat(7,1fr);gap:2px;text-align:center}
.mcal2 .h{font-size:10px;font-weight:700;color:#8a8a8a;padding:4px 0}
.mcal2 .d{display:flex;flex-direction:column;align-items:center;gap:3px;padding:5px 0 6px;border-radius:9px;cursor:pointer;font-size:12px;font-weight:600;min-height:34px;box-sizing:border-box}
.mcal2 .d:hover{background:#f3f3f3}
.mcal2 .d.on{background:#222222;color:#ffffff}
.mcal2 .d.off{color:#c8c8c8;cursor:default}
.mcal2 .d.today{box-shadow:inset 0 0 0 1.5px #ff385c}
.dots{display:flex;gap:2px;flex-wrap:wrap;justify-content:center;max-width:28px}
.dots i{width:5px;height:5px;border-radius:50%;display:block}
.types{display:flex;flex-direction:column;gap:2px}
.ty2{display:flex;align-items:center;gap:10px;padding:8px 8px;border-radius:8px;cursor:pointer;font-size:13px}
.ty2:hover{background:#f5f5f5}
.ty2 .sw{width:12px;height:12px;border-radius:4px;flex-shrink:0}
.ty2.offt{opacity:0.4}
.ty2 .lk{margin-left:auto;font-size:11px;color:#8a8a8a}
.agenda{display:flex;flex-direction:column;gap:18px}
.dayh{display:flex;align-items:baseline;gap:10px;font-size:13px;font-weight:700;color:#484848;padding-bottom:6px;border-bottom:1px solid #ebebeb}
.itm2{display:flex;flex-direction:column;border:1px solid #e6e6e6;border-radius:14px;background:#ffffff;overflow:hidden}
.itm2.lockd{background:#fafafa}
.itm2 .row{display:flex;align-items:center;gap:12px;padding:14px 16px;cursor:pointer}
.itm2 .bar2{width:4px;align-self:stretch;border-radius:2px;flex-shrink:0}
.itm2 .tt{display:flex;flex-direction:column;gap:2px;flex-grow:1;min-width:0}
.itm2 .tt strong{font-size:15px}
.itm2 .tt > span{font-size:12px;color:#6a6a6a}
.pill{display:inline-flex;align-items:center;height:22px;padding:0 9px;border-radius:11px;font-size:11px;font-weight:700;white-space:nowrap}
.p-ap{background:#fff1e0;color:#9a5200}.p-sc{background:#e3eefc;color:#134a91}.p-ok{background:#e3f4e6;color:#1c5f2a}.p-rw{background:#efe8fd;color:#4a2a91}.p-lk{background:#f1f1f1;color:#6a6a6a}
.exp{display:grid;grid-template-columns:260px 1fr;gap:20px;padding:4px 18px 18px 32px}
.img{height:200px;border-radius:12px;background:linear-gradient(135deg,#e8d9cf,#f3ece6);display:flex;align-items:center;justify-content:center;font-size:12px;color:#8a7a6a;font-weight:600}
.body2{font-size:14px;line-height:22px;white-space:pre-line;padding:14px 16px;border-radius:12px;background:#fbfbfa;border:1px solid #efefef}
.note2{display:flex;flex-direction:column;gap:8px;padding:14px;border-radius:12px;background:#f7f5f1}
.note2 textarea{width:100%;height:64px;border:1px solid #d6d0c4;border-radius:10px;padding:10px 12px;font-family:inherit;font-size:14px;box-sizing:border-box;resize:none;background:#ffffff}
.stmt{width:100%;border-collapse:collapse;font-size:14px}
.stmt th{text-align:left;font-size:12px;font-weight:700;color:#6a6a6a;padding:12px 14px;border-bottom:1px solid #e3e3e3;text-transform:uppercase;letter-spacing:0.05em}
.stmt td{padding:16px 14px;border-bottom:1px solid #f0f0f0}
.stmt tr:hover td{background:#fafafa}
.nrow2{display:grid;grid-template-columns:1fr 240px 120px 120px;gap:16px;align-items:center;padding:16px 4px;border-bottom:1px solid #f0f0f0;font-size:14px}
.nrow2.hd{font-size:12px;font-weight:700;color:#6a6a6a;text-transform:uppercase;letter-spacing:0.05em;padding:10px 4px}
'''
exec(open('/tmp/gen/premium2.py').read())
# ---------- REPORTS ----------
rep_b='''<div style="display: flex; justify-content: space-between; align-items: flex-end;"><div style="display: flex; flex-direction: column; gap: 4px;"><a href="OwnerPremium.dc.html" style="font-size: 13px; font-weight: 600; color: #484848;">← Premium</a><h1 class="ttl1">Monthly reports</h1><span class="mu" style="font-size: 15px;">One report every month: what AI says about Lumen, and what we did about it.</span></div><span style="display: flex; gap: 8px;"><span class="btn b-sm">2026</span><span class="btn b-sm">Download all</span></span></div>
<div class="card" style="padding: 8px 18px;"><table class="stmt"><tr><th>Report</th><th>AI Score</th><th>Named by AI</th><th>Wrong facts fixed</th><th>Work delivered</th><th></th></tr><sc-for list="{{reps}}" as="r" hint-placeholder-count="6"><tr><td><strong>{{r.m}}</strong><span class="mu" style="display: block; font-size: 12px;">{{r.sub}}</span></td><td><strong>{{r.s}}</strong> <span style="font-size: 12px; font-weight: 700; color: {{r.cc}};">{{r.ch}}</span></td><td>{{r.p}}</td><td>{{r.f}}</td><td>{{r.w}}</td><td style="text-align: right; white-space: nowrap;"><a href="Audit.dc.html" class="btn b-sm b-dark">View report</a> <a href="#" class="btn b-sm">PDF</a></td></tr></sc-for></table></div>'''
rjs='''    const R = [['October 2026', 'In progress · updates weekly', 58, '+3', '2 of 8', '1 of 3', '6 of 27 pieces'], ['September 2026', 'Sent Oct 1', 55, '+4', '2 of 8', '2', '24 pieces'], ['August 2026', 'Sent Sep 1', 51, '+6', '1 of 8', '3', '22 pieces'], ['July 2026', 'Sent Aug 1', 45, '+5', '1 of 8', '4', '20 pieces'], ['June 2026', 'Sent Jul 1', 40, '+8', '0 of 8', '5', '18 pieces'], ['May 2026', 'Baseline, before any work', 32, '', '0 of 8', '0', 'Setup']];
    const reps = R.map(r => ({ m: r[0], sub: r[1], s: String(r[2]), ch: r[3], cc: '#237233', p: r[4], f: r[5], w: r[6] }));
    return Object.assign(base, { reps });'''

# ---------- AI NOTES LIST ----------
notes_b='''<div style="display: flex; justify-content: space-between; align-items: flex-end;"><div style="display: flex; flex-direction: column; gap: 4px;"><a href="OwnerPremium.dc.html" style="font-size: 13px; font-weight: 600; color: #484848;">← Premium</a><h1 class="ttl1">AI notes</h1><span class="mu" style="font-size: 15px;">Everything you told AI about Lumen. Every draft follows these.</span></div></div>
<div class="card"><div style="display: flex; gap: 10px; align-items: center;"><input type="text" placeholder="Add a note, e.g. Never promise results in a set number of sessions" onChange="{{onAdd}}" value="{{addTxt}}" style="flex-grow: 1; height: 46px; border: 1px solid #dddddd; border-radius: 12px; padding: 0 14px; font-family: inherit; font-size: 14px;"><span class="btn b-dark" onClick="{{add}}">Add note</span></div>
<div><div class="nrow2 hd"><span>Note</span><span>Where it came from</span><span>Used in</span><span></span></div><sc-for list="{{nts}}" as="n" hint-placeholder-count="6"><div class="nrow2" style="background: {{n.bg}};"><span style="display: flex; gap: 10px; align-items: flex-start;"><span style="width: 26px; height: 26px; border-radius: 50%; background: #13203a; color: #ffffff; display: flex; align-items: center; justify-content: center; font-size: 11px; flex-shrink: 0;">✎</span><strong style="font-size: 14px; line-height: 20px;">{{n.t}}</strong></span><span class="mu" style="font-size: 13px; line-height: 18px;">{{n.s}}</span><span style="font-size: 13px;">{{n.u}} drafts</span><span style="display: flex; gap: 6px; justify-content: flex-end;"><span class="btn b-sm">Edit</span><span class="btn b-sm" onClick="{{n.rm}}">Remove</span></span></div></sc-for></div></div>'''
njs='''    const N0 = [["Say 'mild warmth,' never 'painless.'", 'Your feedback on the Morpheus8 post · Sep 18', 14], ["Sign replies 'Priya and the Lumen team.'", 'Your feedback on a review reply · Sep 12', 31], ['Always mention HSA cards are accepted.', 'Your feedback on an answer · Sep 10', 9], ['Never name other med spas.', 'Your feedback on a press draft · Sep 3', 6], ['Dr. Nair does lip filler. Nurses do Botox.', 'From your setup · Sep 1', 22], ["Mention free parking in Structure B.", 'Your feedback on a Google post · just now', 0]];
    const gone = S.gone || {}; const extra = S.extra || [];
    const all = extra.concat(N0).map((n, i) => ({ n, i })).filter(x => !gone[x.i]);
    const nts = all.map(({ n, i }) => ({ t: n[0], s: n[1], u: String(n[2]), bg: n[2] === 0 ? '#fffbe8' : 'transparent', rm: () => { const g = Object.assign({}, gone); g[i] = true; this.setState({ gone: g }); } }));
    return Object.assign(base, { nts, addTxt: S.addTxt || '', onAdd: (e) => this.setState({ addTxt: e.target.value }), add: () => { const v = (S.addTxt || '').trim(); if (v) this.setState({ extra: [[v, 'Added by you · just now', 0]].concat(extra), addTxt: '' }); } });'''
build('OwnerNotes.dc.html','work','AI notes',notes_b,njs,tier0=2)
