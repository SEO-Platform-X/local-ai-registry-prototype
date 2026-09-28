import sys; sys.path.insert(0,'/tmp/gen'); from common import *
TRI="url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='22' height='22' viewBox='0 0 22 22'%3E%3Cpath d='M11 3.5L19.5 18.5H2.5Z' fill='none' stroke='%238a8a8a' stroke-width='2.4' stroke-linejoin='round'/%3E%3C/svg%3E\") center / 100% 100% no-repeat"
HEADX=HEAD.replace('family=Figtree:wght@400;500;600;700;800&amp;display=swap','family=Figtree:wght@400;500;600;700;800&amp;family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&amp;display=swap')
CSS=r'''.srf{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;letter-spacing:-0.01em;color:#13203a}
.srf em{font-style:italic;color:#ff5a3c}
.mk{position:relative;display:inline-block;width:11px;height:11px;margin:0 5px 1px 0;vertical-align:middle;flex-shrink:0}
.mk::after{content:"";position:absolute;inset:0}
.mk-site::after{inset:2px;background:#008a05;border-radius:50%}
.mk-vis::after{inset:2px;border:1.6px solid #e8740c;border-radius:50%}
.mk-ai::after{inset:0;background:'''+TRI+'''}
.mk-none{display:none}
.top{height:64px;padding:0 20px;display:flex;align-items:center;gap:16px;border-bottom:1px solid #e6e6e6;background:#ffffff;flex-shrink:0}
.ask{display:flex;align-items:center;gap:10px;height:44px;flex-grow:1;max-width:560px;padding:0 16px;border:1px solid #dddddd;border-radius:22px;box-shadow:0 2px 10px rgba(0,0,0,0.06)}
.ask input{flex-grow:1;border:none;outline:none;font-family:inherit;font-size:15px;background:transparent;color:#222222}
.nl{font-size:14px;font-weight:600;color:#222222;text-decoration:none;white-space:nowrap}
.row1{display:flex;align-items:center;gap:14px;padding:12px 20px;border-bottom:1px solid #f0f0f0;background:#ffffff;flex-shrink:0}
.seg{display:inline-flex;padding:3px;border-radius:18px;background:#f3f3f3}
.seg span{height:30px;padding:0 14px;border-radius:15px;display:inline-flex;align-items:center;font-size:13px;font-weight:600;color:#6a6a6a;cursor:pointer}
.seg span.on{background:#ffffff;color:#222222;box-shadow:0 1px 3px rgba(0,0,0,0.12)}
.itm{display:inline-flex;align-items:center;height:36px;padding:0 16px;border:1px solid #dddddd;border-radius:18px;font-size:14px;font-weight:600;cursor:pointer;white-space:nowrap;background:#ffffff}
.itm.on{background:#222222;border-color:#222222;color:#ffffff}
.row2{display:flex;align-items:center;gap:8px;padding:10px 20px;border-bottom:1px solid #e6e6e6;background:#ffffff;flex-shrink:0}
.flt{display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 12px;border:1px solid #dddddd;border-radius:8px;font-size:13px;cursor:pointer;white-space:nowrap;background:#ffffff}
.flt .bx{width:14px;height:14px;border-radius:4px;border:1.5px solid #b0b0b0;box-sizing:border-box;display:inline-flex;align-items:center;justify-content:center}
.flt.on{border-color:#222222;background:#f7f7f7;font-weight:600}
.flt.on .bx{background:#222222;border-color:#222222}
.flt.on .bx::after{content:"";width:6px;height:3px;border-left:2px solid #ffffff;border-bottom:2px solid #ffffff;transform:rotate(-45deg) translate(1px,-1px)}
.flt.sp{border-style:dashed}
.dv{width:1px;height:22px;background:#e3e3e3;margin:0 4px}
.sort{margin-left:auto;display:inline-flex;align-items:center;gap:4px;font-size:13px;color:#6a6a6a}
.sort span{padding:5px 9px;border-radius:6px;cursor:pointer;font-weight:600}
.sort span.on{background:#222222;color:#ffffff}
.body{display:grid;grid-template-columns:460px 1fr;flex-grow:1;min-height:0}
.panel{border-right:1px solid #e6e6e6;overflow-y:auto;background:#ffffff}
.pad{padding:18px 20px 24px;display:flex;flex-direction:column;gap:10px}
.pst{position:relative;height:34px;margin:4px 6px 0}
.pst .ln{position:absolute;left:0;right:0;top:9px;height:4px;border-radius:2px;background:#ececec}
.pst .pd{position:absolute;top:4px;width:14px;height:14px;border-radius:50%;background:#222222;border:2px solid #ffffff;transform:translateX(-50%);box-sizing:border-box;box-shadow:0 1px 3px rgba(0,0,0,0.3);cursor:pointer}
.pst .pd.sel{background:#ff5a3c;width:18px;height:18px;top:2px}
.pst .lo,.pst .hi{position:absolute;top:22px;font-size:11px;font-weight:600;color:#6a6a6a}
.pst .hi{right:0}
.rc{display:grid;grid-template-columns:28px 1fr auto;gap:12px;padding:14px 12px;border-radius:12px;border:1px solid transparent;cursor:pointer;align-items:start}
.rc:hover{background:#fafafa}
.rc.on{border-color:#222222;background:#ffffff}
.rk{width:26px;height:26px;border-radius:50%;background:#f3f3f3;font-size:12px;font-weight:700;display:flex;align-items:center;justify-content:center}
.rc.on .rk{background:#ff5a3c;color:#ffffff}
.pr{text-align:right;display:flex;flex-direction:column;align-items:flex-end;gap:2px}
.pr b{font-size:20px;line-height:22px;display:flex;align-items:center}
.pr .un{font-size:11px;color:#8a8a8a}
.pr .ask2{font-size:13px;font-weight:600;color:#8a8a8a;padding:3px 8px;border-radius:6px;background:#f3f3f3}
.tg{display:inline-flex;align-items:center;height:20px;padding:0 7px;border-radius:10px;background:#f3f3f3;font-size:11px;font-weight:600;color:#484848}
.love{font-size:12px;font-weight:600;color:#c2410c}
.map{position:relative;overflow:hidden;background:#e9ede6}
.road{position:absolute;background:#ffffff}
.hood{position:absolute;font-size:12px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#8a9885}
.pin{position:absolute;transform:translate(-50%,-50%);display:flex;align-items:center;height:30px;padding:0 12px;border-radius:15px;background:#ffffff;font-size:13px;font-weight:700;cursor:pointer;box-shadow:0 2px 8px rgba(0,0,0,0.22);white-space:nowrap;color:#222222}
.pin.np{background:#f3f3f3;color:#8a8a8a;box-shadow:0 1px 4px rgba(0,0,0,0.15)}
.pin.sel{background:#222222;color:#ffffff;z-index:6;transform:translate(-50%,-50%) scale(1.12)}
.pop{position:absolute;width:300px;padding:16px;border-radius:14px;background:#ffffff;box-shadow:0 10px 30px rgba(0,0,0,0.2);display:flex;flex-direction:column;gap:7px;z-index:10}
.empty{padding:18px;border-radius:12px;background:#f7f7f7;font-size:13px;line-height:19px;color:#484848}
'''
LOGO2='<svg width="22" height="20" viewBox="0 0 22 20" aria-hidden="true"><path d="M11 1L21 19H1Z" fill="#2d55e6"></path><path d="M11 8L15.5 16H6.5Z" fill="#ffffff"></path></svg>'
MKX=lambda o:'<span class="mk mk-{{'+o+'.mk}}" title="{{'+o+'.ml}}"></span>'
BODY=f'''<div class="top"><a href="Explore.dc.html" style="display: flex; align-items: center; gap: 8px; text-decoration: none; color: #13203a; font-weight: 700; font-size: 15px; white-space: nowrap;">{LOGO2}Local AI Registry</a>
<div class="ask"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#222222" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="M20 20l-4-4"></path></svg><input type="text" value="{{{{it.name}}}}" placeholder="Search a dish, a treatment or a service" aria-label="Search"><span class="mu" style="font-size: 12px; white-space: nowrap;">Irvine, CA</span></div>
<span style="margin-left: auto; display: flex; align-items: center; gap: 18px;"><a href="Request.dc.html" class="nl">Post a request</a><a href="Business.dc.html" class="nl">For business</a><a href="#" class="nl">Sign in</a></span></div>
<div class="row1"><span class="seg"><sc-for list="{{{{groups}}}}" as="g" hint-placeholder-count="3"><span class="{{{{g.on}}}}" onClick="{{{{g.pick}}}}">{{{{g.t}}}}</span></sc-for></span><sc-for list="{{{{items}}}}" as="x" hint-placeholder-count="3"><span class="itm {{{{x.on}}}}" onClick="{{{{x.pick}}}}">{{{{x.t}}}}</span></sc-for><span class="mu" style="font-size: 12px; margin-left: auto;">Every price shows who confirmed it</span></div>
<div class="row2"><sc-for list="{{{{fCommon}}}}" as="f" hint-placeholder-count="4"><span class="flt {{{{f.on}}}}" onClick="{{{{f.pick}}}}"><span class="bx"></span>{{{{f.t}}}}</span></sc-for><span class="dv"></span><sc-for list="{{{{fItem}}}}" as="f" hint-placeholder-count="3"><span class="flt sp {{{{f.on}}}}" onClick="{{{{f.pick}}}}"><span class="bx"></span>{{{{f.t}}}}</span></sc-for><span class="sort">Sort<sc-for list="{{{{sorts}}}}" as="s" hint-placeholder-count="3"><span class="{{{{s.on}}}}" onClick="{{{{s.pick}}}}">{{{{s.t}}}}</span></sc-for></span></div>
<div class="body">
<div class="panel"><div class="pad">
<h1 class="srf" style="margin: 0; font-size: 34px; line-height: 38px;">{{{{it.name}}}} <em>in Irvine</em></h1>
<span style="font-size: 14px; color: #484848;"><strong style="color: #222222;">{{{{nShown}}}} places</strong> · {{{{rangeLbl}}}} {{{{it.unit}}}}<span style="color: #c13515; font-weight: 600;">{{{{noPriceLbl}}}}</span></span>
<sc-if value="{{{{hasPrices}}}}" hint-placeholder-val="{{{{ true }}}}"><div class="pst"><span class="ln"></span><sc-for list="{{{{dots}}}}" as="d" hint-placeholder-count="5"><span class="pd {{{{d.cls}}}}" style="left: {{{{d.x}}}}%;" onClick="{{{{d.pick}}}}" title="{{{{d.t}}}}"></span></sc-for><span class="lo">{{{{lo}}}}</span><span class="hi">{{{{hi}}}}</span></div></sc-if>
<div style="display: flex; flex-direction: column; gap: 2px; padding-top: 8px;"><sc-for list="{{{{list}}}}" as="r" hint-placeholder-count="6"><div class="rc {{{{r.on}}}}" onClick="{{{{r.pick}}}}"><span class="rk">{{{{r.i}}}}</span><span style="display: flex; flex-direction: column; gap: 4px; min-width: 0;"><strong style="font-size: 15px;">{{{{r.n}}}}</strong><span class="mu" style="font-size: 12px;">★ {{{{r.r}}}} · {{{{r.dist}}}} mi · {{{{r.open}}}}</span><span class="love">{{{{r.love}}}}</span><span style="font-size: 13px; line-height: 18px; color: #484848;">{{{{r.blurb}}}}</span><span style="display: flex; gap: 5px; flex-wrap: wrap;"><sc-for list="{{{{r.tags}}}}" as="t" hint-placeholder-count="2"><span class="tg">{{{{t}}}}</span></sc-for></span></span><span class="pr"><sc-if value="{{{{r.hasP}}}}" hint-placeholder-val="{{{{ true }}}}"><b>{MKX('r')}{{{{r.p}}}}</b><span class="un">{{{{r.src}}}}</span></sc-if><sc-if value="{{{{r.noP}}}}" hint-placeholder-val="{{{{ false }}}}"><span class="ask2">No price listed</span></sc-if></span></div></sc-for></div>
<sc-if value="{{{{isEmpty}}}}" hint-placeholder-val="{{{{ false }}}}"><div class="empty">Nothing matches every filter. Turn one off, or <a href="Request.dc.html" style="font-weight: 600;">post a request</a> and let places come to you.</div></sc-if>
<div class="empty" style="margin-top: 6px;"><strong>Know a price?</strong> Add what you paid and when. It shows with a hollow circle until someone else or the business confirms it.</div>
</div></div>
<div class="map">
<span class="road" style="left: -5%; right: -5%; top: 30%; height: 12px; transform: rotate(-9deg);"></span><span class="road" style="top: -5%; bottom: -5%; left: 40%; width: 14px; transform: rotate(14deg);"></span><span class="road" style="left: 0; right: 0; top: 66%; height: 8px; transform: rotate(3deg);"></span><span class="road" style="top: 0; bottom: 0; left: 76%; width: 8px;"></span><span class="road" style="top: 0; bottom: 0; left: 18%; width: 6px; transform: rotate(-6deg);"></span>
<span style="position: absolute; left: 46%; top: 40%; width: 120px; height: 80px; border-radius: 16px; background: #d9e6d3;"></span>
<span class="hood" style="left: 44%; top: 56%;">Irvine Spectrum</span><span class="hood" style="left: 10%; top: 14%;">Woodbridge</span><span class="hood" style="left: 64%; top: 10%;">Great Park</span><span class="hood" style="left: 22%; top: 84%;">University Park</span><span class="hood" style="left: 82%; top: 80%;">Quail Hill</span>
<sc-for list="{{{{pins}}}}" as="p" hint-placeholder-count="6"><span class="pin {{{{p.cls}}}}" style="left: {{{{p.x}}}}%; top: {{{{p.y}}}}%;" onClick="{{{{p.pick}}}}">{{{{p.lbl}}}}</span></sc-for>
<sc-if value="{{{{hasSel}}}}" hint-placeholder-val="{{{{ true }}}}"><div class="pop" style="left: {{{{sel.x}}}}%; top: {{{{sel.y}}}}%; transform: {{{{sel.tf}}}};"><span style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px;"><strong style="font-size: 16px;">{{{{sel.n}}}}</strong><span style="font-size: 18px; font-weight: 700; display: flex; align-items: center;">{MKX('sel')}{{{{sel.p}}}}</span></span><span class="mu" style="font-size: 12px;">{{{{it.name}}}} · {{{{sel.unit}}}} · ★ {{{{sel.r}}}}</span><span class="love">{{{{sel.love}}}}</span><span style="font-size: 13px; line-height: 18px; color: #484848;">{{{{sel.blurb}}}}</span><span class="mu" style="font-size: 11px;">{{{{sel.src}}}}</span><a href="Main.dc.html" class="btn b-sm b-dark" style="margin-top: 4px;">See it on their page</a></div></sc-if>
</div>
</div>'''
JS=r'''    const S = this.state || {};
    const G = { eat: 'Eat and drink', beauty: 'Beauty', car: 'Car' };
    const IT = {
      birria: { name: 'Birria tacos', g: 'eat', unit: 'each', pre: '$', dec: 2, f: [['consomme', 'Comes with consommé'], ['queso', 'Has quesabirria']], P: [
        ['Backyard Tacos', 26, 62, 4, 'site', 40, '4.7', '1.0', true, ['consomme', 'queso'], 'Crispy edges. Consommé comes with every order.', 'Confirmed on their menu'],
        ['Tacos El Guero', 38, 74, 3.5, 'vis', 22, '4.6', '1.8', true, ['consomme'], 'A cash-only truck. The line moves fast.', 'A visitor paid this, Sep 19'],
        ['La Birrieria OC', 62, 70, 4.5, 'site', 31, '4.5', '2.2', false, ['consomme', 'queso'], 'Birria ramen on weekends too.', 'Confirmed on their menu'],
        ['Taqueria Tlaquepaque', 18, 40, 3.25, 'ai', 9, '4.3', '2.9', true, [], 'Cheapest, but the price is from an old menu photo.', 'AI guess from a 2025 menu photo'],
        ['Sol Cocina', 55, 30, 6, 'site', 6, '4.4', '0.8', true, ['queso'], 'Sit-down and pricier. Big plates.', 'Confirmed on their menu']] },
      ramen: { name: 'Ramen', g: 'eat', unit: 'a bowl', pre: '$', dec: 0, f: [['late', 'Open late'], ['solo', 'Counter seats'], ['vegan', 'Vegan broth']], P: [
        ['Kinjiro Ramen', 49, 64, 16, 'site', 58, '4.6', '0.5', true, ['late', 'solo'], 'Rich tonkotsu. Kitchen open until 12:45.', 'Confirmed on their menu'],
        ['Ramen Nagi', 58, 46, 18, 'site', 72, '4.7', '0.3', false, ['solo'], 'Build your own bowl. Expect a line at noon.', 'Confirmed on their menu'],
        ['Santouka', 44, 36, 17, 'vis', 40, '4.5', '0.9', true, ['solo'], 'Known for the shio. Inside the Mitsuwa food court.', 'A visitor paid this, Sep 14'],
        ['Tatsu Ramen', 70, 56, 15, 'ai', 12, '4.2', '1.6', true, ['vegan', 'late'], 'The only vegan broth nearby.', 'AI guess from a delivery app']] },
      botox: { name: 'Botox', g: 'beauty', unit: 'a unit', pre: '$', dec: 0, f: [['md', 'Doctor or nurse injects'], ['hsa', 'Takes HSA']], P: [
        ['Lumen Aesthetics', 53, 48, 12, 'site', 44, '4.9', '0.2', true, ['md', 'hsa'], 'Dr. Nair or a nurse injects. HSA cards accepted.', 'Confirmed on their price list'],
        ['Spectrum Aesthetics MD', 60, 58, 14, 'site', 38, '4.8', '0.6', true, ['md'], 'Dr. Chen injects every patient herself.', 'Confirmed on their price list'],
        ['Glow Bar Irvine', 72, 34, 10, 'ai', 11, '4.5', '1.4', true, ['hsa'], 'Lowest price, from an Instagram story.', 'AI guess from an Instagram story'],
        ['Irvine Face Lab', 30, 30, 11, 'vis', 19, '4.6', '1.7', true, ['md'], 'A nurse practitioner does the injections.', 'A visitor paid this in August'],
        ['Pacific Skin Studio', 44, 78, null, 'none', 6, '4.6', '1.9', false, [], 'Offers Botox. Price not listed anywhere.', ''],
        ['Coastline Med Spa', 80, 66, null, 'none', 14, '4.4', '2.6', true, ['hsa'], 'Price only on a phone call.', '']] },
      lips: { name: 'Lip filler', g: 'beauty', unit: 'a syringe', pre: '$', dec: 0, f: [['half', 'Half syringes'], ['md', 'Doctor or nurse injects'], ['hsa', 'Takes HSA']], P: [
        ['Lumen Aesthetics', 53, 48, 650, 'site', 31, '4.9', '0.2', true, ['half', 'md', 'hsa'], '31 reviews say they talked them out of more.', 'Confirmed on their price list'],
        ['Spectrum Aesthetics MD', 60, 58, 750, 'site', 22, '4.8', '0.6', true, ['md'], 'Doctor-only injections.', 'Confirmed on their price list'],
        ['Irvine Face Lab', 30, 30, 600, 'vis', 12, '4.6', '1.7', true, ['half', 'md'], 'Half syringes for first-timers.', 'A visitor paid this in July'],
        ['Coastline Med Spa', 80, 66, 699, 'ai', 9, '4.4', '2.6', true, ['half'], 'Price from an old promo page.', 'AI guess from a 2025 promo page'],
        ['Glow Bar Irvine', 72, 34, null, 'none', 4, '4.5', '1.4', true, [], 'Offers lip filler. No price anywhere.', '']] },
      oil: { name: 'Synthetic oil change', g: 'car', unit: '', pre: '$', dec: 0, f: [['walkin', 'Walk-ins'], ['fast', 'Under 30 minutes'], ['ev', 'Works on EVs']], P: [
        ['Spectrum Tire and Auto', 58, 24, 85, 'site', 12, '4.7', '0.9', true, ['fast'], 'Done in about 25 minutes, with a free tire rotation.', 'Confirmed on their website'],
        ['Irvine Auto Care', 84, 50, 79, 'site', 18, '4.4', '2.3', true, ['walkin', 'ev'], 'Also services Teslas and Rivians.', 'Confirmed by the owner'],
        ['Valvoline Culver', 66, 76, 74, 'vis', 25, '4.2', '1.8', true, ['fast', 'walkin'], 'Stay in your car. Watch for upsells.', 'A visitor paid this, Sep 20'],
        ['Jiffy Lube Walnut', 36, 56, 69, 'ai', 30, '3.9', '1.1', true, ['walkin', 'fast'], 'Cheapest listed, but coupons vary.', 'AI guess from a coupon site'],
        ['Woodbridge Garage', 16, 24, null, 'none', 8, '4.8', '3.0', false, ['walkin'], 'Loved by locals. Call for a price.', '']] }
    };
    const ML = { site: 'Confirmed', vis: 'Visitor submitted', ai: 'AI guess', none: '' };
    const itemK = S.item || 'botox', it = IT[itemK], grp = S.grp || it.g;
    const fc = S.fc || {}, fi = S.fi || {}, sort = S.sort || 'love';
    const groups = Object.keys(G).map(g => ({ t: G[g], on: g === grp ? 'on' : '', pick: () => { const first = Object.keys(IT).find(k => IT[k].g === g); this.setState({ grp: g, item: first, fi: {}, sel: undefined }); } }));
    const items = Object.keys(IT).filter(k => IT[k].g === grp).map(k => ({ t: IT[k].name, on: k === itemK ? 'on' : '', pick: () => this.setState({ item: k, fi: {}, sel: undefined }) }));
    const tog = (key, o, name) => () => { const n = Object.assign({}, o); n[name] = !n[name]; const st = {}; st[key] = n; st.sel = undefined; this.setState(st); };
    const CF = [['listed', 'Price listed'], ['conf', 'Confirmed price'], ['known', 'Known for it'], ['open', 'Open now']];
    const fCommon = CF.map(c => ({ t: c[1], on: fc[c[0]] ? 'on' : '', pick: tog('fc', fc, c[0]) }));
    const fItem = it.f.map(c => ({ t: c[1], on: fi[c[0]] ? 'on' : '', pick: tog('fi', fi, c[0]) }));
    const sorts = [['love', 'Most loved'], ['price', 'Lowest price'], ['near', 'Closest']].map(s => ({ t: s[1], on: s[0] === sort ? 'on' : '', pick: () => this.setState({ sort: s[0] }) }));
    const money = v => v === null ? '' : it.pre + (it.dec ? v.toFixed(2) : String(v));
    let rows = it.P.map((p, i) => ({ i, p })).filter(({ p }) => (!fc.listed || p[3] !== null) && (!fc.conf || p[4] === 'site') && (!fc.known || p[5] >= 15) && (!fc.open || p[8]) && it.f.every(f => !fi[f[0]] || p[9].includes(f[0])));
    rows.sort((a, b) => sort === 'price' ? ((a.p[3] === null ? 1e9 : a.p[3]) - (b.p[3] === null ? 1e9 : b.p[3])) : sort === 'near' ? (parseFloat(a.p[7]) - parseFloat(b.p[7])) : (b.p[5] - a.p[5]));
    const selI = rows.some(r => r.i === S.sel) ? S.sel : (rows[0] ? rows[0].i : -1);
    const fname = k => (it.f.find(f => f[0] === k) || [k, k])[1];
    const list = rows.map((r, n) => ({ i: String(n + 1), n: r.p[0], r: r.p[6], dist: r.p[7], open: r.p[8] ? 'Open now' : 'Closed now', love: r.p[5] >= 15 ? 'Loved for its ' + it.name.toLowerCase() + ' in ' + r.p[5] + ' reviews' : 'Mentioned in ' + r.p[5] + ' reviews', blurb: r.p[10], tags: r.p[9].map(fname), hasP: r.p[3] !== null, noP: r.p[3] === null, p: money(r.p[3]), mk: r.p[4], ml: ML[r.p[4]], src: r.p[11], on: r.i === selI ? 'on' : '', pick: () => this.setState({ sel: r.i }) }));
    const priced = rows.filter(r => r.p[3] !== null).map(r => r.p[3]);
    const allP = it.P.filter(p => p[3] !== null).map(p => p[3]);
    const mn = Math.min.apply(null, allP), mx = Math.max.apply(null, allP);
    const dots = rows.filter(r => r.p[3] !== null).map(r => ({ x: String(mx === mn ? 50 : Math.round((r.p[3] - mn) / (mx - mn) * 100)), cls: r.i === selI ? 'sel' : '', t: r.p[0] + ' ' + money(r.p[3]), pick: () => this.setState({ sel: r.i }) }));
    const noP = rows.filter(r => r.p[3] === null).length;
    const pins = rows.map(r => ({ x: String(r.p[1]), y: String(r.p[2]), lbl: r.p[3] === null ? 'No price' : money(r.p[3]), cls: (r.p[3] === null ? 'np' : '') + (r.i === selI ? ' sel' : ''), pick: () => this.setState({ sel: r.i }) }));
    const sp = selI >= 0 ? it.P[selI] : null;
    const sel = sp ? { n: sp[0], p: sp[3] === null ? 'No price' : money(sp[3]), mk: sp[4], ml: ML[sp[4]], unit: sp[3] === null ? 'price not listed' : (it.unit || 'per visit'), r: sp[6], love: sp[5] + ' reviews mention it', blurb: sp[10], src: sp[11] || 'Nobody has added a price yet', x: String(sp[1]), y: String(sp[2]), tf: sp[2] < 45 ? 'translate(-50%, 26px)' : 'translate(-50%, calc(-100% - 26px))' } : {};
    const rangeLbl = priced.length ? money(Math.min.apply(null, priced)) + (priced.length > 1 ? ' to ' + money(Math.max.apply(null, priced)) : '') : 'No prices yet';
    return { groups, items, fCommon, fItem, sorts, it: { name: it.name, unit: it.unit }, list, dots, pins, sel, hasSel: !!sp, isEmpty: rows.length === 0, hasPrices: dots.length > 0, lo: money(mn), hi: money(mx), nShown: String(rows.length), rangeLbl, noPriceLbl: noP ? ' · ' + noP + " don't list a price" : '' };'''
t=HEADX.replace('<title>Lumen Aesthetics on Local AI Registry</title>','<title>Local AI Registry: find the thing, not just the place</title>')
out=t+'\n'+CSS+'\n</style>\n</helmet>\n<div style="width: 1440px; height: 960px; box-sizing: border-box; display: flex; flex-direction: column; background: #ffffff; position: relative; overflow: hidden;">\n'+BODY+'\n</div>\n</x-dc>\n<script type="text/x-dc" data-dc-script>\nclass Component extends DCLogic {\n  renderVals() {\n'+JS+'\n  }\n}\n</script>\n</body>\n</html>\n'
open(P+'Explore.dc.html','w').write(out); print('ok')
