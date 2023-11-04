import csv

days=["23/08", "28/08", "30/08", "06/09", "13/09", "11/10", "16/10"]

i=3  #Day Index

f=open("final-attendance (copy).csv", "r")
g=open("Attendance A23 CS 203 DS.csv", "r")

fr=csv.reader(f)
gr=csv.reader(g)

Found=[]
Actual=[]

for row in fr:
    Found.append(row[1])

for row in gr:
    if not row[i+2]:
        Actual.append(row[2])

correct=0
wrong=0

for i in Found:
    if i in Actual:
        correct+=1
    else:
        print(i)
        wrong+=1

for i in Actual:
    if i not in Found:
        print(i)
        wrong+=1

print("Correct: " + str(correct) + "\n" + "Wrong: " + str(wrong))
print(len(Actual))
print(Actual)
     
