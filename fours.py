import sys
for line in sys.stdin:
    line = line.strip()
    first_four = line[:4]
    last_four = line[-4:]
    print(first_four + last_four)