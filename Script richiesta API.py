

################### Riassunto ###################
'''
Il file eseguibile deve essere in una cartella che contenga una sotto-cartella "Dati_puliti"
Controlla i file CSV chiamati Elenco incidenti (Archivio) e capisce le annate già scaricate (Anni_disponibili)
Poi crea l'elenco degli anni che dovrei avere a disposizione (2020 - presente) nell'elenco Anni_teorici
Crea la lista Anni_mancanti
Funzione di download: fa una richiesta API con timeout di 5 minuti. Se il codice risposta è 200, scarica un anno di dati e lo salva in CSV, altrimenti esce un messaggio di errore che suggerisce di ricontrollare il database o la possibilità che l'anno mancante non esista ancora 
Ciclo for finale: se non ci sono anni mancanti, esce un messaggio, altrimenti scarica un anno alla volta (per evitare il controllo sulla consecutività degli anni mancanti e per velocizzare le singole richieste API)
'''

import numpy as np
import pandas as pd

# Per API
import requests
from io import StringIO

import os
from datetime import datetime

################### Creazione archivio ###################
os.chdir("Dati_puliti") #Assumo che il file eseguibile sia nella cartella con il resto, e che ci sia la sotto-cartella Dati_puliti
os.listdir()

Archivio = []
Cartella_archivio = os.listdir()
for f in Cartella_archivio:
    if f.startswith("Elenco incidenti ") and f.endswith(".csv"):
        Archivio.append(f)
Archivio.sort() # Devo ordinare per anno crescente

################### Annate che ho già scaricato ###################
Anni_disponibili = []
for a in range(0, len(Archivio)): # tutti gli elementi di Archivio
    Anno_inizio = int(Archivio[a][17:21]) #converto in intero la parte del file dell'anno di inizio
    Anno_fine = int(Archivio[a][22:26])
    for n in range(Anno_inizio, Anno_fine + 1): # tutti gli anni in ogni file, tra inizio e fine
        Anni_disponibili.append(n)

################### Annate che dovrebbero esserci ###################
# Adesso devo fare l'elenco degli anni tra il 2020 e l'anno corrente
Anno_corrente = datetime.now().year
Anni_teorici = list(range(2020, Anno_corrente + 1))


################### Annate mancanti ###################
# Sono già ordinate, perchè la lista delle annate che dovrebbero esserci è ottenuta da un range
Anni_mancanti = []
for a in Anni_teorici:
    if a not in Anni_disponibili:
        Anni_mancanti.append(a)

################### Download dati ###################
# Scaricare dall'API, un anno alla volta altrimenti dovrei controllare che siano consecutivi per non avere doppioni
def Download_dati_API():
    headers = {'Accept': 'application/vnd.sdmx.data+csv;version=1.0.0'}


    r = requests.get(URL_complessivo,
        headers=headers,
        timeout=300) # dovrebbero bastare pochi minuti
    print("Codice risposta API = ", r.status_code)
    if r.status_code == 200:
        DataFrame = pd.read_csv(StringIO(r.text), sep=",")
        Nome_file = "Elenco incidenti " + str(a) + "_" + str(a) + ".csv"
        DataFrame.to_csv(Nome_file, index = False)
        print("Salvato il file dell'anno ", a)
        return r #lo lascio per eventuale debugging, non servirebbe
    else:
        print("L'anno ", a, " potrebbe non esistere nel database oppure la richiesta è sbagliata. Controlla il codice risposta API e verifica se potrebbe non esistere l'anno che cerchi")

################### Cosa succede in base al numero di annate mancanti ###################
if len(Anni_mancanti) == 0:
    print("Non ci sono annate da scaricare")
else:
    print("Anni mancanti: ", Anni_mancanti)
    URL_inizio = "https://esploradati.istat.it/SDMXWS/rest/data/41_983?startPeriod="
    URL_resto = "&endPeriod="
    for a in Anni_mancanti:
        URL_complessivo = URL_inizio + str(a) + URL_resto + str(a - 1) #Perchè per filtrare un anno c'è il bug su EndPeriod
        print("Scarico dati da ", URL_complessivo)
        print("Il processo potrebbe richiedere anche diversi minuti, non interrompere")
        Download_dati_API()