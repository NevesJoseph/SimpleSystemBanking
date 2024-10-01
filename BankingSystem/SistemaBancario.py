import sys

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, extrato, limite, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: "))
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    elif valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def sair():
    print("Obrigado por usar nosso sistema bancário!")
    return False

def menu():
    return {
        'd': lambda s, e, *_: depositar(s, e),
        's': lambda s, e, l, n, ls: sacar(s, e, l, n, ls),
        'e': lambda s, e, *_: (exibir_extrato(s, e), (s, e)),
        'q': lambda *_: (None, None, False)
    }

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    
    executando = True
    while executando:
        print("\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair")
        opcao = input("=> ").lower()
        
        acao = menu().get(opcao)
        if acao:
            if opcao == 'q':
                saldo, extrato, executando = acao(saldo, extrato)
            elif opcao == 's':
                saldo, extrato, numero_saques = acao(saldo, extrato, limite, numero_saques, LIMITE_SAQUES)
            else:
                saldo, extrato = acao(saldo, extrato)
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()