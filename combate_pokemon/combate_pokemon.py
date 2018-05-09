from combate_pokemon_oo import Charmander, Bulbasaur, Pikachu, Squirtle

def choose_pokemon():
    chosen_pokemon = input("¿Contra qué Pokemon quieres combatir? (Squirtle / Charmander / Bulbasaur): ")

    if chosen_pokemon == "Squirtle":
        return Squirtle()
    elif chosen_pokemon == "Charmander":
        return Charmander()
    elif chosen_pokemon == "Bulbasaur":
        return Bulbasaur()


def main():
    pikachu = Pikachu()
    enemy = choose_pokemon()

    while not enemy.is_defeated() and not pikachu.is_defeated():
        chosen_attack = input("¿Qué ataque vamos a usar? (Chispazo / Bola voltio)")
        pikachu.fight(enemy, chosen_attack)

        enemy.show_health_points()
        enemy.fight(pikachu)

        pikachu.show_health_points()

    if enemy.is_defeated():
        print("¡Has ganado!")

    if pikachu.is_defeated() <= 0:
        print("¡Has perdido!")


if __name__ == "__main__":
    main()
