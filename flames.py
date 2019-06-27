from collections import Counter
list1=['F','L','A','M','E','S']
str1 = 'muthuveerapan'.lower()
str2 = 'varshini'.lower()
dict1 = Counter(str1)
dict2 = Counter(str2)
commonDict = dict1 & dict2
commonChars = list(commonDict.elements())
commonChars = sorted(commonChars)
l1=''.join(commonChars)
str3=str1+str2
str3=str3.split()
str3=''.join(str3)
c=len(str3)-(len(l1)*2)
while len(list1)>1:
    s=((c%len(list1))-1)
    if s>=0:
        r=list1[s+1:]
        l=list1[:s]
        list1=r+l
    else:
        list1=list1[:len(list1)-1]
print(list1)
