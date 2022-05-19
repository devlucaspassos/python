secret_word = 'python'
typed_letter = []
chances = 3

while True:
    if chances < 1:
        print('Game Over')
        break
    
    letter = input('Type a letter: ')
    if len(letter) > 1:
        print(f"Ahh c'mon, it's just one letter my boy.")
        continue
    
    typed_letter.append(letter)

    if letter in secret_word:
        print(f'Yeaah, there is a "{letter}" in the secret word.')
    else:
        print(f'Sorry, but there is no "{letter}" in secret word.')
        typed_letter.pop()
    
    temporary_secret = ''
    for secret_letter in secret_word: # --> Iteration with the secret_word elements
        if secret_letter in typed_letter:
            temporary_secret += secret_letter
        else:
            temporary_secret += '*'
    
    if temporary_secret == secret_word:
        print(f"YEAHH MY NWORD, YOU'VE GOT THE SAUCE. THE SECRET WORD WAS \"{temporary_secret}\".")
        break
    else:
        print(f'The secret word is currently: {temporary_secret}.')
    
    if letter not in secret_word:
        chances -= 1
    
    print(f"Currently you've got {chances} chances.")

    print()


