import csv
fh=open("vrecord1.csv","w")
stuwriter=csv.writer(fh)
stuwriter.writerow(['rollno','name','marks'])
for i in range(5):
    print("studentrecord",(i+1))
    rollno=int(input("enter rollno:"))
    name=input("entre the name:")
    marks=float(input("entre the marks"))
    sturec=[rollno,name,marks] 
    stuwriter.writerow(sturec)
fh.close()
