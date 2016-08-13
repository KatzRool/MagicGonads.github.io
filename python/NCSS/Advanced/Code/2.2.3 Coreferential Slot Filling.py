#Coreferential Slot Filling
tit = [['she', 'her', 'woman', 'wife', 'lady', 'ma\'am.'],['he', 'him', 'his', 'man', 'husband', 'gentleman', 'sir'],['i', 'my', 'me', 'myself', 'you', 'yourself'],['Miss', 'Mrs.', 'Ms.'],['Master', 'Mr.']]
per = {}
for row in open('..\docs\story.txt'):
    row = row.strip(' ').split(']')
    nam = [x.split('[')[1] for x in row[::2] if len(x.split('[')) > 1]
    ind = [int(x.split('[')[1]) for x in row[1::2] if len(x.split('[')) > 1]
    i = 0
    while i < len(nam):
        ali = (nam[i].lower() in tit[0]) + (nam[i].lower() in tit[1]) + (nam[i].lower() in tit[2])
        if nam[i] in tit[0] or nam[i].split(' ')[0] in tit[3]:
            gen = 'female'
        elif nam[i] in tit[1] or nam[i].split(' ')[0] in tit[4]:
            gen = 'male'
        else:
            gen = '<unknown>'
        if ali:
            nam[i] = '<none>'
        if ind[i] in per:
            if nam[i] not in per[ind[i]][0]:
                per[ind[i]][0].append(nam[i])
            if per[ind[i]][1] == '<unknown>':
                per[ind[i]][1] = gen
        else:
            per[ind[i]] = [[nam[i]],gen]
        i+=1
for k in sorted(per.keys()):
    v = per[k]
    if len(v[0]) > 1 and '<none>' in v[0]:
        v[0].remove('<none>')
    n = [x for x in sorted(v[0])]
    print('Person '+str(k)+': gender='+v[1]+' names='+', '.join(n))
input()
