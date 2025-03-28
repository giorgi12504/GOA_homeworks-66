#ცვლადში შეინახეთ პაროლი. შემდეგ მომხმარებელს შემოატანინეთ პაროლი, სანამ მომხმარებლის მიერ შემოტანილი პაროლი არ დაემთხვევა თქვენს პაროლს, გამოუტანეთ "Incorrect password. Try again". იმ შემთხვევაში თუ ეს პაროლები ერთმანეთს დაემთხვევა გამოიტანეთ "Correct password. You have successfully logged in." (გააკეთეთ While ციკლით, არ გამოიყენოთ if else statement-ები.);

password = "paroli223"
user_input = "" 

while user_input != password:  
    user_input = input("Enter your password: ")  
    print("Incorrect password. Try again.")  

print("Correct password. You have successfully logged in.")  

    
    