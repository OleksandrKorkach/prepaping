a = int(input("n: "))
spisok1 = []

while a > 0:
    a -= 1
    b = int(input("chislo"))
    if b in spisok1:
        for j in spisok1:
            if b == j:
                spisok1.remove(j)
    else:
        spisok1.append(b)


print(len(spisok1))
