def lees_inhoud(bestands_naam):
    """Schrijf hier je eigen code die het fasta bestand inleest en deze 
    splitst in header en sequentie.
    Lever twee strings:
        - header = string, header van fasta
        - seq = string met daarin de sequentie behorend bij de header
    Hieronder vind je de return nodig om deze twee strings op te leveren
    """
    # Bonus: probeer zelf het bestand uit te lezen en de header en de sequentie eruit te halen. Gebruik daarvoor onderstaande code
    # bestand = open(bestands_naam)
    header = ">NM_001290071.1 Vicugna pacos transforming growth factor beta 1 (TGFB1), mRNA"
    seq = "GGGGGGGCGCCGCCTCCCCCATGCCGCCCTCCGGGCTGCGGCTGCTGCCACTGCTGCTGCCGCTGCTGTGGCTGCTAGTGCTGACGCCTGGTCGGCCGGCCGCCGGACTATCCACCTGCAAGACCATCGACATGGAGCTGGTGAAGCGGAAGCGCATCGAGGCCATCCGCGGCCAGATTCTGTCCAAGCTTCGGCTCGCCAGCCCCCCGAGTCAGGGGGAGGTGCCGCCCGGCCCGCTGCCGGAGGCCGTACTGGCCCTTTACAACAGTACCCGCGACCGGGTGGCCGGGGAAAGTGCCGAACCCGAGCCCGAGCCAGAGGCGGACTACTACGCCAAGGAGGTCACCCGCGTGCTGATGGTGGAAAACGGCGACAAAATCTATGATAAAATCAAGCGGAGCCCACACAGCATATACATGCTGTTTAACACATCGGAAGTCCGGGAGGCGGTACCCGAACCCGTGCTGCTCTCTCGGGCAGAGCTGCGCCTGCTGAGGCTCAAGTTAAAAGTGGAGCAGCACGTGGAGCTGTACCAGAAATATAGCAACGACTCCTGGCGCTACCTCAGCAACCGGCTGCTGGCCCCAAGCGACTCACCGGAGTGGCTGTCCTTTGATGTCACTGGAGTTGTGCGGCAGTGGCTGACCCACAGAGAGGAAATAGAGGGCTTTCGCCTCAGTGCCCACTGTTCCTGTGACAGCAAAGATAACACACTCCAAGTGGACATTAACGGGTTCAGTTCTGGCCGCCGAGGTGATCTTGCCACCATTCATGGCATGAACCGGCCCTTCCTGCTCCTCATGGCCACCCCGCTGGAGAGGGCCCAGCACCTGCACAGCTCCCGGCACCGCCGAGCCCTGGACACCAACTACTGCTTCAGCTCCACGGAGAAGAACTGCTGTGTGCGGCAGCTCTACATTGACTTCCGCAAGGACCTGGGCTGGAAGTGGATCCATGAGCCCAAGGGCTACCACGCCAATTTCTGCCTGGGGCCCTGCCCCTACATTTGGAGCCTGGACACGCAGTACAGCAAGGTCCTGGCGCTGTACAACCAGCACAACCCTGGCGCGTCGGCGGCGCCATGCTGCGTACCGCAGGCGCTGGAGCCGCTGCCCATCGTGTACTACGTGGGCCGCAAGCCCAAGGTGGAGCAGCTGTCCAACATGATCGTGCGCTCCTGCAAGTGCAGCTGAAGCCCCGCCTCGCCCACAGGCCCCGCCCCACACGCCCCGCCCACCCCGGCAGGCCCGGCCCCACCCCCGACCGCCTCACTGGGACTGTATTTAAGGACACCGCGGCCAAAGCCCACCTGGGGTCCATTAAAGGTGGAGAGAGGAGAGAAAAAAAAAAAAAAAAAAAAAA"

    with open('lamaseq.txt') as f:
        bestands_naam = f.read()
        



        #print(bestands_naam.split('<'))
        


   # print(bestands_naam)

    
def is_dna(seq):
    """Deze functie bepaalt of de sequentie
    DNA is.
    Indien ja, return True
    Zo niet, return False
    """
    
lengte = len(seq)

count_1 = seq.count('A')
print('The count of element: A is ', count_1)
count_2 = seq.count('T')
print('The count of element: T is', count_2)
count_3 = seq.count('G')
print('The count of element: G is', count_3)
count_4 = seq.count('C')
print('The count of element: C is', count_4)

aantal = (count_1 + count_2 + count_3 + count_4)


if aantal/lengte == 1:
   print('True')
else:
    print('False')

def knipt(seq):
    """Bij deze functie kan je een deel van de code die je de afgelopen 
    2 afvinkopdrachten geschreven hebt herbruiken
    Deze functie bepaald of een restrictie enzym in de sequentie 
    (een element uit seqs) knipt.
    Hiervoor mag je kiezen wat je returnt, of wellicht wil je 
    alleen maar printjes maken.
    """

def main():
    # Voer hier de bestandsnaam van het juiste bestand in, of hernoem 
    # je bestand
    bestand = "lamaseq.txt" 
    # Hier onder vind je de aanroep van de lees_inhoud functie, 
    # die gebruikt maakt van de bestand variabele als argument. 
    # De resultaten van de functie, de string met header en de string 
    # met sequentie, sla je op deze manier op in twee losse resultaten.
    headers, seqs = lees_inhoud(bestand)


   # print('Wat is dit gezeik: ',lees_inhoud(bestands_naam))
    
      

    # schrijf hier de rest van de code nodig om de aanroepen te doen
    
main()
