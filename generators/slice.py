# Splits very tall boards into phone-safe parts (each part = same page source, shifted up)
import json,re,subprocess,sys
from playwright.sync_api import sync_playwright
P='/mnt/user-data/outputs/artifacts/01ea5720-d0c8-4528-b8cc-76eb1693feae/project/'
MAXH=2400
TARGETS=['Home.dc.html','Business.dc.html','OwnerPremium.dc.html']
WHOLE=['Main.dc.html','Dashboard.dc.html','Audit.dc.html','MonthReport.dc.html']  # interactive: never slice, tabs must stay on one board
c=json.load(open(P+'canvas.json'))
# drop old parts
for k in [k for k in c['boards'] if re.search(r'_p\d\.dc\.html$',k) and k.split('_p')[0]+'.dc.html' in TARGETS]:
    c['boards'].pop(k); c['order']=[o for o in c['order'] if o!=k]
made=[]
for f in TARGETS:
    subprocess.run(['python3','/tmp/rend2.py',f,'/tmp/x.png','900'],capture_output=True)
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':1440,'height':900}); pg.goto('file:///tmp/r2.html'); pg.wait_for_timeout(300)
        H=pg.evaluate("document.body.scrollHeight")
        boxes=pg.evaluate("[...document.querySelectorAll('body *')].map(e=>{const r=e.getBoundingClientRect();return [r.top+scrollY,r.bottom+scrollY,r.height]}).filter(x=>x[2]>4&&x[2]<700)")
        b.close()
    if H<=MAXH+200: 
        c['boards'][f]['h']=H; continue
    cuts=[0]
    while H-cuts[-1]>MAXH:
        t=cuts[-1]+MAXH; best=None
        for y in range(t,t-700,-8):
            n=sum(1 for a,bb,_ in boxes if a<y<bb)
            if best is None or n<best[0]: best=(n,y)
            if n==0: break
        cuts.append(best[1])
    cuts.append(H)
    src=open(P+f).read()
    stem=f[:-8]; title=re.sub(r'\s*\(part \d+ of \d+\)','',c['boards'][f]['title']); n=len(cuts)-1
    c['boards'][f]['h']=cuts[1]; c['boards'][f]['title']=f'{title} (part 1 of {n})'
    c['boards'][f].pop('expand',None)
    for i in range(1,n):
        off=cuts[i]; hh=cuts[i+1]-cuts[i]
        he=src.index('</helmet>'); j=src.index('<div',he); k=src.index('style="',j)+7
        part=src[:k]+f'margin-top: -{off}px; '+src[k:]
        pf=f'{stem}_p{i+1}.dc.html'
        open(P+pf,'w').write(part)
        c['boards'][pf]={'w':1440,'h':hh,'x':c['boards'][f]['x'],'y':0,'title':f'{title} (part {i+1} of {n})','is_interactive':True}
        o=c['order']; o.insert(o.index(f)+i,pf); made.append(pf)
    print(f,H,cuts)
# restack every column by order
cols={}
for k in c['order']: cols.setdefault(c['boards'][k]['x'],[]).append(k)
for x,ks in cols.items():
    y=0
    for k in ks: c['boards'][k]['y']=y; y+=c['boards'][k]['h']+(120 if '_p' in k else 200)
json.dump(c,open(P+'canvas.json','w'))
print('parts',made)
