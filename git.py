soma=0
x=0
a=int(input('insira um valor para A:'))
b=int(input('Insira um valor maior que A para B:'))
if b>a:
    for i in range(a+1,b,1):
        soma=soma+i
    print(soma)
else:
    print('O segundo valor deve ser obrigatoriamente maior que o primeiro')
    a = int(input('insira um valor para A:'))
    b = int(input('Insira um valor maior que A para B:'))
    for i in range(a+1,b,1):
        soma=soma+i
    print(soma)