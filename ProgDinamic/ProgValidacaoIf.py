#Programa que valida se o usuário é obrigado a votar utilizando IF/ELSE/ELIF
idade = int(input("Quantos anos você tem?"))

if idade<= 16:
  print("Você não pode votar: ")
elif idade < 18:
    print("Você pode votar, mas é facultativo: ")
elif  idade < 78:
    print("No seu caso o voto é obrigatório!")
else:
    print("Você não é mais obrigado a votar, é facultativo")

    print("FIM!")
