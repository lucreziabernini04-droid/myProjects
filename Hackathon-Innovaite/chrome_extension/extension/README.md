# Chrome Extension: DataPizza Chat Helper

Questa cartella contiene uno scaffold minimale per trasformare il progetto in una estensione Chrome.

Cosa fa:
- `popup.html` apre una piccola UI che lancia la pagina frontend nel browser.
- `content.js` inietta un pulsante flottante su ogni pagina che apre la UI in una nuova scheda.
 - `popup.html` apre una piccola UI che lancia il chatbot standalone (`chat.html`) nel browser.
 - `content.js` inietta un pulsante flottante su ogni pagina che apre il chatbot standalone in una nuova scheda.

Prerequisiti:
- Avviare il backend del progetto (vedi `backend/main.py`) sulla porta 8000.

Esempio (PowerShell):

```powershell
# attiva l'ambiente virtuale se ne hai uno
# .\venv\Scripts\Activate.ps1

# avvia il backend (assumendo che main.py esponga il frontend su http://localhost:8000)
python backend\main.py
```

Caricare l'estensione in Chrome (modalità sviluppatore):
1. Apri `chrome://extensions/`.
2. Attiva `Developer mode` (in alto a destra).
3. Clicca `Load unpacked` e seleziona la cartella `extension/` in questo repository.
4. Dovresti vedere l'icona dell'estensione nella barra degli strumenti; cliccala e scegli `Apri Chat` o usa il pulsante iniettato nelle pagine.

Note importanti:
- L'estensione apre la pagina `http://localhost:8000/frontend/bocconi.html`. Assicurati che il server serva quella risorsa e che non ci siano restrizioni CORS o X-Frame-Options se decidi di usare iframe.
 - L'estensione apre ora la pagina interna `chat.html` (standalone chatbot). Se vuoi usare il backend per risposte RAG, avvia il server (`backend/main.py`) su `http://localhost:8000` — la UI chiamerà gli endpoint `/api/*`.
- Questa è una base di partenza. Se vuoi che tutta la logica client (RAG, chiamate API) viva nell'estensione senza dipendere da un server, posso aiutarti a portarvi dentro i file JS/HTML e adattare le chiamate.

Vuoi che copi il frontend (`frontend/bocconi.html`, `frontend/chatbot.js`, `frontend/style.css`) dentro `extension/` così l'estensione è indipendente dal server? Oppure preferisci questa versione che apre la UI servita localmente?
