def convert_currency(dollar):
    peso = dollar * 57.17
    yen = dollar * 146.67
    return peso, yen

dollars = input("Enter currency in ($): ").split(",")

print("Dollar($)   Peso(P)      Yen(¥)")
for d in dollars:
    d = int(d.strip()) 
    peso, yen = convert_currency(d)
    print(d, "      ", round(peso, 2), "   ", round(yen, 2))
