#შექმენით პროგრამა სადაც მომხმარებელს შემოატანინებთ სახელს და ასაკს, შემდეგ შეამოწმეთ ასაკი, თუ ასაკი >= 18 დაუბეჭდეთ რომ მას შეუძლია შევიდეს კლუბში, სხვა შემთხვევაში დაუბეჭდეთ რომ არ შეუძლია.

name=input("Enter your name:")
age=int(input("Enter your age"))
if age >=18:
    print("you can enter to the club")
else:
    print("you cant enter to the club")