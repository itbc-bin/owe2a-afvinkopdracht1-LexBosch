from tkinter.filedialog import askopenfilename
# Naam:
# Datum:
# Versie:1.008

# Voel je vrij om de variabelen/functies andere namen te geven als je die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.

def main():
    try:
        bestand = input("Welke wil je laden? Goed, Slecht of GeenFasta?") # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
        """
        Hier onder vind je de aanroep van de lees_inhoud functie, die gebruikt maakt van de bestand variabele als argument.
        De resultaten van de functie, de lijst met headers en de lijst met sequenties, sla je op deze manier op in twee losse resultaten.
        """
        headers, seqs = lees_inhoud(bestand)            
        zoekwoord = input("Geef een zoekwoord op: ")
        InHeaders, NewSeqs = InSeq(headers, zoekwoord, seqs)
        knipt(NewSeqs, InHeaders, headers)
   # except TypeError:
    #    print("Dat is geen DNA sequensie")
    except FileNotFoundError:
        print("Vul een valide bestand in, 'Goed', 'Slecht' of 'GeenFasta'\nOf zet de goede bestanden in de map")
        main()
    except AssertionError:
        print("Dat is geen FASTA bestand")
    except KeyboardInterrupt:
        print("Je hebt het afgesloten!")
    except LookupError:
        print("Dit zoek woord is niet gevonden")
        main()

    # schrijf hier de rest van de code nodig om de aanroepen te doen
    
    
def lees_inhoud(bestands_naam):
    bestand = open(bestands_naam).readlines()
    if bestand[0][0] != ">":
        raise AssertionError
    headers = []
    seqs = []
    Seq = ''
    for i in range(0,len(bestand)):
        if bestand[i][0] == '>':
            if i == 0:
                headers.append(bestand[i].replace('\n',''))
            else:
                seqs.append(Seq)
                headers.append(bestand[i].replace('\n',''))
                Seq = ''
        else: 
            Seq = Seq + bestand[i].replace('\n','')
    seqs.append(Seq)
    return headers, seqs




def InSeq(header, woord, Seqs):

    Heads = []
    NewSeqs = []
    for i in range(0, len(header)):
        if woord in header[i]:
            Heads.append(header[i])
            NewSeqs.append(Seqs[i])
    if not Heads:
        raise LookupError
    return(Heads, NewSeqs)
    




def is_dna(seq):
    A = seq.count('A')
    C = seq.count('C')
    T = seq.count('T')
    G = seq.count('G')
    tot = A + C + G + T
    if len(seq) == tot:
        Gelijk = True
    else:
        Gelijk = False
    return Gelijk
    

def knipt(Seq, Headers, headers):
    enzymen = open('enzymen.txt', 'r').readlines()
    for i in range(0, len((Seq))):
        try:
            if not is_dna(Seq[i]):
                raise TypeError
            print("-"*40)
            for x in range(0,16):
                Enzym = enzymen[x].split()[1].replace('^','')
                test = Seq[i].find(Enzym)
                if test != -1: print(enzymen[x].split()[0],'zit in',headers[i],'\nHij zit er in', test)
                
                print(Seq[i][test-10:test+10+len(Enzym)].replace(Enzym,'|'+Enzym+'|'))
        except TypeError:
            print(headers[i]," is geen dna sequentie")
            
        
main()
