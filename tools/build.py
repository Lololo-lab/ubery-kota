"""Собирает www/index.html из src/game.html: встраивает шрифт Nunito (работает без интернета)."""
import base64, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / 'src/game.html').read_text(encoding='utf-8')
fdir = root / 'node_modules/@fontsource/nunito/files'
faces = []
ranges = {
    'cyrillic': 'U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116',
    'latin': 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD',
}
for w in (800, 900):
    for sub, rng in ranges.items():
        b = base64.b64encode((fdir / f'nunito-{sub}-{w}-normal.woff2').read_bytes()).decode()
        faces.append(f"@font-face{{font-family:'Nunito';font-style:normal;font-weight:{w};font-display:swap;src:url(data:font/woff2;base64,{b}) format('woff2');unicode-range:{rng}}}")
# 700 -> используем 800
out = src.replace('/*FONTS*/', '\n'.join(faces))
cap = (root / 'node_modules/@capacitor/core/dist/capacitor.js').read_text(encoding='utf-8')
out = out.replace('<script>/*CAPACITOR*/</script>', '<script>' + cap + '</script>')
(root / 'www').mkdir(exist_ok=True)
(root / 'www/index.html').write_text(out, encoding='utf-8')
print('www/index.html', len(out) // 1024, 'KB')

(root / 'www/webview.html').write_text((root / 'src/webview.html').read_text(encoding='utf-8'), encoding='utf-8')
print('www/webview.html')
