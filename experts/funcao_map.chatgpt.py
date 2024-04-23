# Fazer um programa simples que vai descobrir se um aluno passou ou não.
# Nesse projeto simples vou utilizar conceitos como list comprehension, deixar um valor que não vai ser alterado como constante, além de definir funcões bem especificas para cada responsabilidade

# Constante da nota minima 
NOTA_MINIMA_APROVACAO = 7.0

# Descobrir se nota é maior ou menor que a nota minima 
def aprovacao_aluno(aluno):
    return aluno['nota'] >= NOTA_MINIMA_APROVACAO

def descobrir_genero(aluno):
    if aluno['genero'].lower() == 'masculino':
        return True
    else:
        return False

# Formatar a mensagem caso o aluno seja aprovado ou não
def formatar_mensagem(aluno):
    # Operador ternário simplificar o código
    status = 'aprovado' if aprovacao_aluno(aluno) else 'reprovado'
    genero = 'O aluno' if descobrir_genero(aluno) else 'A aluna'
    return f'{genero} {aluno['nome']} foi {status} com a nota {aluno['nota']}'

# Lista com dicionários de alunos e suas notas para verificação caso ele tenha sido aprovado ou não
alunos = [
    {'nome': 'Manoel','nota': 7.0, 'genero': 'Masculino'},
    {'nome': 'Marcos','nota': 8.0, 'genero': 'Masculino'},
    {'nome': 'Vitoria','nota': 6.0, 'genero': 'Feminino'},
    {'nome': 'Joaquim','nota': 8.7, 'genero': 'Masculino'},
    {'nome': 'Melissa','nota': 7.0, 'genero': 'Feminino'},
    {'nome': 'Elen','nota': 5.6, 'genero': 'Feminino'}
]

# Utilizar a list comprehension afim de minimizar o tamanho do código
aprovado_ou_reprovado = [formatar_mensagem(aluno) for aluno in alunos]

# Exibir as mensagem de forma individual, já que elas estão fora da lista
for mensagem in aprovado_ou_reprovado:
    print(mensagem)