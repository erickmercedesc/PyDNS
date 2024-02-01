#!/bin/bash

# Comando a ejecutar
COMANDO="/usr/bin/python3 $(readlink -f "script.py") >> $(readlink -f "updates.log") 2>&1"
echo $COMANDO

# Agregar el cron job
(crontab -l 2>/dev/null; echo "*/10 * * * * $COMANDO") | crontab -

echo "Cron job añadido para ejecutar el script cada 10 minutos."