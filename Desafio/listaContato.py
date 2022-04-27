import json


def salva_arquivo(contato, nomeArquivo):
    with open(nomeArquivo, "a") as f:
        json.dump(contato, f)


nome = input('Qual é seu nome de contato? ').strip().title()
email = input('Qual é o seu email para contato? ').strip()
while True:
    try:  # Forçar o usuário a indicar apenas um número
        telefone = int(input('Qual é o seu telefone para contato? [somente números] '))
    except ValueError:
        print('Digite somente números. Tente novamente.')
        continue
    else:
        break
relacionamento = input('Qual é a sua relação com o contato? ')
contato = {
    "nome": nome,
    "email": email,
    "telefone": telefone,
    "relacionamento": relacionamento
}
salva_arquivo(contato, "contato.json")
