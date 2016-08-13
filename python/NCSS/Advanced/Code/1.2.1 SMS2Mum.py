#SMS2Mum
msg = ''
key = {}
for row in open('..\docs\sms-phrases.txt'):
  shp, lhp = row.split(' ',1)
  key[shp] = lhp.strip()
for row in open('..\docs\sms-message.txt'):
  row___=[]
  for row__ in row.split(','):
    row_=[]
    for ent in row__.split(' '):
      for shp in key.keys():
        if shp in ent.upper():
          ent = key[shp]
      row_+=[ent]
    row___+=[' '.join(row_)]
  msg += ','.join(row___)
print(msg, end='')
input()
