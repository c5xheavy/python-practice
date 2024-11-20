import sys

def tail(lines, n):
    if len(lines) <= n:
        return '\n'.join([line.rstrip('\n') for line in lines])
    return '\n'.join([line.rstrip('\n') for line in lines[-n:]])


if len(sys.argv) > 1:
    for i, filename in enumerate(sys.argv[1:]):
        if len(sys.argv) > 2:
            print(f"==> {filename} <==")
        with open(filename, 'r') as f:
            lines = f.readlines()
        output = tail(lines, 10)
        if output:
            print(output)
        if i < len(sys.argv[1:]) - 1:
            print()
else:
    lines = sys.stdin.readlines()
    output = tail(lines, 17)
    if output:
        print(output)
