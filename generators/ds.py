import glob,os,re
DS='''
/*ds:lair*/.btn{border-radius:9999px !important;font-weight:600 !important;box-shadow:none !important;letter-spacing:0 !important;background-image:none !important}
.btn.b-dark,.btn.b-coral,.btn.grad,.btn.b-lock,.grad{background:#13203a !important;background-image:none !important;color:#ffffff !important;border-color:#13203a !important}
.btn:not(.b-dark):not(.b-coral):not(.grad):not(.b-lock){background:#ffffff !important;border:1px solid #13203a !important;color:#13203a !important}
h1{font-family:"Cormorant Garamond",Georgia,serif !important;font-weight:500 !important;letter-spacing:0 !important}
body{font-family:Figtree,"Helvetica Neue",Helvetica,sans-serif}
'''
os.chdir('/mnt/user-data/outputs/artifacts/01ea5720-d0c8-4528-b8cc-76eb1693feae/project')
for f in glob.glob('*.dc.html'):
    s=open(f).read()
    if '/*ds:lair*/' in s: continue
    i=s.index('</helmet>'); j=s.rfind('</style>',0,i)
    if j<0: continue
    s=s[:j]+DS+s[j:]; open(f,'w').write(s)
print('ds done')
