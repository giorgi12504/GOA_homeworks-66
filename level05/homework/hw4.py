#მომხმარებელს შემოატანინეთ ტემპერატურა ცელსიუსში. დაწერეთ პროგრამა, რომელიც მომხმარებლის მიერ შემოტანილ ტემპერატურას გადაიყვანს ფარენგეიტში და დაბეჭდეთ საბოლოო შედეგი. (მოიძიეთ ფორმულა ინტერნეტში)


celsius = float(input("შეიყვანეთ ტემპერატურა ცელსიუსში: "))

farengeit = (celsius * 9/5) + 32


print(f"{celsius}°C = {farengeit}°F")