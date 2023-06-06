'''--------------------------------------------------------------------------'''

'''BACKUP: La funció 'backup_files' rep la ruta del directori origen i la del destí.'''

import shutil
import os
import datetime

def backup_files(source_dir, backup_dir):
    # Crear un directori de còpia de seguretat amb la data i l'hora actuals
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_path = os.path.join(backup_dir, f"copia_{current_time}")
    os.makedirs(backup_path)

    # Copiar tots els fitxers del directori origen al directori de còpia de destí
    for file_name in os.listdir(source_dir):
        source_file = os.path.join(source_dir, file_name)
        if os.path.isfile(source_file):
            shutil.copy2(source_file, backup_path)
            print(f"El fitxer {file_name} s'ha copiat de seguretat amb èxit.")

    # Còpia de seguretat OK
    print("Còpia de seguretat OK del directori origen " + source_directory + " al directori destí " + backup_directory)

# Directoris origen i destí
source_directory = "/temp"
backup_directory = "/temp/copia_de_seguretat"

backup_files(source_directory, backup_directory)


'''--------------------------------------------------------------------------'''

'''DOMINI: Amb el mòdul 'whois' podem obtenir informació detallada del domini.'''

import whois

def get_domain_info(domain_name):
    try:
        domain = whois.whois(domain_name)
        # Dades del domini
        print("Informació del domini:")
        print(f"Nom del domini: {domain.domain_name}")
        print(f"Registrador: {domain.registrar}")
        print(f"Data de creació: {domain.creation_date}")
        print(f"Data d'expiració: {domain.expiration_date}")
        

    except Exception as e:
        print(f"No s'ha pogut obtenir informació del domini: {e}")

# Demanem domini
domain_name = input("Introdueix el nom de domini: ")
get_domain_info(domain_name)

'''--------------------------------------------------------------------------'''

''' BASE DE DADES: Es crea una connexió amb la base de dades, es crea una taula, s'inserten dades, es realitza una consulta i s'actualitza una entrada. Finalment, es tanca la connexió. '''

import sqlite3

# Obrim connexió 
conn = sqlite3.connect('exemple.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE clients
                  (id INTEGER PRIMARY KEY, nom TEXT, email TEXT)''')

# Insert
cursor.execute("INSERT INTO clients (nom, email) VALUES (?, ?)", ('Marc', 'marc@example.com'))


conn.commit()

# Consulta de dades
cursor.execute("SELECT * FROM clients")
rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Nom: {row[1]}, Email: {row[2]}")

# Update
cursor.execute("UPDATE clients SET email = ? WHERE nom = ?", ('marcnoumail@example.com', 'Marc'))
conn.commit()

# Tancament de la connexió
conn.close()


'''--------------------------------------------------------------------------'''

'''MONITORITZACIÓ: Amb la llibreria 'psutil' podem obtenir informació de CPU, memòria i espai al disc. Com un agent de Nagios. I amb 'platform' tenim accés a informació del sistema operatiu.'''

import psutil
import platform

def monitoritza_equip():
    # Variables conversió
    conversio_a_megabytes = (1024 * 1024)
    conversio_a_gigabytes = (1024 * 1024 * 1024)
    
    # CPU
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"Ús de la CPU: {cpu_percent}%")

    # Memòria
    mem = psutil.virtual_memory()
    mem_percent = mem.percent
    mem_total = mem.total // conversio_a_megabytes
    mem_usada = mem.used  // conversio_a_megabytes
    print(f"Ús de memòria: {mem_usada} MB / {mem_total} MB ({mem_percent}%)")

    # Espai al disc
    disc = psutil.disk_usage("/")
    disc_percent = disc.percent
    disc_total = disc.total // conversio_a_gigabytes
    disc_usat = disc.used  // conversio_a_gigabytes
    print(f"Espai en disc: {disc_usat} GB / {disc_total} GB ({disc_percent}%)")
  
# Funció informació recursos equip
monitoritza_equip()

print("/n")

# Informació sistema operatiu
sistema_operatiu = platform.system()
print("Sistema operatiu:", sistema_operatiu)
versio_sistema_operatiu = platform.release()
print("Versió del sistema operatiu:", versio_sistema_operatiu)
informacio_detallada = platform.uname()
print("Informació detallada:", informacio_detallada)

'''--------------------------------------------------------------------------'''