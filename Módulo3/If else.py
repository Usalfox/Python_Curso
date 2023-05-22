# 1
asteroide = 49
if asteroide > 25:
    print('Un asteroide se acerca, y viaja a una velocidad de'+ str(asteroide) + 'km/s.')
else:
    print('Ningun peligro detectado')


#2
asteroide = 19
if asteroide > 20:
    print('Una luz se logra ver en el cielo')
elif asteroide == 20:
    print('Una luz se logra ver en el cielo')
else:
    print('No hay nada visble en el cielo')

#3
velocidadasteroide = 25
tamanoasteroide = 40
if velocidadasteroide > 25 and tamanoasteroide > 25:
    print('Un asteroide esta por inpactar la tierra')
elif velocidadasteroide >= 20:
    print('Una luz se logra ver el el cielo')
elif tamanoasteroide < 25:
    print('No hay nada visible ne el cielo)')
else:
    print('No hay nada visible en el cielo')
