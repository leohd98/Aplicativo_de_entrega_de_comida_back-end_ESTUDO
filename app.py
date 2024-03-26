restaurantes_cadastrados = [
    {'nome': 'Praça',
     'categoria': 'Japonesa',
     'ativo': False},

    {'nome': 'Pizza Suprema',
     'categoria': 'Pizza',
     'ativo': True},

    {'nome': 'Cantina',
     'categoria': 'Italiano',
     'ativo': False}
]


def exibir_nome_programa():
    '''Essa função serve para escrever o título do programa.'''
    print('🅒🅨🅑🅔🅡 🅕🅞🅞🅓\n')


def menu():
    '''Essa função serve para determinar o funcionamento do programa.'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar Status do Restaurante')
    print('4. Sair do App\n')


def finalizar_app():
    '''Essa função serve para imprimir na tela que o programa finalizou a execução.'''
    print('\n'*80)
    print('[FIM DO PROGRAMA]')


def corrige_erros():
    '''Essa função serve para corrigir erros de input das funções.'''
    print()
    print('ERRO: Digite apenas números de 1 a 4.')
    volta_ao_menu()


def cadastra_restaurante():
    '''Essa função serve para cadastrar o restaurante no aplicativo.'''
    subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes_cadastrados.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso.')
    volta_ao_menu()


def lista_restaurantes():
    '''Essa função serve para listar os restaurantes já cadastrados no aplicativo.'''
    subtitulo('Lista de todos os restaurantes cadastrados')
    n = 1
    print(f"{'NOMES:'.ljust(20)}   {'CATEGORIAS:'.ljust(20)}   {'STATUS:'}")
    for restaurante in restaurantes_cadastrados:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'| {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        # Modo 2
        # print(f'Restaurante {n}')
        # print(f'- Nome: {nome}')
        # print(f'- Categoria: {categoria}')
        # print(f'- Status do restaurante no sistema: {ativo}')
        # print('-' * 20)
        n += 1
    volta_ao_menu()


def volta_ao_menu():
    '''Essa função serve para retornar ao menu após a execução das funções.'''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()


def subtitulo(texto):
    '''Essa função serve para adicionar subtítulos para cada uma das funções do código.'''
    print('\n' * 80)
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()


def ativar_ou_desativar_restaurante():
    '''Essa função serve para alterar o status do restaurante, deixando-o ativo ou não no aplicativo.'''
    subtitulo('Alternando estado do restaurante.')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes_cadastrados:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo']\
                else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado.')
    volta_ao_menu()


def escolhe_opcao():
    '''Essa função serve para que o usuário escolha o que gostaria de fazer no programa.'''
    try:
        escolha = int(input('Escolha uma opção: '))
        if escolha == 1:
            cadastra_restaurante()
        elif escolha == 2:
            lista_restaurantes()
        elif escolha == 3:
            ativar_ou_desativar_restaurante()
        elif escolha == 4:
            finalizar_app()
        else:
            corrige_erros()
    except ValueError:
        corrige_erros()


def main():
    '''Essa função serve para determinar esse arquivo como a main do projeto.'''
    print('\n' * 80)
    exibir_nome_programa()
    menu()
    escolhe_opcao()


if __name__ == '__main__':
    main()
