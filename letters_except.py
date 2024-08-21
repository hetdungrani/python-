i=0
str1='sdj international college'
while i <len(str1):
    if str1[i]=='a' or str1[i]=='t':
        i+=1
        continue
    print('current letter:',str1[i])
    i+=1
