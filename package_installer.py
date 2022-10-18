import subprocess
import sys

unfinished = []


def install(package):
    print(f"installing this package = {package}")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except:
        print(f"couldn't install {package}")
        unfinished.append(package)


with open('requirements.txt') as f:
    lines = f.read()
    print(lines)

lines = lines.split(';')
new = []
lines = [new.append(package.strip()) for package in lines]
f.close()
for package in new:
    install(package)

print(unfinished)
