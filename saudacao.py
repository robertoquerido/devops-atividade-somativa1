def criar_saudacao(nome):
    nome = nome.strip()
    if not nome:
        nome = "Visitante"
    return f"Olá, {nome}! Bem-vindo ao DevOps."


if __name__ == "__main__":
    nome = input("Digite seu nome: ")
    print(criar_saudacao(nome))
