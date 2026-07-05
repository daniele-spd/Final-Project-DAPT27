--- Nota iniziale ---
Mi sono reso conto dopo aver fatto tutti i miei test che la traccia era in inglese, quindi nel dubbio ho cambiato tutti i nomi in inglese con Power Query e rinominando anche le misure

Dopo aver trovato diversi problemi nella regressione lineare, ho capito che aveva letto male i valori (il separatore decimale)

________________________________________________________________________________________________________
--- Importazione dati ---
Non legge bene i decimali del CSV perché ha separatore "." come nello standard inglese
Quindi come secondo step ho aggiunto Replaced Value di "." con "," e poi nel Changed Type ho messo decimale alla colonna della Superficie (unica non intera)

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
--- Creazione tabelle, colonne e misure ---
Creato tabella 
	Coordinate ripartizioni (vedi sopra)
	Codici tipo di dato -> Tabella delle dimensioni per avere in visualizzazione un testo più parlante rispetto ai codici

Creato colonna calcolata 
	Località (vedi sopra)

Creato misura
	Densità di popolazione -> Meglio misura per aggregazione e perché rimane dinamico con i filtri
	Valore relativo_superficie e Valore relativo_1000abitanti
	REGRESSIONE LINEARE IN SOSPESO
	Feriti/Morti per incidenti -> Usato REMOVEFILTERS e cambiato il Filter Context con CALCULATE
	Medie italiane -> Come sopra, rimuovendo anche il filtro sulla Municipality perché sono in pagina Drill through
	Popolazione coinvolta/ferita/ecc. Ho dei doppioni perché se metto il valore complessivo in tabella con Category mi basta uno solo, ma se avessi voluto usarli singolarmente li avevo creati

	ALTRE MISURE PER LA REGRESSIONE LINEARE, DEVO DESCRIVERLE MA PREFERISCO FARE COMMIT NEL FRATTEMPO

Gerarchia
	Region
	Province
	Municipality
	Utile per i grafici con drill down sulla Location