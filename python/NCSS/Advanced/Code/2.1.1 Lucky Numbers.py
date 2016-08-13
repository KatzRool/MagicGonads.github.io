#Lucky Numbers
nek = int(input("Enter number: "))
kek = list(range(1,nek+1))
j = 0
i = 1
while j < len(kek):
    k = 0
    while k < len(kek):
      if kek[k] > i:
          i = kek[k]
          break
      k+=1
    del kek[i-1::i]
    j+=1
print(kek[len(kek)-1])
input()
