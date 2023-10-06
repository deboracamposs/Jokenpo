print(' º▬▬▬▬º BEM VINDO AO JOKENPO º▬▬▬▬º')
print()
print('Primeira regra: Não há regras! \n'
      'Digite seus nomes ↓')
jogador_1=input('Seu nome:' ).upper()
jogador_2=input('Seu nome:'  ).upper()
print(f'Bem vindo {jogador_1} e {jogador_2}! Preparados para a disputa?')
print('QUE OS JOGOS COMECEM!')
while True:
    opcaodoj1 = input(f'{jogador_1}, escolha entre → Pedra - Papel - Tesoura, para começar o disputa: ')
    opcaodoj2 = input(f'{jogador_2}, escolha entre → Pedra - Papel - Tesoura, para começar o disputa: ')
    while opcaodoj1 == opcaodoj2:
        print(f' {opcaodoj1} bate com {opcaodoj2} → TEMOS UM EMPATE! ¯\_(ツ)_/¯ NOVA DISPUTA!! ')
        opcaodoj1 = input(f'{jogador_1}, escolha entre → Pedra - Papel - Tesoura, para começar o disputa: ')
        opcaodoj2 = input(f'{jogador_2}, escolha entre → Pedra - Papel - Tesoura, para começar o disputa: ')
    if opcaodoj1 == 'pedra' and opcaodoj2 == 'tesoura':
        print(f'A {opcaodoj1} quebra a {opcaodoj2} (×﹏×)  {jogador_1} VENCEU! ( ͡ᵔ ͜ʖ ͡ᵔ) ')
    elif opcaodoj1 == 'pedra' and opcaodoj2 == 'papel':
        print(f'O {opcaodoj2} embrulha a {opcaodoj1} (×﹏×)  {jogador_2} VENCEU! ( ͡ᵔ ͜ʖ ͡ᵔ) ')
    elif opcaodoj1 == 'papel' and opcaodoj2 == 'pedra':
        print(f'O {opcaodoj1} embrulha a {opcaodoj2} (×﹏×)  {jogador_1} VENCEU! ( ͡ᵔ ͜ʖ ͡ᵔ) ')
    elif opcaodoj1 == 'papel' and opcaodoj2 == 'tesoura':
        print(f'A {opcaodoj2} corta o {opcaodoj1} (×﹏×)  {jogador_2} VENCEU! ( ͡ᵔ ͜ʖ ͡ᵔ) ')
    elif opcaodoj1 == 'tesoura' and opcaodoj2 == 'papel':
        print(f'A {opcaodoj1} corta o {opcaodoj2} (×﹏×)  {jogador_1} VENCEU! ( ͡ᵔ ͜ʖ ͡ᵔ) ')
    elif opcaodoj1 == 'tesoura' and opcaodoj2 == 'pedra':
        print(f'A {opcaodoj2} quebra a {opcaodoj1} (×﹏×)  {jogador_2} VENCEU! ( ͡ᵔ ͜ʖ ͡ᵔ) ')
    print()
    nova_rodada = input('Deseja disputar novamente? \n'
                            'Digite (S) SIM para continuar \n'
                            'Digite (N)  NÃO para sair. ')
    if nova_rodada == "N" or nova_rodada == "n":
        break
print('Jogo finalizado. Volte sempre para mais disputas! ( ͡^ ͜ʖ ͡^) ')
