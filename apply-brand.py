from pathlib import Path
from PIL import Image

root = Path('/home/ubuntu/mariana-site')
assets = root / 'assets'
source = Path('/home/ubuntu/mariana-briefing/media/image10.png')
logo = Image.open(source).convert('RGBA')
logo = logo.crop(logo.getbbox())
logo.save(assets / 'mariana-gil-logo.png', optimize=True)

page = root / 'index.html'
s = page.read_text()
s = s.replace('<span class="brand-mark" aria-hidden="true">MG</span>', '<img class="brand-logo" src="assets/mariana-gil-logo.png" alt="" width="90" height="60">')
s = s.replace('<div><div class="footer-doctor">Dra. Mariana Gil Furlanetti<small>Dermatologista</small></div></div>', '<div class="footer-identity"><img class="footer-logo" src="assets/mariana-gil-logo.png" alt="" width="110" height="72"><div class="footer-doctor">Dra. Mariana Gil Furlanetti<small>Dermatologista</small></div></div>')
s = s.replace('    .brand-mark { display: grid; width: 40px; height: 40px; place-items: center; border: 1px solid rgba(36, 72, 85, .35); border-radius: 50%; font-family: var(--serif); font-size: 18px; letter-spacing: -.1em; }', '    .brand-logo { display: block; width: 52px; height: 38px; object-fit: contain; object-position: left center; }')
s = s.replace('      .brand-mark { width: 37px; height: 37px; font-size: 17px; }', '      .brand-logo { width: 47px; height: 35px; }')
s = s.replace('    .footer-doctor { color: var(--paper); font-family: var(--serif); font-size: 23px; }', '    .footer-identity { display: flex; align-items: center; gap: 18px; }\n    .footer-logo { width: 72px; height: 48px; object-fit: contain; object-position: left center; }\n    .footer-doctor { color: var(--paper); font-family: var(--serif); font-size: 23px; }')
s = s.replace('      .footer-main { flex-direction: column; gap: 21px; padding-bottom: 24px; }', '      .footer-main { flex-direction: column; gap: 21px; padding-bottom: 24px; }\n      .footer-identity { align-items: flex-start; }')
page.write_text(s)
print('created', assets / 'mariana-gil-logo.png', (assets / 'mariana-gil-logo.png').stat().st_size)
