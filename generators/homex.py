import sys,re,os; sys.path.insert(0,'/tmp/gen'); from plates import plate,street,ITEM
from headers import LOGO
P='/mnt/user-data/outputs/artifacts/01ea5720-d0c8-4528-b8cc-76eb1693feae/project/'
CSS=r'''/*hx*/
#hxWrapA > div,#hxWrapB > div{width:1440px !important;max-width:none !important;margin-left:calc(50% - 720px) !important;margin-right:0 !important;box-sizing:border-box}
#hxWrapA,#hxWrapB{width:100%}
.hx-ey{font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#5b6474}
.hx-h{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;color:#13203a;letter-spacing:-0.01em}
.hx-h em{color:#e5482d}
.hx-rv{opacity:1}

/* the shift */
.hx-shift{position:relative;padding:140px 64px 60px;background:#f3efe7;border-top:1px solid #e4ded2}
.hx-shift .stick{position:sticky;top:90px;display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center;max-width:1260px;margin:0 auto}
.hx-shift .ln{font-family:"Cormorant Garamond",Georgia,serif;font-size:60px;line-height:64px;color:#13203a;margin:0 0 26px}
.hx-shift .ln em{color:#e5482d}
.hx-plate{border-radius:6px;background:#fbf6ec;border:1px solid #e4ded2;padding:26px;display:flex;justify-content:center;}
.hx-mq{overflow:hidden;margin-top:110px;border-top:1px solid #e4ded2;border-bottom:1px solid #e4ded2;padding:28px 0;background:#fbf6ec;}
.hx-mq .hx-trk{display:flex;gap:48px;width:max-content}
.hx-mq .hx-trk > span{display:flex;flex-direction:column;align-items:center;gap:10px;font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:#5b6474}
/* findings */
.hx-find{padding:150px 64px;background:#13203a;color:#fff;display:grid;grid-template-columns:1.1fr 1fr;gap:60px;align-items:center}
.hx-find .big{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:260px;line-height:220px;color:#fff;display:flex;align-items:flex-start}
.hx-find .big sup{font-size:120px;line-height:130px;color:#e5482d}
.hx-find p{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-size:46px;line-height:52px}
.hx-find .rail{height:10px;border-radius:5px;background:rgba(255,255,255,0.14);overflow:hidden;margin-top:34px}.hx-find .rail i{display:block;height:100%;width:73%;background:#e5482d;transform-origin:left}
.hx-find small{display:block;margin-top:14px;font-size:13px;color:#aeb6c6}
/* industries */
.hx-ind{padding:140px 64px;background:#f3efe7;max-width:1440px;box-sizing:border-box}
.hx-tabs{display:flex;gap:10px;flex-wrap:wrap;margin:34px 0 30px}
.hx-tab{height:48px;padding:0 22px;border-radius:9999px;border:1px solid #13203a;display:inline-flex;align-items:center;gap:10px;font-size:15px;font-weight:600;cursor:pointer;background:#fff;color:#13203a}
.hx-tab i{font-style:normal;font-family:"Cormorant Garamond",Georgia,serif;font-size:18px;opacity:0.55}
.hx-tab.on{background:#13203a;color:#fff}
.hx-lead{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:22px}
.hx-lead p{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-size:32px;font-style:italic;color:#3d4658}
.hx-lb{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.hx-lc{display:flex;flex-direction:column;gap:12px;text-decoration:none;color:#13203a}
.hx-lc .im{position:relative;border-radius:8px;overflow:hidden;background:#fbf6ec;border:1px solid #e4ded2;display:flex;justify-content:center;padding:14px 8px;}
.hx-lc:hover .im{transform:translateY(-4px)}
.hx-lc .rk{position:absolute;top:10px;left:12px;font-family:"Cormorant Garamond",Georgia,serif;font-size:34px;color:#13203a}
.hx-lc b{font-size:16px;line-height:21px}.hx-lc .ct{font-size:13px;color:#5b6474}
.hx-lc .sc{display:flex;align-items:center;gap:10px;font-size:13px;font-weight:700}.hx-lc .sc span{flex:1;height:6px;border-radius:3px;background:#e4ded2;overflow:hidden}.hx-lc .sc span i{display:block;height:100%;background:#13203a;transform-origin:left}
/* steps */
.hx-steps{padding:140px 64px;background:#fbf6ec;border-top:1px solid #e4ded2;border-bottom:1px solid #e4ded2}
.hx-rows{max-width:1260px;margin:40px auto 0;display:flex;flex-direction:column}
.hx-row{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center;padding:60px 0;border-top:1px solid #e4ded2}
.hx-row:nth-child(even) .hx-st{order:2}
.hx-stage2{position:relative;height:520px}
.hx-stage2 .hx-card{overflow:hidden;position:absolute;inset:0}
.hx-sg{display:grid;grid-template-columns:1fr 1fr;gap:80px;max-width:1260px;margin:60px auto 0}
.hx-st{display:flex;flex-direction:column;justify-content:center;gap:14px}
.hx-st .no{font-family:"Cormorant Garamond",Georgia,serif;font-size:96px;line-height:90px;color:#e5482d}
.hx-st h3{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:54px;line-height:56px}
.hx-st p{margin:0;font-size:18px;line-height:29px;color:#3d4658;max-width:460px}
.hx-stage{position:sticky;top:120px;height:560px}
.hx-card{overflow:hidden;position:absolute;inset:0;border-radius:14px;background:#fff;border:1px solid #e4ded2;box-shadow:0 30px 70px rgba(19,32,58,0.14);padding:28px;display:flex;flex-direction:column;gap:16px;box-sizing:border-box}
/* method */
.hx-meth{padding:140px 64px;background:#f3efe7;display:grid;grid-template-columns:1fr 1.1fr;gap:70px;max-width:1440px;box-sizing:border-box}
.hx-sig{display:flex;flex-direction:column;border-top:1px solid #d9d2c4}
.hx-si{display:grid;grid-template-columns:48px 1fr 150px;gap:14px;align-items:center;padding:18px 0;border-bottom:1px solid #d9d2c4;cursor:pointer}
.hx-si .n{font-family:"Cormorant Garamond",Georgia,serif;font-size:24px;color:#8a93a3}
.hx-si b{font-size:18px}.hx-si .w{height:8px;border-radius:4px;background:#e4ded2;overflow:hidden}.hx-si .w i{display:block;height:100%;background:#8a93a3;transform-origin:left}
.hx-si.on b{color:#e5482d}.hx-si.on .n{color:#e5482d}.hx-si.on .w i{background:#e5482d}
.hx-si .d{grid-column:2 / span 2;font-size:15px;line-height:24px;color:#3d4658;display:none}.hx-si.on .d{display:block}
.hx-nopay{align-self:flex-start;display:inline-flex;align-items:center;gap:10px;margin-top:28px;height:44px;padding:0 18px;border-radius:9999px;background:#13203a;color:#fff;font-size:14px;font-weight:700}
/* quote */
.hx-q{padding:150px 64px;background:#13203a;color:#fff;display:grid;grid-template-columns:300px 1fr;gap:70px;align-items:center}
.hx-q .pt{width:300px;height:360px;border-radius:150px 150px 8px 8px;background:#f5e3cc;display:flex;align-items:flex-end;justify-content:center;overflow:hidden}
.hx-q blockquote{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-size:62px;line-height:66px}
.hx-q blockquote em{color:#e5482d}
/* journal */
.hx-jr{padding:140px 64px;background:#f3efe7}
.hx-jg{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:40px}
.hx-jc{display:flex;flex-direction:column;gap:12px;padding:30px 28px;min-height:330px;box-sizing:border-box;border-radius:10px;background:#fff;border:1px solid #e4ded2;text-decoration:none;color:#13203a;}
.hx-jc:hover{transform:translateY(-4px);box-shadow:0 20px 40px rgba(19,32,58,0.12)}
.hx-jc .n{font-family:"Cormorant Garamond",Georgia,serif;font-size:44px;color:#e5482d;line-height:44px}
.hx-jc h3{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:32px;line-height:35px}
.hx-jc p{margin:0;font-size:15px;line-height:24px;color:#3d4658;flex:1}
/* cta */
.hx-cta{padding:150px 64px 0;background:#f5e3cc;display:flex;flex-direction:column;align-items:center;text-align:center;gap:18px;border-top:1px solid #e6cfb2;overflow:hidden}
.hx-cta .srch{display:flex;align-items:center;gap:10px;width:640px;height:68px;border-radius:34px;background:#fff;box-shadow:0 12px 34px rgba(19,32,58,0.16);padding:0 8px 0 26px;box-sizing:border-box;font-size:18px;color:#8a93a3;margin-top:18px}
.hx-cta .srch a{margin-left:auto;height:52px;padding:0 28px;border-radius:26px;background:#e5482d;color:#fff !important;display:flex;align-items:center;font-size:16px;font-weight:700;text-decoration:none}
.hx-street{width:1200px;margin-top:80px}
/* footer */
.hx-ft{background:#0e1830;color:#d8dde8;padding:90px 64px 36px;display:flex;flex-direction:column;gap:60px}
.hx-ft a{color:#d8dde8;text-decoration:none}.hx-ft a:hover{color:#fff}
.hx-ftop{display:grid;grid-template-columns:1.4fr repeat(4,1fr);gap:40px}
.hx-ft h4{margin:0 0 16px;font-size:12px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:#8a93a3}
.hx-ft ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:11px;font-size:15px}
.hx-sub{display:flex;gap:8px;margin-top:18px}.hx-sub span{flex:1;height:50px;border-radius:25px;border:1px solid #3a4763;display:flex;align-items:center;padding:0 18px;font-size:15px;color:#8a93a3}.hx-sub b{height:50px;padding:0 22px;border-radius:25px;background:#fff;color:#13203a;display:flex;align-items:center;font-size:14px}
.hx-word{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:178px;line-height:190px;padding-bottom:10px;letter-spacing:-0.02em;color:#fff;white-space:nowrap;overflow:hidden}
.hx-word em{color:#e5482d}
.hx-fbot{display:flex;justify-content:space-between;align-items:center;gap:20px;font-size:13px;color:#8a93a3;border-top:1px solid #26324d;padding-top:24px;flex-wrap:wrap}
.hx-soc{display:flex;gap:10px}.hx-soc a{width:40px;height:40px;border-radius:50%;border:1px solid #3a4763;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700}
'''
KINDS=list(ITEM)
def mq():
    one=''.join(f'<span>{plate(k,"m"+k+str(r),200,144)}{k.replace("surgeon","plastic surgeon").replace("optometry","eye doctor")}</span>' for r in (0,) for k in KINDS)
    two=one.replace('id="hm','id="hn').replace('url(#hm','url(#hn').replace('id="vm','id="vn').replace('url(#vm','url(#vn').replace('id="xm','id="xn').replace('url(#xm','url(#xn')
    return f'<div class="hx-mq"><div class="hx-trk">{one}</div></div>'
