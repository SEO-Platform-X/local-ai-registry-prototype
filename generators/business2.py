import sys; sys.path.insert(0,'/tmp/gen'); from common import *
SERIF='family=Figtree:wght@400;500;600;700;800&amp;family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&amp;display=swap'
CHK='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#237233" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5 9-10"></path></svg>'
NO='<span style="color: #c8c8c8; font-size: 18px; line-height: 1;">·</span>'
CSS=HNL_CSS+'.sec,.ft,header{flex-shrink:0}\n'+r'''.srf{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;letter-spacing:-0.01em;color:#13203a}
.srf em{font-style:italic;color:#ff5a3c}
.nl{font-size:14px;font-weight:600;color:#222222;text-decoration:none}
.sec{padding:72px 120px;display:flex;flex-direction:column;gap:28px}
.eyb{font-size:12px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:#a8452c}
.h2x{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-size:52px;line-height:54px;font-weight:500;color:#13203a;max-width:900px}
.h2x em{font-style:italic;color:#ff5a3c}
.lead{font-size:17px;line-height:27px;color:#484848;max-width:760px;margin:0}
.pil{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.pil div{display:flex;flex-direction:column;gap:10px;padding:28px;border-radius:18px;background:#ffffff;border:1px solid #e6e0d4}
.pil .n{font-family:"Cormorant Garamond",Georgia,serif;font-size:44px;line-height:44px;color:#ff5a3c;font-weight:600}
.pil strong{font-size:19px;line-height:25px}
.pil p{margin:0;font-size:15px;line-height:23px;color:#484848}
.cmp{width:100%;border-collapse:collapse;font-size:15px}
.cmp th{text-align:left;padding:14px 16px;font-size:13px;color:#6a6a6a;font-weight:600;border-bottom:1px solid #e3e3e3}
.cmp th.us{color:#13203a;font-weight:800;background:#fdece6;border-radius:12px 12px 0 0}
.cmp td{padding:14px 16px;border-bottom:1px solid #efefef}
.cmp td.us{background:#fff6f2}
.fg{display:grid;grid-template-columns:repeat(2,1fr);gap:24px}
.fc{display:flex;flex-direction:column;gap:12px;padding:20px 22px 24px;border-radius:16px;border:1px solid #e6e6e6;background:#ffffff}
.fc .t{display:flex;justify-content:space-between;align-items:center;gap:10px}
.fc strong{font-size:17px}
.fc p{margin:0;font-size:14px;line-height:21px;color:#484848}
.tier{display:inline-flex;align-items:center;height:22px;padding:0 9px;border-radius:11px;font-size:11px;font-weight:700;white-space:nowrap}
.t0{background:#eeeeee;color:#484848}.t1{background:#e3eefc;color:#134a91}.t2{background:#e3f4e6;color:#1c5f2a}.t3{background:#13203a;color:#ffffff}
.plans{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.pl{display:flex;flex-direction:column;gap:12px;padding:26px;border-radius:18px;border:1px solid #e3e3e3;background:#ffffff}
.pl.hot{border:2px solid #13203a;box-shadow:0 10px 30px rgba(19,32,58,0.12)}
.pl h4{margin:0;font-size:20px}
.pl .pr{font-family:"Cormorant Garamond",Georgia,serif;font-size:36px;line-height:38px;color:#13203a;font-weight:600}
.pl ul{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:8px;font-size:14px;line-height:20px;color:#484848}
.pl li{display:flex;gap:8px}
.stp{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.stp div{display:flex;flex-direction:column;gap:8px;padding:22px;border-top:3px solid #13203a}
.stp b{font-size:13px;color:#a8452c;letter-spacing:0.06em}
.look{display:flex;align-items:center;gap:12px;width:620px;height:62px;padding:0 8px 0 22px;border-radius:31px;background:#ffffff;box-shadow:0 8px 30px rgba(19,32,58,0.14);box-sizing:border-box}
.look input{flex-grow:1;border:none;outline:none;font-family:inherit;font-size:16px;background:transparent}
.ft{padding:28px 120px;border-top:1px solid #ebebeb;display:flex;justify-content:space-between;font-size:13px;color:#6a6a6a}
'''
feat=[
 ('t0','Free','Your page, claimed','Take control of the page that already exists and edit every fact.'),
 ('t0','Free','AI Score and prompts','See what ChatGPT, Gemini and Claude say about you, and who they name instead.'),
 ('t0','Free','Answer your neighbors','Owner answers go to the top of every thread.'),
 ('t1','Fix','Directory submissions every day','A new directory every day, so every source AI reads has your facts.'),
 ('t2','Trust','Negative review disputes','We dispute reviews that break platform rules.'),
 ('t2','Trust','Autopilot review replies and answers','Replies and answers in your voice, following your AI notes.'),
 ('t2','Trust','Press releases','Your news, sent to outlets AI cites.'),
 ('t2','Trust','AI code on your photos','What, where and who on every photo, in the format AI reads.'),
 ('t2','Trust','Google posts and optimization','Weekly posts and a fully tuned Google Business Profile.'),
 ('t2','Trust','Review link and velocity check','One link for happy customers, and a check that reviews keep coming.'),
 ('t3','Authority','Technical and speed fixes','Broken links, redirects and mobile speed on your site.'),
 ('t3','Authority','URL restructuring and topical map','One page per treatment, mapped to every topic AI connects to you.'),
 ('t3','Authority','Semantic content and cannibalization fix','Pages rewritten around the questions people ask AI, with no overlap.'),
 ('t3','Authority','Entity mapping','You, your team and each treatment tied together across every source.'),
 ('t3','Authority','Articles and blogs','Placements and posts that AI pulls recommendations from.'),
 ('t3','Authority','Only, first and best story','The one thing only you can claim, built into every source.')]
