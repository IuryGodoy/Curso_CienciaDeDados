#definindo variáveis
num1 = float(input("Digite um número: "))
num2 = float()
operacao = str()
#condições de existencia
while operacao != "=":
#informa qual operação deve ser feita
  operacao = str(input("Qual operação você gostaria de fazer?(+, -, *, /), para ver resultado final(=)"))
#verifica resultado final quando encerrar calculadora
  if operacao == "=":
    print("Resultado final é:", num1)
    break
#valida se a operação é válida
  if operacao != "+" or "-" or "*" or "/" or "=":
    print("Operação inválida")
    continue
#recebe segunda variável
  num2 = float(input("Digite outro número: "))

#calculando
  if operacao == "+":
    resultado = num1 + num2
  elif operacao == "-":
    resultado = num1 - num2
  elif operacao == "*":
    resultado = num1 * num2
  elif operacao == "/":
    if num2 != 0:
      resultado = num1 / num2
#verifica se divisão existe
    else:
      print("Divisão por 0 não existe")
      continue
  else:
    print("Operação inválida")
    continue

#exibe resultado da operação
  print("O resultadoo é: ", resultado)

#atribuindo resultado a uma variável para poder fazer outro cálculo
  num1 = resultado
