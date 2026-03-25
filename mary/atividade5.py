operador = int(input("digite um numero de 1 a 30 para saber a procedencia"))


match operador:
    case n if n ==1: 
        print(" sul ")
    case n if n ==2:
        print(" norte")
    case n if n ==3:
        print("leste")
    case n if n ==4:
        print("oeste")
    case n if n >= 5 and n <=6:
        print("nortesde")
    case n if n >=7 and n <=9:
        print("suldeste")
    case n if n >=10 and n<=20:
        print("centro-oeste")
    case n if n >=21 and n <=30:
        print("nordeste")