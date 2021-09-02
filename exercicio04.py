valort = float(input("Digite o valor total do prêmio: "))
 
vestado = (valort * 0.07)
vestado2 = (valort * 0.93)
primeiro = (vestado2 * 0.46)
segundo = (vestado2 * 0.32)
terceiro = (vestado2 * 0.22)

print("Valor do premio é igual a {}, teve um desconto de {}, Primeiro, Segundo e Terceiro ganhram respectivamente : {}, {}, {} : " .format(valort, vestado, primeiro, segundo, terceiro))
