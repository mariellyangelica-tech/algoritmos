comando = int(input("digete agenda ou sair"))

match comando:
    case "agenda":
        print("novo documento")
    case "sair":
        print("documento salvo")
    case "aditar":
        print("aditar documento")
    case _:
        print("opção invalida ")