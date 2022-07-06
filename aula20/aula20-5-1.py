secret_word = 'girafa' # --> Palavra secreta da forca.
typed_letter = []
chances = 3

while True:
    if chances < 1:
        print('Você perdeu! kkkkkkkkk')
        break
    
    letter = input('Digite uma letra: ')
    if len(letter) > 1:
        print("Digite apenas uma letra meu chapa!")
        continue
    
    typed_letter.append(letter)

    if letter in secret_word:
        print(f'BOA! existe uma letra "{letter}" na palavra secreta. ')
    else:
        print(f'Que pena! Não existe a letra "{letter}" na palavra secreta.')
        typed_letter.pop()
    
    temporary_secret = ''
    for secret_letter in secret_word: # --> Iteration with the secret_word elements
        if secret_letter in typed_letter:
            temporary_secret += secret_letter
        else:
            temporary_secret += '*'
    
    if temporary_secret == secret_word:
        print("\U0001f600")
        print(f"Parabéns, a palavra secreta é:  \"{temporary_secret}\".")
        break
    else:
        print(f'Palavra: {temporary_secret}.')
    
    if letter not in secret_word:
        chances -= 1
    
    print(f"Atualmente você tem {chances} chances.")

    print()


