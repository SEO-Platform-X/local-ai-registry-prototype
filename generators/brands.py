import sys,os,re; sys.path.insert(0,'/tmp/gen')
os.chdir('/mnt/user-data/outputs/artifacts/01ea5720-d0c8-4528-b8cc-76eb1693feae/project')
S='fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"'
IC={'gym':'<path d="M3 9v6M6 7v10M18 7v10M21 9v6M6 12h12"/>','burger':'<path d="M4 10a8 5 0 0 1 16 0z"/><path d="M3 14h18M4 17h16a0 0 0 0 1 0 0 2 2 0 0 1-2 2H6a2 2 0 0 1-2-2z"/>','cart':'<path d="M3 4h2l2 11h11l2-8H6"/><circle cx="9" cy="19" r="1.5"/><circle cx="17" cy="19" r="1.5"/>','shirt':'<path d="M8 3l-5 3 2 4 3-1v12h8V9l3 1 2-4-5-3a4 4 0 0 1-8 0z"/>','drop':'<path d="M12 3s6 7 6 11a6 6 0 0 1-12 0c0-4 6-11 6-11z"/>','mountain':'<path d="M2 20l7-12 4 6 3-4 6 10z"/>','sofa':'<path d="M4 11V8a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v3"/><path d="M2 12a2 2 0 0 1 4 0v2h12v-2a2 2 0 0 1 4 0v6H2z"/>','bike':'<circle cx="6" cy="16" r="3.5"/><circle cx="18" cy="16" r="3.5"/><path d="M6 16l4-7h6l2 7M10 9l3 7"/>','leaf':'<path d="M5 19c0-9 6-14 15-14 0 9-5 15-14 15"/><path d="M5 19l8-8"/>','gem':'<path d="M6 4h12l3 5-9 11L3 9z"/><path d="M3 9h18M9 4l3 16 3-16"/>','moto':'<circle cx="5" cy="16" r="3.5"/><circle cx="19" cy="16" r="3.5"/><path d="M5 16h6l3-6h4l1 6M14 10l-2-3h-3"/>','store':'<path d="M4 9l1-5h14l1 5M4 9v11h16V9M4 9h16"/><path d="M10 20v-6h4v6"/>','beauty':'<path d="M9 3h6v5H9zM8 8h8v13H8z"/>','glasses':'<circle cx="6.5" cy="14" r="3.5"/><circle cx="17.5" cy="14" r="3.5"/><path d="M10 14h4M3 14l1-6M21 14l-1-6"/>','flame':'<path d="M12 3c1 4 5 5 5 10a5 5 0 0 1-10 0c0-3 2-4 2-7 2 1 3 3 3 5 0-3 0-5 0-8z"/>','chicken':'<path d="M14 4a4 4 0 0 1 4 4c0 3-3 4-3 7v5H9v-5c-3-1-5-3-5-6a5 5 0 0 1 10-5z"/>','yoga':'<circle cx="12" cy="5" r="2"/><path d="M4 12l8-3 8 3M12 9v6l-4 5M12 15l4 5"/>'}
B=[('equinox','Equinox','Gym','gym','#13203a'),('in-n-out','In-N-Out','Burgers','burger','#d52b1e'),('trader-joes',"Trader Joe's",'Grocery','cart','#c8102e'),
('lululemon','Lululemon','Athletic wear','shirt','#d31f37'),('lush','Lush','Bath and body','drop','#13203a'),('rei','REI','Outdoor gear','mountain','#3a6b35'),('patagonia','Patagonia','Outdoor apparel','mountain','#1f3a5f'),('ikea','IKEA','Home','sofa','#0058a3'),('supreme','Supreme','Streetwear','shirt','#ed1c24'),
('soulcycle','SoulCycle','Cycling studio','bike','#c9a400'),('aesop','Aesop','Skincare','leaf','#5b5a4e'),('kith','Kith','Streetwear','store','#13203a'),('brandy-melville','Brandy Melville','Apparel','shirt','#c2708a'),('alo-yoga','Alo Yoga','Yoga','yoga','#13203a'),('harley-davidson','Harley-Davidson','Motorcycles','moto','#e36a16'),
('costco','Costco','Warehouse club','cart','#0060a9'),('sephora','Sephora','Beauty','beauty','#13203a'),('warby-parker','Warby Parker','Eyewear','glasses','#1e5aa0'),('chrome-hearts','Chrome Hearts','Jewelry','gem','#13203a'),("barrys","Barry's",'Fitness','flame','#e2231a'),('chick-fil-a','Chick-fil-A','Restaurant','chicken','#dd0031')]
def ico(k,s=28): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" {S} aria-hidden="true">{IC[k]}</svg>'
def card(slug,n,cat,k,col,big=False):
    r,g,b=int(col[1:3],16),int(col[3:5],16),int(col[5:7],16); tint=f'rgb({round(r*0.12+255*0.88)}, {round(g*0.12+255*0.88)}, {round(b*0.12+255*0.88)})'
    return f'<a href="ExploreSearch.dc.html" class="bcard{" big" if big else ""}" data-logo="logos/{slug}.svg"><span class="bstripe" style="background: {col};"></span><span class="blogo" style="color: {col}; background: {tint};">{ico(k,42 if big else 32)}</span><span class="bname{" long" if len(n)>=12 and not big else ""}">{n}</span><span class="bfoot"><span>{cat}</span><span class="bok">✓ On the registry</span></span></a>'
