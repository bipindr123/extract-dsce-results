import re
rt=[]
f = open("mydata.txt","r")
for i in f.readlines():
    res = re.findall(r"\s(\d\.\d+)", i)
    if str(res) == "[]":
        res = re.findall(r"\s(\d)",i)
    tstr=re.sub("\[\'","",str(res))
    tstr=re.sub("\'\]","",tstr)
    if(tstr != "[]"):
        a = float(str(tstr))
    rt.append(a)

count=0
for i in rt:
    if i>8.72:
        count+=1
print(count)
