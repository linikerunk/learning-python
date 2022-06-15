"""
Por que testar nosso código?

Testar Automatizados!


Aplicação Web
/---------------------/
/  frontend e backend /
/----------------------/
/ teste automatizados  /
/----------------------/

Por que testar nosso código?
    - Reduzir bugs (problemas) no código existe;
    - Testes garantem que novos recursos da sua aplicação não quebram (alterar)
    recursos antigos;
    - Teste garantem que bugs (problemas) que foram corrigidos anteriormente con-
    tinuem corrigidos;
    - Teste garantem que a refatoração que costumamos a fazer, não tragam novos
    bugs (problemas);

TDD - TEste Driven Development (Desenvolvimento Guiado por Teste)

com TDD é utilizado estágios de desenvolvimento:
    - Você escreve seu teste primeiro;
    - Então você escreve o código minimo suficiente para fazer o teste passar
    (ou seja, executar com sucesso);
    - Então refatora o código para realizar a funcionalidade e testa novamente;
    - Uma vez que o teste passe, o recurso e considerado completo;

Estes estágios de desenvolvimento do TDD são quase como um mantra que os desenvol-
vedores seguem, conhecidos como;
    - Red;
    - Green;
    - Refactor;
    
"""


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando...')


felix = Gato('Felix')

felix.miar()

print(felix.nome)