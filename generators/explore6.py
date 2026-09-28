import sys; sys.path.insert(0,'/tmp/gen'); from common import *
HEADX=HEAD.replace('family=Figtree:wght@400;500;600;700;800&amp;display=swap','family=Figtree:wght@400;500;600;700;800&amp;family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&amp;display=swap')
CSS=r'''.srf{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;letter-spacing:-0.01em;color:#13203a}
.srf em{font-style:italic;color:#ff5a3c}
.top{height:64px;padding:0 32px;display:flex;align-items:center;gap:16px;border-bottom:1px solid #eeeeee;background:#ffffff}
.nl{font-size:14px;font-weight:600;color:#222222;text-decoration:none;white-space:nowrap}
.cats{display:flex;justify-content:center;gap:34px;padding:14px 32px 0;border-bottom:1px solid #eeeeee;background:#ffffff}
.cat{display:flex;flex-direction:column;align-items:center;gap:6px;padding-bottom:12px;border-bottom:2px solid transparent;cursor:pointer;color:#6a6a6a;font-size:12px;font-weight:600;margin-bottom:-1px}
.cat .ic{font-size:22px;line-height:24px;filter:grayscale(1);opacity:0.7}
.cat.on{color:#222222;border-bottom-color:#222222}
.cat.on .ic{filter:none;opacity:1}
.grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:28px 22px}
.kc{display:flex;flex-direction:column;gap:10px;text-decoration:none;color:#222222}
.kc .ph{height:230px;border-radius:14px;position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center}
.kc .ph .phl{font-size:11px;font-weight:600;color:rgba(0,0,0,0.45)}
.kc .ph .lv{position:absolute;top:12px;right:12px;height:26px;padding:0 10px;border-radius:13px;background:rgba(255,255,255,0.92);font-size:12px;font-weight:700;display:flex;align-items:center;color:#222222}
.kc .meta .it{font-family:"Cormorant Garamond",Georgia,serif;font-size:28px;line-height:30px;font-weight:600;color:#13203a;letter-spacing:-0.01em}
.kc .xface{height:210px;border-radius:16px;padding:20px;box-sizing:border-box;display:flex;flex-direction:column;justify-content:space-between;position:relative;overflow:hidden}
.kc .face .kn{font-size:11px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;opacity:0.65}
.kc .face .it{font-family:"Cormorant Garamond",Georgia,serif;font-size:36px;line-height:36px;font-weight:600;letter-spacing:-0.01em}
.kc .face .lv{position:absolute;top:16px;right:16px;height:26px;padding:0 10px;border-radius:13px;background:rgba(255,255,255,0.85);font-size:12px;font-weight:700;display:flex;align-items:center;color:#222222}
.kc:hover .ph{filter:brightness(0.96)}
.kc .meta{display:flex;flex-direction:column;gap:3px}
.kc .meta .r1{display:flex;justify-content:space-between;gap:8px;font-size:15px;font-weight:600}
.kc .meta .r2{font-size:14px;color:#6a6a6a}
.kc .meta .r3{font-size:14px;color:#222222}
'''
LOGO2='<svg width="22" height="20" viewBox="0 0 22 20" aria-hidden="true"><path d="M11 1L21 19H1Z" fill="#2d55e6"></path><path d="M11 8L15.5 16H6.5Z" fill="#ffffff"></path></svg>'
BODY=f'''<div class="top"><a href="Explore.dc.html" style="display: flex; align-items: center; gap: 8px; text-decoration: none; color: #13203a; font-weight: 700; font-size: 15px;">{LOGO2}Local AI Registry</a><span style="margin-left: auto; display: flex; align-items: center; gap: 22px;"><span style="font-size: 14px; font-weight: 600; display: flex; align-items: center; gap: 6px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#222222" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M12 21s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"></path><circle cx="12" cy="9" r="2.5"></circle></svg>Irvine, CA</span><a href="Business.dc.html" class="nl">For business</a><a href="#" class="nl">Sign in</a></span></div>
<div class="cats"><sc-for list="{{{{cats}}}}" as="c" hint-placeholder-count="9"><span class="cat {{{{c.on}}}}" onClick="{{{{c.pick}}}}"><span class="ic">{{{{c.ic}}}}</span>{{{{c.t}}}}</span></sc-for></div>
<div style="padding: 30px 32px 48px; display: flex; flex-direction: column; gap: 24px;">
<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 20px;"><div style="display: flex; flex-direction: column; gap: 6px;"><h1 class="srf" style="margin: 0; font-size: 40px; line-height: 42px;">{{{{headA}}}} <em>{{{{headB}}}}</em></h1><span style="font-size: 15px; color: #484848;">The product, procedure or service each place is best at, from what thousands of reviews keep saying.</span></div><span class="mu" style="font-size: 13px;">{{{{n}}}} places</span></div>
<div class="grid"><sc-for list="{{{{cards}}}}" as="k" hint-placeholder-count="12"><a href="Item.dc.html" class="kc"><span class="ph" style="background: {{{{k.bg}}}};"><span class="phl">[Google Business Profile photo]</span><span class="lv">♥ {{{{k.m}}}} reviews</span></span><span class="meta"><span class="it">{{{{k.it}}}}</span><span class="r1"><span>{{{{k.b}}}}</span><span style="font-weight: 500;">★ {{{{k.r}}}}</span></span><span class="r2">{{{{k.hood}}}} · {{{{k.d}}}} mi</span><span class="r2" style="color: #484848;">Loved for: {{{{k.why}}}}</span><span class="r3"><strong>{{{{k.p}}}}</strong> {{{{k.pu}}}}</span></span></a></sc-for></div>
</div>
</div>'''
JS=r'''    const S = this.state || {};
    const c = S.c || 'all';
    const CAT = [['all', 'Everything', '✦'], ['food', 'Food', '🌮'], ['drinks', 'Drinks', '☕'], ['beauty', 'Beauty', '💄'], ['health', 'Health', '🦷'], ['fitness', 'Fitness', '🧘'], ['car', 'Car', '🚗'], ['pets', 'Pets', '🐾'], ['home', 'Home', '🔧']];
    const COL = { food: ['#f6e3d3', '#6b3514'], drinks: ['#e6ddf3', '#3b2a6b'], beauty: ['#f7dfe4', '#7a2340'], health: ['#dcebe4', '#1f5240'], fitness: ['#e0e9f5', '#1f3d66'], car: ['#e4e4e0', '#34342e'], pets: ['#f3ead0', '#5e4a12'], home: ['#e3eadb', '#34482a'] };
    const K = [
      ['food', 'Birria tacos', 'Backyard Tacos', '4.7', 'University Park', '1.0', 40, '$4', 'each', 'crispy edges, consommé with every order'],
      ['beauty', 'Lip filler', 'Lumen Aesthetics', '4.9', 'Irvine Spectrum', '0.2', 31, '$650', 'a syringe', 'natural results, half syringes'],
      ['food', 'Tonkotsu ramen', 'Kinjiro Ramen', '4.6', 'Irvine Spectrum', '0.5', 58, '$16', 'a bowl', 'rich broth, open until 12:45'],
      ['drinks', 'Brown sugar boba', 'Tea Maru', '4.6', 'Woodbridge', '1.4', 64, '$6.50', '', 'chewy pearls made every hour'],
      ['health', 'Kids teeth cleaning', 'Woodbridge Kids Dental', '4.9', 'Woodbridge', '1.2', 47, '$95', 'a visit', 'gentle with nervous kids, Saturdays'],
      ['car', 'Tesla service', 'Irvine Auto Care', '4.4', 'Quail Hill', '2.3', 18, '$129', 'inspection', 'certified, fair quotes'],
      ['food', 'Har gow dumplings', 'Capital Seafood', '4.5', 'Irvine Spectrum', '0.4', 52, '$7', 'a plate', 'carts until 2 PM'],
      ['beauty', 'Curly haircut', 'Heritage Hair Studio', '4.6', 'University Park', '1.9', 29, '$95', 'a cut', 'three stylists trained in curls'],
      ['fitness', 'Reformer Pilates class', 'Great Park Pilates', '4.8', 'Great Park', '2.1', 33, '$25', 'first class', 'good for first-timers'],
      ['drinks', 'Oat milk cortado', 'Blue Door Coffee', '4.7', 'Woodbridge', '1.6', 27, '$5', '', 'quiet before 11 AM'],
      ['food', 'Shio ramen', 'Santouka', '4.5', 'Irvine Spectrum', '0.9', 40, '$17', 'a bowl', 'light broth, fast counter'],
      ['pets', 'Dog vaccines', 'Quail Hill Vet', '4.9', 'Quail Hill', '2.6', 22, '$68', 'exam', 'no upsell, same-day visits'],
      ['beauty', 'Acne facial', 'Pacific Skin Studio', '4.6', 'University Park', '1.9', 26, '$120', 'a facial', 'esthetician Maya'],
      ['food', 'Pork belly bao', 'Bao Wow', '4.6', 'Irvine Spectrum', '0.3', 35, '$7', 'each', 'crispy, sells out by dinner'],
      ['health', 'Same-day crown', 'Spectrum Dental', '4.7', 'Irvine Spectrum', '0.8', 19, '$1,200', 'a tooth', 'done in one visit'],
      ['drinks', 'Natural wine by the glass', 'Spectrum Social', '4.4', 'Irvine Spectrum', '0.2', 16, '$14', 'a glass', 'rotating list'],
      ['beauty', 'Botox', 'Spectrum Aesthetics MD', '4.8', 'Irvine Spectrum', '0.6', 38, '$14', 'a unit', 'Dr. Chen injects every patient'],
      ['food', 'Egg tarts', 'Sea Harbour', '4.4', 'Woodbridge', '1.5', 24, '$5.50', 'for 3', 'warm out of the oven at 11'],
      ['home', 'AC repair', 'Cool Breeze HVAC', '4.8', 'Irvine', '3.2', 21, '$89', 'a visit', 'same-week appointments'],
      ['fitness', 'Hot yoga class', 'Heat Yoga Irvine', '4.7', 'Woodbridge', '1.1', 30, '$22', 'drop-in', '6 AM classes'],
      ['car', 'Synthetic oil change', 'Spectrum Tire and Auto', '4.7', 'Irvine Spectrum', '0.9', 12, '$85', '', 'done in 25 minutes'],
      ['food', 'Chilaquiles', 'Sol Cocina', '4.4', 'Irvine Spectrum', '0.8', 28, '$16', '', 'weekend brunch favorite'],
      ['pets', 'Dog grooming', 'Coastline Pet Grooming', '4.5', 'Quail Hill', '2.8', 17, '$75', 'a groom', 'calm with anxious dogs'],
      ['home', 'Deep house cleaning', 'Sparkle Irvine', '4.6', 'Irvine', '2.0', 25, '$160', 'a clean', 'same crew every time']
    ];
    const rows = K.filter(k => c === 'all' || k[0] === c);
    const cards = rows.map(k => ({ it: k[1], b: k[2], r: k[3], hood: k[4], d: k[5], m: String(k[6]), p: k[7], pu: k[8], why: k[9], bg: COL[k[0]][0], fg: COL[k[0]][1] }));
    const cats = CAT.map(x => ({ t: x[1], ic: x[2], on: x[0] === c ? 'on' : '', pick: () => this.setState({ c: x[0] }) }));
    const name = (CAT.find(x => x[0] === c) || CAT[0])[1];
    return { cats, cards, n: String(cards.length), headA: c === 'all' ? 'Known for' : name + ',', headB: c === 'all' ? 'in Irvine.' : 'known for.' };'''
t=HEADX.replace('<title>Lumen Aesthetics on Local AI Registry</title>','<title>Local AI Registry: known for, in Irvine</title>')
out=t+'\n'+CSS+'\n</style>\n</helmet>\n<div style="width: 1440px; box-sizing: border-box; background: #ffffff;">\n'+BODY+'\n</div>\n</x-dc>\n<script type="text/x-dc" data-dc-script>\nclass Component extends DCLogic {\n  renderVals() {\n'+JS+'\n  }\n}\n</script>\n</body>\n</html>\n'
open(P+'Explore.dc.html','w').write(out); print('ok')
