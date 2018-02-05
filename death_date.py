
import datetime
import random

AVERAGE_LIFESPAN = 80

SMOKER_PENALIZATION = 5
DRINKER_PENALIZATION = 10
SEDENTARY_PENALIZATION = 20


def print_with_underscores(message):
    print(message)
    print(len(message) * "-")


def ask_yes_or_not(message):
    response = None
    while response != "S" and response != "N":
        response = input(message + " [S/N]")
    return response == "S"


print_with_underscores("¡Averigua cuanto te queda de vida!")
print("Completa esta encuesta para saber cuanto tiempo de vida te queda")

birth_date = input("¿Cuál es tu fecha de nacimiento (formato: dd/mm/yyyy)? ")

birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")
years_lost = 0

if ask_yes_or_not("¿Fumas?"):
    years_lost += SMOKER_PENALIZATION

if ask_yes_or_not("¿Bebes?"):
    years_lost += DRINKER_PENALIZATION

if not ask_yes_or_not("¿Haces deporte?"):
    years_lost += SEDENTARY_PENALIZATION

base_lifespan = random.random() * AVERAGE_LIFESPAN / 2 + AVERAGE_LIFESPAN / 2

lifespan = AVERAGE_LIFESPAN - years_lost
death_day = birth_date + datetime.timedelta(days=lifespan*365)
days_to_death = death_day - datetime.datetime.now()

print("Fecha de muerte {}, te quedan {} días para morir".format(death_day.strftime("%d/%m/%Y"), days_to_death.days))
