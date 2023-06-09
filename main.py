import os

for i in range(1, 250, 25):
    sec = f'lectures_{i:03d}-{i + 24:03d}'
    os.mkdir(sec)
    for j in range(i, i + 25):
        lec = f"{sec}/lecture_{j:03d}"
        os.mkdir(lec)
        open(f'{lec}/main.py', 'w').close()
