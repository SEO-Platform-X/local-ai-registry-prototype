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
.top{height:64px;padding:0 20px;display:flex;align-items:center;gap:16px;border-bottom:1px solid #e6e6e6;background:#ffffff;flex-shrink:0}
.ask{display:flex;align-items:center;gap:10px;height:44px;flex-grow:1;max-width:600px;padding:0 6px 0 16px;border:1px solid #dddddd;border-radius:22px;box-shadow:0 2px 10px rgba(0,0,0,0.06)}
.ask input{flex-grow:1;border:none;outline:none;font-family:inherit;font-size:15px;background:transparent;color:#222222}
.nl{font-size:14px;font-weight:600;color:#222222;text-decoration:none;white-space:nowrap}
.cats{display:flex;gap:6px;padding:10px 20px;border-bottom:1px solid #eeeeee;background:#ffffff;overflow:hidden;flex-shrink:0}
.cat{display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 13px;border:1px solid #dddddd;border-radius:16px;font-size:13px;font-weight:600;cursor:pointer;white-space:nowrap;background:#ffffff}
.cat.on{background:#222222;border-color:#222222;color:#ffffff}
.cat i{width:9px;height:9px;border-radius:50%;display:inline-block}
.body{display:grid;grid-template-columns:420px 1fr;flex-grow:1;min-height:0}
.panel{border-right:1px solid #e6e6e6;overflow-y:auto;background:#ffffff;display:flex;flex-direction:column}
.pad{padding:16px 20px;display:flex;flex-direction:column;gap:10px}
.it{display:grid;grid-template-columns:62px 1fr;gap:12px;padding:12px;border:1px solid #ebebeb;border-radius:12px;cursor:pointer}
.it:hover,.it.on{border-color:#222222}
.it .tm{display:flex;flex-direction:column;align-items:center;justify-content:center;border-radius:10px;font-size:12px;font-weight:700;line-height:15px;text-align:center;padding:6px 2px}
.map{position:relative;overflow:hidden;background:#e9ede6}
.road{position:absolute;background:#ffffff}
.hood{position:absolute;font-size:12px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#8a9885}
.pin{position:absolute;transform:translate(-50%,-50%);display:flex;align-items:center;gap:5px;height:28px;padding:0 10px 0 6px;border-radius:14px;background:#ffffff;font-size:12px;font-weight:700;cursor:pointer;box-shadow:0 2px 6px rgba(0,0,0,0.2);white-space:nowrap;border:2px solid #ffffff}
.pin i{width:14px;height:14px;border-radius:50%;flex-shrink:0}
.pin.sel{z-index:6;border-color:#222222;transform:translate(-50%,-50%) scale(1.12)}
.pin.soon{opacity:0.45}
.pop{position:absolute;width:310px;padding:16px;border-radius:14px;background:#ffffff;box-shadow:0 10px 30px rgba(0,0,0,0.2);display:flex;flex-direction:column;gap:7px;z-index:10}
.tl{position:absolute;left:16px;right:16px;bottom:16px;padding:14px 18px 12px;border-radius:16px;background:rgba(255,255,255,0.97);box-shadow:0 6px 24px rgba(0,0,0,0.16);display:flex;flex-direction:column;gap:10px;z-index:8}
.days{display:flex;gap:6px}
.day{height:30px;padding:0 12px;border-radius:15px;display:inline-flex;align-items:center;font-size:13px;font-weight:600;cursor:pointer;color:#484848;border:1px solid #e3e3e3}
.day.on{background:#13203a;border-color:#13203a;color:#ffffff}
.hist{display:grid;grid-template-columns:repeat(19,minmax(0,1fr));gap:3px;align-items:end;height:54px}
.hb{display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:4px;height:100%;cursor:pointer}
.hb i{display:block;width:100%;border-radius:4px 4px 0 0;background:#d5dbe6}
.hb.on i{background:#ff5a3c}
.hb.now i{background:#9aa9c4}
.hb span{font-size:10px;color:#6a6a6a;white-space:nowrap}
.hb.on span{color:#222222;font-weight:700}
.nowb{position:absolute;top:16px;left:16px;padding:10px 14px;border-radius:12px;background:#13203a;color:#ffffff;z-index:7;display:flex;flex-direction:column;gap:2px}
'''
LOGO2='<svg width="22" height="20" viewBox="0 0 22 20" aria-hidden="true"><path d="M11 1L21 19H1Z" fill="#2d55e6"></path><path d="M11 8L15.5 16H6.5Z" fill="#ffffff"></path></svg>'
BODY=f'''<div class="top"><a href="Explore.dc.html" style="display: flex; align-items: center; gap: 8px; text-decoration: none; color: #13203a; font-weight: 700; font-size: 15px; white-space: nowrap;">{LOGO2}Local AI Registry</a>
<div class="ask"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#222222" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="M20 20l-4-4"></path></svg><input type="text" placeholder="What's on? Try: happy hour with food near the Spectrum" aria-label="Ask"><span class="mu" style="font-size: 12px; white-space: nowrap;">Irvine, CA</span><span class="btn b-coral b-sm" style="border-radius: 18px;">Ask</span></div>
<span style="margin-left: auto; display: flex; align-items: center; gap: 18px;"><a href="Request.dc.html" class="nl">Post a request</a><a href="Business.dc.html" class="nl">For business</a><a href="#" class="nl">Sign in</a></span></div>
<div class="cats"><sc-for list="{{{{cats}}}}" as="c" hint-placeholder-count="9"><span class="cat {{{{c.on}}}}" onClick="{{{{c.pick}}}}"><i style="background: {{{{c.col}}}};"></i>{{{{c.t}}}}<span style="opacity: 0.6; font-weight: 500;">{{{{c.n}}}}</span></span></sc-for></div>
<div class="body">
<div class="panel"><div class="pad">
<h1 class="srf" style="margin: 0; font-size: 34px; line-height: 36px;">{{{{headA}}}} <em>{{{{headB}}}}</em></h1>
<span style="font-size: 13px; line-height: 19px; color: #484848;">Happy hours, brunch, markets, events and deals, checked for today. AI can't keep up with what changes every week. Neighbors and owners can.</span>
<span style="display: flex; justify-content: space-between; align-items: baseline; padding-top: 4px;"><strong style="font-size: 15px;">{{{{onCount}}}} on at {{{{hourLbl}}}}</strong><span class="mu" style="font-size: 12px;">{{{{soonCount}}}} more starting soon</span></span>
<sc-for list="{{{{onList}}}}" as="x" hint-placeholder-count="8"><div class="it {{{{x.on}}}}" onClick="{{{{x.pick}}}}"><span class="tm" style="background: {{{{x.bg}}}}; color: {{{{x.fg}}}};">{{{{x.s}}}}<span style="font-weight: 500; opacity: 0.8;">to {{{{x.e}}}}</span></span><span style="display: flex; flex-direction: column; gap: 3px; min-width: 0;"><span style="display: flex; justify-content: space-between; gap: 8px;"><strong style="font-size: 14px;">{{{{x.t}}}}</strong><span style="font-size: 11px; font-weight: 700; color: {{{{x.col}}}}; white-space: nowrap;">{{{{x.left}}}}</span></span><span style="font-size: 13px; color: #484848;">{{{{x.b}}}} · {{{{x.cat}}}}</span><span style="font-size: 12px; color: #6a6a6a; display: flex; align-items: center;"><span class="mk mk-{{{{x.mk}}}}"></span>{{{{x.src}}}}</span></span></div></sc-for>
<sc-if value="{{{{hasSoon}}}}" hint-placeholder-val="{{{{ true }}}}"><strong style="font-size: 14px; padding-top: 6px;">Starting soon</strong><sc-for list="{{{{soonList}}}}" as="x" hint-placeholder-count="3"><div class="it" onClick="{{{{x.pick}}}}" style="opacity: 0.75;"><span class="tm" style="background: {{{{x.bg}}}}; color: {{{{x.fg}}}};">{{{{x.s}}}}</span><span style="display: flex; flex-direction: column; gap: 2px;"><strong style="font-size: 14px;">{{{{x.t}}}}</strong><span style="font-size: 13px; color: #484848;">{{{{x.b}}}}</span></span></div></sc-for></sc-if>
<div style="padding: 14px 16px; border-radius: 12px; background: #f6f3ee; display: flex; flex-direction: column; gap: 6px; margin-top: 6px;"><strong style="font-size: 14px;">See something that is not here?</strong><span style="font-size: 13px; line-height: 19px; color: #484848;">A pop-up, a new happy hour, a trivia night. Add it, and say how you know. It shows with a hollow circle until someone confirms it.</span><span class="btn b-sm b-dark" style="align-self: flex-start;">+ Add what's on</span></div>
</div></div>
<div class="map">
<span class="road" style="left: -5%; right: -5%; top: 30%; height: 12px; transform: rotate(-9deg);"></span><span class="road" style="top: -5%; bottom: -5%; left: 40%; width: 14px; transform: rotate(14deg);"></span><span class="road" style="left: 0; right: 0; top: 62%; height: 8px; transform: rotate(3deg);"></span><span class="road" style="top: 0; bottom: 0; left: 76%; width: 8px;"></span><span class="road" style="top: 0; bottom: 0; left: 18%; width: 6px; transform: rotate(-6deg);"></span>
<span style="position: absolute; left: 46%; top: 38%; width: 120px; height: 80px; border-radius: 16px; background: #d9e6d3;"></span>
<span class="hood" style="left: 44%; top: 52%;">Irvine Spectrum</span><span class="hood" style="left: 10%; top: 14%;">Woodbridge</span><span class="hood" style="left: 64%; top: 10%;">Great Park</span><span class="hood" style="left: 22%; top: 66%;">University Park</span><span class="hood" style="left: 82%; top: 62%;">Quail Hill</span>
<span class="nowb"><span style="font-size: 11px; font-weight: 700; letter-spacing: 0.08em; color: #aab4c8;">{{{{dayLbl}}}}, {{{{hourLbl}}}}</span><span style="font-size: 15px; font-weight: 600;">{{{{onCount}}}} things on nearby</span></span>
<sc-for list="{{{{pins}}}}" as="p" hint-placeholder-count="12"><span class="pin {{{{p.cls}}}}" style="left: {{{{p.x}}}}%; top: {{{{p.y}}}}%;" onClick="{{{{p.pick}}}}"><i style="background: {{{{p.col}}}};"></i>{{{{p.lbl}}}}</span></sc-for>
<sc-if value="{{{{hasSel}}}}" hint-placeholder-val="{{{{ true }}}}"><div class="pop" style="left: {{{{sel.x}}}}%; top: {{{{sel.y}}}}%; transform: {{{{sel.tf}}}};"><span style="display: flex; align-items: center; gap: 8px; font-size: 11px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: {{{{sel.col}}}};"><i style="width: 9px; height: 9px; border-radius: 50%; background: {{{{sel.col}}}}; display: inline-block;"></i>{{{{sel.cat}}}} · {{{{sel.s}}}} to {{{{sel.e}}}}</span><strong style="font-size: 16px;">{{{{sel.t}}}}</strong><span style="font-size: 13px; color: #484848;">{{{{sel.b}}}}</span><span style="font-size: 13px; line-height: 19px;">{{{{sel.d}}}}</span><span style="font-size: 12px; color: #6a6a6a; display: flex; align-items: center;"><span class="mk mk-{{{{sel.mk}}}}"></span>{{{{sel.src}}}}</span><sc-if value="{{{{sel.hasAi}}}}" hint-placeholder-val="{{{{ false }}}}"><span style="font-size: 12px; color: #c13515; padding: 6px 8px; border-radius: 8px; background: #fbe9e7;">{{{{sel.ai}}}}</span></sc-if><span style="display: flex; gap: 8px; margin-top: 4px;"><a href="Main.dc.html" class="btn b-sm b-dark">See the business</a><span class="btn b-sm">Save</span></span></div></sc-if>
<div class="tl"><div style="display: flex; align-items: center; justify-content: space-between; gap: 12px;"><span class="days"><sc-for list="{{{{days}}}}" as="d" hint-placeholder-count="7"><span class="day {{{{d.on}}}}" onClick="{{{{d.pick}}}}">{{{{d.t}}}}</span></sc-for></span><span class="mu" style="font-size: 12px;">Bars show how much is on each hour. Tap an hour.</span></div>
<div class="hist"><sc-for list="{{{{hours}}}}" as="h" hint-placeholder-count="19"><span class="hb {{{{h.cls}}}}" onClick="{{{{h.pick}}}}"><i style="height: {{{{h.px}}}}px;"></i><span>{{{{h.l}}}}</span></span></sc-for></div></div>
</div>
</div>'''
JS=r'''    const S = this.state || {};
    const day = S.day === undefined ? 0 : S.day, hr = S.hr === undefined ? 17 : S.hr, cat = S.cat || 'all', selK = S.sel;
    const C = { hh: ['Happy hour', '#e8a000', '#fff4d6', '#7a5200'], br: ['Brunch', '#e0457b', '#fde6ee', '#8a1f45'], ev: ['Event', '#7b4fd6', '#efe8fd', '#4a2a91'], mk: ['Market', '#2f9e44', '#e3f4e6', '#1c5f2a'], mu: ['Live music', '#1d6fd6', '#e3eefc', '#134a91'], kd: ['Kids', '#0f9d8f', '#dff4f1', '#0b5f57'], dl: ['Deal', '#c13515', '#fbe9e7', '#8a2410'], nw: ['New and pop-up', '#222222', '#eeeeee', '#222222'], lt: ['Open late', '#3d4a66', '#e6e9f0', '#26304a'] };
    const I = [
      [0, 9, 13, 'mk', 'Irvine Farmers Market', 'Mariners Church lot', 38, 22, 'About 60 stands. Strawberries from Harry\'s Berries sell out by 11.', 'site', 'Confirmed by the market, checked this morning', ''],
      [0, 9, 14, 'br', 'Bottomless mimosa brunch', 'Sol Cocina', 55, 34, '$22 bottomless with any entree. 90-minute limit on weekends.', 'vis', 'Carmen V. was there last Saturday', 'ChatGPT says $18. It went up in August.'],
      [0, 10, 14, 'br', 'Dim sum brunch', 'Capital Seafood', 60, 44, 'Carts until 2. Expect a 30-minute wait after 11.', 'site', 'Confirmed by the owner this week', ''],
      [0, 10, 12, 'kd', 'Storytime and craft hour', 'Irvine Spectrum Barnes and Noble', 49, 40, 'Free, ages 2 to 6. Fills up by 10:15.', 'site', 'From their events calendar', ''],
      [0, 11, 16, 'ev', 'Oktoberfest on the Plaza', 'Irvine Spectrum Center', 51, 46, 'Live polka, $12 steins, kids zone with a bounce house.', 'site', 'Confirmed by the organizer', ''],
      [0, 12, 18, 'nw', 'Birria pop-up', 'Blue Door Coffee parking lot', 42, 60, 'Birria Boyz, until they sell out, usually around 4.', 'vis', 'Diego R. spotted it 40 minutes ago', 'No AI engine knows about this.'],
      [0, 15, 19, 'hh', 'Happy hour: $6 drafts, half-off apps', 'Backyard Tacos', 26, 58, 'Bar and patio only. Fenced lawn for kids next to the patio.', 'site', 'Confirmed by the owner, checked today', 'ChatGPT says 5 to 7. It is 3 to 7 on weekends.'],
      [0, 16, 18, 'hh', 'Happy hour: $1 oysters', 'Sakura Ramen and Oyster Bar', 47, 28, 'Until 6 or until they run out.', 'vis', 'Linh T. was there yesterday', ''],
      [0, 16, 19, 'hh', 'Happy hour: $9 cocktails', 'The Pointe Rooftop', 65, 38, 'Rooftop fills by 5:30 on Saturdays. Arrive early for the sunset side.', 'ai', 'From their Instagram. Nobody has confirmed today', ''],
      [0, 17, 21, 'dl', 'Kids eat free with an adult entree', 'Heritage Pizza Co.', 20, 36, 'One kids meal per adult. Dine in only.', 'site', 'Confirmed by the owner', ''],
      [0, 18, 22, 'mu', 'Live jazz trio', 'Blue Note Lounge', 72, 48, 'No cover before 8. Quiet enough to talk at the back tables.', 'vis', 'Tom H. went last Saturday', ''],
      [0, 19, 21, 'ev', 'Trivia night', 'Great Park Brewing', 70, 18, 'Teams up to 6. Free. Winners get a $50 tab.', 'site', 'Confirmed by the brewery', ''],
      [0, 20, 23, 'ev', 'Outdoor movie: Coco', 'Great Park lawn', 76, 14, 'Free. Bring a blanket. Food trucks from 7.', 'site', 'From the City of Irvine calendar', ''],
      [0, 21, 25, 'lt', 'Open late: ramen until 1 AM', 'Kinjiro Ramen', 58, 56, 'Kitchen stays open until 12:45 on Fridays and Saturdays.', 'vis', 'Aisha M. ate there at midnight', 'Google says it closes at 10.'],
      [0, 22, 25, 'mu', 'DJ night', 'Spectrum Social', 53, 52, '$10 cover after 10. 21 and up.', 'ai', 'From their Instagram. Not confirmed', ''],
      [1, 8, 13, 'mk', 'Tustin Sunday Market', 'Old Town Tustin', 12, 54, 'Smaller, with a great tamale stand at the far end.', 'site', 'Confirmed by the market', ''],
      [1, 10, 15, 'br', 'Jazz brunch', 'Sol Cocina', 55, 34, 'Live trio from 11. Reservations recommended.', 'site', 'Confirmed by the owner', ''],
      [1, 11, 15, 'kd', 'Kids clinic: learn to skate', 'Great Park Ice', 68, 22, 'Ages 4 to 10, $15 with rentals.', 'site', 'From their schedule', ''],
      [1, 15, 18, 'hh', 'Sunday happy hour all afternoon', 'Great Park Brewing', 70, 18, '$5 pints until 6.', 'vis', 'Two neighbors confirmed last week', ''],
      [1, 17, 20, 'dl', 'Sunday supper: family meal for 4, $49', 'Heritage Pizza Co.', 20, 36, 'Pizza, salad and dessert. Takeout too.', 'site', 'Confirmed by the owner', ''],
      [2, 16, 19, 'hh', 'Monday happy hour', 'Backyard Tacos', 26, 58, '$2 tacos, $6 drafts.', 'site', 'Confirmed by the owner', ''],
      [2, 19, 21, 'ev', 'Board game night', 'Blue Door Coffee', 42, 60, 'Free. Bring a game or borrow one.', 'vis', 'Linh T. goes every week', '']
    ];
    const DAYS = ['Today, Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri'];
    const fmt = h => { const x = h % 24; return x === 0 ? '12 AM' : x === 12 ? '12 PM' : x > 12 ? (x - 12) + ' PM' : x + ' AM'; };
    const items = I.map((x, k) => ({ k, day: x[0], s0: x[1], e0: x[2], c: x[3], t: x[4], b: x[5], x: x[6], y: x[7], d: x[8], mk: x[9], src: x[10], ai: x[11] }));
    const inCat = it => cat === 'all' || it.c === cat;
    const onNow = items.filter(it => it.day === day && it.s0 <= hr && it.e0 > hr && inCat(it));
    const soon = items.filter(it => it.day === day && it.s0 > hr && it.s0 <= hr + 2 && inCat(it));
    const dec = it => { const c = C[it.c]; const left = it.e0 - hr; return { t: it.t, b: it.b, cat: c[0], col: c[1], bg: c[2], fg: c[3], s: fmt(it.s0), e: fmt(it.e0), mk: it.mk, src: it.src, left: left <= 1 ? 'Ends within the hour' : 'Ends in ' + left + ' hours', on: it.k === selK ? 'on' : '', pick: () => this.setState({ sel: it.k }) }; };
    const onList = onNow.map(dec), soonList = soon.map(dec);
    const shown = onNow.concat(soon);
    const pins = shown.map(it => ({ x: String(it.x), y: String(it.y), col: C[it.c][1], lbl: it.b.split(' ').slice(0, 2).join(' ') + ' · ' + fmt(it.e0), cls: (it.k === selK ? 'sel ' : '') + (it.s0 > hr ? 'soon' : ''), pick: () => this.setState({ sel: it.k }) }));
    const selIt = items.find(it => it.k === selK && shown.includes(it)) || onNow[0] || shown[0];
    const hasSel = !!selIt;
    const sel = selIt ? { t: selIt.t, b: selIt.b, cat: C[selIt.c][0], col: C[selIt.c][1], s: fmt(selIt.s0), e: fmt(selIt.e0), d: selIt.d, mk: selIt.mk, src: selIt.src, ai: selIt.ai, hasAi: !!selIt.ai, x: String(selIt.x), y: String(selIt.y), tf: selIt.y < 45 ? 'translate(-50%, 24px)' : 'translate(-50%, calc(-100% - 24px))' } : {};
    const hours = Array.from({ length: 19 }, (_, i) => { const h = 7 + i; const n = items.filter(it => it.day === day && it.s0 <= h && it.e0 > h && inCat(it)).length; return { l: i % 2 === 0 ? fmt(h).replace(' ', '').replace('AM', 'a').replace('PM', 'p') : '', px: String(4 + n * 9), cls: h === hr ? 'on' : '', pick: () => this.setState({ hr: h, sel: undefined }) }; });
    const days = DAYS.map((t, i) => ({ t, on: i === day ? 'on' : '', pick: () => this.setState({ day: i, sel: undefined }) }));
    const cats = [['all', 'Everything', '#222222']].concat(Object.keys(C).map(k => [k, C[k][0], C[k][1]])).map(c => ({ t: c[1], col: c[2], n: String(items.filter(it => it.day === day && (c[0] === 'all' || it.c === c[0])).length), on: cat === c[0] ? 'on' : '', pick: () => this.setState({ cat: c[0], sel: undefined }) }));
    const isNow = day === 0 && hr === 17;
    return { cats, days, hours, pins, sel, hasSel, onList, soonList, hasSoon: soonList.length > 0, onCount: String(onNow.length), soonCount: String(soon.length), hourLbl: fmt(hr), dayLbl: DAYS[day], headA: isNow ? "What's on" : "What's on", headB: isNow ? 'right now.' : (day === 0 ? 'today at ' + fmt(hr) + '.' : DAYS[day] + ' at ' + fmt(hr) + '.') };'''
t=HEADX.replace('<title>Lumen Aesthetics on Local AI Registry</title>',"<title>Local AI Registry: what's on near you</title>")
out=t+'\n'+CSS+'\n</style>\n</helmet>\n<div style="width: 1440px; height: 960px; box-sizing: border-box; display: flex; flex-direction: column; background: #ffffff; position: relative; overflow: hidden;">\n'+BODY+'\n</div>\n</x-dc>\n<script type="text/x-dc" data-dc-script>\nclass Component extends DCLogic {\n  renderVals() {\n'+JS+'\n  }\n}\n</script>\n</body>\n</html>\n'
open(P+'Explore.dc.html','w').write(out); print('ok')
