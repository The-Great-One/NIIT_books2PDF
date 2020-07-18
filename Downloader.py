import os
import img2pdf
from urllib.request import urlopen
import os
import canvas as canvas
from bs4 import BeautifulSoup
url=input("Enter Url for the book you want(Without 1&pit=2): ")
pages=int(input("Enter the pages in the book: "))
dire=input("Enter Directory to be saved in with the file name(EX: C:\\MyDirectory\\FileName): ")

count=1
for i in range(1,pages+1):
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
	imgs.sort(key=len)
	f.write(img2pdf.convert(imgs))
	print("PDF Created")
print("Done")