exec(open('/tmp/gen/featsvg.py').read())
fcards=''.join(f'<div class="fc">{F.get(t,"")}<span class="t"><strong>{t}</strong><span class="tier {c}">{lbl}</span></span><p>{d}</p></div>' for c,lbl,t,d in feat)
rows=[('Shows what AI says about you',1,0,0,0),('Real neighbors answering questions about you',1,0,0,0),('Every fact marked: confirmed, visitor or AI guess',1,0,0,0),('Fixes facts at the sources AI reads',1,1,0,0),('Press releases and articles',1,1,0,0),('Review link and review replies',1,0,1,0),('Free to claim, no contract',1,0,0,1)]
ck=lambda v,us=False: f'<td class="{"us" if us else ""}">{CHK if v else NO}</td>'
trs=''.join(f'<tr><td>{r[0]}</td>{ck(r[1],True)}{ck(r[2])}{ck(r[3])}{ck(r[4])}</tr>' for r in rows)
def plan(name,price,sub,items,hot=False,cta='Start',tag=''):
    li=''.join(f'<li>{CHK}<span>{i}</span></li>' for i in items)
    return f'<div class="pl {"hot" if hot else ""}"><span style="display: flex; justify-content: space-between; align-items: center;"><h4>{name}</h4>{tag}</span><span class="pr">{price}</span><span class="mu" style="font-size: 13px;">{sub}</span><ul>{li}</ul><a href="{"Main.dc.html" if price=="Free" else "Upgrade.dc.html"}" class="btn {"b-dark" if hot else ""}" style="margin-top: auto;">{cta}</a></div>'
plans=plan('Get listed','Free','Forever',['Claim and edit your page','AI Score and prompts','Answer questions from locals'],cta='Claim your page')+\
 plan('Fix','$500','a month · no contract',['Everything in Get listed','Directory submissions every day'])+\
 plan('Trust','$1,500','a month · no contract',['Everything in Fix','Negative review disputes','Autopilot review replies and answers','Press releases','AI code on photos','Google posts and optimization','Review link and velocity check'],hot=True,tag='<span class="tier t2">Most picked</span>')+\
 plan('Authority','$3,000','a month · no contract',['Everything in Trust','Technical and speed fixes','URL restructuring and topical map','Semantic content, entity mapping','Articles and blogs','Only, first and best story'],cta='Talk to us')
