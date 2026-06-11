medical_cause=input("did you have any medical cause?(y/n):")
if medical_cause=='y':
    print("you are allowed")
else:
    attendance=int(input("enter the attendance of the student:"))
    if attendance>=75:
        print("you are allowed")
    else:
        print("you are not allowed")