#=======================================================
#	IMPORTS:
#=======================================================

import assign



#=======================================================
#	CONSTANTS:
#=======================================================

month = 9
year = 2024

ls_weekdays = [ 'wtorek', 'czwartek', 'piątek', 'sobota' ]


#=======================================================
#	TESTING:
#=======================================================

if ( __name__ == '__main__' ):
    assign_pub = assign.AssignPublishers( 'grafik.csv', 'dyspozycyjnosc.csv', month, year )
    assign_pub.generate_month_template( ls_weekdays )
    assign_pub.assign_people( 'sobota', 202 )
