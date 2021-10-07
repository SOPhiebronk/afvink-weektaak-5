def average(score1,score2,score3,score4,score5):
    ''' Gaat het gemiddelde berekenen van de score

 input:int
 output:int

'''
    calc_average = (score1 + score2 + score3 + score4 + score5)/5

    return 'Dit is de gemiddelde score:  ',calc_average


def grade(score):
    ''' Gaat het cijfer bepalen
input:
output:
'''
    if score <= 100 and score >= 90:
        print('A')
    




def main():
     score_1 = int(input('Enter a test score '))
     score_2 = int(input('Enter a test score '))
     score_3 = int(input('Enter a test score '))
     score_4 = int(input('Enter a test score '))
     score_5 = int(input('Enter a test score '))
     print(average(score_1,score_2,score_3,score_4,score_5))
     print(grade(score_1)

