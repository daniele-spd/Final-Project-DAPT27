--- Elenco province ---
Niente pulizia, c'è un NaN nella targa di Napoli ma non dovrebbe dare fastidio perché i dati ci sono tutti nella tabella dei comuni

________________________________________________________________________________________________________
--- Elenco comuni ---
Ho lasciato che dal 2024 i capoluoghi di provincia fossero duplicati, perché non penso di utilizzare la colonna ma non volevo eliminarla. Magari più in là decido che potrebbe essere carino fare qualche analisi e poi mi dimenticherei dell'esistenza del dato.
Colonna Superficie
	Prima sostituito . con niente (separatore migliaia)
	Poi sostituito , con . (separatore decimale) e convertito in float
Colonna Targa
	Corretto manualmente NaN in NA (Napoli)
Comune NaN
	Corretto in "None", in provincia di Torino

________________________________________________________________________________________________________

--- Elenco incidenti 2020_2024 ---
Niente pulizia

________________________________________________________________________________________________________

--- Complessivo ---
Corretto alcuni codici provincia manualmente prima del Join, per evitare NaN in Ripartizione geografica, Regione e Provincia/Uts
