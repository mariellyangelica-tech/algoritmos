nadador = int(input("digite a sua idade"))


match nadador:
    case n if n >= 5 and n <= 7:
        print (" sua categoria é infantil")
    case n if n >= 8 and n  <= 10:
        print("sua categoria é juvenil")
    case n if n >= 11 and n <= 15:
        print("sua categoria é adolecente")
    case n if n >= 16 and n <= 30:
        print(" sua categoria é adulto")
    case n if n > 30:
        print("sua categoria é senior")
        