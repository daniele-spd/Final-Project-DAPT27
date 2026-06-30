--- Importazione dati ---
Non legge bene i decimali del CSV perché ha separatore "." come nello standard inglese
Quindi come secondo step ho aggiunto Replaced Value di "." con "," e poi nel Changed Type ho messo decimale alla colonna della Superficie (unica non intera)

Coordinate ripartizioni
Vedi nota in Modifiche dati

________________________________________________________________________________________________________
--- Modifiche dati ---
Rimosso la colonna DATA_TYPE
Ho deciso di tenere la colonna RESULT perché penso che possa tornarmi utile per separare i dati con un filtro piuttosto che fare dei segnalibri su tabelle diverse
Rendo più parlanti alcune colonne
Ho eliminato i dati del 2025 perché non ho disponibili i dati di incidenti di quell'anno

Ho reso dati geografici:
Ripartizione geografica = tramite coordinate della tabella Coordinate ripartizioni, vedi sotto
Regione = County
Provincia = State or Province
Comune = in realtà ho lasciato Uncategorized perchè faceva casino, ma ho fatto Place (tramite colonna calcolata Località che include anche provincia e stato)

	Creato tabella Coordinate ripartizioni
	Coordinate ripartizioni inserendo manualmente i dati copiati da internet di coordinate di riferimento delle ripartizioni geografiche
	Pulito la tabella cambiando il separatore
	Creato la relazione tra la tabella dei fatti e la tabella delle dimensioni appena creata
	Reso geografiche Latitudine e Longitudine, mettendo come Path ID la ripartizione

________________________________________________________________________________________________________
--- Creazione colonne e misure ---
Creato tabella 
	Coordinate ripartizioni (vedi sopra)
	Codici tipo di dato -> Tabella delle dimensioni per avere in visualizzazione un testo più parlante rispetto ai codici

Creato colonna calcolata 
	Località (vedi sopra)

Creato misura
	Densità di popolazione -> Meglio misura per aggregazione e perché rimane dinamico con i filtri
	Valore relativo_superficie e Valore relativo_1000abitanti -> Idem
	Valore, valore anno precedente e variazione % -> Per identificare i comuni in cui la situazione peggiora/migliora