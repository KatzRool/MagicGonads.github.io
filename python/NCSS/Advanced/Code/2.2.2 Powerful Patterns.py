#Powerful Patterns
vow = ['a','e','i','o','u']
for line in open('..\docs\words.txt'):
    line = line.rstrip()
    if line.lower().replace('t','m')[0] == 'm' and line.lower()[::-1][0] == 'y':
        kek = 0
        for v in vow:
            for w in vow:
                kek += v+w in line.lower()
        if kek == 0:
           print(line)
input()
