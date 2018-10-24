from random import *
from io import BytesIO
from PIL import Image
from requests import get
def pokemongame():
    while True:
        x = randint(1,152)
    #print(x)
        result = get(f'https://pokeapi.co/api/v2/pokemon/{x}/')
        mypokemon = result.json()
        pokemonname = mypokemon['name']
    #print(pokemonname)
        image_url = get(f'https://pokeapi.co/api/v2/pokemon/{pokemonname}').json().get('sprites',{}).get('front_default')
        Image.open(BytesIO(get(image_url).content)).show()
        playeranswer = str(input("What Pokemon is this?"))
        if playeranswer.lower() == pokemonname:
            print("That's right! Good job! Would you like to play again?\nType 'yes' to play again")
            playagain = input('')
            if playagain.lower == 'yes':
                pass
            else:
                return "Goodbye!"
        if playeranswer.lower() != pokemonname:
            return "OOF"
            
