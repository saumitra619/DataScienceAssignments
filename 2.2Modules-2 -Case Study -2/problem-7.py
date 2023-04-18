
dic = {} 
input_str=input('Enter string :- ') 

for s in input_str:
  dic[s] = dic.get(s,0)+1 
print('\n'.join(['%s,%s' % (char, count) for char, count in dic.items()]))