import urllib2
import re
import slate
import pdfminer
url="http://45.32.111.231:8080/birt/frameset?__report=mydsi/exam/Exam_Result_Sheet_dsce.rptdesign&__format=pdf&USN="
usn = "1DS15IS00"
i=0
def main():
    global i,usn
    for i in range(1,9):
        download_file(url+usn+str(i))
    usn = "1DS15IS0"
    for i in range(10,99):
        print(usn)
        download_file(url+usn+str(i))
    usn="1DS15IS"
    for i in range(134,200):
        download_file(url+usn+str(i))
    return 0

    #download_file(url+"1DS15CS015")
def download_file(download_url):
    response = urllib2.urlopen(download_url)
    file = open("documentbast.pdf", 'wb')
    file.write(response.read())
    file.close()
    with open('documentbast.pdf',"rb") as f:
        doc = slate.PDF(f)
    s1= str(doc)
    print(s1)
    f2 = open("mydata.txt","a")
    res1 = re.findall(r"the Student:(\w+\s\w+)",s1)
    tstr=str(res1)
    if tstr == "[]":
        res1 = re.findall(r"CODE(\w+\s\w+)",s1)
        tstr=str(res1)
    if tstr == "[]":
        res1 = re.findall(r"the Student:(\w+)",s1)
        tstr=str(res1)

    res2 = re.findall(r'(\d\.\d*)', s1)
    if str(res2)=="[]":
        res2 = re.findall(r'SGPA\\n\\n(\d)', s1)
    tstr = tstr + " "
    tstr=tstr + str(res2)
    tstr=re.sub("\[\'","",tstr,2)
    tstr=re.sub("\'\]","",tstr,2)
    print(tstr)
    f2.write(usn+str(i)+" ")
    f2.write(tstr)
    f2.write("\n")
    f2.close()
if __name__ == "__main__":
    main()
