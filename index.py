from win10toast import ToastNotifier
import random
import json
import schedule
import time

def charger_versets():
    with open('D:/BibleVersets/bible.json', 'r', encoding='utf-8-sig') as f:
        return json.load(f)

def verset_aleatoire():
    data = charger_versets()
    testament = random.choice(data['Testaments'])
    livre = random.choice(testament['Books'])
    chapitre = random.choice(livre['Chapters'])
    verset = random.choice(chapitre['Verses'])
    texte_verset = f"{livre['Text']} {livre['Chapters'].index(chapitre)+1}:{chapitre['Verses'].index(verset)+1} - {verset['Text']}"
    return texte_verset

def envoyer_notification():
    texte_verset = verset_aleatoire()
    toast = ToastNotifier()
    toast.show_toast(
        "Verset Biblique", 
        texte_verset, 
        duration=60  # La notification reste pendant 60 secondes
    )

envoyer_notification()
schedule.every(15).minutes.do(envoyer_notification)

while True:
    schedule.run_pending()
    time.sleep(1)
