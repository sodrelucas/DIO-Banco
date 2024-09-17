menu = f"""
    {"SEJA BEM-VINDO".center(20, "#")}

    DIGITE A OPERAÇÃO QUE DESEJA REALIZAR

    1 - SACAR

    2 - DEPOSITAR

    3 - EXTRATO

    4 - SAIR
    
"""

historico= []
saldo = 0
limite = 500
saques_por_dia = 0


def sacar():
    global historico
    global saques_por_dia
    global saldo
    if saques_por_dia > 3:
        print("\n \n LIMITE DE SAQUES ATINGIDOS")     
    else:
        valor = input("DIGITE O VALOR QUE DESEJA SACAR:")
        if saldo < float(valor):
            print("\n \n SALDO INSUFICIENTE \n")
        else:
            if float(valor) <= limite:
                saldo -= float(valor)
                saques_por_dia += 1
                historico.append(f"SAQUE R${valor}")
                

def depositar():
    global historico
    global saldo

    valor = input("DIGITE O VALOR A SER DEPOSITADO: ")
    saldo += float(valor)
    historico.append(f"DEPOSITO R${valor}")


def extrato():
    global saldo
    global historico

    extrato = ""

    for item in historico:
        extrato += f"{item}\n"

    print(f"""SALDO ATUAL R${saldo}
{"EXTRATO".center(20,"#")}
{extrato}""")


while True:
    opcao = input(menu)

    if opcao == "1":
        sacar()
    
    elif opcao == "2":
        depositar()

    elif opcao == "3":
        extrato()

    else:
        break