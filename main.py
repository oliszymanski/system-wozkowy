#=======================================================
#	IMPORTS:
#=======================================================

import assign



#=======================================================
#	CONSTANTS:
#=======================================================

month = 11
year = 2024

ls_weekdays = [ 'wtorek', 'czwartek', 'piątek', 'sobota' ]



#=======================================================
#	TESTING:
#=======================================================

if ( __name__ == '__main__' ):
    assign_pub = assign.AssignPublishers( 'grafik.csv', 'dyspozycyjnosc.csv', month, year )
    # assign_pub.generate_month_schedule( ls_weekdays )
    
    # assign_pub.assign_people( 'grafik.csv', 'sobota', 220 ) # working

    assign_pub.assign_people_to_schedue( start_line=1 )