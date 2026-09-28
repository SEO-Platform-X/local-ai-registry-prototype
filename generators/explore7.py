import sys; sys.path.insert(0,'/tmp/gen'); from common import *
TRI="url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='22' height='22' viewBox='0 0 22 22'%3E%3Cpath d='M11 3.5L19.5 18.5H2.5Z' fill='none' stroke='%238a8a8a' stroke-width='2.4' stroke-linejoin='round'/%3E%3C/svg%3E\") center / 100% 100% no-repeat"
HEADX=HEAD.replace('family=Figtree:wght@400;500;600;700;800&amp;display=swap','family=Figtree:wght@400;500;600;700;800&amp;family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&amp;display=swap')
CSS=r'''.srf{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;letter-spacing:-0.01em;color:#13203a}
.srf em{font-style:italic;color:#ff5a3c}
.mk{position:relative;display:inline-block;width:11px;height:11px;margin:0 5px 1px 0;vertical-align:middle;flex-shrink:0}
.mk::after{content:"";position:absolute;inset:0}
.mk-site::after{inset:2px;background:#008a05;border-radius:50%}
.mk-vis::after{inset:2px;border:1.6px solid #e8740c;border-radius:50%}
.top{height:64px;padding:0 24px;display:flex;align-items:center;gap:16px;border-bottom:1px solid #e6e6e6;background:#ffffff;flex-shrink:0}
.nl{font-size:14px;font-weight:600;color:#222222;text-decoration:none;white-space:nowrap}
.cats{display:flex;gap:26px;padding:12px 24px 0;border-bottom:1px solid #e6e6e6;background:#ffffff;flex-shrink:0}
.cat{display:flex;align-items:center;gap:6px;padding-bottom:11px;border-bottom:2px solid transparent;cursor:pointer;color:#6a6a6a;font-size:14px;font-weight:600;margin-bottom:-1px}
.cat.on{color:#222222;border-bottom-color:#222222}
.body{display:grid;grid-template-columns:640px 1fr;flex-grow:1;min-height:0}
.feed{border-right:1px solid #e6e6e6;overflow-y:auto;background:#f7f7f5}
.fpad{padding:16px 20px 30px;display:flex;flex-direction:column;gap:12px}
.ask{display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:14px;background:#ffffff;border:1px solid #e3e3e3}
.ask .av{width:34px;height:34px;border-radius:50%;background:#e8e2d6;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;flex-shrink:0}
.ask .in{flex-grow:1;height:38px;border-radius:19px;background:#f3f3f3;display:flex;align-items:center;padding:0 14px;font-size:14px;color:#8a8a8a}
.sorts{display:flex;align-items:center;gap:6px}
.sorts span{height:30px;padding:0 12px;border-radius:15px;display:inline-flex;align-items:center;font-size:13px;font-weight:600;color:#6a6a6a;cursor:pointer}
.sorts span.on{background:#222222;color:#ffffff}
.th{display:grid;grid-template-columns:44px 1fr;gap:4px;padding:14px 16px 14px 8px;border-radius:14px;background:#ffffff;border:1px solid #e6e6e6;cursor:pointer}
.th:hover{border-color:#bdbdbd}
.th.on{border-color:#222222;box-shadow:0 2px 10px rgba(0,0,0,0.06)}
.vt{display:flex;flex-direction:column;align-items:center;gap:2px;font-size:13px;font-weight:700;color:#484848}
.vt svg{color:#9a9a9a}
.th .cz{font-size:12px;color:#6a6a6a;display:flex;align-items:center;gap:6px}
.th .cz b{color:#222222}
.th h3{margin:4px 0 6px;font-size:17px;line-height:23px;font-weight:600}
.ans{display:flex;flex-direction:column;gap:4px;padding:10px 12px;border-radius:10px;background:#f7f7f5;border-left:3px solid #d8d2c4}
.ans .who{font-size:12px;color:#6a6a6a;display:flex;align-items:center;gap:6px}
.ans .who b{color:#222222}
.badge{display:inline-flex;align-items:center;height:18px;padding:0 6px;border-radius:9px;background:#13203a;color:#ffffff;font-size:10px;font-weight:700}
.ans p{margin:0;font-size:14px;line-height:20px;color:#222222}
.bz{display:flex;gap:6px;flex-wrap:wrap;margin-top:8px}
.bz a{display:inline-flex;align-items:center;gap:5px;height:26px;padding:0 10px;border-radius:13px;border:1px solid #dddddd;background:#ffffff;font-size:12px;font-weight:600;color:#222222;text-decoration:none}
.bz a i{width:8px;height:8px;border-radius:50%;background:#ff5a3c;display:inline-block}
.foot{display:flex;align-items:center;gap:16px;margin-top:10px;font-size:12px;font-weight:600;color:#6a6a6a}
.open{padding:10px 12px;border-radius:10px;border:1.5px dashed #e0c9a8;background:#fffaf2;display:flex;align-items:center;justify-content:space-between;gap:10px;font-size:13px;color:#7a5200}
.map{position:relative;overflow:hidden;background:#e9ede6}
.road{position:absolute;background:#ffffff}
.hood{position:absolute;font-size:12px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#8a9885}
.pin{position:absolute;transform:translate(-50%,-50%);display:flex;align-items:center;gap:6px;height:28px;padding:0 10px 0 8px;border-radius:14px;background:#ffffff;font-size:12px;font-weight:700;box-shadow:0 2px 6px rgba(0,0,0,0.18);white-space:nowrap;color:#222222;text-decoration:none}
.pin .ct{min-width:18px;height:18px;border-radius:9px;background:#f0f0f0;font-size:11px;display:inline-flex;align-items:center;justify-content:center;padding:0 4px}
.pin.dim{opacity:0.35;box-shadow:none}
.pin.hot{background:#222222;color:#ffffff;z-index:5;transform:translate(-50%,-50%) scale(1.1)}
.pin.hot .ct{background:#ff5a3c;color:#ffffff}
.mhead{position:absolute;top:16px;left:16px;right:16px;display:flex;justify-content:space-between;align-items:flex-start;gap:12px;z-index:6}
.mcard{padding:12px 14px;border-radius:12px;background:#ffffff;box-shadow:0 2px 12px rgba(0,0,0,0.12);font-size:13px;line-height:18px;max-width:340px}
.exp{position:absolute;bottom:16px;left:16px;right:16px;padding:12px 16px;border-radius:14px;background:#ffffff;box-shadow:0 4px 18px rgba(0,0,0,0.14);display:flex;align-items:center;gap:18px;z-index:6}
.exp .p{display:flex;align-items:center;gap:8px;font-size:13px}
.exp .p span.a{width:30px;height:30px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;background:#e8e2d6}
'''
LOGO2='<svg width="22" height="20" viewBox="0 0 22 20" aria-hidden="true"><path d="M11 1L21 19H1Z" fill="#2d55e6"></path><path d="M11 8L15.5 16H6.5Z" fill="#ffffff"></path></svg>'
UP='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5l7 8h-4v6H9v-6H5z"></path></svg>'
BODY=f'''<div class="top"><a href="Explore.dc.html" style="display: flex; align-items: center; gap: 8px; text-decoration: none; color: #13203a; font-weight: 700; font-size: 15px;">{LOGO2}Local AI Registry</a><span class="mu" style="font-size: 13px; display: flex; align-items: center; gap: 6px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6a6a6a" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M12 21s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"></path><circle cx="12" cy="9" r="2.5"></circle></svg>Irvine, CA · 4,812 neighbors</span><span style="margin-left: auto; display: flex; align-items: center; gap: 20px;"><a href="Business.dc.html" class="nl">For business</a><a href="#" class="nl">Sign in</a><span class="btn b-sm b-dark" style="border-radius: 18px;">Join Irvine</span></span></div>
<div class="cats"><sc-for list="{{{{cats}}}}" as="c" hint-placeholder-count="9"><span class="cat {{{{c.on}}}}" onClick="{{{{c.pick}}}}">{{{{c.t}}}}<span style="font-weight: 500; color: #9a9a9a; font-size: 12px;">{{{{c.n}}}}</span></span></sc-for></div>
<div class="body">
<div class="feed"><div class="fpad">
<div class="ask"><span class="av">You</span><span class="in">Ask Irvine about a place, or share a tip</span><span class="btn b-sm b-coral" style="border-radius: 16px;">Post</span></div>
<div style="display: flex; align-items: center; justify-content: space-between;"><span class="sorts"><sc-for list="{{{{sorts}}}}" as="s" hint-placeholder-count="3"><span class="{{{{s.on}}}}" onClick="{{{{s.pick}}}}">{{{{s.t}}}}</span></sc-for></span><span class="mu" style="font-size: 12px;">Answers from people who have been there</span></div>
<sc-for list="{{{{threads}}}}" as="t" hint-placeholder-count="7"><div class="th {{{{t.on}}}}" onClick="{{{{t.pick}}}}"><span class="vt">{UP}{{{{t.up}}}}</span><span style="display: flex; flex-direction: column; min-width: 0;"><span class="cz"><b>{{{{t.cat}}}}</b>· {{{{t.kind}}}} · {{{{t.who}}}} · {{{{t.when}}}}</span><h3>{{{{t.q}}}}</h3>
<sc-if value="{{{{t.hasA}}}}" hint-placeholder-val="{{{{ true }}}}"><div class="ans"><span class="who"><span class="mk mk-{{{{t.mk}}}}"></span><b>{{{{t.aw}}}}</b><span class="badge" style="display: {{{{t.bd}}}};">{{{{t.badge}}}}</span>{{{{t.how}}}}</span><p>{{{{t.a}}}}</p></div></sc-if>
<sc-if value="{{{{t.noA}}}}" hint-placeholder-val="{{{{ false }}}}"><div class="open"><span>No answer yet. <strong>{{{{t.ask}}}}</strong></span><span class="btn b-sm b-dark">Answer</span></div></sc-if>
<span class="bz"><sc-for list="{{{{t.biz}}}}" as="b" hint-placeholder-count="2"><a href="Main.dc.html"><i></i>{{{{b}}}}</a></sc-for></span>
<span class="foot"><span>{{{{t.n}}}} answers</span><span>Share</span><span>Save</span></span></span></div></sc-for>
</div></div>
<div class="map">
<span class="road" style="left: -5%; right: -5%; top: 30%; height: 12px; transform: rotate(-9deg);"></span><span class="road" style="top: -5%; bottom: -5%; left: 40%; width: 14px; transform: rotate(14deg);"></span><span class="road" style="left: 0; right: 0; top: 66%; height: 8px; transform: rotate(3deg);"></span><span class="road" style="top: 0; bottom: 0; left: 76%; width: 8px;"></span><span class="road" style="top: 0; bottom: 0; left: 18%; width: 6px; transform: rotate(-6deg);"></span>
<span style="position: absolute; left: 46%; top: 40%; width: 120px; height: 80px; border-radius: 16px; background: #d9e6d3;"></span>
<span class="hood" style="left: 44%; top: 56%;">Irvine Spectrum</span><span class="hood" style="left: 10%; top: 20%;">Woodbridge</span><span class="hood" style="left: 64%; top: 18%;">Great Park</span><span class="hood" style="left: 22%; top: 78%;">University Park</span><span class="hood" style="left: 80%; top: 76%;">Quail Hill</span>
<div class="mhead"><span class="mcard"><strong style="display: block; padding-bottom: 2px;">{{{{selQ}}}}</strong><span class="mu">{{{{selNote}}}}</span></span></div>
<sc-for list="{{{{pins}}}}" as="p" hint-placeholder-count="14"><a href="Main.dc.html" class="pin {{{{p.cls}}}}" style="left: {{{{p.x}}}}%; top: {{{{p.y}}}}%;">{{{{p.n}}}}<span class="ct">{{{{p.c}}}}</span></a></sc-for>
<div class="exp"><strong style="font-size: 13px; white-space: nowrap;">Local experts</strong><sc-for list="{{{{experts}}}}" as="e" hint-placeholder-count="4"><span class="p"><span class="a">{{{{e.i}}}}</span><span style="display: flex; flex-direction: column;"><strong>{{{{e.n}}}}</strong><span class="mu" style="font-size: 11px;">{{{{e.t}}}}</span></span></span></sc-for></div>
</div>
</div>'''
JS=r'''    const S = this.state || {};
    const c = S.c || 'all', sort = S.sort || 'hot';
    const BZ = { 'Backyard Tacos': [26, 62], 'Tacos El Guero': [38, 70], 'La Birrieria OC': [62, 72], 'Lumen Aesthetics': [53, 46], 'Spectrum Aesthetics MD': [60, 56], 'Irvine Face Lab': [30, 34], 'Woodbridge Kids Dental': [16, 26], 'Kinjiro Ramen': [49, 62], 'Ramen Nagi': [57, 42], 'Blue Door Coffee': [34, 24], 'Irvine Auto Care': [84, 50], 'Quail Hill Vet': [82, 70], 'Great Park Pilates': [68, 22], 'Heritage Hair Studio': [30, 84] };
    const T = [
      ['food', 'Question', 'Where can I take my kids to eat where they can also run around?', 'Linh T.', '2 hours ago', 64, 'Maria K.', 'Local expert · Food', 'vis', 'Went last Saturday', 'Backyard Tacos has a fenced lawn right next to the patio. You can see the kids from every table, and the kids menu is under $8.', ['Backyard Tacos'], 11, ''],
      ['beauty', 'Question', 'First time getting lip filler. Who will not overdo it?', 'Anon', '5 hours ago', 88, 'Aisha M.', 'Local expert · Beauty', 'vis', 'Had it done twice', 'Lumen. Dr. Nair talked me down to half a syringe and told me to come back in two weeks if I wanted more. Spectrum Aesthetics is also doctor-only.', ['Lumen Aesthetics', 'Spectrum Aesthetics MD'], 23, ''],
      ['food', 'Tip', 'Best birria in Irvine is not where you think', 'Diego R.', 'Yesterday', 51, 'Diego R.', '', 'vis', 'Eats there weekly', 'Tacos El Guero, the truck on Culver. Cash only, $3.50, consommé included. Backyard Tacos is great but twice the wait.', ['Tacos El Guero', 'Backyard Tacos'], 17, ''],
      ['health', 'Question', 'Any dentist open Saturdays that is good with anxious kids?', 'Carmen V.', 'Yesterday', 39, 'Woodbridge Kids Dental', 'Owner', 'site', 'Replied as the business', 'We are open Saturdays 8 to 1 and only see children. First visits are a tour and a ride in the chair, no cleaning unless they are ready.', ['Woodbridge Kids Dental'], 8, ''],
      ['car', 'Question', 'Who in Irvine actually knows Teslas and will not upsell me?', 'Tom H.', '2 days ago', 27, 'Jordan P.', 'Local expert · Car', 'vis', 'Took his Model Y in August', 'Irvine Auto Care. They told me my brakes had another 15,000 miles and did not charge for the check.', ['Irvine Auto Care'], 6, ''],
      ['food', 'Question', 'Late-night ramen after 11 on a weeknight?', 'Priya S.', '3 hours ago', 22, '', '', '', '', '', ['Kinjiro Ramen', 'Ramen Nagi'], 0, 'Been to Kinjiro recently?'],
      ['drinks', 'Tip', 'Blue Door is the quietest place to work before 11', 'Kelly W.', '4 days ago', 33, 'Kelly W.', '', 'vis', 'Works there Tuesdays', 'Outlets along the bar, strong Wi-Fi, and nobody minds laptops until the lunch rush.', ['Blue Door Coffee'], 9, ''],
      ['pets', 'Question', 'Is Quail Hill Vet worth it for emergencies?', 'Sam L.', '6 hours ago', 14, '', '', '', '', '', ['Quail Hill Vet'], 0, 'Been to Quail Hill Vet?'],
      ['beauty', 'Question', 'Who does curly cuts in Irvine?', 'Nadia F.', '3 days ago', 29, 'Jordan P.', '', 'vis', 'Gets her hair cut there', 'Heritage Hair Studio. Ask for Renee, she cuts dry, curl by curl.', ['Heritage Hair Studio'], 12, ''],
      ['fitness', 'Question', 'Pilates studio that is actually good for total beginners?', 'Ella V.', '5 days ago', 18, 'Maria K.', 'Local expert · Food', 'vis', 'Goes twice a week', 'Great Park Pilates. The intro class is $25 and they keep it to 6 people.', ['Great Park Pilates'], 5, '']
    ];
    const CAT = [['all', 'Everything'], ['food', 'Food'], ['drinks', 'Drinks'], ['beauty', 'Beauty'], ['health', 'Health'], ['fitness', 'Fitness'], ['car', 'Car'], ['pets', 'Pets'], ['home', 'Home']];
    const NM = { food: 'Food', drinks: 'Drinks', beauty: 'Beauty', health: 'Health', fitness: 'Fitness', car: 'Car', pets: 'Pets', home: 'Home' };
    let rows = T.map((t, i) => ({ t, i })).filter(r => c === 'all' || r.t[0] === c);
    if (sort === 'new') rows = rows.slice().sort((a, b) => (a.t[4].includes('hour') ? 0 : 1) - (b.t[4].includes('hour') ? 0 : 1));
    if (sort === 'open') rows = rows.filter(r => !r.t[6]);
    if (sort === 'hot') rows = rows.slice().sort((a, b) => b.t[5] - a.t[5]);
    const selI = rows.some(r => r.i === S.sel) ? S.sel : (rows[0] ? rows[0].i : -1);
    const threads = rows.map(({ t, i }) => ({ cat: NM[t[0]], kind: t[1], q: t[2], who: t[3], when: t[4], up: String(t[5]), aw: t[6], badge: t[7], bd: t[7] ? 'inline-flex' : 'none', mk: t[8], how: t[9], a: t[10], biz: t[11], n: String(t[12]), ask: t[13], hasA: !!t[6], noA: !t[6], on: i === selI ? 'on' : '', pick: () => this.setState({ sel: i }) }));
    const mention = {}; rows.forEach(({ t }) => t[11].forEach(b => { mention[b] = (mention[b] || 0) + 1; }));
    const hot = selI >= 0 ? T[selI][11] : [];
    const pins = Object.keys(BZ).map(n => ({ n, x: String(BZ[n][0]), y: String(BZ[n][1]), c: String(mention[n] || 0), cls: hot.includes(n) ? 'hot' : (mention[n] ? '' : 'dim') }));
    const cats = CAT.map(x => ({ t: x[1], n: String(x[0] === 'all' ? T.length : T.filter(t => t[0] === x[0]).length), on: x[0] === c ? 'on' : '', pick: () => this.setState({ c: x[0], sel: undefined }) }));
    const sorts = [['hot', 'Hot'], ['new', 'New'], ['open', 'Unanswered']].map(s => ({ t: s[1], on: s[0] === sort ? 'on' : '', pick: () => this.setState({ sort: s[0], sel: undefined }) }));
    const experts = [['MK', 'Maria K.', 'Food · 212 answers'], ['AM', 'Aisha M.', 'Beauty · 148 answers'], ['JP', 'Jordan P.', 'Car · 96 answers'], ['DR', 'Diego R.', 'Food · 88 answers']].map(x => ({ i: x[0], n: x[1], t: x[2] }));
    const st = selI >= 0 ? T[selI] : null;
    return { cats, sorts, threads, pins, experts, selQ: st ? st[2] : 'Nothing here yet', selNote: st ? 'Mentions ' + st[11].join(' and ') + '. Tap a pin to see the business.' : 'Pick another category.' };'''
t=HEADX.replace('<title>Lumen Aesthetics on Local AI Registry</title>','<title>Irvine on Local AI Registry</title>')
out=t+'\n'+CSS+'\n</style>\n</helmet>\n<div style="width: 1440px; height: 960px; box-sizing: border-box; display: flex; flex-direction: column; background: #ffffff; position: relative; overflow: hidden;">\n'+BODY+'\n</div>\n</x-dc>\n<script type="text/x-dc" data-dc-script>\nclass Component extends DCLogic {\n  renderVals() {\n'+JS+'\n  }\n}\n</script>\n</body>\n</html>\n'
open(P+'Explore.dc.html','w').write(out); print('ok')
