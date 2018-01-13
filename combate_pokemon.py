
pokemon_elegido = input("¿Contra qué Pokemon quieres combatir? (Squirtle / Charmander / Bulbasaur): ")

vida_pikachu = 100
vida_enemigo = 0
ataque_pokemon = 0

if pokemon_elegido == "Squirtle":
    vida_enemigo = 90
    nombre_pokemon = "Squirtle"
    ataque_pokemon = 8

elif pokemon_elegido == "Charmander":
    vida_enemigo = 80
    nombre_pokemon = "Charmander"
    ataque_pokemon = 7

elif pokemon_elegido == "Bulbasaur":
    vida_enemigo = 100
    nombre_pokemon = "Bulbasaur"
    ataque_pokemon = 10

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿Qué ataque vamos a usar? (Chispazo / Bola voltio)")

    if ataque_elegido == "Chispazo":
        vida_enemigo -= 10
    elif ataque_elegido == "Bola voltio":
        vida_enemigo -= 12

    print("La vida del {} ahora es de {}".format(nombre_pokemon, vida_enemigo))

    print("{} te hace un ataque de {} de daño".format(nombre_pokemon, ataque_pokemon))
    vida_pikachu -= ataque_pokemon

    print("La vida de Pikachu es de {}".format(vida_pikachu))

if vida_enemigo <= 0:
    print("¡Has ganado!")

if vida_pikachu <= 0:
    print("¡Has perdido!")

print("El combate ha terminado")
