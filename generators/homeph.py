import re
P='/mnt/user-data/outputs/artifacts/01ea5720-d0c8-4528-b8cc-76eb1693feae/project/'
s=open(P+'Home.dc.html').read()
while 'id="hxWrapA"' in s:
    a=s.index('<div id="hxWrapA"'); e=s.index('<span id="hxWrapAEnd"></span></div>',a)+len('<span id="hxWrapAEnd"></span></div>'); s=s[:a]+s[e:]
for idm in ['hxNext','phSections','phFooter']:
    while f'id="{idm}"' in s:
        a=s.rindex('<',0,s.index(f'id="{idm}"')); tag=s[a+1:s.index(' ',a)]
        e=s.index(f'</{tag}>',a)+len(tag)+3
        # find matching close for div blocks
        if tag=='div':
            depth=0
            for m in re.finditer(r'<(/?)div\b[^>]*>',s[a:]):
                depth+= -1 if m.group(1) else 1
                if depth==0: e=a+m.end(); break
        s=s[:a]+s[e:]
if '/*hx*/' in s:
    a=s.index('/*hx*/'); e=s.index('</style>',a); s=s[:a]+s[e:]
s=re.sub(r"const ind = \(this\.state && this\.state\.ind\).*?return v;","return { q, hasQ: q.length > 0, onQ: (e) => this.setState({ q: e.target.value }) };",s,flags=re.S)
def ph(idn,label,title,lines,dark=False):
    bg='#13203a' if dark else '#ece6da'; fg='#ffffff' if dark else '#13203a'; bd='#3a4763' if dark else '#b9b0a0'
    li=''.join(f'<li>{x}</li>' for x in lines)
    return f'<div id="{idn}" style="margin: 48px 64px; padding: 64px; border: 3px dashed {bd}; border-radius: 12px; background: {bg}; color: {fg}; display: flex; flex-direction: column; gap: 14px; align-items: flex-start;"><span style="font-size: 12px; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; opacity: 0.7;">{label}</span><span style="font-family: \'Cormorant Garamond\', Georgia, serif; font-size: 56px; line-height: 58px;">{title}</span><span style="font-size: 17px; line-height: 27px; max-width: 900px; opacity: 0.85;">Copy these straight from today\'s live homepage at localairegistry.com, same order, same animations. Do not redesign them.</span><ul style="margin: 6px 0 0; padding-left: 22px; font-size: 16px; line-height: 28px; opacity: 0.85;">{li}</ul></div>'
SEC=ph('phSections','Placeholder for the developer','Insert current homepage sections here',['The shift (scrolling storefront plates)','The findings: 73%','The industries we watch closest (leaderboard tabs)','Three steps, and it is free','The method: eight signals','Customer quote (QUIKTOX)','The journal','Find out what AI says about you (final search)'])
FOOT=ph('phFooter','Placeholder for the developer','Insert current footer here',['Sign up for updates','The registry, For owners, Company, Resources link columns','73% disclaimer, legal links, social links'],dark=True)
# insert sections placeholder before trending? place after trending, replace small footer
if '<div class="ft">' in s:
    a=s.index('<div class="ft">'); e=s.index('</div>',a)+6; s=s[:a]+SEC+FOOT+s[e:]
else:
    j=s.rindex('</div>',0,s.index('</x-dc>')); s=s[:j]+SEC+FOOT+s[j:]
open(P+'Home.dc.html','w').write(s)
print('ok', 'hx-' in s, s.count('phSections'), len(s))
