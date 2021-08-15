# usando a função lambda.
# a lambida é boa por usar 1 linha
# e deixar as coisas mais "simples".
# exemplo:
# usando a função def:
print("def:")
def soma(a,b):
     print(a + b)
soma(9,6)
# multiplica.
def mult(a,b):
    vezes = a * b
    return vezes
print(mult(12,9))
# agora usando a lambda:
# soma.
print("\nlambda:")
soma2 = lambda x,y:x+y
print(soma2(2,2))
# multiplica.
mult2=lambda x,y:print(x*y)
mult2(2,11)
divi = lambda d,o: d/o
print(divi(15,5))
print(divi(10,2))
# ....
# por isso a lambida é melhor por ser mais curta e ate rapida