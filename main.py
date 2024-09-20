#=======================================================
#	IMPORTS:
#=======================================================

import assign



#=======================================================
#	GLOBALS:
#=======================================================

_DBG0_ = False                               # debuggers
_DBG1_ = True

month = 9                                   # calendar setup
year = 2024

dict_days = {
    'wtorek':'Tuesday',
    'czwartek':'Thursday',
    'piątek':'Friday',
    'sobota':'Saturday'
}

ls_fieldnames = [ 'godzina dyżuru', 'głosiciel 1', 'głosiciel 2' ]

ls_weekdays = list( dict_days.keys() )

csv_grafik_reader = csv.DictReader( open('grafik.csv', 'r') )
csv_grafik_writer = csv.DictWriter( open('grafik.csv', 'r'), fieldnames=ls_fieldnames )
csv_dyspozycyjnosc_reader = csv.DictReader( open('dyspozycyjnosc.csv', 'r') )



#=======================================================
#	FUNCTIONS:
#=======================================================




#=======================================================
#	TESTING:
#=======================================================

if ( __name__ == '__main__' ):
    assign_people( 'sobota', 202, 'grafik.csv', 'dyspozycyjnosc.csv' )



#=======================================================
#	END
#=======================================================