#Given a YOB by the user, calculate and return the age of the user.



def calculateage(currentyear,YOB):
    age = currentyear - YOB
    return age
print(calculateage(2021,2000))

print(calculateage(2019,1990))

def userinput():
    currentyear = int(input("Enter currentyear")) 
    YOB = int(input("Enter YOB"))
    age = calculateage(currentyear,YOB)
    print(age)

userinput()