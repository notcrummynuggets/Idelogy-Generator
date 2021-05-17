import random
import time

ideologies = ["Anarchist", "Communist", "Conservitive", "Corporatist", "Democratic", "Environmentalist", "Fascist", "Liberalist", "Libertarian", "Nationalist", "Populist", "Socialist", "Posadist", "Fuedalist"]
adgectives = ["Neo", "Classical", "Anarcho", "Post"]
ideology1 = random.choice(ideologies)
ideology2 = random.choice(ideologies)
adgective = random.choice(adgectives)

question = input("Enter your polotical opinions: ")
print("Calculating...")
time.sleep(0.5)
print("Generating..")
time.sleep(1)
print("Your Ideology is... " + adgective + "-" + ideology1 + "-" + ideology2 + "!")
