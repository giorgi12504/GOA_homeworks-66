#ეხუთე დავალების მსგავსად, შემოატანინეთ მომხმარებელს ტემპერატურა, თუმცა ამჯერად ფარენგეიტში. შემდეგ კი დაწერეთ პროგრამა, რომელიც შემოტანილ ტემპერატურას ცელსიუსში გადაიყვანს და საბოლოოდ დაბეჭდეთ შედეგი.

fahrenheit = float(input("შეიყვანეთ ტემპერატურა ფარენგეიტში: "))

celsius = (fahrenheit - 32) * 5/9

print(f"{fahrenheit}°F = {celsius:.2f}°C")