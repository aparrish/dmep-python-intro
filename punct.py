import sys
for line in sys.stdin:
    line = line.strip()
    punctuation = line.count(".") + line.count(",") + line.count("-") + line.count("?")
    if punctuation >= 2:
        print("many")
    elif punctuation == 1:
        print("only one")
    else:
        print("none :(")