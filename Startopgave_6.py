from tkinter.filedialog import askopenfilename
# Naam:
# Datum:
# Versie:

# Voel je vrij om de variabelen/functies andere namen te geven als je die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.

def main():
    try:
        bestand = input("Welke wil je laden? Goed of Slecht?") # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
        """
        Hier onder vind je de aanroep van de lees_inhoud functie, die gebruikt maakt van de bestand variabele als argument.
        De resultaten van de functie, de lijst met headers en de lijst met sequenties, sla je op deze manier op in twee losse resultaten.
        """
        headers, seqs = lees_inhoud(bestand)
        Gelijk = is_dna(seqs)
            
        zoekwoord = input("Geef een zoekwoord op: ")
        InHeaders = InSeq(headers, zoekwoord)
        knipt(seqs, InHeaders, headers)
    except TypeError:
        print("Dat is geen DNA sequensie")
    except FileNotFoundError:
        print("Vul een valide bestand in, 'Goed' of 'Slecht'\nOf zet de goede bestanden in de map")
        main()

    # schrijf hier de rest van de code nodig om de aanroepen te doen
    
    
def lees_inhoud(bestands_naam):
    bestand = open(bestands_naam).readlines()
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
            i += 1
    return headers, seqs



def InSeq(header, woord):
    Heads = []
    for i in range(0, len(header)):
        if woord in header[i]:
            Heads.append(i)
    return(Heads)
    




def is_dna(seqs):
    seq=''.join(seqs)
    A = seq.count('A')
    C = seq.count('C')
    T = seq.count('T')
    G = seq.count('G')
    tot = A + C + G + T
    if len(seq) == tot:
        Gelijk = True
    else:
        raise TypeError
    return Gelijk
    

def knipt(Seq, Headers, headers):
    enzymen = open('enzymen.txt', 'r').readlines()
    for i in range(0, len((Seq))):
        for x in range(0,16):
            Enzym = enzymen[x].split()[1].replace('^','')
            test = Seq[i].find(Enzym)
            if test != -1: print(enzymen[x].split()[0],'zit in',headers[i],'\nHij zit er in', test,'\n',Seq[i][test-10:test+10+len(Enzym)].replace(Enzym,'|'+Enzym+'|'))

        
main()
