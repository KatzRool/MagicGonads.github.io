#ABN Validator
out = "Invalid"
dpw = [10,1,3,5,7,9,11,13,15,17,19]
res = 0
try:
  abn = input("ABN: ").replace(' ','')
  abn = str(int(abn[0])-1) + abn.split(abn[0],1)[1]
  for i in range(11):
    res += int(abn[i])*dpw[i]
  res %= 89
  if res == 0 and len(abn) == 11:
    out = "Valid"
except:
  pass
print(out)
input()
