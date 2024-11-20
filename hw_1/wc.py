import sys

if len(sys.argv) == 1:
    input = sys.stdin.read()
    lines = len(input.splitlines())
    words = len(input.split())
    chars = len(input)
    print(f"{lines}\t{words}\t{chars}")
else:
    total_lines = 0
    total_words = 0
    total_chars = 0
    for filename in sys.argv[1:]:
        with open(filename, 'r') as file:
            lines = 0
            words = 0
            chars = 0
            for line in file:
                w = line.split()
                lines += 1
                words += len(w)
                chars += len(line)
            total_lines += lines
            total_words += words
            total_chars += chars
            print(f"{lines}\t{words}\t{chars}\t{filename}")
    if len(sys.argv) > 2:
        print(f"{total_lines}\t{total_words}\t{total_chars}\ttotal")
