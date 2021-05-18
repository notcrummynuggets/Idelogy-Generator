import random
import time

ideologies = ["Anarchist", "Communist", "Conservitive", "Corporatist", "Democratic", "Environmentalist", "Fascist", "Liberalist", "Libertarian", "Nationalist", "Populist", "Socialist", "Posadist", "Fuedalist"]
adgectives = ["Neo", "Classical", "Anarcho", "Post"]

def derfinings():
    global ideology1
    global ideology2
    global adgective
    ideology1 = random.choice(ideologies)
    ideology2 = random.choice(ideologies)
    adgective = random.choice(adgectives)
    if ideology1 == ideology2:
        derfinings()

def printing():
    print("Calculating...")
    time.sleep(0.5)
    print("Generating..")
    time.sleep(1)
    print("Your Ideology is... " + adgective + "-" + ideology1 + "-" + ideology2 + "!")

derfinings()
printing()
