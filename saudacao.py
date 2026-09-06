def criar_saudacao(nome):
    if not nome.strip():
        nome = "Visitante"
    return f"Olá, {nome}! Bem-vindo ao DevOps."

nome = input("Digite seu nome: ").strip()
print(criar_saudacao(nome))

