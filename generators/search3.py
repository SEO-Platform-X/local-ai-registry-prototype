import re,json
P='/mnt/user-data/outputs/artifacts/01ea5720-d0c8-4528-b8cc-76eb1693feae/project/'
T=open(P+'Types.dc.html').read()
he=T.index('</header>')+9; end=T.rindex('</x-dc>')
root_close=T.rindex('</div>',0,end)  # closes the page root
CSS='''/*s3*/
.s3{max-width:1180px;margin:0 auto;padding:28px 40px 70px;display:flex;flex-direction:column;gap:22px}
.s3-bar{display:flex;gap:10px;align-items:center}
.s3-city{height:48px;padding:0 16px;border-radius:24px;border:1px solid #e4ded2;background:#fff;display:inline-flex;align-items:center;gap:6px;font-size:14px;font-weight:700;color:#13203a}
.s3-q{flex:1;height:48px;border-radius:24px;border:1px solid #e4ded2;background:#fff;display:flex;align-items:center;padding:0 18px;font-size:16px;color:#13203a;box-shadow:0 6px 18px rgba(19,32,58,0.06)}
.s3 h1{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:48px;line-height:52px;color:#13203a}.s3 h1 em{color:#e5482d}
.s3-g{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:26px;align-items:start}
.s3-card{background:#fff;border:1px solid #e4ded2;border-radius:16px;padding:20px 22px;display:flex;flex-direction:column;gap:12px}
.s3-lb{font-size:11px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#8a93a3}
.s3-sum{background:#13203a;color:#fff;border-color:#13203a}.s3-sum p{margin:0;font-size:17px;line-height:27px}.s3-sum .s3-lb{color:#aeb6c6}
.s3-a{display:flex;gap:14px;padding:12px 0;border-top:1px solid #f0ebe1;text-decoration:none !important;color:#13203a}
.s3-v{width:34px;display:flex;flex-direction:column;align-items:center;font-size:13px;color:#e5482d;flex-shrink:0}.s3-v b{color:#13203a}
.s3-a,.s3-p,.sf-rule{font-weight:400}.s3-a .s3t{display:flex;flex-direction:column;gap:4px}.s3-a .s3q{font-size:13px;color:#5b6474;border:none;padding:0}.s3-a .s3x{font-size:16px;line-height:23px;color:#13203a}.s3-a .s3m{font-size:12px;color:#8a93a3}
.s3-w{font-size:10px;font-weight:700;text-transform:uppercase;color:#a8452c;margin-left:4px}
.s3-p{display:flex;align-items:center;gap:12px;padding:10px 0;border-top:1px solid #f0ebe1;text-decoration:none !important;color:#13203a}
.s3-av{width:40px;height:40px;border-radius:10px;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px;flex-shrink:0}
.s3-p .s3n{flex:1;display:flex;flex-direction:column}.s3-p .s3n b{font-size:15px}.s3-p .s3n > span{font-size:12px;color:#5b6474}
.s3-go{font-size:13px;font-weight:700;color:#2b59d9;white-space:nowrap}
.s3-ask{background:#fbf4ea;border-color:#f0dcc4}
.s3-btn{align-self:flex-start;height:44px;padding:0 20px;border-radius:22px;background:#13203a;color:#fff !important;display:inline-flex;align-items:center;font-size:14px;font-weight:700;text-decoration:none !important}
.s3-mk{display:inline-block;width:8px;height:8px;border-radius:50%;margin-left:4px}
/* flow map */
.sf{max-width:1320px;margin:0 auto;padding:30px 40px 70px;display:flex;flex-direction:column;gap:22px}
.sf h1{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:46px;color:#13203a}
.sf-g{display:grid;grid-template-columns:420px minmax(0,1fr);gap:40px;align-items:start}
.sf-dd{background:#fff;border:1px solid #e4ded2;border-radius:16px;box-shadow:0 20px 50px rgba(19,32,58,0.10);overflow:hidden}
.sf-in{padding:14px 18px;border-bottom:1px solid #f0ebe1;font-size:16px;color:#13203a;display:flex;gap:8px;align-items:center}
.sf-h{display:block;padding:10px 18px 4px;font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#8a93a3}
.sf-r{display:flex;align-items:center;gap:10px;padding:9px 18px;font-size:14px;color:#13203a}.sf-r .ic{width:28px;height:28px;border-radius:8px;background:#f3efe7;display:flex;align-items:center;justify-content:center;font-size:13px;flex-shrink:0}
.sf-r .n{flex:1;display:flex;flex-direction:column}.sf-r .n span{font-size:12px;color:#8a93a3}
.sf-tag{font-size:11px;font-weight:700;color:#fff;border-radius:10px;padding:3px 8px}
.sf-rules{display:flex;flex-direction:column;gap:12px}
.sf-rule{display:grid;grid-template-columns:34px 220px minmax(0,1fr) 170px;gap:14px;align-items:center;background:#fff;border:1px solid #e4ded2;border-radius:14px;padding:14px 18px;text-decoration:none !important;color:#13203a}
.sf-rule .k{width:30px;height:30px;border-radius:50%;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px}
.sf-rule b{font-size:15px}.sf-rule span{font-size:14px;line-height:21px;color:#3d4658}.sf-rule .go{font-size:13px;font-weight:700;color:#2b59d9;text-align:right}
'''
def page(title,body):
    s=T[:he]+body+T[root_close:]
    s=re.sub(r'<title>[^<]*</title>',f'<title>{title}</title>',s,1)
    s=s.replace('</style>',CSS+'</style>',1)
    return s
