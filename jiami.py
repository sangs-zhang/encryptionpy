
mima=''
intmima=[]*len(mima)
intmima=[ord(c) for c in mima]
print(intmima)
#读取原文件
with open (file='1.txt',mode='r') as file1:
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
    #一句长度为ichr
    ichr=len(yuanwen[num])
    int10=[]*ichr
    int10=[ord(c) for c in yuanwen[num]]
    print(int10)
    #加密后转化为chr组
    chrmi=['']*ichr
    j=0
    for i in range(ichr):
        #用mima加密
        int10[i]=int10[i]+intmima[j]
        j+=1
        if j>=len(mima):
            j=0
        chrmi[i]=chr(int10[i])
    #将chr组变为字符串
    strmi=''
    for i in range(ichr):
        strmi=strmi+chrmi[i]
    #将加密后的字符串赋值给jiamistr
    jiamistr[num]=strmi
    num+=1
with open (file='jiami1.txt',mode='w+') as file2:
    num =0
    while num<length1:
        file2.write(jiamistr[num]+'\n')
        num+=1
