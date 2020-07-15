import os
import img2pdf
from urllib.request import urlopen
import os
import canvas as canvas
from bs4 import BeautifulSoup
url="http://courseware.training.com/ResourceReader/RadPdf.axd?rt=3&dk=0002D09E3226RWXHAG505BOFK88ETVKOB&pn="
        #input("Enter Url for the book you want(Without 1&pit=2): ")
pages=276
        #int(input("Enter the pages in the book: "))
dire="D:\\Desktop\\book\\book"
    #input("Enter Directory to be saved in with the file name(EX: C:\\MyDirectory\\FileName): ")


count=1
for i in range(1,pages+1):
        #resource=urlopen("http://courseware.training.com/ResourceReader/RadPdf.axd?rt=3&dk=0002D09E3226RWXHAG505BOFK88ETVKOB&pn="+str(i)+"&pit=2")
        resource=urlopen(url+str(i)+"&pit=2")
        output=open(dire+str(count)+".jpg","wb")
        output.write(resource.read())
        output.close()
        print("Page "+str(count)+" Complete")
        count+=1

dirname = "D:/Desktop/book"
with open("book.pdf","wb") as f:
	imgs = []
	print("Writing PDF!")
	for fname in os.listdir(dirname):
		if not fname.endswith(".jpg"):
			continue
		path = os.path.join(dirname, fname)
		if os.path.isdir(path):
			continue
		imgs.append(path)
	f.write(img2pdf.convert(imgs))
	print("PDF Created")
print("Done")