cells=''.join(card(*b,big=i<2) for i,b in enumerate(B))+'<a href="ExploreSearch.dc.html" class="bcard more"><span class="bname long" style="color: #ffffff;">+ 12,400 more</span><span class="bfoot" style="color: #c9d0dc;"><span>41 cities</span><span style="color: #ffffff; text-transform: none; letter-spacing: 0;">Find yours ⟶</span></span></a>'
CSS='''/*brands*/.brs{padding:96px 40px;display:flex;flex-direction:column;align-items:center;gap:10px;border-top:1px solid #e4ded2;border-bottom:1px solid #e4ded2;background:#f3efe7}
.brs .ey{font-family:"Cormorant Garamond",Georgia,serif;font-style:italic;font-size:26px;color:#5b6474}
.brs h2{margin:0 0 36px;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:72px;line-height:74px;color:#13203a;text-align:center;max-width:1000px}
.brs h2 em{color:#e5482d}
.bgrid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px;width:100%;max-width:1320px}
.bcard{grid-column:span 1;position:relative;overflow:hidden;display:flex;flex-direction:column;gap:14px;min-height:250px;padding:30px 26px 22px;border-radius:14px;background:#ffffff;border:1px solid #e4ded2;text-decoration:none !important;color:#13203a;box-sizing:border-box;transition:transform .15s,box-shadow .15s}
.bcard:hover{transform:translateY(-3px);box-shadow:0 14px 34px rgba(19,32,58,0.14)}
.bcard.big{grid-column:span 2;min-height:320px;padding:38px 34px 28px}
.bcard.more{background:#13203a;border-color:#13203a;justify-content:flex-end}
.bstripe{position:absolute;top:0;left:0;right:0;height:6px}
.blogo{width:68px;height:68px;border-radius:18px;display:flex;align-items:center;justify-content:center;}
.bcard.big .blogo{width:88px;height:88px;border-radius:22px}
.bname{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:40px;line-height:42px;margin-top:auto;white-space:nowrap}
.bcard.big .bname{font-size:72px;line-height:72px}
.bfoot{display:flex;flex-direction:column;gap:4px;font-size:12px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:#8a93a3}
.bcard.big .bfoot,.bcard.more .bfoot{flex-direction:row;justify-content:space-between;font-size:13px}
.bname.long{font-size:31px;line-height:34px}
.bok{color:#237233;letter-spacing:0.02em;text-transform:none;font-weight:700}
.brs .note{display:none}
'''
def block(h,ey,note): return f'<div class="brs"><span class="ey">{ey}</span><h2>{h}</h2><div class="bgrid">{cells}</div><span class="note">{note}</span></div>'
def put(f,html):
    s=open(f).read()
    a=s.index('<div class="brs">'); e=s.index('</span></div>',s.index('class="note"',a))+len('</span></div>'); s=s[:a]+html+s[e:]
    a=s.index('/*brands*/'); e=s.index('</style>',a); s=s[:a]+CSS+s[e:]
    open(f,'w').write(s)
put('Home.dc.html',block('The places you know are <em>already here</em>.','On the registry','And 12,400 local businesses in 41 cities. Tap one to see what locals say.'))
put('Business.dc.html',block('Your neighbors are <em>already on it</em>.','On the registry','Every one of these has a record AI reads. Yours does too. Claim it.'))
print('ok')
