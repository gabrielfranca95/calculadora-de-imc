peso= float (input ('Digite o seu peso em KG:'))
altura= float ( input ('Digite a sua altura em M:'))
IMC= peso/(altura**2)
print ('Seu IMC é de', IMC)
if IMC>= 40:
    print ('Você possui obesidade morbida procure um medico e evite várias doenças...')
elif IMC>= 35 and IMC < 40:
    print ('Você possui obesidade com altos níveis procure ajuda proficional')
elif IMC>= 30 and IMC< 35:
    print ('Você está acima do peso, o ideal é fazer uma reeducação alimentar')
elif IMC>=25 and IMC <30:
    print ('Você esta levemente acima do peso, vamos fazer exercicios?!')
elif IMC>= 18.5 and IMC <25:
    print ('Você está com o peso ideal parabens!você faz parte de um pequeno grupo de possoas potencialmente saldaveis')
elif IMC>= 17 and IMC< 18.5:
    print ('Você está magro, mas no estágio inicial, levemente abaixo do peso')
elif IMC>=16 and IMC<17:
    print ('Você está bem magro')
elif IMC <16:
    print ('você esta com alto nivel de magresa!!')