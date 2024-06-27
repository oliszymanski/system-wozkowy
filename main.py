#=======================================================
#	IMPORTS:
#=======================================================

import csv



#=======================================================
#	GLOBALS:
#=======================================================

csv_file_reader = csv.DictReader( open('dyspozycyjnosc.csv', 'r') )
csv_file_writer = csv.DictWriter( open('grafik.csv', 'w') )



#=======================================================
#	FUNCTIONS:
#=======================================================

def wpisz_wt():
    for row in csv_file_reader:
        print( row[ 'wtorek' ] )

    return



def wpisz_czw():
    for row in csv_file_reader:
        print( row[ 'czwartek' ] )

    return



def wpisz_pt():
    for row in csv_file_reader:
        print( row[ 'piatek' ] )

    return



def wpisz_sob():
    for row in csv_file_reader:
        print( row[ 'sobota' ] )

    return


#=======================================================
#	TESTING
#=======================================================

if ( __name__ == '__main__' ):
    wpisz_wt()