import sys,json
exec(open('/tmp/gen/m/base.py').read())
for f in sys.argv[1:]: exec(open(f).read())
c=json.load(open(P+'canvas.json'))
x0=20400; y=0
for fn,t,w,h in BOARDS:
    ex=c['boards'].get(fn)
    c['boards'][fn]={'expand':'fill','h':h,'is_interactive':True,'title':t,'w':w,'x':ex['x'] if ex else x0,'y':ex['y'] if ex else None}
    if fn not in c['order']: c['order'].append(fn)
# stack mobile boards vertically
yy=0
for fn in [o for o in c['order'] if o.startswith('M') and o[1].isupper() and c['boards'][o].get('x')==x0 or (o.startswith('M') and o[1].isupper() and o not in ('Main.dc.html','Me.dc.html','Moderation.dc.html','MonthReport.dc.html'))]:
    b=c['boards'][fn]; b['x']=x0; b['y']=yy; yy+=b['h']+300
json.dump(c,open(P+'canvas.json','w'))
print([b[0] for b in BOARDS])
