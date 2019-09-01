#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa deve perguntar o valor da casa a comprar, o salário e a quantidade
#de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do
#salário. Calcule o valor da prestação como sendo o valor da casa a comprar
#dividido pelo número de meses a pagar.

valor_casa = float(input('Digite o valor da casa desejada : '))
salario = float(input('Digite seu sálario : '))
qtd_anos = int(input('Quantidade de ano(s) a se pagar : '))
    
prestacao = (valor_casa / (qtd_anos * 12))
salario_taxa = salario * 0.3

if prestacao  > salario_taxa:
    print(' Infelizmente você não foi aprovado..')
    print(f' valor da prestação : {prestacao} e maior que 30% do seu \n \
    salario : {salario_taxa} <- 30%')

elif prestacao <= salario_taxa:
    print(' Parabéns !!!! sua casa foi aprovada')
    print(f'Sua prestação será : {prestacao}')
