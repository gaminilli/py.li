# -*- coding: utf-8 -*-
import requests, datetime

api_n = "http://api.openweathermap.org/data/2.5/weather?q=Nantes,fr&units=metric&appid=4b40ffccf6492f6d907b9f4d44c9b0d1"
heure = f"{datetime.datetime.now():%d-%m-%Y}"
x = requests.get(api_n)
resn = x.json()
y = 'Actuellement il fait {} ° Celcius à Nantes'
print (heure)
print (y.format(resn["main"]["temp"]))


############################################################################################################
# Le code au dessus est a usage personnel, pour une ville précise.
# Dans le cas ou quelqu'un souhaite personnaliser avoir l'information pour différentes villes
# il suffit de rajouter un input() qui sera ré-utilisé 
# 	---------------------------------------
#
#
# import requests
# API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  <--- Créez une API KEY sur openweathermap.org
# ville = input("De quelles ville souhaitez vous connaitre la température ?")
# api = "http://api.openweathermap.org/data/2.5/weather?q="+ville+",fr&units=metric&appid="+API_KEY 
# resultat = requests.get(api)
# file = resultat.json()
# text = "Il fait y fait actuellement {} ° Celsius {}"
# print(text.format(file["main"]["temp"]))
# 
# Pour aller plus loin, on pourrait s'envoyer le résultat par e-mail, ou generer une base de donnée (sqlib)
# grace a la collecte d'information journalieres, generer des graphiques... Les possibilités sont
# nombreuses si on souhaite le personnaliser. 
