#Ordinal Numbers
ent = input("Enter a number: ")
num = abs(int(ent.split('.',1)[0]))
ten = round(int(str(num/100).split('.',1)[1])/10-0.5)
end = ['th','st','nd','rd']
num%=10
print(ent+end[num*(ten!=1)*(num<4)])
input()
