#გაიხსენეთ გაკვეთილზე გაკეთებული დავალება მომხმარებლის სისტემაში შესვლის მცდელობაზე და დამოუკიდებლად გააკეთეთ იგივე while ციკლის საშუალებით.


password = "paroli223"
user_input = "" 

while user_input != password:  
    user_input = input("Enter your password: ")  
    print("Incorrect password. Try again.")  

print("Correct password. You have successfully logged in.")  


