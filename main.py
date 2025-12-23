print("Son raqamlari yig'indisi")

son = input("Sonni kiriting: ").strip()

if son.isdigit() and son != "":
    yigindi = 0
    for raqam in son:
        yigindi += int(raqam)
    
    print(f"Raqamlar yig'indisi: {yigindi}")
else:
    print("Iltimos, faqat musbat butun son kiriting!")