MK=lambda c: f'<span class="s3-mk" style="background: {c};"></span>'
ANS=[(31,'First time getting lip filler. Who will not overdo it?','aisha_m','went','Dr. Nair at Lumen talked me down to half a syringe. Looked like me, just better.','23 answers · Beauty'),
     (22,'Natural lip filler that does not look done?','maria_k','went','Ask for "just hydration" at Lumen. They go slow and book a free touch-up at two weeks.','14 answers · Beauty'),
     (17,'Is Glow Bar good for filler or just facials?','spectrum_regular','went','Great for facials. For lips I went to Lumen, and Glow Bar sent me there themselves.','9 answers · Beauty'),
     (9,'How much is lip filler in Irvine right now?','new_in_tustin','local','Most places near Spectrum charge $450 to $700 a syringe. Lumen credits the $75 consult.','6 answers · Beauty')]
ans=''.join(f'<a href="Thread.dc.html" class="s3-a"><span class="s3-v">▲<b>{v}</b></span><span class="s3t"><span class="s3q">{q}</span><span class="s3x"><b>{u}</b><span class="s3-w">{w}</span> "{x}"</span><span class="s3m">{m}</span></span></a>' for v,q,u,w,x,m in ANS)
PL=[('LA','#13203a','Lumen Aesthetics','Med spa · Irvine Spectrum · Named in 31 answers','Main.dc.html','#237233'),('GB','#c2708a','Glow Bar Irvine','Med spa · Irvine · Named in 6 answers','Main.dc.html','#e8740c'),('CM','#2b59d9','Coastline MedSpa','Med spa · Newport Beach · Named in 4 answers','Main.dc.html','#237233')]
pl=''.join(f'<a href="{h}" class="s3-p"><span class="s3-av" style="background: {c};">{i}</span><span class="s3n"><b>{n}{MK(mk)}</b><span>{d}</span></span><span class="s3-go">View ›</span></a>' for i,c,n,d,h,mk in PL)
Q=f'''<div class="s3"><div class="s3-bar"><span class="s3-city">⌖ Irvine, CA ▾</span><span class="s3-q">natural lip filler</span></div>
<h1>What locals say about <em>natural lip filler</em></h1>
<div class="s3-g"><div style="display: flex; flex-direction: column; gap: 18px;">
<div class="s3-card s3-sum"><span class="s3-lb">The short answer · from 52 local answers</span><p>Most locals point to <b>Lumen Aesthetics</b> at Irvine Spectrum. The same three tips come up again and again: book a consult first, ask for Dr. Nair, and start with half a syringe.</p></div>
<div class="s3-card"><span class="s3-lb">Answers from people who went</span>{ans}<a href="Explore.dc.html" class="s3-go" style="padding-top: 6px;">See all 18 conversations ›</a></div>
</div><div style="display: flex; flex-direction: column; gap: 18px;">
<div class="s3-card"><span class="s3-lb">Places locals named</span>{pl}<a href="BestOf.dc.html" class="s3-go" style="padding-top: 6px; text-decoration: none;">Best med spas in Irvine ›</a></div>
<div class="s3-card s3-ask"><b style="font-size: 16px;">Still not sure?</b><span style="font-size: 14px; color: #3d4658;">Ask Irvine. Locals usually answer within a few hours. No account needed.</span><a href="Post.dc.html" class="s3-btn">Ask locals</a></div>
</div></div></div>'''
def rule(k,c,what,how,go,href): return f'<a href="{href}" class="sf-rule"><span class="k" style="background: {c};">{k}</span><b>{what}</b><span>{how}</span><span class="go">{go} ›</span></a>'
FL=f'''<div class="sf"><span class="s3-lb">Storyboard · search</span><h1>What happens when you search</h1><span style="font-size: 15px; color: #3d4658; max-width: 820px;">One box on the homepage and in the header. As you type, it suggests four kinds of result. Each kind always goes to the same place.</span>
<div class="sf-g"><div class="sf-dd"><div class="sf-in">⌕ <b>lumen</b></div>
<span class="sf-h">Businesses</span><div class="sf-r"><span class="ic">✦</span><span class="n"><b>Lumen Aesthetics</b><span>Med spa · Irvine Spectrum</span></span><span class="sf-tag" style="background: #13203a;">1</span></div><div class="sf-r"><span class="ic">✦</span><span class="n"><b>Lumen Eye Care</b><span>Eye doctor · Costa Mesa</span></span><span class="sf-tag" style="background: #13203a;">1</span></div>
<span class="sf-h">Cities</span><div class="sf-r"><span class="ic">⌖</span><span class="n"><b>Irvine, CA</b><span>4,812 neighbors · 1,904 conversations</span></span><span class="sf-tag" style="background: #2b59d9;">2</span></div>
<span class="sf-h">Types</span><div class="sf-r"><span class="ic">▦</span><span class="n"><b>Med spas in Irvine</b><span>148 places</span></span><span class="sf-tag" style="background: #237233;">3</span></div>
<span class="sf-h">Ask locals</span><div class="sf-r" style="padding-bottom: 14px;"><span class="ic">?</span><span class="n"><b>"lumen" in Irvine conversations</b><span>Press Enter to see answers</span></span><span class="sf-tag" style="background: #e5482d;">4</span></div></div>
<div class="sf-rules">
{rule('1','#13203a','Click a business','Goes straight to its page: facts with their marks, what locals say, photos. If the business is not on the registry yet, the page offers "Add it" and "Ask locals about it."','Business page','Main.dc.html')}
{rule('2','#2b59d9','Click a city','Opens that city: a map of what people are talking about, the live feed of questions and tips, and the categories. Your city is remembered for next time.','City page','Explore.dc.html')}
{rule('3','#237233','Click a type','Opens the best-of list for that type in that city, ranked by what locals say and what owners confirm. Nobody can pay to rank.','Best-of list','BestOf.dc.html')}
{rule('4','#e5482d','Press Enter','A name ("lumen") shows matching places on the map. A question ("natural lip filler") shows the short answer from locals, their top answers, and the places they named.','Results','QResults.dc.html')}
{rule('5','#8a93a3','No match or a typo','Suggests the closest name ("Did you mean Lumen Aesthetics?"). If nothing matches, offers "Add it" for owners and "Ask locals" for everyone.','Edge cases','Search.dc.html')}
</div></div></div>'''
open(P+'QResults.dc.html','w').write(page('Search results: a question',Q))
open(P+'SearchFlow.dc.html','w').write(page('What happens when you search',FL))
# homepage dropdown: business goes to its page; add types and ask locals
h=open(P+'Home.dc.html').read()
print('biz links',h.count('<a href="ExploreLumen.dc.html"><span class="ic">✦</span>'))
h=h.replace('<a href="ExploreLumen.dc.html"><span class="ic">✦</span>','<a href="Main.dc.html"><span class="ic">✦</span>')
CITY='<span class="mu" style="font-size: 13px;">4,812 neighbors · 1,904 conversations</span></span></a>'
if 'id="sugTypes"' not in h:
    h=h.replace(CITY,CITY+'<span class="h" style="display: block;" id="sugTypes">Types</span><a href="BestOf.dc.html"><span class="ic">▦</span><span style="display: flex; flex-direction: column;"><strong>Med spas in Irvine</strong><span class="mu" style="font-size: 13px;">148 places</span></span></a><span class="h" style="display: block;">Ask locals</span><a href="QResults.dc.html"><span class="ic">?</span><span style="display: flex; flex-direction: column;"><strong>See what locals say</strong><span class="mu" style="font-size: 13px;">Press Enter for answers</span></span></a>',1)
open(P+'Home.dc.html','w').write(h)
print('done', h.count('sugTypes'))
