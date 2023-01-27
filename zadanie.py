chislo = int(input("Кол-во чисел:"))
first = float(input("Первое число:"))

for i in range(chislo):
    next = float(input("Ещё одно число::"))
    s = input("Что с ними сделать? +,-,*,/ : ")

    
    if s in ('+', '-', '*', '/'):
        if s == '+':
            first +=next
            print(first)
        elif s == '-':
            first = first-next
            print(first)
        elif s == '*':
            first = first*next
            print(first)
        elif s == '/':
            if next != 0:
                first = first/next
                print(first)
            else:
                print("Деление на ноль!")
    else:
        print("Такого я не знаю((")

print (f"Ответ: {first}")


    