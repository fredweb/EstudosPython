__author__ = 'george'

numberOne = int(input("Digite o numero 1"))
numberTwon = int(input("Digite o numero 2"))

while numberTwon == 0:
    print "Divisor Igual a Zero!\n Digite divisor novamente"
    numberTwon = int(input("Digite o numero 2"))

divisao = int(numberOne/numberTwon)

print "Divisao e " + str(divisao)

