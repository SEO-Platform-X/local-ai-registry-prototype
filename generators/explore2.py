import sys; sys.path.insert(0,'/tmp/gen'); from common import *
TRI="url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='22' height='22' viewBox='0 0 22 22'%3E%3Cpath d='M11 3.5L19.5 18.5H2.5Z' fill='none' stroke='%238a8a8a' stroke-width='2.4' stroke-linejoin='round'/%3E%3C/svg%3E\") center / 100% 100% no-repeat"
HEADX=HEAD.replace('family=Figtree:wght@400;500;600;700;800&amp;display=swap','family=Figtree:wght@400;500;600;700;800&amp;family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&amp;display=swap')
CSS=r'''.srf{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;letter-spacing:-0.01em;color:#13203a}
.srf em{font-style:italic;color:#ff5a3c}
.mk{position:relative;display:inline-block;width:11px;height:11px;margin:0 6px 1px 0;vertical-align:middle;flex-shrink:0}
.mk::after{content:"";position:absolute;inset:0}
.mk-site::after{inset:2px;background:#008a05;border-radius:50%}
.mk-vis::after{inset:2px;border:1.6px solid #e8740c;border-radius:50%}
.mk-ai::after{inset:0;background:'''+TRI+'''}
.stbar{display:flex;align-items:center;gap:8px;padding:8px 20px;background:#1f1f1f;color:#ffffff;font-size:12px}
.stbar .stl{font-weight:700;letter-spacing:0.06em;text-transform:uppercase;font-size:10px;color:#b0b0b0;margin-right:4px}
.stp{display:inline-flex;align-items:center;height:28px;padding:0 12px;border-radius:14px;border:1px solid #4a4a4a;color:#dddddd;cursor:pointer}
.stp.on{background:#ffffff;border-color:#ffffff;color:#222222;font-weight:600}
.top{height:64px;padding:0 20px;display:flex;align-items:center;gap:16px;border-bottom:1px solid #e6e6e6;background:#ffffff;flex-shrink:0}
.ask{display:flex;align-items:center;gap:10px;height:46px;flex-grow:1;max-width:640px;padding:0 6px 0 16px;border:1px solid #dddddd;border-radius:23px;box-shadow:0 2px 10px rgba(0,0,0,0.06)}
.ask input{flex-grow:1;border:none;outline:none;font-family:inherit;font-size:15px;background:transparent;color:#222222}
.nl{font-size:14px;font-weight:600;color:#222222;text-decoration:none;white-space:nowrap}
.body{display:grid;grid-template-columns:440px 1fr;flex-grow:1;min-height:0}
.panel{border-right:1px solid #e6e6e6;overflow-y:auto;display:flex;flex-direction:column;background:#ffffff}
.pad{padding:18px 20px;display:flex;flex-direction:column;gap:12px}
.chips{display:flex;gap:6px;flex-wrap:wrap}
.chip{display:inline-flex;align-items:center;height:30px;padding:0 12px;border:1px solid #dddddd;border-radius:15px;font-size:12px;cursor:pointer;background:#ffffff}
.chip.on{border:2px solid #222222;padding:0 11px;font-weight:600}
.wr{display:flex;flex-direction:column;gap:4px;padding:12px 14px;border:1px solid #ebebeb;border-radius:12px;cursor:pointer;text-decoration:none;color:#222222}
.wr:hover,.wr.on{border-color:#222222}
.wr .old{font-size:13px;color:#a0a0a0;text-decoration:line-through}
.wr .nw{font-size:14px;font-weight:600;display:flex;align-items:center}
.tabs2{display:flex;border-bottom:1px solid #ebebeb;padding:0 20px}
.tabs2 span{height:42px;display:inline-flex;align-items:center;padding:0 12px;font-size:14px;font-weight:600;color:#6a6a6a;cursor:pointer;border-bottom:2px solid transparent;margin-bottom:-1px}
.tabs2 span.on{color:#222222;border-bottom-color:#222222}
.ans p{margin:0 0 8px;font-size:14px;line-height:21px}
.cite{display:inline-flex;align-items:center;justify-content:center;min-width:16px;height:16px;padding:0 4px;border-radius:8px;background:#f0f0f0;font-size:10px;font-weight:700;color:#484848;vertical-align:2px;margin-left:2px}
.rc{display:grid;grid-template-columns:72px 1fr;gap:12px;padding:10px 0;border-top:1px solid #f0f0f0;text-decoration:none;color:#222222}
.rph{height:64px;border-radius:8px}
.sc{display:inline-flex;align-items:center;height:20px;padding:0 7px;border-radius:10px;font-size:11px;font-weight:700}
.map{position:relative;overflow:hidden;background:#e9ede6}
.road{position:absolute;background:#ffffff}
.hood{position:absolute;font-size:12px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#8a9885}
.pin{position:absolute;transform:translate(-50%,-50%);display:flex;align-items:center;justify-content:center;gap:4px;min-width:30px;height:30px;padding:0 8px;border-radius:15px;font-size:12px;font-weight:700;cursor:pointer;box-shadow:0 2px 6px rgba(0,0,0,0.2);box-sizing:border-box;white-space:nowrap}
.pin.ok{background:#ffffff;color:#237233;border:2px solid #237233}
.pin.bad{background:#c13515;color:#ffffff;border:2px solid #ffffff}
.pin.unk{background:#ffffff;color:#8a8a8a;border:2px dashed #b0b0b0}
.pin.sel{transform:translate(-50%,-50%) scale(1.2);z-index:5;box-shadow:0 0 0 4px rgba(34,34,34,0.25),0 4px 12px rgba(0,0,0,0.3)}
.pop{position:absolute;width:300px;padding:16px;border-radius:14px;background:#ffffff;box-shadow:0 10px 30px rgba(0,0,0,0.2);display:flex;flex-direction:column;gap:8px;z-index:10;transform:translate(-50%,calc(-100% - 26px))}
.lay{position:absolute;top:16px;left:16px;display:flex;gap:4px;padding:4px;border-radius:22px;background:#ffffff;box-shadow:0 2px 10px rgba(0,0,0,0.12);z-index:6}
.lay span{height:32px;padding:0 14px;border-radius:16px;display:inline-flex;align-items:center;font-size:13px;font-weight:600;cursor:pointer;color:#484848}
.lay span.on{background:#222222;color:#ffffff}
.leg{position:absolute;bottom:16px;left:16px;display:flex;gap:14px;padding:10px 14px;border-radius:12px;background:#ffffff;box-shadow:0 2px 10px rgba(0,0,0,0.12);font-size:12px;z-index:6}
.leg i{display:inline-block;width:12px;height:12px;border-radius:50%;margin-right:5px;vertical-align:-2px}
.stat{position:absolute;top:16px;right:16px;padding:12px 16px;border-radius:12px;background:#13203a;color:#ffffff;z-index:6;max-width:260px}
.fy{display:flex;flex-direction:column;gap:4px;padding:12px 14px;border:1px solid #ebebeb;border-radius:12px}
'''
LOGO2='<svg width="22" height="20" viewBox="0 0 22 20" aria-hidden="true"><path d="M11 1L21 19H1Z" fill="#2d55e6"></path><path d="M11 8L15.5 16H6.5Z" fill="#ffffff"></path></svg>'
BODY=f'''<div class="stbar"><span class="stl">Prototype</span><span class="stp {{{{outOn}}}}" onClick="{{{{goOut}}}}">Logged out</span><span class="stp {{{{inOn}}}}" onClick="{{{{goIn}}}}">Logged in</span><span style="margin-left: auto; color: #8a8a8a;">This is the root page, localairegistry.com</span></div>
<div class="top"><a href="Explore.dc.html" style="display: flex; align-items: center; gap: 8px; text-decoration: none; color: #13203a; font-weight: 700; font-size: 15px; white-space: nowrap;">{LOGO2}Local AI Registry</a>
<div class="ask"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#222222" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="M20 20l-4-4"></path></svg><input type="text" value="{{{{askText}}}}" placeholder="Ask anything, or search a business. Every answer is fact-checked." aria-label="Ask"><span class="mu" style="font-size: 12px; white-space: nowrap;">Irvine, CA</span><span class="btn b-coral b-sm" style="border-radius: 18px;">Ask</span></div>
<span style="margin-left: auto; display: flex; align-items: center; gap: 18px;"><a href="Business.dc.html" class="nl">For business</a><sc-if value="{{{{out}}}}" hint-placeholder-val="{{{{ true }}}}"><a href="#" class="nl">Sign in</a><span class="btn b-sm b-dark" style="border-radius: 18px;">Join your neighbors</span></sc-if><sc-if value="{{{{inn}}}}" hint-placeholder-val="{{{{ false }}}}"><span style="display: flex; align-items: center; gap: 8px; font-size: 13px;"><span style="width: 32px; height: 32px; border-radius: 50%; background: #e8e2d6; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 12px;">MK</span>Maria K.</span></sc-if></span></div>
<div class="body">
<div class="panel">
<sc-if value="{{{{inn}}}}" hint-placeholder-val="{{{{ false }}}}"><div class="tabs2"><span class="{{{{tA}}}}" onClick="{{{{pickA}}}}">Explore</span><span class="{{{{tF}}}}" onClick="{{{{pickF}}}}">For you<span style="margin-left: 6px; min-width: 18px; height: 18px; border-radius: 9px; background: #c13515; color: #ffffff; font-size: 11px; display: inline-flex; align-items: center; justify-content: center;">3</span></span></div></sc-if>
<sc-if value="{{{{showExplore}}}}" hint-placeholder-val="{{{{ true }}}}">
<div class="pad"><sc-if value="{{{{noQ}}}}" hint-placeholder-val="{{{{ true }}}}"><h1 class="srf" style="margin: 0; font-size: 36px; line-height: 38px;">The fact-checked map of <em>Irvine</em>.</h1><span style="font-size: 14px; line-height: 21px; color: #484848;">Yelp shows what people thought. ChatGPT shows what it guesses. This shows what is true, who checked it, and where AI is wrong.</span></sc-if>
<div class="chips"><sc-for list="{{{{chips}}}}" as="c" hint-placeholder-count="4"><span class="chip {{{{c.on}}}}" onClick="{{{{c.pick}}}}">{{{{c.t}}}}</span></sc-for></div></div>
<sc-if value="{{{{noQ}}}}" hint-placeholder-val="{{{{ true }}}}"><div class="pad" style="padding-top: 0;"><div style="display: flex; align-items: baseline; justify-content: space-between;"><strong style="font-size: 16px;">Where AI is wrong right now</strong><span class="mu" style="font-size: 12px;">{{{{wrongCount}}}} places</span></div><sc-for list="{{{{wrongList}}}}" as="w" hint-placeholder-count="6"><div class="wr {{{{w.on}}}}" onClick="{{{{w.pick}}}}"><span style="display: flex; justify-content: space-between; font-size: 13px;"><strong>{{{{w.n}}}}</strong><span class="mu">{{{{w.cat}}}}</span></span><span class="old">{{{{w.eng}}}} says: {{{{w.old}}}}</span><span class="nw"><span class="mk mk-{{{{w.mk}}}}"></span>{{{{w.nw}}}}</span><span class="mu" style="font-size: 12px;">{{{{w.by}}}}</span></div></sc-for>
<sc-if value="{{{{out}}}}" hint-placeholder-val="{{{{ true }}}}"><div style="padding: 16px; border-radius: 12px; background: #f6f3ee; display: flex; flex-direction: column; gap: 8px;"><strong style="font-size: 15px;">Know one of these places?</strong><span style="font-size: 13px; line-height: 19px; color: #484848;">Add what you know. Once a second neighbor or the owner agrees, it is confirmed, and AI starts repeating it.</span><span class="btn b-sm b-dark" style="align-self: flex-start;">Join your neighbors</span></div></sc-if></div></sc-if>
<sc-if value="{{{{hasQ}}}}" hint-placeholder-val="{{{{ false }}}}"><div class="pad" style="padding-top: 0;"><div class="ans" style="padding: 14px 16px; border: 1px solid #dddddd; border-radius: 12px;"><strong style="font-size: 13px; display: block; padding-bottom: 6px;">Answer · {{{{q.src}}}} checked facts</strong><sc-for list="{{{{q.lines}}}}" as="l" hint-placeholder-count="3"><p>{{{{l.t}}}}<span class="mk mk-{{{{l.m}}}}" style="margin: 0 0 1px 5px;"></span><span class="cite">{{{{l.c}}}}</span></p></sc-for></div>
<div><sc-for list="{{{{q.biz}}}}" as="b" hint-placeholder-count="5"><a href="Main.dc.html" class="rc"><span class="rph" style="background: {{{{b.bg}}}};"></span><span style="display: flex; flex-direction: column; gap: 3px;"><span style="display: flex; justify-content: space-between; gap: 6px;"><strong style="font-size: 14px;">{{{{b.i}}}}. {{{{b.n}}}}</strong><span class="sc" style="background: {{{{b.sbg}}}}; color: {{{{b.sc}}}};">AI {{{{b.s}}}}</span></span><span class="mu" style="font-size: 12px;">★ {{{{b.r}}}} · {{{{b.cat}}}} · {{{{b.dist}}}}</span><span style="font-size: 12px; color: #484848;">{{{{b.why}}}}</span></span></a></sc-for></div>
<div style="padding: 14px 16px; border-radius: 12px; border: 1px dashed #c8c8c8; display: flex; align-items: center; justify-content: space-between; gap: 12px;"><span style="font-size: 13px; line-height: 19px;">Not the right fit? Tell businesses what you want.</span><a href="Request.dc.html" class="btn b-sm b-dark">Post a request</a></div></div></sc-if>
</sc-if>
<sc-if value="{{{{showFY}}}}" hint-placeholder-val="{{{{ false }}}}"><div class="pad">
<strong style="font-size: 16px;">Your places</strong><sc-for list="{{{{mine}}}}" as="m" hint-placeholder-count="3"><a href="Main.dc.html" class="fy" style="text-decoration: none; color: #222222;"><span style="display: flex; justify-content: space-between; font-size: 13px;"><strong>{{{{m.n}}}}</strong><span class="mu">{{{{m.when}}}}</span></span><span style="font-size: 13px; color: #484848;">{{{{m.t}}}}</span></a></sc-for>
<strong style="font-size: 16px; padding-top: 6px;">You can help</strong><span class="mu" style="font-size: 12px; margin-top: -6px;">Questions about places you have been</span><sc-for list="{{{{help}}}}" as="h" hint-placeholder-count="2"><div class="fy"><strong style="font-size: 14px;">{{{{h.q}}}}</strong><span class="mu" style="font-size: 12px;">{{{{h.b}}}} · {{{{h.n}}}} people want to know</span><a href="Main.dc.html" class="btn b-sm" style="align-self: flex-start; margin-top: 4px;">Answer</a></div></sc-for>
<strong style="font-size: 16px; padding-top: 6px;">Your impact</strong><div class="fy" style="background: #13203a; border-color: #13203a; color: #ffffff;"><span class="srf" style="font-size: 44px; line-height: 44px; color: #ffffff;">212</span><span style="font-size: 13px; line-height: 19px; color: #d0d6e2;">people read your fixes this month. ChatGPT now repeats 3 of them, including Lumen's Monday hours.</span></div>
<strong style="font-size: 16px; padding-top: 6px;">Neighbors are asking</strong><sc-for list="{{{{asking}}}}" as="a" hint-placeholder-count="2"><div class="fy"><strong style="font-size: 14px;">{{{{a.q}}}}</strong><span class="mu" style="font-size: 12px;">{{{{a.who}}}} · {{{{a.n}}}} replies</span></div></sc-for>
</div></sc-if>
</div>
<div class="map">
<span class="road" style="left: -5%; right: -5%; top: 34%; height: 12px; transform: rotate(-9deg);"></span><span class="road" style="top: -5%; bottom: -5%; left: 40%; width: 14px; transform: rotate(14deg);"></span><span class="road" style="left: 0; right: 0; top: 70%; height: 8px; transform: rotate(3deg);"></span><span class="road" style="top: 0; bottom: 0; left: 76%; width: 8px;"></span><span class="road" style="top: 0; bottom: 0; left: 18%; width: 6px; transform: rotate(-6deg);"></span>
<span style="position: absolute; left: 46%; top: 44%; width: 120px; height: 80px; border-radius: 16px; background: #d9e6d3;"></span>
<span class="hood" style="left: 44%; top: 58%;">Irvine Spectrum</span><span class="hood" style="left: 12%; top: 20%;">Woodbridge</span><span class="hood" style="left: 64%; top: 16%;">Great Park</span><span class="hood" style="left: 22%; top: 80%;">University Park</span><span class="hood" style="left: 80%; top: 76%;">Quail Hill</span>
<span class="lay"><span class="{{{{lAll}}}}" onClick="{{{{pickAll}}}}">Everything</span><span class="{{{{lWrong}}}}" onClick="{{{{pickWrong}}}}">Where AI is wrong</span></span>
<span class="stat"><span class="srf" style="font-size: 34px; line-height: 34px; color: #ffffff; display: block;">1 in 3</span><span style="font-size: 12px; line-height: 17px; color: #c3c9d6;">businesses in Irvine have something AI gets wrong. Neighbors fixed 412 this month.</span></span>
<sc-for list="{{{{pins}}}}" as="p" hint-placeholder-count="24"><span class="pin {{{{p.cls}}}}" style="left: {{{{p.x}}}}%; top: {{{{p.y}}}}%; display: {{{{p.show}}}};" onClick="{{{{p.pick}}}}">{{{{p.lbl}}}}</span></sc-for>
<sc-if value="{{{{hasSel}}}}" hint-placeholder-val="{{{{ true }}}}"><div class="pop" style="left: {{{{sel.x}}}}%; top: {{{{sel.y}}}}%;"><span style="display: flex; justify-content: space-between; gap: 8px;"><strong style="font-size: 15px;">{{{{sel.n}}}}</strong><span class="sc" style="background: {{{{sel.sbg}}}}; color: {{{{sel.sc}}}};">AI {{{{sel.s}}}}</span></span><span class="mu" style="font-size: 12px;">{{{{sel.cat}}}} · ★ {{{{sel.r}}}}</span><span style="font-size: 13px; color: #a0a0a0; text-decoration: line-through;">{{{{sel.eng}}}} says: {{{{sel.old}}}}</span><span style="font-size: 14px; font-weight: 600; display: flex; align-items: center;"><span class="mk mk-{{{{sel.mk}}}}"></span>{{{{sel.nw}}}}</span><span class="mu" style="font-size: 12px;">{{{{sel.by}}}}</span><a href="Main.dc.html" class="btn b-sm b-dark" style="margin-top: 4px;">See the full record</a></div></sc-if>
<span class="leg"><span><i style="background: #c13515;"></i>AI is wrong here</span><span><i style="background: #ffffff; border: 2px solid #237233; box-sizing: border-box;"></i>AI gets it right</span><span><i style="background: #ffffff; border: 2px dashed #b0b0b0; box-sizing: border-box;"></i>Not checked yet</span></span>
</div>
</div>'''
JS=r'''    const S = this.state || {};
    const logged = !!S.logged, tab = S.tab || 'x', qi = S.qi === undefined ? -1 : S.qi, layer = S.layer || 'all', selId = S.sel === undefined ? 0 : S.sel;
    const P = [
      ['Lumen Aesthetics', 'Med spa', 58, '4.9', 53, 50, 'bad', 'ChatGPT', 'Open Mondays', 'Closed Mondays', 'site', 'Tom H. called on a Monday. Confirmed by 3 neighbors and the owner', '#e8d9cf'],
      ['Pho Saigon Bay', 'Restaurant', 64, '4.6', 30, 42, 'bad', 'Gemini', 'Street parking only', 'Free lot behind the building', 'vis', 'Diego R. parked there Friday. Waiting for a second neighbor', '#efe7d6'],
      ['Glow Bar Irvine', 'Facial spa', 52, '4.5', 70, 30, 'bad', 'Claude', 'Closed Sundays', 'Open Sundays, 10 AM to 4 PM', 'vis', 'Priya S. went last Sunday. Waiting for a second neighbor', '#f0dfd0'],
      ['Spectrum Aesthetics MD', 'Med spa', 81, '4.8', 58, 56, 'bad', 'Perplexity', 'Aestheticians do Botox', 'Dr. Chen or a nurse practitioner', 'site', 'Aisha M. had Botox there. Confirmed by the state license lookup', '#d9dfe8'],
      ['Woodbridge Kids Dental', 'Dentist', 77, '4.9', 18, 26, 'bad', 'ChatGPT', 'No Saturday hours', 'Saturdays 8 AM to 1 PM', 'site', 'Confirmed by the owner and 2 parents', '#dfe8d9'],
      ['Blue Door Coffee', 'Cafe', 70, '4.7', 40, 70, 'bad', 'Gemini', 'No outlets or Wi-Fi', 'Free Wi-Fi, outlets at the bar', 'vis', 'Linh T. worked there Tuesday', '#e4e0ef'],
      ['Great Park Pilates', 'Fitness', 74, '4.8', 66, 20, 'ok', '', '', 'AI gets its classes and prices right', 'site', 'Checked this morning', '#e8e2d6'],
      ['Quail Hill Vet', 'Veterinarian', 83, '4.9', 82, 72, 'ok', '', '', 'AI gets its hours and emergency line right', 'site', 'Checked this morning', '#e8e2d6'],
      ['Irvine Auto Care', 'Auto repair', 69, '4.4', 84, 44, 'bad', 'ChatGPT', 'Does not work on EVs', 'Certified for Tesla and Rivian', 'site', 'Confirmed by the owner', '#e8e2d6'],
      ['Heritage Hair Studio', 'Hair salon', 61, '4.6', 24, 60, 'ok', '', '', 'AI gets its stylists and prices right', 'site', 'Checked this morning', '#e8e2d6'],
      ['University Park Chiro', 'Chiropractor', 0, '4.3', 30, 84, 'unk', '', '', 'Not checked yet', 'ai', 'Nobody has added anything yet', '#e8e2d6'],
      ['Sakura Ramen', 'Restaurant', 72, '4.7', 47, 32, 'ok', '', '', 'AI gets its hours and menu right', 'site', 'Checked this morning', '#e8e2d6'],
      ['Spectrum Eye Center', 'Eye doctor', 79, '4.8', 62, 64, 'ok', '', '', 'AI gets its insurance list right', 'site', 'Checked this morning', '#e8e2d6'],
      ['Coastline Pet Grooming', 'Pet groomer', 0, '4.5', 90, 60, 'unk', '', '', 'Not checked yet', 'ai', 'Nobody has added anything yet', '#e8e2d6'],
      ['Northwood Tutoring', 'Tutoring', 66, '4.9', 36, 14, 'bad', 'Claude', 'Online only', 'In person at Northwood Town Center', 'vis', 'Two parents confirmed it', '#e8e2d6'],
      ['Canyon Dry Cleaners', 'Dry cleaner', 0, '4.2', 12, 46, 'unk', '', '', 'Not checked yet', 'ai', 'Nobody has added anything yet', '#e8e2d6'],
      ['Pacific Skin Studio', 'Skin care', 69, '4.6', 50, 78, 'ok', '', '', 'AI gets its services right', 'site', 'Checked this morning', '#e8e2d6'],
      ['Spectrum Florist', 'Florist', 0, '4.8', 72, 50, 'unk', '', '', 'Not checked yet', 'ai', 'Nobody has added anything yet', '#e8e2d6']
    ];
    const pins = P.map((p, i) => ({ cls: p[6] + (i === selId ? ' sel' : ''), x: String(p[4]), y: String(p[5]), lbl: p[6] === 'bad' ? '!' : (p[6] === 'ok' ? '✓' : '?'), show: (layer === 'wrong' && p[6] !== 'bad') ? 'none' : 'flex', pick: () => this.setState({ sel: i }) }));
    const sp = P[selId];
    const scC = s => s >= 75 ? ['#ddf1e1', '#237233'] : s >= 60 ? ['#fdeeda', '#b86a00'] : ['#fbe9e7', '#c13515'];
    const sel = { n: sp[0], cat: sp[1], s: sp[2] ? String(sp[2]) : 'not scored', sbg: scC(sp[2])[0], sc: scC(sp[2])[1], r: sp[3], x: String(sp[4]), y: String(sp[5]), eng: sp[7] || 'AI', old: sp[8] || 'Nothing checked yet', nw: sp[9], mk: sp[10], by: sp[11] };
    const bad = P.map((p, i) => [p, i]).filter(x => x[0][6] === 'bad');
    const wrongList = bad.map(([p, i]) => ({ n: p[0], cat: p[1], eng: p[7], old: p[8], nw: p[9], mk: p[10], by: p[11], on: i === selId ? 'on' : '', pick: () => this.setState({ sel: i }) }));
    const Q = [
      { t: 'Kids dentist open Saturday', q: 'Which dentist near me sees kids on Saturdays?', src: '22', lines: [['Woodbridge Kids Dental is open Saturdays 8 AM to 1 PM and only sees children.', 'site', '1'], ['ChatGPT still says it has no Saturday hours. The owner and 2 parents confirmed it does.', 'site', '2']], biz: [['Woodbridge Kids Dental', 'Dentist', '4.9', 77, '1.2 mi', 'Saturdays, kids only', '#dfe8d9']] },
      { t: 'Natural lip filler, takes HSA', q: 'Who does natural-looking lip filler in Irvine and takes HSA cards?', src: '41', lines: [['Lumen Aesthetics and Spectrum Aesthetics MD are the two where a doctor or nurse does every lip filler and HSA cards are accepted.', 'site', '1'], ['Lumen is the one most described as natural: 31 reviews mention being talked out of more.', 'vis', '2']], biz: [['Lumen Aesthetics', 'Med spa', '4.9', 58, '0.4 mi', 'Half syringes, takes HSA', '#e8d9cf'], ['Spectrum Aesthetics MD', 'Med spa', '4.8', 81, '0.9 mi', 'Doctor-led, takes HSA', '#d9dfe8']] },
      { t: 'Coffee shop to work from', q: 'Where can I work from a coffee shop with Wi-Fi near the Spectrum?', src: '17', lines: [['Blue Door Coffee has free Wi-Fi and outlets at the bar, 0.6 miles from Irvine Spectrum.', 'vis', '1'], ['Gemini says it has neither. A neighbor worked there Tuesday.', 'vis', '2']], biz: [['Blue Door Coffee', 'Cafe', '4.7', 70, '0.6 mi', 'Wi-Fi, outlets at the bar', '#e4e0ef'], ['Sakura Ramen', 'Restaurant', '4.7', 72, '0.8 mi', 'Not for working', '#efe7d6']] },
      { t: 'Mechanic for EVs', q: 'Which mechanic in Irvine works on Teslas?', src: '12', lines: [['Irvine Auto Care is certified for Tesla and Rivian repairs, confirmed by the owner.', 'site', '1'], ['ChatGPT still says it does not work on EVs.', 'ai', '2']], biz: [['Irvine Auto Care', 'Auto repair', '4.4', 69, '2.1 mi', 'Tesla and Rivian certified', '#e8e2d6']] }
    ];
    const chips = Q.map((x, i) => ({ t: x.t, on: i === qi ? 'on' : '', pick: () => this.setState({ qi: qi === i ? -1 : i }) }));
    const cq = qi >= 0 ? Q[qi] : Q[0];
    const q = { src: cq.src, lines: cq.lines.map(l => ({ t: l[0], m: l[1], c: l[2] })), biz: cq.biz.map((b, i) => ({ i: String(i + 1), n: b[0], cat: b[1], r: b[2], s: String(b[3]), sbg: scC(b[3])[0], sc: scC(b[3])[1], dist: b[4], why: b[5], bg: b[6] })) };
    const mine = [['Lumen Aesthetics', 'Added Morpheus8 Body. Consults start October 1.', '2 hours ago'], ['Blue Door Coffee', 'Your Wi-Fi fix was confirmed by a second neighbor.', 'Yesterday'], ['Sakura Ramen', 'New fall hours: open until 11 PM Fridays.', '3 days ago']].map(x => ({ n: x[0], t: x[1], when: x[2] }));
    const help = [['Does Lumen Aesthetics take HSA cards?', 'Lumen Aesthetics', '14'], ['Is Blue Door Coffee quiet enough for calls?', 'Blue Door Coffee', '6']].map(x => ({ q: x[0], b: x[1], n: x[2] }));
    const asking = [['Who is a good dentist for kids who is open Saturdays?', 'Linh T., Costa Mesa', '11'], ['Any mechanic near the Spectrum that works on hybrids?', 'Diego R., Tustin', '7']].map(x => ({ q: x[0], who: x[1], n: x[2] }));
    const showFY = logged && tab === 'f';
    return { out: !logged, inn: logged, outOn: logged ? '' : 'on', inOn: logged ? 'on' : '', goOut: () => this.setState({ logged: false }), goIn: () => this.setState({ logged: true, tab: 'f' }),
      tA: showFY ? '' : 'on', tF: showFY ? 'on' : '', pickA: () => this.setState({ tab: 'x' }), pickF: () => this.setState({ tab: 'f' }), showExplore: !showFY, showFY,
      noQ: qi < 0, hasQ: qi >= 0, askText: qi >= 0 ? Q[qi].q : '', chips, q, wrongList, wrongCount: String(bad.length), pins, sel, hasSel: true,
      lAll: layer === 'all' ? 'on' : '', lWrong: layer === 'wrong' ? 'on' : '', pickAll: () => this.setState({ layer: 'all' }), pickWrong: () => this.setState({ layer: 'wrong' }), mine, help, asking };'''
t=HEADX.replace('<title>Lumen Aesthetics on Local AI Registry</title>','<title>Local AI Registry: the fact-checked map</title>')
out=t+'\n'+CSS+'\n</style>\n</helmet>\n<div style="width: 1440px; height: 960px; box-sizing: border-box; display: flex; flex-direction: column; background: #ffffff; position: relative; overflow: hidden;">\n'+BODY+'\n</div>\n</x-dc>\n<script type="text/x-dc" data-dc-script>\nclass Component extends DCLogic {\n  renderVals() {\n'+JS+'\n  }\n}\n</script>\n</body>\n</html>\n'
open(P+'Explore.dc.html','w').write(out); print('ok')
