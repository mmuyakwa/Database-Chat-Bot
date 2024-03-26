#!/bin/bash
# Schritt 1: Erstelle eine Python Virtual Environment in einem Ordner namens '.venv'
python3.12 -m venv .venv  
# Schritt 2: Aktiviere die virtuelle Umgebung
source .venv/bin/activate  
# Schritt 3: Aktualisiere `pip` und installiere die Pakete `wheel` und `python-dotenv` mit der Option `--upgrade`
pip install --upgrade pip
pip install --upgrade wheel python-dotenv autopep8

# Wenn eine requirements.txt-Datei vorhanden ist, installiere die darin aufgelisteten Pakete
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

# Gib eine Nachricht aus, die darauf hinweist, dass das Skript abgeschlossen ist
echo "Entwicklungsumgebung wurde eingerichtet."
