name=input("Enter student name")
rollnumber = input("enter roll number")
course =input("enter course")
marks =float(input("total marks"))

if marks >= 90:
    grade="A"
elif marks >= 80:
        grade="B" 
elif marks >= 70:
         grade="c"
elif marks >= 60:
       grade="D"
elif marks >= 50:
       grade="E"
else :
       grade =" f"  
if marks >=40 :
        result="pass"
else :
       result="fail"
        
    

print("student name : {}".format(name))
print("roll number  : {}".format(rollnumber))
print("course       : {}".format(course))
print("marks        :{}" .format(marks))
print("grade        :{}".format(grade))
print("result       :{}".format(result))