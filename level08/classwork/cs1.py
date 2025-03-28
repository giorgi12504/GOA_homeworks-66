#მომხმარებელს შემოატანინეთ ერთი რიცხვი, შემდეგ შეამოწმეთ არის თუ არა ეგ რიცხვი >= 5 და <= 10 (ანუ არის თუ არა 5დან 10შორის დიაპაზონში (შუალედში))

num=int(input("Enter your number:"))
if num>=5 and num<=10:
    print("your number is in dypazon")
else:
    input("Try again your number must be in between 5-10,:")
    print(" Good job your number is finally in dypazon :)")
