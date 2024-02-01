#!/bin/bash

# Ruta al script de Python
SCRIPT_PYTHON= $(readlink -f "script.py")
LOG_FILE=$(readlink -f "updates.log")

# Comando a ejecutar
COMANDO="/usr/bin/python3 $SCRIPT_PYTHON >> $LOG_FILE 2>&1"

# Agregar el cron job
(crontab -l 2>/dev/null; echo "*/10 * * * * $COMANDO") | crontab -

echo "Cron job añadido para ejecutar el script cada 10 minutos."