import datetime

manana = datetime.datetime.now() + datetime.timedelta(days=1)
manana_medianoche = datetime.datetime(year=manana.year, month=manana.month, day=manana.day)
hoy = datetime.datetime.now()
faltante_para_manana = manana_medianoche - hoy

days = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print("Mañana es {} {}".format(days[manana.weekday()], manana.strftime("%d del %m de %Y")))
print("Faltan {} horas para mañana".format(int(faltante_para_manana.total_seconds() / 3600)))
