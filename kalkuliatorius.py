while True:
    print("-------------------\n"
          "1. Sudėtis"
          "\n"
          "2. Atimtis"
          "\n"
          "3. Daugyba"
          "\n"
          "4. Dalyba"
          "\n"
          "q - išeiti"
          "\n"
          "-------------------\n"
          )

    meniu_pasirinkimas = input(" ")

    if meniu_pasirinkimas == "q":
        break

    # naudojam float - skaičius su kableliu
    sk1 = float(input("Įveskite pirmąjį skaičių "))
    sk2 = float(input("Įveskite antrąjį skaičių "))

    if meniu_pasirinkimas == "1":
        res = f"{sk1} + {sk2} = {sk1 + sk2}"

    elif meniu_pasirinkimas == "2":
        res = f"{sk1} - {sk2} = {sk1 - sk2}"

    elif meniu_pasirinkimas == "3":
        res = f"{sk1} * {sk2} = {sk1 * sk2}"

    elif meniu_pasirinkimas == "4":
        res = f"{sk1} / {sk2} = {sk1 / sk2}"

    print(res)

    input("\nEnter - tęsti")
