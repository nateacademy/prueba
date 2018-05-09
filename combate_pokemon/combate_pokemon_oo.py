
class BasePokemon:
    base_health_points = 100
    damage = 10
    name = "Pokemon"
    attacks = []

    def __init__(self):
        self.health_points = self.base_health_points

    def fight(self, enemy, attack_name=None):
        print("{} ataca a {} con {}".format(self.name, enemy.name, attack_name if attack_name else "ataque base"))
        if not attack_name:
            enemy.take_damage(self.damage)
        else:
            for attack in self.attacks:
                if attack.name == attack_name:
                    enemy.take_damage(attack.damage)
                    return

    def take_damage(self, damage):
        self.health_points -= damage

    def show_health_points(self):
        print("Vida de {}: {}".format(self.name, self.health_points))

    def is_defeated(self):
        return self.health_points <= 0


class BasePokemonAttack:
    name = ""
    damage = 0


class ChispazoAttack(BasePokemonAttack):
    name = "Chispazo"
    damage = 10


class BolaVoltioAttack(BasePokemonAttack):
    name = "Bola Voltio"
    damage = 9


class Charmander(BasePokemon):
    base_health_points = 100
    damage = 10
    name = "Charmander"


class Pikachu(BasePokemon):
    base_health_points = 120
    damage = 12
    name = "Pikachu"
    attacks = [ChispazoAttack, BolaVoltioAttack]


class Bulbasaur(BasePokemon):
    base_health_points = 90
    damage = 7
    name = "Bulbasaur"


class Squirtle(BasePokemon):
    base_health_points = 100
    damage = 3
    name = "Squirtle"
