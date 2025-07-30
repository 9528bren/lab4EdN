def verificar_senha():
    senha = input("Digite sua senha: ")

    # Verifica o comprimento
    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        return

    # Verifica se contém pelo menos um número
    if not any(caractere.isdigit() for caractere in senha):
        print("A senha deve conter pelo menos um número.")
        return

    print("Senha válida!")

# Executar o verificador
verificar_senha()
