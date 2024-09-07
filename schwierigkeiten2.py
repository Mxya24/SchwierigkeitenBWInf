gesuchteBuchstaben = ["A", "C", "D", "F", "G"]
kombinationen = [["A", "B"],["A","C"],["A","D"],["B","C"],["B","D"],["C","D"],["A","E"],["A","C"],["E","C"],["C","F"],["F","D"],["E","G"],["E","F"],["G","F"]]
besucht = []
ziel = []
konflikt = []

#print (kombinationen)

def isNotwendig(added, buchstabe):
    for i in range (len(added)):
        if (added[i] == buchstabe):
            return True
        return False
        
def searchBuchstabe(array, buchstabe):
    for i in range (len(array)):
        if (array[i] == buchstabe):
            return i
            
buchstabe = gesuchteBuchstaben[0]      


while (gesuchteBuchstaben): #check ob das stimmt! whilemliste nicht leer

    adding = True
    
    for i in range (len(kombinationen)):
        if (kombinationen[i][1] == buchstabe and not isNotwendig(ziel ,kombinationen[i][0]) and not isNotwendig (besucht,kombinationen[i][0]) and isNotwendig(gesuchteBuchstaben, kombinationen[i][0])):
            besucht.append(buchstabe)
            buchstabe = kombinationen[i][0]
            print (buchstabe)
            adding = False
            break
        if (isNotwendig(besucht,kombinationen[i][0])):
            adding = True
            konflikt.append(buchstabe)
    
    if (adding == True):        
        ziel.append(buchstabe)
        popzahl = searchBuchstabe(gesuchteBuchstaben, buchstabe)
        gesuchteBuchstaben.pop(popzahl)
        
        if (besucht):
                buchstabe = besucht[-1]
        elif (gesuchteBuchstaben):
            buchstabe = gesuchteBuchstaben[0]
        
        besucht = []
    
 
    
print (ziel)
        