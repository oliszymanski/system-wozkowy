#=======================================================
#	IMPORTS:
#=======================================================

import csv
import calendar
import templates



#=======================================================
#	GLOBALS:
#=======================================================

_DBG0_ = True                               # debuggers

month = 7                                   # calendar setup
year = 2024

dict_days = {
    'wtorek':'Tuesday',
    'czwartek':'Thursday',
    'piątek':'Friday',
    'sobota':'Saturday'
}


csv_output = open( 'grafik.csv', 'w' )      # csv

csv_file_reader = csv.DictReader( open('dyspozycyjnosc.csv', 'r') )
csv_file_writer = csv_output





#=======================================================
#	FUNCTIONS:
#=======================================================

def generate_monthly_template( month, year ):

    dict_calendar = {}

    ls_weekdays = [ 'wtorek', 'czwartek', 'piątek', 'sobota' ]
    
    for weekday_name in ls_weekdays:
        weekday = list( calendar.day_name ).index( dict_days[ weekday_name ] )
        cal = calendar.monthcalendar( year, month )

        for week in cal:
            if ( week[ weekday ] != 0 ):
                day = week[ weekday ]
                dict_calendar[f"{ day }/{ month }/{ year }"] = weekday_name


    dict_calendar = dict( sorted( dict_calendar.items(), key=lambda x: tuple(map(int, x[0].split('/'))) ) )
    
    for date, weekday_name in dict_calendar.items():
        print(f"{date} - {weekday_name}")

        


    # if ( _DBG0_ ): print( dict_calendar )

    return dict_calendar



def wpisz_wt( month, year, weekday_name='wtorek' ):
    
    weekday = list( calendar.day_name ).index( dict_days[ weekday_name ] )
    cal = calendar.monthcalendar( year, month )

    for week in cal:
        if ( week[ weekday ] != 0 ):
            day = week[ weekday ]
            date_string = f"{ month }/{ day }/{ year }"
            print( f"{ date_string } - { weekday_name }" )
    
    for row in csv_file_reader:
        print( row[ 'wtorek' ] )

    return



def wpisz_czw( month, year, weekday_name='czwartek' ):
    weekday = list( calendar.day_name ).index( dict_days[ weekday_name ] )
    cal = calendar.monthcalendar( year, month )

    for week in cal:
        if ( week[ weekday ] != 0 ):
            day = week[ weekday ]
            date_string = f"{ month }/{ day }/{ year }"
            print( f"{ date_string } - { weekday_name }" )

    for row in csv_file_reader:
        print( row[ 'czwartek' ] )

    return



def wpisz_pt( month, year, weekday_name='piątek' ):

    weekday = list( calendar.day_name ).index( dict_days[ weekday_name ] )
    cal = calendar.monthcalendar( year, month )

    for week in cal:
        if ( week[ weekday ] != 0 ):
            day = week[ weekday ]
            date_string = f"{ month }/{ day }/{ year }"
            print( f"{ date_string } - { weekday_name }" )


    for row in csv_file_reader:
        print( row[ 'piątek' ] )

    return



def wpisz_sob( month, year, weekday_name='sobota' ):
    
    weekday = list( calendar.day_name ).index( dict_days[ weekday_name ] )
    cal = calendar.monthcalendar( year, month )

    for week in cal:
        if ( week[ weekday ] != 0 ):
            day = week[ weekday ]
            date_string = f"{ month }/{ day }/{ year }"
            print( f"{ date_string } - { weekday_name }" )

    for row in csv_file_reader:
        print( row[ 'sobota' ] )

    return



#=======================================================
#	TESTING
#=======================================================

if ( __name__ == '__main__' ):
    # wpisz_wt( month, year )
    # wpisz_czw( month, year )
    # wpisz_pt( month, year )
    # wpisz_sob( month, year )

    template = generate_monthly_template( month, year )
    print( template )