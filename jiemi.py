
mima=''
intmima=[]*len(mima)
intmima=[ord(c) for c in mima]
print(intmima)
#读取原文件
with open (file='jiami1.txt',mode='r') as file1:
    lines1 =file1.readlines()
    num1 = 0
    length1 = len(lines1)
    yuanwen = [''] * length1
    while num1<length1:
        yuanwen[num1] = str(lines1[num1]) 
        num1+=1

num=0
jiamistr = [''] * length1
while num<length1:
    #转化为ASCII码
    int10=[]*len(yuanwen[num])
    int10=[ord(c) for c in yuanwen[num]]
    print(int10)
    #加密后转化为chr组
    chrmi=['']*len(int10)
    j=0
    #len(int10)-1因为加密时最后有个\n
    for i in range(len(int10)-1):
        #用mima解密
        int10[i]=int10[i]-intmima[j]
        j+=1
        if j>=len(mima):
            j=0
        chrmi[i]=chr(int10[i])
    #print(chrmi)
    #将chr组变为字符串
    strmi=''
    for i in range(len(chrmi)):
        strmi=strmi+chrmi[i]
    #print('strmi',strmi)
    #将加密后的字符串赋值给jiamistr
    jiamistr[num]=strmi
    num+=1
with open (file='jiemi1.txt',mode='w+') as file2:
    num =0
    while num<length1:
        file2.write(jiamistr[num])
        num+=1
