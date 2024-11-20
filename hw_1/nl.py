import sys

if len(sys.argv) == 1:
    lines = sys.stdin
else:
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        lines = f.readlines()
    
line_count = 1
for line in lines:
    print(f"     {line_count}\t{line.rstrip()}")
    sys.stdout.flush()
    line_count += 1
