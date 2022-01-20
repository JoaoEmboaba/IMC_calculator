altura = float(input('Entre com sua altura:'))
peso = float(input('Entre com seu peso:'))
imc = peso/(altura * altura)
print('Seu índice de massa corporal é {:.2f}'.format(imc))
if (imc) < 17.0:
  print('Você está muito abaixo do peso')
  exit()
if (imc) <= 18.0:
  print('Você está abaixo do peso')
  exit()
if (imc) <= 24.99:
  print('Seu peso está normal')
  exit()
if (imc) <= 29.99:
  print('Você está acima do peso')
  exit()
if (imc) <= 34.99:
  print('Obesidade I')
  exit()
if (imc) <= 39.00:
  print('Obesidade II')
  exit()
