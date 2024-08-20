#=======================================================
#	IMPORTS:
#=======================================================

import io
import random

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

ls_weekdays = list( dict_days.keys() )


csv_file_reader = csv.DictReader( open('dyspozycyjnosc.csv', 'r') )
csv_file_writer = open( 'grafik.csv', 'w', newline='' )




#=======================================================
#	FUNCTIONS:
#=======================================================

def generate_month_template( ls_weekdays : list, month : int, year : int ):

    dict_calendar = {}

    for weekday_name in ls_weekdays:
        weekday = list( calendar.day_name ).index( dict_days[ weekday_name ] )
        cal = calendar.monthcalendar( year, month )

        for week in cal:
            if ( week[ weekday ] != 0 ):
                day = week[ weekday ]
                dict_calendar[f"{ day }/{ month }/{ year }"] = weekday_name


    dict_calendar = dict( sorted( dict_calendar.items(), key=lambda x: tuple(map(int, x[0].split('/'))) ) )
    
    csv_file_writer.truncate()
    csv_file_writer.write( templates.header )

    for date, weekday_name in dict_calendar.items():
        print( f"{ date } - { weekday_name }" )

        if ( weekday_name == 'wtorek' ):
            csv_file_writer.write( f'wtorek { date }\n' + templates.day_wtorek )
        if ( weekday_name == 'czwartek' ):
            csv_file_writer.write( f'czwartek { date }\n' + templates.day_czwartek )
        if ( weekday_name == 'piątek' ):
            csv_file_writer.write( f'piątek { date }\n' + templates.day_piatek )
        if ( weekday_name == 'sobota' ):
            csv_file_writer.write( f'sobota { date }\n' + templates.day_sobota )

    return dict_calendar



def add_people( grafik, ls_dyspozycyjnosc : str ):

    return


def test_func():
    ls = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]

    ones_indices = random.sample( range( len(ls) ), 5 )

    for index in ones_indices:
        ls[ index ] = 1

    print( f'new ls:\n{ls}' )

    return


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

    template = generate_month_template( ls_weekdays, 8, 2024 )
    # print( template )

    test_func()