class Aluno:
    alunos = [] # lista para armazenar os alunos cadastrados

    def __init__(self, id_aluno, nome, idade, peso, altura):
        self.id_aluno = id_aluno
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def __str__(self):
        return f"Aluno(ID: {self.id_aluno}, Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso}, Altura: {self.altura}, IMC: {self.calcular_imc():.2f})"

    @classmethod
    def cadastrar_alunos(cls):
        nome = input('Digite seu nome: ')
        idade = input('Digite a sua idade: ')
        telefone = input('Digite o número do seu telefone: ')
        tipo_plano = input('Digite o plano que pretende contratar (mensal, trimestral, anual): ')

        # dicionário com as informações
        aluno = {
            "nome": nome,
            "idade": idade,
            "tipo de plano": tipo_plano,
            "telefone": telefone
        }
        # Adicionar o dicionário à lista de alunos
        cls.alunos.append(aluno)

        print(f'Aluno {nome} cadastrado com sucesso.')

# Exemplo de utilização
Aluno.cadastrar_alunos()