BODY=header('<a href="Explore.dc.html" class="hnl">Explore</a><a href="#plans" class="hnl">Plans</a><a href="#" class="hnl">Sign in</a><a href="Main.dc.html" class="btn b-sm b-coral" style="margin-left: 6px;">Claim your page</a>')+f'''
<div class="sec" style="background: #f3f0ea; align-items: flex-start; padding-top: 88px; padding-bottom: 80px;"><span class="eyb">For business owners</span><h1 class="srf" style="margin: 0; font-size: 72px; line-height: 74px; max-width: 1000px;">Get your business into <em>AI answers</em>.</h1><p class="lead">People ask ChatGPT, Gemini and Claude who to go to. They answer from what they can read and trust. Local AI Registry is the source they trust for local businesses, and your page is already live on it.</p>
<label class="look"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#222222" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="M20 20l-4-4"></path></svg><input type="text" placeholder="Your business name and city" aria-label="Your business"><a href="Audit.dc.html" class="btn b-coral" style="border-radius: 24px; height: 48px;">See what AI says</a></label>
<span style="display: flex; gap: 28px; align-items: center; font-size: 13px; color: #6a6a6a; padding-top: 8px;"><span><strong style="color: #13203a; font-size: 22px;">73%</strong> of local businesses are never recommended by AI</span><span>·</span><span>As covered in <strong style="color: #13203a;">USA Today</strong></span><span>·</span><span>Free to claim, no credit card</span></span></div>
<div class="sec"><span class="eyb">Why AI trusts the registry</span><h2 class="h2x">AI repeats what <em>real people</em> and real sources agree on.</h2>
<div class="pil"><div><span class="n">01</span><strong>Real neighbors, not marketing copy</strong><p>Locals ask, answer and give heads-ups about your business, dated and firsthand. That is the kind of authentic signal AI weighs most, and no agency can fake it.</p></div><div><span class="n">02</span><strong>Every fact is marked</strong><p>Confirmed, visitor submitted or AI guess, with the source and the date. AI can tell what is checked, so it trusts the checked facts on your page.</p></div><div><span class="n">03</span><strong>Built to be read by machines</strong><p>Every page ships with clean structured data, references and a machine-readable version. The registry itself is a source AI engines already cite.</p></div></div></div>
<div class="sec" style="background: #fbfaf8;"><span class="eyb">Why not the usual options</span><h2 class="h2x">Agencies chase rankings. We fix <em>what AI says</em>.</h2>
<table class="cmp"><tr><th></th><th class="us">Local AI Registry</th><th>SEO agency</th><th>Review tools</th><th>Directories</th></tr>{trs}</table></div>
<div class="sec"><span class="eyb">Everything we do</span><h2 class="h2x">One page, and all the work behind it.</h2><div class="fg">{fcards}</div></div>
<div class="sec" id="plans" style="background: #f3f0ea;"><span class="eyb">Plans</span><h2 class="h2x">Start free. Add work <em>when you see the gap</em>.</h2><p class="lead">Every plan includes everything below it. No contracts, cancel anytime.</p><div class="plans">{plans}</div></div>
<div class="sec"><span class="eyb">How it works</span><div class="stp"><div><b>STEP 1</b><strong style="font-size: 18px;">Find your page</strong><span class="mu" style="font-size: 14px; line-height: 21px;">It is already live, built from what AI and your neighbors say.</span></div><div><b>STEP 2</b><strong style="font-size: 18px;">Claim it free</strong><span class="mu" style="font-size: 14px; line-height: 21px;">Email and phone, then a code by text.</span></div><div><b>STEP 3</b><strong style="font-size: 18px;">Confirm your info</strong><span class="mu" style="font-size: 14px; line-height: 21px;">Confirm or fix what AI guessed, in a few minutes.</span></div><div><b>STEP 4</b><strong style="font-size: 18px;">Stay free or add a plan</strong><span class="mu" style="font-size: 14px; line-height: 21px;">We do the work, you approve it.</span></div></div>
<div style="display: flex; align-items: center; justify-content: space-between; gap: 24px; padding: 32px 36px; border-radius: 20px; background: #13203a; color: #ffffff; margin-top: 12px;"><span style="display: flex; flex-direction: column; gap: 6px;"><strong style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: 36px; font-weight: 500;">See what AI says about you.</strong><span style="color: #c3c9d6; font-size: 15px;">It takes a minute, and it is free.</span></span><a href="Audit.dc.html" class="btn b-coral">Look up your business</a></div></div>
<div class="ft"><span>Local AI Registry · Irvine, California</span><span><a href="Home.dc.html" style="color: #6a6a6a;">Home</a> · Privacy · Terms</span></div>'''
out=page('Local AI Registry for business: get into AI answers',CSS,BODY,'    return {};')
out=out.replace('family=Figtree:wght@400;500;600;700;800&amp;display=swap',SERIF)
open(P+'Business.dc.html','w').write(out); print('ok', out.count('\u2014'), out.count('<table'))