SHIFT=f'''<div class="hx-shift" id="hxShift"><div class="stick"><div><span class="hx-ey">The shift</span><p class="ln hx-line" style="margin-top: 22px;">Somewhere nearby, a customer is asking <em>which business to trust</em>.</p><p class="ln hx-line">An assistant will name one.</p><p class="ln hx-line">Right now, that one <em>is not you</em>.</p></div><div class="hx-plate hx-rv">{plate("coffee","sh",480,345)}</div></div>{mq()}</div>
<div class="hx-find" id="hxFind"><div class="hx-rv"><span class="hx-ey" style="color: #aeb6c6;">The findings</span><div class="big" style="margin-top: 20px;"><span class="hx-rv">73</span><sup>%</sup></div></div><div class="hx-rv"><p>of local businesses are <em style="color: #e5482d;">never</em> recommended by AI.</p><div class="rail"><i class="hx-bar"></i></div><small>An estimate based on Local AI Registry's AI visibility checks across the businesses we have scored.</small></div></div>'''
IND=[('Plastic surgeons','Where one recommendation is worth a year of ads.',[('Dr. Michael Jazayeri, Plastic and Reconstructive Surgery','Santa Ana, CA',68,'surgeon'),('Heavenly Plastic Surgery','Foothill Ranch, CA',66,'surgeon'),('Wave Plastic Surgery and Aesthetic Laser Center','Costa Mesa, CA',55,'surgeon'),('Renaissance Plastic Surgery: Richard H. Lee, MD','Newport Beach, CA',47,'surgeon')]),
('Cannabis dispensaries','Where AI answers "what is open near me" all night.',[('Sample dispensary A','Santa Ana, CA',71,'dispensary'),('Sample dispensary B','Costa Mesa, CA',64,'dispensary'),('Sample dispensary C','Irvine, CA',52,'dispensary'),('Sample dispensary D','Tustin, CA',41,'dispensary')]),
('Eye doctors','Where "who takes my insurance" decides the visit.',[('Sample eye clinic A','Irvine, CA',74,'optometry'),('Sample eye clinic B','Newport Beach, CA',63,'optometry'),('Sample eye clinic C','Tustin, CA',58,'optometry'),('Sample eye clinic D','Orange, CA',44,'optometry')]),
('Auto dealers','Where AI already picks the shortlist.',[('Sample dealer A','Irvine, CA',69,'restaurant'),('Sample dealer B','Tustin, CA',61,'restaurant'),('Sample dealer C','Orange, CA',50,'restaurant'),('Sample dealer D','Costa Mesa, CA',43,'restaurant')]),
('Med spas','Where trust is the whole sale.',[('Coastline MedSpa','Newport Beach, CA',84,'salon'),('Derm + Co','Tustin, CA',79,'salon'),('Glow Bar Irvine','Irvine, CA',71,'salon'),('Lumen Aesthetics','Irvine, CA',58,'salon')])]
def lb(i):
    n,lead,rows=IND[i]
    cards=''.join(f'<a href="{"Main.dc.html" if nm=="Lumen Aesthetics" else "ExploreSearch.dc.html"}" class="hx-lc hx-rv"><span class="im"><span class="rk">0{j+1}</span>{plate(k,"lb"+str(i)+str(j),260,187)}</span><b>{nm}</b><span class="ct">{ct}</span><span class="sc">AI Score {sc}<span><i class="hx-bar" style="width: {sc}%;"></i></span></span></a>' for j,(nm,ct,sc,k) in enumerate(rows))
    return f'<sc-if value="{{{{ind{i}}}}}" hint-placeholder-val="{{{{ {"true" if i==0 else "false"} }}}}"><div class="hx-lead"><p>{lead}</p><a href="ExploreSearch.dc.html" style="font-size: 15px; font-weight: 700;">See the {n.lower()} ranking ⟶</a></div><div class="hx-lb">{cards}</div></sc-if>'
