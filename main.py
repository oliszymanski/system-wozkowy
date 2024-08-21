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

ls_fieldnames = [ 'godzina dyżuru', 'głosiciel 1', 'głosiciel 2', 'zastępstwo 1', 'zastępstwo 2' ]

ls_weekdays = list( dict_days.keys() )

csv_grafik_reader = csv.DictReader( open('grafik.csv', 'r') )
csv_grafik_writer = csv.DictWriter( open('grafik.csv', 'r'), fieldnames=ls_fieldnames )
csv_dyspozycyjnosc_reader = csv.DictReader( open('dyspozycyjnosc.csv', 'r') )



#=======================================================
#	FUNCTIONS:
#=======================================================

def assign_people( grafik_read, grafik_write, dyspozycyjnosc, weekdays : list, view_result=False ):

    # if (_DBG0_):
    #     for row in dyspozycyjnosc:
    #         print( row, '\n' )



    if ( view_result ):
        for row in grafik_read:
            print( row )

    for row in grafik_read:
        if ( any( day in row[ 'godzina dyżuru' ] for day in weekdays ) ):
            print( f'row = { row }' )

    return None



# def get_person_availability( dyspozycyjnosc : csv.DictReader, display_result=True ):

#     """
#     """

#     person_availability = {}

#     for row in dyspozycyjnosc:
#         person_name = row['imię i nazwisko']
#         person_availability[ person_name ] = {}

#         for weekday_name in ls_weekdays:
#             person_availability[ person_name ][ weekday_name ] = {}


#     if ( display_result ): print( person_availability )

#     return person_availability



def generate_month_template( template_file: str, ls_weekdays : list, month : int, year : int, display_result=True ):

    dict_calendar = {}

    for weekday_name in ls_weekdays:
        weekday = list( calendar.day_name ).index( dict_days[ weekday_name ] )
        cal = calendar.monthcalendar( year, month )

        for week in cal:
            if ( week[ weekday ] != 0 ):
                day = week[ weekday ]
                dict_calendar[f"{ day }/{ month }/{ year }"] = weekday_name


    dict_calendar = dict( sorted( dict_calendar.items(), key=lambda x: tuple(map(int, x[0].split('/'))) ) ) # sorting by date
    
    csv_file_writer = open( template_file, 'w', newline='' )

    csv_file_writer.truncate()
    csv_file_writer.write( templates.header )

    for date, weekday_name in dict_calendar.items():
        if ( display_result ): print( f"{ date } - { weekday_name }" )

        if ( weekday_name == 'wtorek' ): csv_file_writer.write( f'wtorek { date }\n' + templates.day_wtorek )
        if ( weekday_name == 'czwartek' ): csv_file_writer.write( f'czwartek { date }\n' + templates.day_czwartek )
        if ( weekday_name == 'piątek' ): csv_file_writer.write( f'piątek { date }\n' + templates.day_piatek )
        if ( weekday_name == 'sobota' ): csv_file_writer.write( f'sobota { date }\n' + templates.day_sobota )


        if ( display_result ): print( dict_calendar )

    return dict_calendar



def test_func():
    ls = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]

    ones_indices = random.sample( range( len(ls) ), 5 )

    for index in ones_indices:
        ls[ index ] = 1

    print( f'new ls:\n{ls}' )

    return



#=======================================================
#	TESTING
#=======================================================

if ( __name__ == '__main__' ):
    template = generate_month_template( 'grafik.csv', ls_weekdays, month, year, display_result=False )

    assign_people( csv_grafik_reader, csv_grafik_writer, csv_dyspozycyjnosc_reader, ls_weekdays )

    # person_availability = get_person_availability( csv_dyspozycyjnosc_reader )

    # for row in csv_grafik_writer:
    #     print( row )

    # print( dir( csv.DictReader ) )



#=======================================================
#	END
#=======================================================