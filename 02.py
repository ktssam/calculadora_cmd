while True:
    print("1.Somar \n2.Subtrair \n3.Multiplicar \n4.Dividir")
    inp1 = int(input("O que deseja agora?\n R: "))

    if inp1 == 1:
        v1 = float(input("\nDigite o primeiro valor: "))
        v2 = float(input("Agora o segundo: "))
        result = v1 + v2

        print("\n--> Seu resultado é ", result)

        inp2 = input("\nVoltar ao início? \n R: ")

        if inp2 == "Sim" or inp2 == "sim" or inp2 == "S" or inp2 == "s" or inp2 == "Si" or inp2 == "si":
            print("\n---------------")
            continue
        elif inp2 == "tabaco" or inp2 == "Tabaco" or inp2 == "TABACO":
            print("\nAcende aí kkkk \n---------------")
            continue
        else:
            exit()

    elif inp1 == 2:
        v1 = float(input("\nValor incial: "))
        v2 = float(input("Valor subtraído: "))
        result = v1 - v2

        print("\n--> Seu resultado é ", result)

        inp2 = input("\nVoltar ao início? \n R: ")

        if inp2 == "Sim" or inp2 == "sim" or inp2 == "S" or inp2 == "s" or inp2 == "Si" or inp2 == "si":
            print("\n---------------")
            continue
        elif inp2 == "tabaco" or inp2 == "Tabaco" or inp2 == "TABACO":
            print("\nAcende aí kkkk \n---------------")
            continue
        else:
            exit()

    elif inp1 == 3:
        v1 = float(input("\nValor multiplicado: "))
        v2 = float(input("Multiplicador: "))
        result = v1 * v2

        print("\n--> Seu resultado é ", result)

        inp2 = input("\nVoltar ao início? \n R: ")

        if inp2 == "Sim" or inp2 == "sim" or inp2 == "S" or inp2 == "s" or inp2 == "Si" or inp2 == "si":
            print("\n---------------")
            continue
        elif inp2 == "tabaco" or inp2 == "Tabaco" or inp2 == "TABACO":
            print("\nAcende aí kkkk \n---------------")
            continue
        else:
            exit()
    
    elif inp1 == 4:
        v1 = float(input("\nValor divido: "))
        v2 = float(input("Divisor: "))
        result = v1 / v2

        print("\n--> Seu resultado é ", result)

        inp2 = input("\nVoltar ao início? \n R: ")

        if inp2 == "Sim" or inp2 == "sim" or inp2 == "S" or inp2 == "s" or inp2 == "Si" or inp2 == "si":
            print("\n---------------")
            continue
        elif inp2 == "tabaco" or inp2 == "Tabaco" or inp2 == "TABACO":
            print("\nAcende aí kkkk \n---------------")
            continue
        else:
            exit()
