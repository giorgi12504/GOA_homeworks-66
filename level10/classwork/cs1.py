#დაწერეთ პროგრამა, რომელიც მომხმარებლს მოსთხოვს, რომ შემოიტანოს დადებითი რიცხვი. 
#თუ მომხმარებელი შემოიტანს უარყოფით რიცხვს ან ნულს, პროგრამამ უნდა მოსთხოვოს რიცხვის თავიდან შემოტანა
 
make_positive = int(input("Enter a positive number:"))
while make_positive<=0:
    make_positive = int(input("Enter a positive number:"))

if make_positive > 0:

    print("you have Enter a positive number :)")

    