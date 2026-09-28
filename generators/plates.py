# Line-engraving style storefront plates (stand-ins for /images/brand/plates/*.webp)
N='#13203a'
def defs(uid):
    return f'''<defs><pattern id="h{uid}" width="4" height="4" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="4" stroke="{N}" stroke-width="0.7"/></pattern><pattern id="v{uid}" width="3" height="3" patternUnits="userSpaceOnUse"><line x1="0" y1="0" x2="0" y2="3" stroke="{N}" stroke-width="0.6"/></pattern><pattern id="x{uid}" width="5" height="5" patternUnits="userSpaceOnUse"><path d="M0 0L5 5M5 0L0 5" stroke="{N}" stroke-width="0.5"/></pattern></defs>'''
ITEM={
'coffee':'<path d="M-14 -6h22v12a11 11 0 0 1-22 0z"/><path d="M8 -2h5a5 5 0 0 1 0 10h-5"/><path d="M-8 -16c0-4 4-4 4-8M0 -16c0-4 4-4 4-8"/>',
'dental':'<path d="M-14 -14c6-4 10 0 14 0s8-4 14 0c4 4 2 14-2 22-2 6-4 12-6 12s-3-12-6-12-4 12-6 12-4-6-6-12c-4-8-6-18-2-22z"/>',
'salon':'<circle cx="-8" cy="10" r="6"/><circle cx="8" cy="10" r="6"/><path d="M-4 5L10 -20M4 5L-10 -20"/>',
'optometry':'<circle cx="-11" cy="0" r="9"/><circle cx="11" cy="0" r="9"/><path d="M-2 0h4M-20 -2l-6-6M20 -2l6-6"/>',
'restaurant':'<path d="M-12 -20v14a4 4 0 0 0 8 0v-14M-8 -6v28"/><path d="M10 -20c-6 4-6 16 0 18v24"/>',
'surgeon':'<path d="M-4 -20h8v16h16v8h-16v16h-8v-16h-16v-8h16z"/>',
'dispensary':'<path d="M0 22V-4M0 -4c-2-10 0-18 0-22 0 4 2 12 0 22zM0 -2c-8-6-16-6-20-6 4 2 12 6 20 8zM0 -2c8-6 16-6 20-6-4 2-12 6-20 8zM0 4c-6-2-12 0-16 2 4 0 10 0 16-2zM0 4c6-2 12 0 16 2-4 0-10 0-16-2z"/>',
}
SIGN={'coffee':'COFFEE','dental':'DENTAL','salon':'SALON','optometry':'OPTOMETRY','restaurant':'KITCHEN','surgeon':'SURGERY','dispensary':'DISPENSARY'}
def plate(kind,uid,w=320,h=230,num=None):
    it=ITEM[kind]; sg=SIGN[kind]
    hatch=''.join(f'<path d="M{x} 214l14-14"/>' for x in range(0,320,10))
    awn=''.join(f'<path d="M{60+i*12} 26l-6 22"/>' for i in range(18))
    door=''.join(f'<path d="M190 {110+i*14}h54"/>' for i in range(7))
    num_svg=f'<circle cx="274" cy="44" r="22" fill="#e5482d" stroke="#e5482d"/><text x="274" y="51" font-family="Cormorant Garamond,Georgia,serif" font-size="22" text-anchor="middle" fill="#fff" stroke="none">{num}</text>' if num else ''
    return f'''<svg viewBox="0 0 320 230" width="{w}" height="{h}" aria-hidden="true" fill="none" stroke="{N}" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round"><g stroke-width="0.6" opacity="0.5">{hatch}</g><path d="M0 214h320" stroke-width="1.4"/>
<rect x="46" y="50" width="228" height="164" fill="#fbf6ec"/><path d="M36 50h248l-10-26H46z" fill="#efe6d6"/><g stroke-width="0.6" opacity="0.55">{awn}</g>
<path d="M36 50q15 14 31 0q15 14 31 0q15 14 31 0q15 14 31 0q15 14 31 0q15 14 31 0q15 14 31 0q15 14 32 0" fill="#fbf6ec"/>
<rect x="96" y="8" width="128" height="18" fill="#fbf6ec"/><text x="160" y="21" font-family="Figtree,sans-serif" font-size="10" font-weight="700" letter-spacing="3" text-anchor="middle" fill="{N}" stroke="none">{sg}</text>
<rect x="60" y="82" width="104" height="92" fill="#ffffff"/><path d="M60 128h104M112 82v92" stroke-width="0.9"/>
<g transform="translate(112 128) scale(1.6)" stroke-width="1.1" fill="#fbf6ec">{it}</g>
<rect x="186" y="96" width="62" height="118" fill="#f3ede1"/><g stroke-width="0.5" opacity="0.45">{door}</g><circle cx="238" cy="158" r="2.4" fill="{N}"/>
<path d="M56 174h112v10H56z" fill="#e4dccb"/>
<path d="M16 214v-38a10 10 0 0 1 20 0v38" fill="#efe6d6"/><path d="M292 214v-44l10-10 10 10v44" fill="#efe6d6"/>{num_svg}</svg>'''
def street(uid):
    shops=['coffee','dental','salon','optometry','restaurant']
    g=''
    for i,s in enumerate(shops):
        num=('0'+str(i+1)) if i<3 else None
        g+='<g transform="translate(%d %d) scale(0.6)">%s</g>'%(i*190, 0, plate(s,uid+str(i),320,230,num=num))
    return '<svg viewBox="0 0 960 170" width="100%" aria-hidden="true">'+g+'<path d="M0 168h960" stroke="#13203a" stroke-width="1.4"/></svg>'
