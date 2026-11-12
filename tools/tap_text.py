"""Нажимает в эмуляторе на элемент с указанным текстом (через uiautomator)."""
import re, subprocess, sys, time
want = sys.argv[1]
exact = '--exact' in sys.argv
for attempt in range(6):
    subprocess.run(['adb', 'shell', 'uiautomator', 'dump', '/sdcard/ui.xml'], capture_output=True)
    xml = subprocess.run(['adb', 'shell', 'cat', '/sdcard/ui.xml'], capture_output=True, text=True).stdout
    for m in re.finditer(r'<node [^>]*>', xml):
        n = m.group(0)
        txt = ' '.join(x.group(1) for x in re.finditer(r'(?:text|content-desc)="([^"]*)"', n))
        texts = [x.group(1).strip() for x in re.finditer(r'(?:text|content-desc)="([^"]*)"', n)]
        if (want in texts) if exact else (want in txt):
            b = re.search(r'bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"', n)
            if not b:
                continue
            x = (int(b.group(1)) + int(b.group(3))) // 2
            y = (int(b.group(2)) + int(b.group(4))) // 2
            subprocess.run(['adb', 'shell', 'input', 'tap', str(x), str(y)])
            print('tapped', want, x, y)
            sys.exit(0)
    time.sleep(2)
print('NOT FOUND:', want)
