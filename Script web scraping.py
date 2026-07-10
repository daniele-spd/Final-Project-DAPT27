'''
Il file eseguibile funziona se esiste una cartella "C:/Users/Computer/Downloads"
Chiede in input l'anno/gli anni da scaricare (devono essere consecutivi)
Scarica tutti i file CSV richiesti (finiscono nella cartella download del computer)
Cerca tutti i file CSV che hanno un nome simile a quello dei file appena scaricati
Se non esiste già, crea una cartella "Dataset scraping" nei download e ci sposta dentro i file 
Ciclo for finale: se non ci sono anni mancanti, esce un messaggio, altrimenti scarica un anno alla volta (per evitare il controllo sulla consecutività degli anni mancanti e per velocizzare le singole richieste API)
'''

import numpy as np
import pandas as pd


from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time #questa per aspettare che si carichi la pagina e il download


print("Seleziona gli anni che ti interessa scaricare. Devono essere consecutivi, altrimenti lancia lo script più volte per ottenere tutti gli anni")
Anno_inizio = int(input("Scrivi il primo anno che vuoi scaricare: "))
Anno_fine = int(input("Scrivi l'ultimo anno (compreso) che vuoi scaricare. Se ti interessa solo un anno, riscrivi quello di prima: "))
years = range(Anno_inizio, Anno_fine + 1)

# Tutti gli URL cominciano e finiscono nello stesso modo, cambia solo l'anno
URL_inizio = "https://situas.istat.it/web/#/territorio/body?id=74&dateFrom="
URL_fine = "-12-31"

# Apro la pagina solo una volta, fuori dal ciclo, e poi ogni volta cambio l'URL
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)

# Per ogni anno, cambio URL, poi scarico il CSV
for y in years:
    URL_complessivo = URL_inizio + str(y) + URL_fine #serve str perchè era un numero intero
    driver.get(URL_complessivo)

    time.sleep(5) #Aspetto qualche secondo per il caricamento della pagina, un paio di volte era andato in errore 
    Bottone_Esporta = driver.find_element(By.ID, "dati-report-export-btn") 
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", Bottone_Esporta) #scrollo fino a rendere visibile il bottone, altrimenti va in errore
    time.sleep(2) #Aspetto ancora per il caricamento del buttone, andava spesso in errore
    driver.find_element(By.ID, "dati-report-export-btn").click() # clicco

    Bottone_CSV = driver.find_element(By.XPATH, "//button[@title='Scarica dati in formato CSV']")
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", Bottone_CSV)
    driver.find_element(By.XPATH, "//button[@title='Scarica dati in formato CSV']").click()
    print("Scaricato anno ", y) # Aggiunto questo perchè negli script mi sembra più sensato
    

######################## Fine del ciclo for di scraping ########################

#Provo ad aspettare qualche secondo perchè una volta non mi ha spostato il file 2024 nonostante fosse tutto giusto, forse non lo avevo ancora scaricato
time.sleep(5) 


######################## Ciclo for di spostamento ########################

# Scelgo solo i file che sono nei download, che sono CSV e si chiamano in un certo modo
os.chdir(r"C:\Users\Computer\Downloads")
File_da_spostare = []
Download = os.listdir()
for f in Download:
    if f.startswith("Comuni - Dimensione Data Indagine") and f.endswith(".csv"):
        File_da_spostare.append(f)

# In un secondo momento, ho pensato anche di implementare il controllo sull'esistenza della cartella. Inizialmente avevo fatto solo mkdir
os.makedirs("Dataset scraping", exist_ok = True)

# Qui non servono controlli perchè la directory Download credo che esista in tutti i computer, quella in cui spostare i file l'ho appena creata io se non esisteva già
Partenza = r"C:\Users\Computer\Downloads"
Destinazione = r"C:\Users\Computer\Downloads\Dataset scraping"
for f in File_da_spostare:
    os.rename(os.path.join(Partenza, f),
              os.path.join(Destinazione, f))

print("Script completato, trovi i file nella cartella Dataset scraping all'interno dei download") # Aggiunto questo perchè negli script mi sembra più sensato
print("Attenzione, se hai inserito un anno non ancora completo o futuro, verranno scaricati i dati aggiornati al giorno in cui viene lanciato lo script") # Aggiunto 