import sys; sys.path.insert(0,'/tmp/gen'); from common import *
HEADX=HEAD.replace('family=Figtree:wght@400;500;600;700;800&amp;display=swap','family=Figtree:wght@400;500;600;700;800&amp;family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&amp;display=swap')
CSS=r'''.srf{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;letter-spacing:-0.01em;color:#13203a}
.srf em{font-style:italic;color:#ff5a3c}
.top{height:64px;padding:0 20px;display:flex;align-items:center;gap:16px;border-bottom:1px solid #e6e6e6;background:#ffffff;flex-shrink:0}
.ask{display:flex;align-items:center;gap:10px;height:44px;flex-grow:1;max-width:560px;padding:0 16px;border:1px solid #dddddd;border-radius:22px;box-shadow:0 2px 10px rgba(0,0,0,0.06)}
.ask input{flex-grow:1;border:none;outline:none;font-family:inherit;font-size:15px;background:transparent;color:#222222}
.nl{font-size:14px;font-weight:600;color:#222222;text-decoration:none;white-space:nowrap}
.kf{display:flex;gap:8px;padding:12px 20px;border-bottom:1px solid #eeeeee;background:#ffffff;flex-shrink:0;flex-wrap:nowrap;overflow:hidden}
.kc{display:inline-flex;align-items:center;height:34px;padding:0 14px;border:1px solid #dddddd;border-radius:17px;font-size:13px;font-weight:600;cursor:pointer;white-space:nowrap;background:#ffffff}
.kc.on{background:#222222;border-color:#222222;color:#ffffff}
.body{display:grid;grid-template-columns:420px 1fr;flex-grow:1;min-height:0}
.panel{border-right:1px solid #e6e6e6;overflow-y:auto;background:#ffffff}
.pad{padding:18px 20px;display:flex;flex-direction:column;gap:4px}
.rc{display:grid;grid-template-columns:76px 1fr;gap:14px;padding:14px 0;border-top:1px solid #f0f0f0;text-decoration:none;color:#222222}
.rc.on strong{text-decoration:underline}
.rph{height:76px;border-radius:10px}
.tg{display:inline-flex;align-items:center;height:22px;padding:0 8px;border-radius:11px;background:#f3f3f3;font-size:11px;font-weight:600;color:#484848}
.tg.hit{background:#fff1ec;color:#c2410c}
.map{position:relative;overflow:hidden;background:#e9ede6}
.road{position:absolute;background:#ffffff}
.hood{position:absolute;font-size:12px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#8a9885}
.pin{position:absolute;transform:translate(-50%,-50%);display:flex;align-items:center;height:28px;padding:0 10px;border-radius:14px;background:#ffffff;font-size:12px;font-weight:700;cursor:pointer;box-shadow:0 2px 6px rgba(0,0,0,0.18);white-space:nowrap;color:#222222;border:2px solid #ffffff}
.pin.dim{opacity:0.35;box-shadow:none}
.pin.hit{background:#222222;color:#ffffff;border-color:#222222}
.pin.sel{z-index:6;transform:translate(-50%,-50%) scale(1.12);box-shadow:0 0 0 4px rgba(255,90,60,0.35),0 4px 12px rgba(0,0,0,0.25)}
.pop{position:absolute;width:290px;padding:16px;border-radius:14px;background:#ffffff;box-shadow:0 10px 30px rgba(0,0,0,0.2);display:flex;flex-direction:column;gap:8px;z-index:10}
'''
LOGO2='<svg width="22" height="20" viewBox="0 0 22 20" aria-hidden="true"><path d="M11 1L21 19H1Z" fill="#2d55e6"></path><path d="M11 8L15.5 16H6.5Z" fill="#ffffff"></path></svg>'
BODY=f'''<div class="top"><a href="Explore.dc.html" style="display: flex; align-items: center; gap: 8px; text-decoration: none; color: #13203a; font-weight: 700; font-size: 15px; white-space: nowrap;">{LOGO2}Local AI Registry</a>
<div class="ask"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#222222" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="M20 20l-4-4"></path></svg><input type="text" value="{{{{q}}}}" placeholder="Search what places are known for" aria-label="Search"><span class="mu" style="font-size: 12px; white-space: nowrap;">Irvine, CA</span></div>
<span style="margin-left: auto; display: flex; align-items: center; gap: 18px;"><a href="Request.dc.html" class="nl">Post a request</a><a href="Business.dc.html" class="nl">For business</a><a href="#" class="nl">Sign in</a></span></div>
<div class="kf"><span style="font-size: 12px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: #8a8a8a; align-self: center; margin-right: 4px;">Known for</span><sc-for list="{{{{chips}}}}" as="c" hint-placeholder-count="10"><span class="kc {{{{c.on}}}}" onClick="{{{{c.pick}}}}">{{{{c.t}}}}</span></sc-for></div>
<div class="body">
<div class="panel"><div class="pad">
<h1 class="srf" style="margin: 0 0 4px; font-size: 32px; line-height: 36px;">{{{{headA}}}} <em>{{{{headB}}}}</em></h1>
<span style="font-size: 13px; line-height: 19px; color: #484848; padding-bottom: 8px;">What each place is actually known for, pulled from thousands of reviews and checked by neighbors.</span>
<sc-for list="{{{{list}}}}" as="b" hint-placeholder-count="8"><a href="Main.dc.html" class="rc {{{{b.on}}}}"><span class="rph" style="background: {{{{b.bg}}}};"></span><span style="display: flex; flex-direction: column; gap: 5px; min-width: 0;"><span style="display: flex; justify-content: space-between; gap: 8px;"><strong style="font-size: 15px;">{{{{b.n}}}}</strong><span style="font-size: 13px; white-space: nowrap;">★ {{{{b.r}}}}</span></span><span class="mu" style="font-size: 12px;">{{{{b.cat}}}} · {{{{b.hood}}}}</span><span style="display: flex; gap: 5px; flex-wrap: wrap;"><sc-for list="{{{{b.tags}}}}" as="t" hint-placeholder-count="3"><span class="tg {{{{t.c}}}}">{{{{t.t}}}}</span></sc-for></span><span style="font-size: 12px; color: #6a6a6a;">{{{{b.why}}}}</span></span></a></sc-for>
</div></div>
<div class="map">
<span class="road" style="left: -5%; right: -5%; top: 30%; height: 12px; transform: rotate(-9deg);"></span><span class="road" style="top: -5%; bottom: -5%; left: 40%; width: 14px; transform: rotate(14deg);"></span><span class="road" style="left: 0; right: 0; top: 66%; height: 8px; transform: rotate(3deg);"></span><span class="road" style="top: 0; bottom: 0; left: 76%; width: 8px;"></span><span class="road" style="top: 0; bottom: 0; left: 18%; width: 6px; transform: rotate(-6deg);"></span>
<span style="position: absolute; left: 46%; top: 40%; width: 120px; height: 80px; border-radius: 16px; background: #d9e6d3;"></span>
<span class="hood" style="left: 44%; top: 56%;">Irvine Spectrum</span><span class="hood" style="left: 10%; top: 14%;">Woodbridge</span><span class="hood" style="left: 64%; top: 10%;">Great Park</span><span class="hood" style="left: 22%; top: 76%;">University Park</span><span class="hood" style="left: 82%; top: 72%;">Quail Hill</span>
<sc-for list="{{{{pins}}}}" as="p" hint-placeholder-count="16"><span class="pin {{{{p.cls}}}}" style="left: {{{{p.x}}}}%; top: {{{{p.y}}}}%;" onClick="{{{{p.pick}}}}">{{{{p.lbl}}}}</span></sc-for>
<div class="pop" style="left: {{{{sel.x}}}}%; top: {{{{sel.y}}}}%; transform: {{{{sel.tf}}}};"><span style="display: flex; justify-content: space-between; gap: 8px;"><strong style="font-size: 16px;">{{{{sel.n}}}}</strong><span style="font-size: 13px;">★ {{{{sel.r}}}}</span></span><span class="mu" style="font-size: 12px;">{{{{sel.cat}}}} · {{{{sel.hood}}}}</span><span style="font-size: 11px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: #8a8a8a; padding-top: 2px;">Known for</span><span style="display: flex; gap: 5px; flex-wrap: wrap;"><sc-for list="{{{{sel.tags}}}}" as="t" hint-placeholder-count="3"><span class="tg {{{{t.c}}}}">{{{{t.t}}}}</span></sc-for></span><span style="font-size: 13px; line-height: 18px; color: #484848;">{{{{sel.why}}}}</span><a href="Main.dc.html" class="btn b-sm b-dark" style="margin-top: 4px;">See the business</a></div>
</div>
</div>'''
JS=r'''    const S = this.state || {};
    const k = S.k || 'all', selI = S.sel;
    const B = [
      ['Lumen Aesthetics', 'Med spa', 'Irvine Spectrum', '4.9', 53, 48, ['Natural lip filler', 'Morpheus8', 'Takes HSA'], '31 reviews say they talked them out of more filler', '#e8d9cf'],
      ['Spectrum Aesthetics MD', 'Med spa', 'Irvine Spectrum', '4.8', 60, 58, ['Doctor-led Botox', 'Natural lip filler'], 'Dr. Chen does every injection herself', '#d9dfe8'],
      ['Backyard Tacos', 'Restaurant', 'University Park', '4.7', 26, 62, ['Birria tacos', 'Kids can run around', 'Dog-friendly patio'], 'Fenced lawn next to the patio, 40 reviews mention the birria', '#e7eed9'],
      ['Capital Seafood', 'Restaurant', 'Irvine Spectrum', '4.5', 58, 42, ['Dim sum', 'Big groups'], 'Carts until 2 PM, round tables for 12', '#efe7d6'],
      ['Kinjiro Ramen', 'Restaurant', 'Irvine Spectrum', '4.6', 49, 64, ['Late-night ramen', 'Solo dining'], 'Counter seats and a kitchen open until 12:45', '#efe7d6'],
      ['Sol Cocina', 'Restaurant', 'Irvine Spectrum', '4.4', 55, 30, ['Bottomless brunch', 'Big groups'], '$22 bottomless mimosas with any entree', '#f0dfd0'],
      ['Blue Door Coffee', 'Cafe', 'Woodbridge', '4.7', 34, 26, ['Quiet place to work', 'Dog-friendly patio'], 'Outlets at the bar, quiet before 11 AM', '#e4e0ef'],
      ['Woodbridge Kids Dental', 'Dentist', 'Woodbridge', '4.9', 16, 22, ['Kids dentist', 'Saturday hours'], 'Only sees children, open Saturday mornings', '#dfe8d9'],
      ['Irvine Auto Care', 'Auto repair', 'Quail Hill', '4.4', 84, 50, ['Tesla repair', 'Honest quotes'], 'Tesla and Rivian certified, 18 reviews say fair prices', '#e8e2d6'],
      ['Great Park Pilates', 'Fitness', 'Great Park', '4.8', 68, 18, ['Beginner friendly', 'Reformer classes'], 'Most reviews are from first-timers', '#e8e2d6'],
      ['Quail Hill Vet', 'Veterinarian', 'Quail Hill', '4.9', 82, 76, ['Emergency visits', 'Honest quotes'], 'Takes same-day emergencies, 22 reviews say no upsell', '#e8e2d6'],
      ['Heritage Hair Studio', 'Hair salon', 'University Park', '4.6', 30, 82, ['Curly hair', 'Balayage'], 'Three stylists trained in curly cuts', '#e8e2d6'],
      ['Sakura Oyster Bar', 'Restaurant', 'Irvine Spectrum', '4.7', 45, 34, ['$1 oysters', 'Date night'], 'Dim lighting, oyster happy hour', '#e8e2d6'],
      ['Glow Bar Irvine', 'Facial spa', 'Great Park', '4.5', 72, 34, ['Quick facials', 'Beginner friendly'], '30-minute facials on lunch breaks', '#f0dfd0'],
      ['Blue Note Lounge', 'Bar', 'Great Park', '4.6', 74, 46, ['Live jazz', 'Date night'], 'Trio on weekends, quiet back tables', '#e8e2d6'],
      ['Pacific Skin Studio', 'Skin care', 'University Park', '4.6', 44, 78, ['Acne facials', 'Takes HSA'], 'Esthetician Maya is named in 26 reviews', '#e8e2d6']
    ];
    const CH = ['Natural lip filler', 'Birria tacos', 'Kids can run around', 'Dim sum', 'Bottomless brunch', 'Late-night ramen', 'Quiet place to work', 'Dog-friendly patio', 'Kids dentist', 'Tesla repair', 'Date night', 'Honest quotes', 'Takes HSA'];
    const hit = b => k === 'all' || b[6].includes(k);
    const chips = [['all', 'Everything']].concat(CH.map(c => [c, c])).map(c => ({ t: c[1], on: k === c[0] ? 'on' : '', pick: () => this.setState({ k: c[0], sel: undefined }) }));
    const tagsOf = b => b[6].map(t => ({ t, c: t === k ? 'hit' : '' }));
    const idx = B.map((b, i) => i).filter(i => hit(B[i]));
    const selIdx = selI !== undefined ? selI : idx[0];
    const list = idx.map(i => ({ n: B[i][0], cat: B[i][1], hood: B[i][2], r: B[i][3], tags: tagsOf(B[i]), why: B[i][7], bg: B[i][8], on: i === selIdx ? 'on' : '' }));
    const pins = B.map((b, i) => ({ x: String(b[4]), y: String(b[5]), lbl: b[0], cls: (hit(b) ? (k === 'all' ? '' : 'hit') : 'dim') + (i === selIdx ? ' sel' : ''), pick: () => this.setState({ sel: i }) }));
    const sb = B[selIdx];
    const sel = { n: sb[0], cat: sb[1], hood: sb[2], r: sb[3], tags: tagsOf(sb), why: sb[7], x: String(sb[4]), y: String(sb[5]), tf: sb[5] < 45 ? 'translate(-50%, 24px)' : 'translate(-50%, calc(-100% - 24px))' };
    return { chips, list, pins, sel, q: k === 'all' ? '' : k, headA: k === 'all' ? 'Known for' : String(idx.length) + ' places known for', headB: k === 'all' ? 'something.' : k.toLowerCase() + '.' };'''
t=HEADX.replace('<title>Lumen Aesthetics on Local AI Registry</title>','<title>Local AI Registry: what places are known for</title>')
out=t+'\n'+CSS+'\n</style>\n</helmet>\n<div style="width: 1440px; height: 960px; box-sizing: border-box; display: flex; flex-direction: column; background: #ffffff; position: relative; overflow: hidden;">\n'+BODY+'\n</div>\n</x-dc>\n<script type="text/x-dc" data-dc-script>\nclass Component extends DCLogic {\n  renderVals() {\n'+JS+'\n  }\n}\n</script>\n</body>\n</html>\n'
open(P+'Explore.dc.html','w').write(out); print('ok')
