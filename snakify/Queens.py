rows = set()
cols = set()
diag1 = set()
diag2 = set()

attack = False

for _ in range(8):
    r, c = map(int, input().split())

    if (r in rows) or (c in cols) or ((r-c) in diag1) or((r+c) in diag2):
        attack = True

    rows.add(r)
    cols.add(c)
    diag1.add(r - c)
    diag2.add(r + c)

print("YES" if attack else "NO")