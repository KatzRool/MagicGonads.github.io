#Columnar Cipher
key = input("Key: ")
msg = [x for x in input("Message: ") if x.isalpha()]
ref = [x for x in sorted(enumerate(list(key)),key=lambda x: x[1])]
dic = list(range(len(ref)))
for t in ref:
    dic[t[0]] = ref.index(t)
col = round(len(msg)/len(key)+0.5)
msg+=[chr(97+x%26) for x in range(len(key)*col-len(msg))]
cyp = [''.join(msg[x::len(key)]) for x in range(len(key))]
kek = list(range(len(ref)))
i=0
for v in dic:
    kek[v] = cyp[i]
    i+=1
print(''.join(kek))
input()
