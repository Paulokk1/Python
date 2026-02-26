ci1 = input('Estamos caçando alguém do rio de janeiro, digite o nome da sua cidade: ').lower()
ci2 = ci1.find('montes claros')
if ci2 == 0:
    print('Você é de moc')
else:
    print('não é de moc')