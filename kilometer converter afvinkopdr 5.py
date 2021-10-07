

def kilometer_converter(blaat):
    ''' Voer een afstand in kilometer in en reken dat om naar Miles

input: int
output: string

'''   

    miles = blaat*0.6214

    return 'Dit is de afstand in miles:  ', miles
             
def main():
    kilometer = int(input('Wat is de afstand in kilometers?  '))
    print(kilometer_converter(kilometer))
     

main()



    
