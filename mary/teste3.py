numero =2

match numero:
    case n if n < 0:
        print("numero negativo")
    case n if n % 2 == 0:
        print(f"{n} é um numero pra positivo")
    case n:
        print(f"{n} é um numero impar positivo")