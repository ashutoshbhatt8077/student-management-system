import json
import random
import string
from pathlib import Path


class Student:
    database='data.json'
    data=[]

    try:
        if Path(database).exists():
            with open(database) as fs:
                data=json.loads(fs.read())
    except Exception as err:
        print(f"an exception occour as {err}")


    @staticmethod
    def update():
        with open(Student.database,'w') as fs:
            fs.write(json.dumps(Student.data))
    @classmethod
    def __reggenerate(cls):
        alpha= random.choices(string.ascii_letters,k=3)
        num= random.choices(string.digits,k=3)
        spchr=random.choices("!@#$%^&*",k=3)
        id=alpha+num+spchr
        random.shuffle(id)
        return "".join(id)


    def createaccount(self):
        info={
            "name":input(" Tell your Name  -: "),
            "brach":input("Tell your Brach  -: "),
            "year":input("Tell your acadmic year  -: "),
            "roll_no":input("Tell your roll number  -: "),
            "email_id":input("Tell your email id  -: "),
            "registration_number":Student.__reggenerate()
        }
        for i in info :
            print(f"{i} : {info[i]}")
        print("please note down your registration number")

        Student.data.append(info)
 
        Student.update()

    def updatedetail(self):
        regnum=input("Please enter your registration number")

        userdata=[ i for i in Student.data if i['registration_number'] == regnum ]
        print(userdata)
        if not userdata:
            print("Sorry no data found")
            return
        else:
            print("What do you want to update?")
            print("1 - Name")
            print("2 - Roll Number")
            print("3 - Email")

            choice = input("Enter choice: ")

            if choice == "1":
                userdata[0]["name"] = input("Enter new name: ")
            elif choice == "2":
                userdata[0]["roll_no"] = input("Enter new roll number: ")
            elif choice == "3":
                userdata[0]["email_id"] = input("Enter new email: ")
            else:
                print("Invalid choice")
                return

        Student.update()
        print("Details updated successfully")

    def fetchdetail(self):

        regnum=input("Please enter your registration number")

        userdata=[ i for i in Student.data if i.get("registration_number") == regnum ]
        if not userdata:
            print("Sorry no data found")
            return
        else:
            for i in userdata[0]:
                print(f"{i}->{userdata[0][i]}")
             
    def delete(self):
     regnum = input("Please enter your registration number: ")

     for i in Student.data:
        if i.get("registration_number") == regnum:
            Student.data.remove(i)
            print("Data deleted successfully")
            Student.update()
            return

     print("Sorry no data found")



user=Student()
print("press 1 for creating a account")
print("press 2 for update details")
print("press 3 for fetching details")
print("press 4 for deleting account")

check=int(input("Enter the response :-"))

if check==1:
    user.createaccount()
elif check==2:
    user.updatedetail()
elif check==3:
    user.fetchdetail()
elif check==4:
    user.delete()
else:
    print("Invalid choise please try again later")