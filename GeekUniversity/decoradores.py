"""
Decoradores (Decorators)

O que são decorators?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar / Açúcar Sintático)


|------------------------------------------------|
|                Function Decorator              |
|------------------------------------------------|

-------------------------------------------------------
|  |------------------------------------------------| |
|  |------------------------------------------------| |
|  |                 Function  Decorator            | |
|  |------------------------------------------------| |
|  |------------------------------------------------| |
-------------------------------------------------------

"""

# Decorators como funções (Sintaxe não recomendada / Sem Açucar Sintático)

# def seja_educado(funcao):
#     def sendo():
#         print("Foi um prazer conhecer você!")
#         funcao()
#         print("Tenha um ótimo dia!")
#     return sendo


# def saudacao():
#     print("Seja bem vindo ao lugar do codehard.")

# # Testando 1

# teste = seja_educado(saudacao) # a função decorator recebe uma função como parametro

# teste()

# # Testando 2

# def raiva():
#     print('EU TE ODEIO')

# print(raiva())

# raiva_educada = seja_educado(raiva)

# raiva_educada()

# DECORATORS COM Syntax Sugar / Açucar Sintático


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print("Meu nome é João!")

apresentando()

@seja_educado_mesmo
def dormir():
    print("Quero dormir...")

dormir()



"""
|--------------------------------------------------------------|
|  Home        | Serviço     | Produtos    |  Administrativo   |
|______________________________________________________________|

/home -> home
/serviço -> serviço
/produtos -> produtos
/administrativo -> administrativo


# OBS: Não funciona código...

def checa_login(request):
    if not request.usuario:
        redirect('http://www.suaempresa.com.br)

def home(request):
    return 'Pode acessar o home'

@checa_login
def admin(request):
    return 'Pode acessar admin'

"""

# OBS: Não confunda Decorator com Decorator Function
# Decorator é o @nome_funcao / decorator function é a própria funcao decoradora...

