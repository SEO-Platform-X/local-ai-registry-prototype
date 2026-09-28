import sys; sys.path.insert(0,'/tmp/gen')
src=open('/tmp/gen/story.py').read(); exec(src[:src.index('# ---------- REPORT')])
exec(open('/tmp/gen/stories2.py').read().split("def board")[0].split("CSS2=")[1].join(["CSS2=",""]) if False else "")
C=r'''.pw{max-width:1040px;margin:0 auto;padding:32px 40px 64px;display:flex;flex-direction:column;gap:22px}
.crumb{font-size:13px;color:#667085}.crumb a{color:#2b59d9;text-decoration:none}
.card2{background:#ffffff;border:1px solid #e4ded2;border-radius:16px;padding:20px 22px;display:flex;flex-direction:column;gap:12px}
.un{font-size:13px;font-weight:700}.un i{font-style:normal;font-weight:500;color:#8a8a8a}
.tg{display:inline-flex;height:20px;padding:0 8px;border-radius:10px;font-size:10px;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;align-items:center;background:#efeae0;color:#667085}
.act{display:flex;gap:8px}.act span{height:32px;padding:0 12px;border:1px solid #e4ded2;border-radius:16px;display:inline-flex;align-items:center;font-size:13px;font-weight:600;background:#ffffff}
.ans{padding:14px 16px;border-radius:12px;border:1px solid #efeae0;display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:21px}
.own{background:#eaf5ec;border-color:#cfe8d4}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.ty{background:#ffffff;border:1px solid #e4ded2;border-radius:14px;padding:14px 16px;display:flex;flex-direction:column;gap:4px;text-decoration:none;color:#13203a}
.ty strong{font-size:15px}.ty span{font-size:12px;color:#667085}
.rk{display:grid;grid-template-columns:40px 1fr 200px;gap:16px;align-items:start;padding:18px 0;border-top:1px solid #e4ded2}
.rk .n{font-size:28px;font-family:"Cormorant Garamond",Georgia,serif}
.kf{display:flex;gap:6px;flex-wrap:wrap}.kf span{height:26px;padding:0 10px;border-radius:13px;background:#efeae0;font-size:12px;font-weight:600;display:inline-flex;align-items:center}
.q{font-size:14px;line-height:21px;color:#3d4658;padding:10px 12px;border-left:3px solid #e5482d;background:#ffffff;border-radius:0 10px 10px 0}
h1{margin:0;font-size:38px;line-height:44px}
'''
CSSX=CSS+C
# THREAD
T=header('<a href="Main.dc.html" class="btn b-sm">Lumen\'s page</a><a href="Post.dc.html" class="btn b-sm b-coral">Post</a>')+'''<div class="pw"><span class="crumb"><a href="Types.dc.html">Irvine</a> › <a href="BestOf.dc.html">Med spas</a> › <a href="Main.dc.html">Lumen Aesthetics</a> › Locals</span>
<div class="card2"><span class="un">curious_in_woodbridge <i>· Sep 24, 2026</i> <span class="tg">Researching</span></span><h1>Does Dr. Nair do the lip filler herself, or a nurse?</h1><span style="font-size: 15px; line-height: 23px; color: #3d4658;">First time, want it subtle. Budget around $700. Heard mixed things.</span><div class="act"><span>▲ 14 ▼</span><span>💬 5 answers</span><span>↗ Share</span><span>⚑ Report</span></div></div>
<div class="ans own"><span class="un">Lumen Aesthetics <i>· owner · Sep 24</i></span><span>Dr. Nair does every lip filler herself. Nurse injectors do Botox. Consults are $75, credited if you book the same day.</span></div>
<div class="ans"><span class="un">aisha_m_irvine <i>· went · Sep 25</i> <span class="tg">Local expert</span></span><span>She did mine in March. Talked me down to half a syringe, which was the right call.</span></div>
<div class="ans"><span class="un">oc_skin_nerd <i>· went · Sep 25</i></span><span>Same. Ask for a morning slot, she runs behind by the afternoon.</span></div>
<div style="height: 44px; border: 1px solid #e4ded2; border-radius: 22px; background: #ffffff; display: flex; align-items: center; padding: 0 16px; font-size: 14px; color: #8a8a8a;">Add an answer</div>
<div class="card2" style="background: #f7f4ee;"><strong style="font-size: 14px;">Cite this post</strong><span style="font-size: 13px; color: #3d4658;">localairegistry.com/irvine/lumen-aesthetics/locals/t/4790 · Permanent link, listed in Lumen's AI references.</span></div>
<div style="display: flex; flex-direction: column; gap: 8px;"><strong style="font-size: 17px;">More about Lumen</strong><a href="#" style="font-size: 14px;">Is parking validated?</a><a href="#" style="font-size: 14px;">Morpheus8 Body wait list?</a><a href="#" style="font-size: 14px;">Real doctors or aestheticians?</a></div></div>'''
open(P+'Thread.dc.html','w').write(page('A single post',CSSX,T,'    return {};'))
# TYPES
TYP=[('Med spas',148,'Botox, filler, lasers'),('Dermatologists',41,'Skin checks, acne'),('Plastic surgeons',23,'Surgical and injectables'),('Dentists',212,'Cleanings to implants'),('Hair salons',186,'Cuts, color'),('Nail salons',164,'Gel, acrylics'),('Coffee',97,'Cafes and roasters'),('Tacos',64,'Trucks to sit-down'),('Ramen',38,'Tonkotsu, vegan'),('Gyms',88,'Big box to boutique'),('Pilates',31,'Reformer studios'),('Auto repair',73,'Brakes, oil, body'),('Vets',29,'Clinics and emergency'),('Dog groomers',34,'Mobile and in-shop'),('Plumbers',46,'Emergency and remodel')]
cards=''.join(f'<a href="BestOf.dc.html" class="ty"><strong>{n}</strong><span>{c} places · {d}</span><span style="color: #2b59d9; font-weight: 600;">Best {n.lower()} in Irvine ›</span></a>' for n,c,d in TYP)
B=header('<a href="Explore.dc.html" class="btn b-sm">Explore the map</a>')+f'''<div class="pw"><span class="crumb"><a href="Home.dc.html">Local AI Registry</a> › Irvine</span><h1>Everything in Irvine</h1><span style="font-size: 15px; color: #3d4658;">12,400 businesses by type. Each one leads to a best-of list built from what locals say and what owners confirm.</span><div class="grid3">{cards}</div></div>'''
open(P+'Types.dc.html','w').write(page('All types in a city',CSSX,B,'    return {};'))
# BEST OF
R=[('Lumen Aesthetics','Irvine Spectrum · Verified owner',['Natural lip filler','Dr. Nair injects','Validated parking'],'"She talked me down to half a syringe." aisha_m_irvine','Main.dc.html'),('Coastline Med Spa','Irvine Business District',['Same-day replies','Botox pricing posted','Cashback on OrbitBack'],'"They text you back in minutes." kellyw_irvine','Main.dc.html'),('Glow Bar Irvine','Woodbridge',['HydraFacial','Walk-ins','Late hours'],'"Best facial for the price." oc_skin_nerd','Main.dc.html'),('Spectrum Aesthetics MD','Irvine Spectrum',['Morpheus8','Two MDs'],'"Pricey but thorough." reading_reviews_waiting_room','Main.dc.html')]
rows=''.join(f'<div class="rk"><span class="n">{i}</span><div style="display: flex; flex-direction: column; gap: 8px;"><a href="{h}" style="font-size: 20px; font-weight: 700; color: #13203a; text-decoration: none;">{n}</a><span class="crumb">{s}</span><span class="kf">{"".join(f"<span>{k}</span>" for k in kf)}</span><span class="q">{q}</span></div><div style="display: flex; flex-direction: column; gap: 8px; align-items: flex-end;"><a href="Book.dc.html" class="btn b-sm b-dark">Request a booking</a><a href="{h}" class="btn b-sm">See what locals say</a></div></div>' for i,(n,s,kf,q,h) in enumerate(R,1))
B=header('<a href="Types.dc.html" class="btn b-sm">All types</a>')+f'''<div class="pw"><span class="crumb"><a href="Types.dc.html">Irvine</a> › Med spas</span><h1>Best med spas in Irvine</h1><span style="font-size: 15px; line-height: 23px; color: #3d4658;">Ranked by what 1,904 locals posted and confirmed, not by who pays. Every claim links to the post it came from. Updated Sep 27, 2026.</span><div class="kf"><span>Lip filler</span><span>Botox</span><span>Morpheus8</span><span>Open Mondays</span><span>Cashback</span></div><div>{rows}</div><div class="card2" style="background: #f7f4ee;"><strong style="font-size: 14px;">Own a med spa in Irvine?</strong><span style="font-size: 13px; color: #3d4658;">This list is what AI reads. <a href="Claim.dc.html">Claim your page</a> to make sure it's right.</span></div></div>'''
open(P+'BestOf.dc.html','w').write(page('Best of',CSSX,B,'    return {};'))
print('ok')
