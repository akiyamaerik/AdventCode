def lineBreak(infilepath, n):
    with open(infilepath) as infile:
        lines = infile.readlines()
    with open(infilepath, 'w') as outfile:
        for i,line in enumerate(lines):
            outfile.write(line)
            if not i%n:
                outfile.write('\n')

lineBreak('input.txt',3)