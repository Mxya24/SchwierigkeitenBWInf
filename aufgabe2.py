#Dateiname einlesen
inp = input('Gib den Dateinamen ein: ')

#Datei einlesen
try:
        with open(inp, 'r') as file:    
            num1, num2, num3 = map(int, file.readline().split()) #Anzahl Klausuren, insgesamte Anzahl an Aufgaben, Anzahl zu ordnender Aufgaben
            kombinationen1 = [] #leere Liste für Klausuren
            for i in range(num1):
                kombinationen1.append([x for x in file.readline().rstrip().split(" < ")]) #Buchstaben pro Klausur ohne'<'
            gesuchteBuchstaben = [x for x in file.readline().split()] #alle zu ordneneden aufgaben in Liste

#Fehleremeldung bei nicht vorhandener Datei   
except FileNotFoundError:
    print(f"File {inp} not found.")

kombinationen = [] #neue Liste für Ordnung der Schwierigkeit
lengths = [len(sublist) for sublist in kombinationen1] #Anzahl der Aufgaben jeder Klausur in Liste
for j in range(num1): #für jede Klausur
    for i in range(lengths[j]): 
        for k in range (i+1, lengths[j]): 
            kombinationen.append([kombinationen1[j][i], kombinationen1[j][k]]) #jew. vordere Aufagbe in extra sublist mit allen hinteren

#Variablen 
besucht = [] #besucht liste (Erweiterung)
ziel = [] #fertige Ordnung
konflikt = [] #alle Konflikte (Erweiterung)
buchstabe = gesuchteBuchstaben[0] #aktueller buchstabe erster in gesucht Liste

def isNotwendig(added, buchstabe): #gibt an, ob buchstabe in Liste ist
    for i in range (len(added)):
        if (added[i] == buchstabe): #falls buchstabe in Liste
            return True #Rueckgabe wahrheitswert
    return False
        
def searchBuchstabe(array, buchstabe): #sucht stelle an der buchstabe in Liste ist
    for i in range (len(array)):
        if (array[i] == buchstabe): #wenn stelle gefunden
            return i #gibt stelle als int zurueck

while (gesuchteBuchstaben): #solange es zu sortierende buchstaben gibt
    adding = True #adding zuruecksetzen pro Durchgang
    
    for i in range (len(kombinationen)): #durch alle vorgaben zu schwierigkeit durch

        #Wahrheitswerte fuer linken, d.h. nächstkleineren buchstben des aktuellen zur ueberpruefung in if Funktion
        ziel1 = isNotwendig(ziel ,kombinationen[i][0]) #True wenn buchstabe schon in Ziel
        gesucht1 = isNotwendig(gesuchteBuchstaben, kombinationen[i][0]) #true wenn ein gesuchter buchstabe
        besucht1 = isNotwendig(besucht, kombinationen[i][0]) #true wenn buchstabe schon in besucht => Konflikt (Erweiterung)
        
        if (kombinationen[i][1] == buchstabe and gesucht1 == True and ziel1 == False and besucht1 == False): #aktueller Buchstabe entspricht Stand in Liste
            besucht.append(buchstabe) #zu besucht hinzufuegen (Erweiterung)
            buchstabe = kombinationen[i][0] #neuer buchtabe, niedrigerer neben an
            adding = False #wird nicht hinzugefuegt
            break
        if (besucht1 == True and kombinationen[i][1] == buchstabe and gesucht1 == True and ziel1 == False): #falls Konflikt entsteht (Erweiterung)
            adding = True #wird hinzugefuegt
            buchstabe = kombinationen[i][0] #neuer buchstabe, naechst 'kleinere', d.h. Anfang der Schleife
            konflikt.append([buchstabe, kombinationen[i][1]]) #fuegt buchstabenset zu konflikt hinzu
            break      
    
    if (adding == True):  #hinzufuegen      
        ziel.append(buchstabe) #buchstabe hinzugefuegt
        popzahl = searchBuchstabe(gesuchteBuchstaben, buchstabe) #stelle an der hinzugefuegter buchstabe in gesucht steht
        gesuchteBuchstaben.pop(popzahl) #entfernt von gesucht

        #neuer buchstabe
        if (besucht1):
            buchstabe = besucht[-1] #wenn moeglich letzter davor besuchte buchstabe
        elif (gesuchteBuchstaben):
            buchstabe = gesuchteBuchstaben[0] #sonst erster buchstabe aus gesucht liste
        besucht = [] #reset besucht Liste
 
#Ausgabe
print ("Geordnete Reihenfolge der Buchstaben:",ziel[0], end= '')    
for i in range(1, len(ziel)):
    print("; ",ziel[i], end = '')
#falls Konflikt (Erweiterung)
print('')
if (konflikt):
    print ("Es gab Konflikte bei jeweils folgenden Buchstabenkombinationen:", konflikt[0][0], "und",konflikt[0][1], end = '')
    for i in range(1, len(konflikt)):
        print("; ",konflikt[i][0],"und",konflikt[i][1], end = '')