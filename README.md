Il progetto riguarda la situazione degli incidenti stradali in Italia negli ultimi anni.
Sono incluse statistiche su feriti e morti, con calcoli su popolazione e superficie dei comuni in cui sono stati registrati gli incidenti.
I dati sono aggregati per anno, e per regione-provincia-comune.

I dati sono stati scaricati dall'ISTAT e riguardano le annate dal 2020 al 2024 (ultimo anno disponibile).
Nota: i dati utilizzati in Power BI e nei notebook Python sono stati scaricati manualmente, e solo in seguito è stato aggiunto a scopo dimostrativo uno script che utilizza web scraping, più una automatizzazione della richiesta API.

I dati di partenza sono nella cartella Dataset, mentre quelli esportati da Python dopo la pulizia sono nella cartella Dati_puliti.
Sono stati fatti due ReadMe sulla pulizia dei dati con Python e sulla gestione dei dati in Power BI.

Strumenti utilizzati:
Python, Power BI.

Contenuto repository:
* Dataset = dati di partenza scaricati manualmente
* Dati_puliti = dati esportati da Python, dopo pulizia
* Immagini = immagini usate nella presentazione PowerPoint o in Power BI
* API filtrato = notebook dimostrativo per download migliorato dei dati tramite richiesta API
* Incidenti (ipynb) = Trattamento dei dati principale
* Incidenti (pbix) = Report di Power BI
* Presentazione = Breve presentazione del progetto in PowerPoint
* ReadMe_Power_BI = Appunti e indicazioni per il trattamento dei dati in Power BI
* ReadMe_data_cleaning = Appunti e indicazioni per il trattamento dei dati in Python
* Script richiesta API = script dimostrativo per download migliorato dei dati tramite richiesta API
* Script web scraping = script dimostrativo per download tramite web scraping
* Web scraping = notebook dimostrativo per download tramite web scraping