tabs=''.join(f'<span class="hx-tab {{{{indc{i}}}}}" onClick="{{{{indp{i}}}}}">{n}<i>0{i+1}</i></span>' for i,(n,_,_) in enumerate(IND))
INDS=f'<div class="hx-ind" id="hxInd"><span class="hx-ey">The registry, by industry</span><h2 class="hx-h hx-rv" style="font-size: 76px; line-height: 78px; margin-top: 14px;">The industries we <em>watch closest</em>.</h2><div class="hx-tabs">{tabs}</div>{"".join(lb(i) for i in range(len(IND)))}<span class="xs" style="display: block; margin-top: 18px; font-size: 12px; color: #8a93a3;">Plastic surgeon ranking is live data from localairegistry.com. Other tabs are sample rows for the prototype.</span></div>'
C1=f'<div class="hx-card"><span class="hx-ey">Look it up</span><div style="height: 58px; border-radius: 29px; border: 2px solid #13203a; display: flex; align-items: center; padding: 0 22px; font-size: 18px;">QUIKTOX Botox<span style="width: 2px; height: 24px; background: #2b59d9; margin-left: 4px;"></span></div><div style="display: flex; flex-direction: column; gap: 10px;">{"".join(f"<span style=\'display: flex; gap: 10px; align-items: center; font-size: 15px;\'><span style=\'width: 22px; height: 22px; border-radius: 50%; background: #237233; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 12px;\'>✓</span>{t}</span>" for t in ["Pulled search results","Asked ChatGPT, Gemini and Claude","Read 1,240 reviews","Checked 31 directories"])}</div><div style="margin-top: auto; display: flex; justify-content: center;">{plate("optometry","c1",300,216)}</div></div>'
C2=f'<div class="hx-card c2"><span class="hx-ey">See what AI says</span><div style="display: flex; align-items: center; gap: 22px;"><span style="width: 150px; height: 150px; border-radius: 50%; border: 12px solid #237233; display: flex; align-items: center; justify-content: center; font-family: \'Cormorant Garamond\', Georgia, serif; font-size: 72px; box-sizing: border-box;">93</span><span style="display: flex; flex-direction: column; gap: 6px;"><b style="font-size: 22px;">QUIKTOX Botox</b><span style="font-size: 15px; color: #3d4658;">AI Score 93. Named by ChatGPT and Claude.</span></span></div><div style="border-radius: 10px; background: #f3efe7; padding: 16px 18px; font-size: 15px; line-height: 23px;"><b>The verdict, in plain English:</b> AI trusts QUIKTOX for Botox in Irvine. It is not named for filler yet.</div><div style="margin-top: auto; display: flex; justify-content: center;">{plate("optometry","c2",250,180,"93")}</div></div>'
C3=f'<div class="hx-card c3" style="background: #13203a; color: #fff; border-color: #13203a;"><span class="hx-ey" style="color: #aeb6c6;">It is free</span><span class="hx-h" style="font-size: 110px; line-height: 100px; color: #fff;">Free<em>.</em></span><span style="font-size: 18px; line-height: 28px; color: #d8dde8;">Claim your record and watch it over time. No card, no catch, ever.</span><a href="ExploreSearch.dc.html" style="align-self: flex-start; height: 56px; padding: 0 28px; border-radius: 28px; background: #e5482d; color: #fff; display: flex; align-items: center; font-size: 16px; font-weight: 700; text-decoration: none;">Get your free AI Score ⟶</a><div style="margin-top: auto; display: flex; justify-content: center; background: #fbf6ec; border-radius: 10px; padding: 10px;">{plate("dental","c3",250,180,"✓")}</div></div>'
STEPS=f'<div class="hx-steps" id="hxSteps"><div style="max-width: 1260px; margin: 0 auto;"><span class="hx-ey">How it works</span><h2 class="hx-h hx-rv" style="font-size: 76px; line-height: 78px; margin-top: 14px;">Three steps, and it is <em>free</em>.</h2></div><div class="hx-rows">'+''.join(f'<div class="hx-row"><div class="hx-st hx-rv"><span class="no">0{i+1}</span><h3>{h}</h3><p>{p}</p></div><div class="hx-stage2 hx-in">{c}</div></div>' for i,(h,p,c) in enumerate([('Look it up.','Type any local business. We pull its whole public footprint: search, AI, reviews, all of it.',C1),('See what AI says.','Its AI Score, which assistants name it, and the verdict in plain English. Nothing hidden.',C2),('It is free.','Claim your record and watch it over time. No card, no catch, ever.',C3)]))+'</div></div>'
SIG=[('Retrieval grounding','Whether you appear in the results AI retrieves and cites: AI Overviews, the organic top 10, and the index ChatGPT leans on.',100),('Off-property attestation','How much others say about you off your own site: mentions, videos, third-party best-of lists. This is what makes you retrievable.',84),('AI visibility','Whether ChatGPT, Gemini and Claude name you when asked, and for the right service.',76),('Reviews and response','Not the star average. How many reviews, how recent, and how specific. AI quotes specifics, not stars.',62),('Backlink and citation authority','The links and citations across the web that vouch for you.',50),('Google Business Profile','Whether your Google Business Profile is complete, accurate and current.',42),('Speed and mobile','Whether your site is genuinely fast and works on a phone.',30),('Content freshness and schema','Whether your pages stay fresh and machine-readable, with clean schema.',24)]
sig=''.join(f'<div class="hx-si {{{{sgc{i}}}}}" onClick="{{{{sgp{i}}}}}"><span class="n">0{i+1}</span><b>{t}</b><span class="w"><i class="hx-bar" style="width: {w}%;"></i></span><span class="d">{d}</span></div>' for i,(t,d,w) in enumerate(SIG))
METH=f'<div class="hx-meth" id="hxMeth"><div style="position: sticky; top: 110px; align-self: start; display: flex; flex-direction: column; gap: 18px;"><span class="hx-ey">The method</span><h2 class="hx-h hx-rv" style="font-size: 76px; line-height: 78px;">Exactly how the score is <em>made</em>.</h2><p style="margin: 0; font-size: 19px; line-height: 30px; color: #3d4658; max-width: 520px;">Eight signals, weighted. The heaviest is simply whether AI can retrieve and cite you at all. The same for every business, and we show our work.</p><span class="hx-nopay">No pay-to-rank. Ever.</span><a href="#" style="font-size: 15px; font-weight: 700;">Read the full method ⟶</a></div><div class="hx-sig">{sig}<span style="font-size: 12px; color: #8a93a3; padding-top: 12px;">Bar length shows relative weight. Weights here are illustrative, use the ones from /methodology.</span></div></div>'
QUOTE=f'<div class="hx-q" id="hxQuote"><div class="pt hx-rv" style="align-items: center; flex-direction: column; justify-content: center; gap: 10px;"><span style="font-family: \'Cormorant Garamond\', Georgia, serif; font-size: 120px; line-height: 110px; color: #13203a;">DS</span><span style="font-size: 11px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: #8a7b69;">Portrait goes here</span></div><div class="hx-rv" style="display: flex; flex-direction: column; gap: 26px;"><blockquote>A year ago, AI did not know we existed. Now patients walk in saying <em>ChatGPT sent them</em>.</blockquote><span style="font-size: 16px; color: #aeb6c6;"><b style="color: #fff;">Deanna Shah, MPAP, PA-C</b> · Aesthetic Injection Specialist, QUIKTOX Botox</span><a href="#" style="align-self: flex-start; font-size: 15px; font-weight: 700; color: #fff;">See QUIKTOX on the registry ⟶</a></div></div>'
JR=[('Announcement','Local AI Registry is live: look up what AI says about your business','The first public registry of AI business recommendations is open. Any US business can look up its record free.'),('AI and local discovery','How AI decides which local business to recommend','When a customer asks for the best dentist near me, one name comes back, not ten links. Here is what decides whose.'),('The AI Score','What is an AI Score, and how is it calculated?','A single number, 0 to 100, for how findable and recommendable your business is to AI. Here is what goes into it.')]
JOUR='<div class="hx-jr" id="hxJournal"><div style="display: flex; justify-content: space-between; align-items: flex-end;"><div><span class="hx-ey">The journal</span><h2 class="hx-h hx-rv" style="font-size: 76px; line-height: 78px; margin-top: 14px;">Notes from the <em>registry</em>.</h2></div><a href="#" style="font-size: 15px; font-weight: 700;">Read the journal ⟶</a></div><div class="hx-jg">'+''.join(f'<a href="#" class="hx-jc hx-rv"><span class="n">0{i+1}</span><span class="hx-ey">{c}</span><h3>{t}</h3><p>{d}</p><span style="font-size: 14px; font-weight: 700;">Read ⟶</span></a>' for i,(c,t,d) in enumerate(JR))+'</div></div>'
CTA=f'<div class="hx-cta" id="hxCta"><h2 class="hx-h hx-rv" style="font-size: 96px; line-height: 96px; max-width: 1000px;">Find out what AI says <em>about you</em>.</h2><span style="font-family: \'Cormorant Garamond\', Georgia, serif; font-style: italic; font-size: 32px; color: #3d4658;">And it is free.</span><div class="srch hx-rv"><span>Your business name or website</span><a href="ExploreSearch.dc.html">Look it up</a></div><div class="hx-street hx-rv">{street("cta")}</div></div>'
COLS=[('The registry',['Leaderboards','Methodology','Discover','Trust']),('For owners',['Get your AI Score','The platform','By industry','Pricing','Register','Book a demo']),('Company',['About','The team','Careers','Contact']),('Resources',['Journal','Help center','FAQ','For agencies','Partners','Media kit'])]
LINK={'Get your AI Score':'ExploreSearch.dc.html','Pricing':'Upgrade.dc.html','Register':'Claim.dc.html','Help center':'OwnerHelp.dc.html','Discover':'Explore.dc.html','The platform':'Business.dc.html','The team':'OwnerTeam.dc.html'}
cols=''.join(f'<div><h4>{h}</h4><ul>{"".join(f"<li><a href=\'{LINK.get(x,"#")}\'>{x}</a></li>" for x in xs)}</ul></div>' for h,xs in COLS)
soc=''.join(f'<a href="#" title="{n}">{a}</a>' for n,a in [('LinkedIn','in'),('X','X'),('Instagram','IG'),('Facebook','f'),('TikTok','TT'),('Pinterest','P')])
FOOT=f'''<div class="hx-ft" id="hxFooter"><div class="hx-ftop"><div><span style="display: flex; align-items: center; gap: 10px;">{LOGO}<b style="font-size: 18px; color: #fff;">Local AI Registry</b></span><p style="margin: 18px 0 0; font-size: 15px; line-height: 24px; max-width: 320px;">The public registry of what AI says about local businesses.</p><h4 style="margin-top: 30px;">Sign up for updates</h4><div class="hx-sub"><span>you@business.com</span><b>Subscribe</b></div></div>{cols}</div>
<div class="hx-word hx-rv">Local AI <em>Registry</em></div>
<div class="hx-fbot"><span>The 73% figure is an estimate based on Local AI Registry's AI visibility checks across the local businesses we have scored.</span></div>
<div class="hx-fbot" style="border-top: none; padding-top: 0;"><span>© 2026 Local AI Registry · <a href="#">Privacy Policy</a> · <a href="#">Terms of Service</a> · <a href="#">Data policy</a> · <a href="#">Opt out</a></span><span class="hx-soc">{soc}</span></div></div>'''
def build():
    s=open(P+'Home.dc.html').read()
    for idm in ['hxWrapA','hxWrapB']:
        while f'id="{idm}"' in s:
            a=s.index(f'<div id="{idm}"'); e=s.index(f'<span id="{idm}End"></span></div>',a)+len(f'<span id="{idm}End"></span></div>'); s=s[:a]+s[e:]
    if 'id="hxNext"' in s:
        a=s.index('<a id="hxNext"'); e=s.index('</a>',a)+4; s=s[:a]+s[e:]
    A=f'<div id="hxWrapA">{SHIFT}<span id="hxWrapAEnd"></span></div>'
    B=f'<div id="hxWrapB">{INDS}{STEPS}{METH}{QUOTE}{JOUR}{CTA}{FOOT}<span id="hxWrapBEnd"></span></div>'
    NEXT='<a id="hxNext" href="HomeMore.dc.html" style="display: flex; justify-content: center; align-items: center; gap: 12px; height: 120px; background: #13203a; color: #ffffff; font-size: 18px; font-weight: 700; text-decoration: none;">The homepage continues on board 1b: industries, three steps, the method, journal and footer ⟶</a>'
    i=s.index('<div class="brs">'); s=s[:i]+A+s[i:]
    if '<div class="ft">' in s:
        a=s.index('<div class="ft">'); e=s.index('</div>',a)+6; s=s[:a]+NEXT+s[e:]
    else:
        j=s.rindex('</div>',0,s.index('</x-dc>')); s=s[:j]+NEXT+s[j:]
    if '/*hx*/' in s:
        a=s.index('/*hx*/'); e=s.index('</style>',a); s=s[:a]+CSS+s[e:]
    else:
        j=s.rfind('</style>',0,s.index('</helmet>')); s=s[:j]+CSS+s[j:]
    old="return { q, hasQ: q.length > 0, onQ: (e) => this.setState({ q: e.target.value }) };"
    new=f"const ind = (this.state && this.state.ind) || 0, sg = (this.state && this.state.sg !== undefined) ? this.state.sg : 0; const v = {{ q, hasQ: q.length > 0, onQ: (e) => this.setState({{ q: e.target.value }}) }}; for (let i = 0; i < {len(IND)}; i++) {{ v['ind' + i] = ind === i; v['indc' + i] = ind === i ? 'on' : ''; v['indp' + i] = () => this.setState({{ ind: i }}); }} for (let i = 0; i < {len(SIG)}; i++) {{ v['sgc' + i] = sg === i ? 'on' : ''; v['sgp' + i] = () => this.setState({{ sg: i }}); }} return v;"
    if old in s: s=s.replace(old,new)
    import re as _re
    s=_re.sub(r'animation:[^;}]*infinite[^;}]*;?','',s)
    open(P+'Home.dc.html','w').write(s)
    # HomeMore: same head, header, CSS and JS; body = B
    hs=s.index('<x-dc>'); he=s.index('</helmet>')+len('</helmet>')
    body_start=s.index('>',s.index('<div',he))+1
    hdr_a=s.index('<header',he); hdr_e=s.index('</header>',hdr_a)+9
    rest=s[s.index('</x-dc>'):]
    root=s[s.index('<div',he):body_start]
    more=s[:he]+'\n'+root+s[hdr_a:hdr_e]+B+'</div>\n'+rest
    more=more.replace('<title>','<title>Homepage, continued: ',1) if '<title>' in more else more
    open(P+'HomeMore.dc.html','w').write(more)
build(); print('ok')
