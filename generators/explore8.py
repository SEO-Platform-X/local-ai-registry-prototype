import sys; sys.path.insert(0,'/tmp/gen'); from common import *
HEADX=HEAD.replace('family=Figtree:wght@400;500;600;700;800&amp;display=swap','family=Figtree:wght@400;500;600;700;800&amp;family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&amp;display=swap')
CSS=r'''.srf{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;letter-spacing:-0.01em;color:#13203a}
.srf em{font-style:italic;color:#ff5a3c}
.mk{position:relative;display:inline-block;width:11px;height:11px;margin:0 5px 1px 0;vertical-align:middle;flex-shrink:0}
.mk::after{content:"";position:absolute;inset:0}
.mk-site::after{inset:2px;background:#008a05;border-radius:50%}
.mk-vis::after{inset:2px;border:1.6px solid #e8740c;border-radius:50%}
.top{height:64px;padding:0 24px;display:flex;align-items:center;gap:16px;border-bottom:1px solid #e6e6e6;background:#ffffff;flex-shrink:0}
.nl{font-size:14px;font-weight:600;color:#222222;text-decoration:none;white-space:nowrap}
.cats{display:flex;gap:8px;padding:10px 24px;border-bottom:1px solid #e6e6e6;background:#ffffff;flex-shrink:0}
.cat{display:inline-flex;align-items:center;gap:6px;height:34px;padding:0 14px;border:1px solid #dddddd;border-radius:17px;font-size:13px;font-weight:600;cursor:pointer;background:#ffffff;white-space:nowrap}
.cat.on{background:#222222;border-color:#222222;color:#ffffff}
.cat span{font-weight:500;opacity:0.6}
.body{display:grid;grid-template-columns:1fr 600px;flex-grow:1;min-height:0}
.map{position:relative;overflow:hidden;background:#eef0ea;border-right:1px solid #e6e6e6}
.road{position:absolute;background:#ffffff}
.park{position:absolute;border-radius:18px;background:#dde8d6}
.heat{position:absolute;transform:translate(-50%,-50%);border-radius:50%;cursor:pointer;display:flex;align-items:center;justify-content:center}
.heat .glow{position:absolute;inset:0;border-radius:50%;background:radial-gradient(circle,rgba(255,90,60,0.55) 0%,rgba(255,90,60,0.18) 55%,rgba(255,90,60,0) 72%)}
.heat .core{position:relative;min-width:24px;height:24px;padding:0 6px;border-radius:12px;background:#ff5a3c;color:#ffffff;font-size:12px;font-weight:700;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 6px rgba(0,0,0,0.25);border:2px solid #ffffff;box-sizing:border-box}
.heat.cold .glow{display:none}
.heat.cold .core{background:#ffffff;color:#8a8a8a;border-color:#d8d8d8;min-width:16px;height:16px;font-size:0;padding:0}
.heat.sel .core{background:#222222;transform:scale(1.2)}
.heat.dim{opacity:0.25}
.lab{position:absolute;transform:translate(-50%,0);margin-top:18px;font-size:12px;font-weight:700;color:#222222;white-space:nowrap;text-shadow:0 0 3px #ffffff,0 0 3px #ffffff,0 0 3px #ffffff;pointer-events:none}
.hoodb{position:absolute;transform:translate(-50%,-50%);display:flex;flex-direction:column;align-items:center;gap:3px;cursor:pointer}
.hoodb .hn{font-size:12px;font-weight:800;letter-spacing:0.1em;text-transform:uppercase;color:#7d8c77}
.hoodb .hq{display:inline-flex;align-items:center;gap:5px;height:24px;padding:0 10px;border-radius:12px;background:#ffffff;border:1.5px dashed #e8740c;font-size:11px;font-weight:700;color:#b35c00}
.hoodb.on .hn{color:#222222}
.hoodb.on .hq{background:#e8740c;color:#ffffff;border-style:solid}
.mtl{position:absolute;top:16px;left:16px;display:flex;gap:8px;z-index:6}
.mtl span{display:inline-flex;align-items:center;gap:7px;height:36px;padding:0 14px;border-radius:18px;background:#ffffff;box-shadow:0 2px 10px rgba(0,0,0,0.12);font-size:13px;font-weight:600}
.mtl .bx{width:15px;height:15px;border-radius:4px;background:#222222;display:inline-flex;align-items:center;justify-content:center}
.mtl .bx::after{content:"";width:7px;height:3px;border-left:2px solid #ffffff;border-bottom:2px solid #ffffff;transform:rotate(-45deg) translate(1px,-1px)}
.mleg{position:absolute;bottom:16px;left:16px;display:flex;align-items:center;gap:16px;padding:10px 14px;border-radius:12px;background:#ffffff;box-shadow:0 2px 10px rgba(0,0,0,0.12);font-size:12px;color:#484848;z-index:6}
.mleg i{display:inline-block;border-radius:50%;margin-right:6px;vertical-align:-2px}
.res{overflow-y:auto;background:#ffffff}
.rpad{padding:20px 24px 32px;display:flex;flex-direction:column;gap:12px}
.ph{display:flex;flex-direction:column;gap:6px;padding:16px 18px;border-radius:14px;background:#f7f5f1}
.back{font-size:13px;font-weight:600;color:#484848;cursor:pointer;align-self:flex-start}
.askb{display:flex;align-items:center;gap:10px;height:44px;padding:0 6px 0 16px;border-radius:22px;border:1px solid #dddddd;font-size:14px;color:#8a8a8a}
.sorts{display:flex;gap:4px}
.sorts span{height:28px;padding:0 11px;border-radius:14px;display:inline-flex;align-items:center;font-size:12px;font-weight:600;color:#6a6a6a;cursor:pointer}
.sorts span.on{background:#222222;color:#ffffff}
.th{display:flex;flex-direction:column;gap:6px;padding:14px 0;border-top:1px solid #eeeeee}
.th .cz{font-size:12px;color:#6a6a6a}
.th .cz b{color:#222222}
.th .cz a{color:#222222;font-weight:600}
.th h3{margin:0;font-size:16px;line-height:22px;font-weight:600}
.ans{display:flex;flex-direction:column;gap:3px;padding:10px 12px;border-radius:10px;background:#f7f7f5}
.ans .who{font-size:12px;color:#6a6a6a;display:flex;align-items:center;gap:6px}
.ans .who b{color:#222222}
.badge{display:inline-flex;align-items:center;height:18px;padding:0 6px;border-radius:9px;background:#13203a;color:#ffffff;font-size:10px;font-weight:700}
.ans p{margin:0;font-size:14px;line-height:20px}
.open{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:10px 12px;border-radius:10px;border:1.5px dashed #e0c9a8;background:#fffaf2;font-size:13px;color:#7a5200}
.foot{display:flex;gap:16px;font-size:12px;font-weight:600;color:#6a6a6a}
'''
LOGO2='<svg width="22" height="20" viewBox="0 0 22 20" aria-hidden="true"><path d="M11 1L21 19H1Z" fill="#2d55e6"></path><path d="M11 8L15.5 16H6.5Z" fill="#ffffff"></path></svg>'
BODY=f'''<div class="top"><a href="Explore.dc.html" style="display: flex; align-items: center; gap: 8px; text-decoration: none; color: #13203a; font-weight: 700; font-size: 15px;">{LOGO2}Local AI Registry</a><span class="mu" style="font-size: 13px;">Irvine, CA · 4,812 neighbors</span><span style="margin-left: auto; display: flex; align-items: center; gap: 20px;"><a href="Business.dc.html" class="nl">For business</a><a href="#" class="nl">Sign in</a><span class="btn b-sm b-dark" style="border-radius: 18px;">Join Irvine</span></span></div>
<div class="cats"><sc-for list="{{{{cats}}}}" as="c" hint-placeholder-count="9"><span class="cat {{{{c.on}}}}" onClick="{{{{c.pick}}}}">{{{{c.t}}}}<span>{{{{c.n}}}}</span></span></sc-for></div>
<div class="body">
<div class="map">
<span class="road" style="left: -5%; right: -5%; top: 34%; height: 12px; transform: rotate(-8deg);"></span><span class="road" style="top: -5%; bottom: -5%; left: 42%; width: 14px; transform: rotate(12deg);"></span><span class="road" style="left: 0; right: 0; top: 68%; height: 9px; transform: rotate(3deg);"></span><span class="road" style="top: 0; bottom: 0; left: 78%; width: 9px;"></span><span class="road" style="top: 0; bottom: 0; left: 20%; width: 7px; transform: rotate(-6deg);"></span>
<span class="park" style="left: 60%; top: 8%; width: 180px; height: 110px;"></span><span class="park" style="left: 8%; top: 12%; width: 110px; height: 70px;"></span><span class="park" style="left: 48%; top: 44%; width: 90px; height: 60px;"></span>
<sc-for list="{{{{hoods}}}}" as="h" hint-placeholder-count="5"><span class="hoodb {{{{h.on}}}}" style="left: {{{{h.x}}}}%; top: {{{{h.y}}}}%;" onClick="{{{{h.pick}}}}"><span class="hn">{{{{h.n}}}}</span><span class="hq" style="display: {{{{h.qd}}}};">? {{{{h.q}}}} open</span></span></sc-for>
<sc-for list="{{{{heats}}}}" as="p" hint-placeholder-count="14"><span class="heat {{{{p.cls}}}}" style="left: {{{{p.x}}}}%; top: {{{{p.y}}}}%; width: {{{{p.sz}}}}px; height: {{{{p.sz}}}}px;" onClick="{{{{p.pick}}}}"><span class="glow"></span><span class="core">{{{{p.c}}}}</span></span><span class="lab" style="left: {{{{p.x}}}}%; top: {{{{p.y}}}}%; display: {{{{p.ld}}}};">{{{{p.n}}}}</span></sc-for>
<div class="mtl"><span><span class="bx"></span>Update as I move the map</span></div>
<div class="mleg"><span><i style="width: 14px; height: 14px; background: #ff5a3c;"></i>People are talking</span><span><i style="width: 10px; height: 10px; background: #ffffff; border: 2px solid #d8d8d8; box-sizing: border-box;"></i>Quiet</span><span><span style="display: inline-block; padding: 0 6px; border: 1.5px dashed #e8740c; border-radius: 8px; color: #b35c00; font-weight: 700; font-size: 10px; margin-right: 6px;">?</span>Open questions in an area</span></div>
</div>
<div class="res"><div class="rpad">
<sc-if value="{{{{isAll}}}}" hint-placeholder-val="{{{{ true }}}}"><h1 class="srf" style="margin: 0; font-size: 34px; line-height: 38px;">{{{{headA}}}} <em>{{{{headB}}}}</em></h1><span class="mu" style="font-size: 13px; margin-top: -6px;">{{{{subLine}}}}</span></sc-if>
<sc-if value="{{{{isPlace}}}}" hint-placeholder-val="{{{{ false }}}}"><span class="back" onClick="{{{{clear}}}}">← All of Irvine</span><div class="ph"><span style="display: flex; justify-content: space-between; align-items: baseline; gap: 10px;"><strong style="font-size: 22px;">{{{{pl.n}}}}</strong><span style="font-size: 13px;">★ {{{{pl.r}}}}</span></span><span class="mu" style="font-size: 13px;">{{{{pl.cat}}}} · {{{{pl.hood}}}} · {{{{pl.c}}}} conversations</span><a href="Main.dc.html" class="btn b-sm b-dark" style="align-self: flex-start; margin-top: 4px;">See the business</a></div></sc-if>
<sc-if value="{{{{isHood}}}}" hint-placeholder-val="{{{{ false }}}}"><span class="back" onClick="{{{{clear}}}}">← All of Irvine</span><h1 class="srf" style="margin: 0; font-size: 34px; line-height: 38px;">{{{{hoodName}}}}</h1><span class="mu" style="font-size: 13px; margin-top: -6px;">{{{{subLine}}}}</span></sc-if>
<div class="askb">{{{{askTxt}}}}<span class="btn b-sm b-coral" style="margin-left: auto; border-radius: 16px;">Post</span></div>
<span class="sorts"><sc-for list="{{{{sorts}}}}" as="s" hint-placeholder-count="3"><span class="{{{{s.on}}}}" onClick="{{{{s.pick}}}}">{{{{s.t}}}}</span></sc-for></span>
<div><sc-for list="{{{{threads}}}}" as="t" hint-placeholder-count="6"><div class="th"><span class="cz"><b>{{{{t.cat}}}}</b> · {{{{t.where}}}} · {{{{t.who}}}} · {{{{t.when}}}} · ▲ {{{{t.up}}}}</span><h3>{{{{t.q}}}}</h3>
<sc-if value="{{{{t.hasA}}}}" hint-placeholder-val="{{{{ true }}}}"><div class="ans"><span class="who"><span class="mk mk-{{{{t.mk}}}}"></span><b>{{{{t.aw}}}}</b><span class="badge" style="display: {{{{t.bd}}}};">{{{{t.badge}}}}</span>{{{{t.how}}}}</span><p>{{{{t.a}}}}</p></div></sc-if>
<sc-if value="{{{{t.noA}}}}" hint-placeholder-val="{{{{ false }}}}"><div class="open"><span>No answer yet. <strong>{{{{t.ask}}}}</strong></span><span class="btn b-sm b-dark">Answer</span></div></sc-if>
<span class="foot"><span>{{{{t.n}}}} answers</span><span>Share</span><span>Save</span></span></div></sc-for></div>
<sc-if value="{{{{isEmpty}}}}" hint-placeholder-val="{{{{ false }}}}"><div class="open" style="justify-content: flex-start;">Nobody has asked about this yet. Be the first.</div></sc-if>
</div></div>
</div>'''
JS=r'''    const S = this.state || {};
    const c = S.c || 'all', sort = S.sort || 'hot', pk = S.place, hd = S.hood;
    const PL = {
      bt: ['Backyard Tacos', 'food', 'University Park', '4.7', 24, 64], eg: ['Tacos El Guero', 'food', 'University Park', '4.6', 34, 76], lb: ['La Birrieria OC', 'food', 'Quail Hill', '4.5', 66, 74],
      lu: ['Lumen Aesthetics', 'beauty', 'Irvine Spectrum', '4.9', 54, 50], sa: ['Spectrum Aesthetics MD', 'beauty', 'Irvine Spectrum', '4.8', 62, 58], hh: ['Heritage Hair Studio', 'beauty', 'University Park', '4.6', 30, 86],
      wk: ['Woodbridge Kids Dental', 'health', 'Woodbridge', '4.9', 16, 28], kr: ['Kinjiro Ramen', 'food', 'Irvine Spectrum', '4.6', 48, 64], rn: ['Ramen Nagi', 'food', 'Irvine Spectrum', '4.7', 58, 40],
      bd: ['Blue Door Coffee', 'drinks', 'Woodbridge', '4.7', 32, 22], ia: ['Irvine Auto Care', 'car', 'Quail Hill', '4.4', 86, 52], qv: ['Quail Hill Vet', 'pets', 'Quail Hill', '4.9', 82, 72],
      gp: ['Great Park Pilates', 'fitness', 'Great Park', '4.8', 70, 20], tm: ['Tea Maru', 'drinks', 'Woodbridge', '4.6', 24, 40]
    };
    const HD = { 'Woodbridge': [14, 12], 'Great Park': [70, 7], 'Irvine Spectrum': [52, 30], 'University Park': [16, 94], 'Quail Hill': [88, 88] };
    const T = [
      ['bt', 'food', 'Question', 'Where can I take my kids to eat where they can also run around?', 'Linh T.', '2 hours ago', 64, 'Maria K.', 'Local expert · Food', 'vis', 'Went last Saturday', 'Backyard Tacos has a fenced lawn right next to the patio. You can see the kids from every table.', 11, ''],
      ['bt', 'food', 'Tip', 'Get the birria plate, not the tacos. Same price, twice the consommé.', 'Tom H.', '3 days ago', 21, 'Tom H.', '', 'vis', 'Eats there most Fridays', 'Ask for extra onions and cilantro on the side.', 4, ''],
      ['bt', 'food', 'Question', 'Is the patio heated at night?', 'Ella V.', '1 hour ago', 6, '', '', '', '', '', 0, 'Been to Backyard Tacos at night?'],
      ['eg', 'food', 'Tip', 'Best birria in Irvine is the truck on Culver', 'Diego R.', 'Yesterday', 51, 'Diego R.', 'Local expert · Food', 'vis', 'Eats there weekly', 'Cash only, $3.50, consommé included. Half the wait of Backyard Tacos.', 17, ''],
      ['lu', 'beauty', 'Question', 'First time getting lip filler. Who will not overdo it?', 'Anon', '5 hours ago', 88, 'Aisha M.', 'Local expert · Beauty', 'vis', 'Had it done twice', 'Lumen. Dr. Nair talked me down to half a syringe and told me to come back in two weeks if I wanted more.', 23, ''],
      ['lu', 'beauty', 'Question', 'Does Lumen take HSA cards?', 'Priya S.', 'Yesterday', 14, 'Lumen Aesthetics', 'Owner', 'site', 'Replied as the business', 'Yes, for most treatments. Bring the card to your consult.', 3, ''],
      ['lu', 'beauty', 'Tip', 'Park on level 3 of Structure B', 'Kelly W.', '2 days ago', 31, 'Kelly W.', '', 'vis', 'Goes every month', 'It is the only level with an elevator straight to the second floor.', 5, ''],
      ['sa', 'beauty', 'Question', 'Is Dr. Chen the one who actually injects?', 'M. from Newport', '4 days ago', 19, 'Aisha M.', 'Local expert · Beauty', 'vis', 'Patient since 2024', 'Every time, in my experience. Book early, her Saturdays fill up a month out.', 6, ''],
      ['wk', 'health', 'Question', 'Any dentist open Saturdays that is good with anxious kids?', 'Carmen V.', 'Yesterday', 39, 'Woodbridge Kids Dental', 'Owner', 'site', 'Replied as the business', 'We are open Saturdays 8 to 1 and only see children. First visits are a tour, no cleaning unless they are ready.', 8, ''],
      ['ia', 'car', 'Question', 'Who in Irvine actually knows Teslas and will not upsell me?', 'Tom H.', '2 days ago', 27, 'Jordan P.', 'Local expert · Car', 'vis', 'Took his Model Y in August', 'Irvine Auto Care. They told me my brakes had another 15,000 miles and did not charge for the check.', 6, ''],
      ['kr', 'food', 'Question', 'Late-night ramen after 11 on a weeknight?', 'Priya S.', '3 hours ago', 22, '', '', '', '', '', 0, 'Been to Kinjiro recently?'],
      ['bd', 'drinks', 'Tip', 'Blue Door is the quietest place to work before 11', 'Kelly W.', '4 days ago', 33, 'Kelly W.', '', 'vis', 'Works there Tuesdays', 'Outlets along the bar, strong Wi-Fi, and nobody minds laptops until lunch.', 9, ''],
      ['qv', 'pets', 'Question', 'Is Quail Hill Vet worth it for emergencies?', 'Sam L.', '6 hours ago', 14, '', '', '', '', '', 0, 'Been to Quail Hill Vet?'],
      ['hh', 'beauty', 'Question', 'Who does curly cuts in Irvine?', 'Nadia F.', '3 days ago', 29, 'Jordan P.', '', 'vis', 'Gets her hair cut there', 'Heritage Hair Studio. Ask for Renee, she cuts dry, curl by curl.', 12, ''],
      ['gp', 'fitness', 'Question', 'Pilates studio that is actually good for total beginners?', 'Ella V.', '5 days ago', 18, 'Maria K.', 'Local expert · Food', 'vis', 'Goes twice a week', 'Great Park Pilates. The intro class is $25 and they keep it to 6 people.', 5, ''],
      [null, 'food', 'Question', 'Somewhere in Woodbridge for a quiet dinner for two?', 'Jordan P.', '1 hour ago', 9, '', '', '', '', '', 0, 'Live in Woodbridge? Answer this', 'Woodbridge'],
      [null, 'health', 'Question', 'Urgent care near Quail Hill with short waits on Sundays?', 'Sam L.', '4 hours ago', 12, '', '', '', '', '', 0, 'Live near Quail Hill? Answer this', 'Quail Hill'],
      [null, 'drinks', 'Question', 'Best boba near Great Park that is not too sweet?', 'Linh T.', 'Yesterday', 16, '', '', '', '', '', 0, 'Know Great Park? Answer this', 'Great Park']
    ];
    const NM = { food: 'Food', drinks: 'Drinks', beauty: 'Beauty', health: 'Health', fitness: 'Fitness', car: 'Car', pets: 'Pets', home: 'Home' };
    const hoodOf = t => t[0] ? PL[t[0]][2] : t[14];
    const inCat = t => c === 'all' || t[1] === c;
    let rows = T.map((t, i) => ({ t, i })).filter(r => inCat(r.t));
    if (pk) rows = rows.filter(r => r.t[0] === pk);
    else if (hd) rows = rows.filter(r => hoodOf(r.t) === hd);
    if (sort === 'open') rows = rows.filter(r => !r.t[7]);
    if (sort === 'hot') rows = rows.slice().sort((a, b) => b.t[6] - a.t[6]);
    if (sort === 'new') rows = rows.slice().sort((a, b) => (a.t[5].includes('hour') ? 0 : 1) - (b.t[5].includes('hour') ? 0 : 1));
    const threads = rows.map(({ t }) => ({ cat: NM[t[1]], where: t[0] ? PL[t[0]][0] : t[14], q: t[3], who: t[4], when: t[5], up: String(t[6]), aw: t[7], badge: t[8], bd: t[8] ? 'inline-flex' : 'none', mk: t[9], how: t[10], a: t[11], n: String(t[12]), ask: t[13], hasA: !!t[7], noA: !t[7] }));
    const cnt = {}; T.filter(inCat).forEach(t => { if (t[0]) cnt[t[0]] = (cnt[t[0]] || 0) + 1; });
    const heats = Object.keys(PL).map(k => { const n = cnt[k] || 0; const inHood = !hd || PL[k][2] === hd; return { n: PL[k][0], x: String(PL[k][4]), y: String(PL[k][5]), c: String(n), sz: String(n ? 36 + n * 22 : 20), ld: n >= 2 || k === pk ? 'block' : 'none', cls: (n ? '' : 'cold') + (k === pk ? ' sel' : '') + (inHood ? '' : ' dim'), pick: () => this.setState({ place: k, hood: undefined }) }; });
    const openBy = {}; T.filter(inCat).forEach(t => { if (!t[0] && !t[7]) openBy[t[14]] = (openBy[t[14]] || 0) + 1; });
    const hoods = Object.keys(HD).map(h => ({ n: h, x: String(HD[h][0]), y: String(HD[h][1]), q: String(openBy[h] || 0), qd: openBy[h] ? 'inline-flex' : 'none', on: h === hd ? 'on' : '', pick: () => this.setState({ hood: h, place: undefined }) }));
    const cats = [['all', 'Everything']].concat(Object.keys(NM).map(k => [k, NM[k]])).map(x => ({ t: x[1], n: String(x[0] === 'all' ? T.length : T.filter(t => t[1] === x[0]).length), on: x[0] === c ? 'on' : '', pick: () => this.setState({ c: x[0] }) }));
    const sorts = [['hot', 'Hot'], ['new', 'New'], ['open', 'Unanswered']].map(s => ({ t: s[1], on: s[0] === sort ? 'on' : '', pick: () => this.setState({ sort: s[0] }) }));
    const p = pk ? PL[pk] : null;
    const openN = rows.filter(r => !r.t[7]).length;
    return { cats, sorts, heats, hoods, threads, isAll: !pk && !hd, isPlace: !!pk, isHood: !pk && !!hd, isEmpty: rows.length === 0,
      pl: p ? { n: p[0], cat: NM[p[1]], hood: p[2], r: p[3], c: String(cnt[pk] || 0) } : {}, hoodName: hd || '',
      headA: c === 'all' ? 'What Irvine is' : NM[c] + ':', headB: c === 'all' ? 'talking about.' : 'what Irvine is saying.',
      subLine: rows.length + (rows.length === 1 ? ' conversation' : ' conversations') + (openN ? ' · ' + openN + (openN === 1 ? ' needs an answer' : ' need an answer') : ''),
      askTxt: p ? 'Ask about ' + p[0] + ', or share a tip' : (hd ? 'Ask ' + hd + ' anything' : 'Ask Irvine about a place, or share a tip'),
      clear: () => this.setState({ place: undefined, hood: undefined }) };'''
t=HEADX.replace('<title>Lumen Aesthetics on Local AI Registry</title>','<title>What Irvine is talking about | Local AI Registry</title>')
out=t+'\n'+CSS+'\n</style>\n</helmet>\n<div style="width: 1440px; height: 960px; box-sizing: border-box; display: flex; flex-direction: column; background: #ffffff; position: relative; overflow: hidden;">\n'+BODY+'\n</div>\n</x-dc>\n<script type="text/x-dc" data-dc-script>\nclass Component extends DCLogic {\n  renderVals() {\n'+JS+'\n  }\n}\n</script>\n</body>\n</html>\n'
open(P+'Explore.dc.html','w').write(out); print('ok')
