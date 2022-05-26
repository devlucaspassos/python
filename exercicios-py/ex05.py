'''
5º Exercício
    Fazer um algoritmo que ao receber o salário atual de um funcionário, calcule o valor do novo salário reajustado de acordo com a tabela abaixo.

    Abaixo de R$500,00 - 15%
    de R$500,00 até R$1000,00 - 10%
    Acima de R$1000,00 - 5%
'''


salario_atual = int(input('Digite o salário do funcionário: '))

if salario_atual <= 500:
    reajuste = salario_atual * 0.15
    print(f'O salário total deste funcionário após o reajuste é de: {salario_atual + reajuste:.0f}')
elif salario_atual > 500 or salario_atual <= 1000:
    reajuste = salario_atual * 0.10
    print(f'O salário total deste funcionário após o reajuste é de: {salario_atual + reajuste:.0f}')
elif salario_atual > 1000:
    reajuste = salario_atual * 0.05
    print(f'O salário total deste funcionário após o reajuste é de: {salario_atual + reajuste:.0f}')




