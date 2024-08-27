#=======================================================
#	IMPORTS:
#=======================================================

import io
from random import choice

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

ls_fieldnames = [ 'godzina dyżuru', 'głosiciel 1', 'głosiciel 2' ]

ls_weekdays = list( dict_days.keys() )

csv_grafik_reader = csv.DictReader( open('grafik.csv', 'r') )
csv_grafik_writer = csv.DictWriter( open('grafik.csv', 'r'), fieldnames=ls_fieldnames )
csv_dyspozycyjnosc_reader = csv.DictReader( open('dyspozycyjnosc.csv', 'r') )



#=======================================================
#	FUNCTIONS:
#=======================================================

def assign_people( grafik_read, grafik_write, dyspozycyjnosc, weekdays : list, view_result=False ):

    if ( view_result ):
        for row in grafik_read:
            print( row )

    for row in grafik_read:
        if ( any( day in row[ 'godzina dyżuru' ] for day in weekdays ) ):
            print( f'row = { row }' )



    return None



def assign_people_01( weekday : str, dyspozycyjnosc, view_result=True ):
    """
    input:
        weekday:            day of the week,
        dyspozycyjnosc:     list of people and their availability;

    output:
        

    """
    
    csv_col_vals = []
    dict_filtered_csv_col_vals = {}

    csv_reader = csv.DictReader( open( dyspozycyjnosc, 'r' ) )

    for row in csv_reader:
        csv_col_vals.append( row[ weekday ] )
    
    filtered_csv_col_vals = [  ]

    if ( view_result ): print( csv_col_vals )

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

    """
    input:
        template_file:      .csv file for schedule,
        ls_weekdays:        list of weekdays with templates,
        month:              month number,
        year:               year number;

    output:
        dict_calendar:      dictionary with dates and weekdays;
    """

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

    line_number_counter = 1

    csv_file_writer.truncate()
    csv_file_writer.write( templates.header )

    for date, weekday_name in dict_calendar.items():
        if ( display_result ): print( f"{ date } - { weekday_name }" )


        if ( weekday_name == 'wtorek' ):
            csv_file_writer.write( f'wtorek { date }\n' + templates.day_wtorek )
            line_number_counter += len( templates.day_wtorek.splitlines() ) + 1

        if ( weekday_name == 'czwartek' ):
            csv_file_writer.write( f'czwartek { date }\n' + templates.day_czwartek )
            line_number_counter += len( templates.day_czwartek.splitlines() ) + 1
        
        if ( weekday_name == 'piątek' ):
            csv_file_writer.write( f'piątek { date }\n' + templates.day_piatek )
            line_number_counter += len( templates.day_piatek.splitlines() ) + 1
        
        if ( weekday_name == 'sobota' ):
            csv_file_writer.write( f'sobota { date }\n' + templates.day_sobota )
            line_number_counter += len( templates.day_sobota.splitlines() ) + 1

        if ( display_result ):
            print( f'{dict_calendar}' )


    if ( display_result ): print(f'number of lines in file: { line_number_counter }')


    return dict_calendar



def test_func( weekday: str, start_line: int, reader_file: str, dyspozycyjnosc: csv.DictReader ):
    """
    """
    
    reader = csv.reader( open( reader_file, 'r', newline='' ) )
    rows = list( reader )

    if ( start_line < len( rows ) ):
        for i in range( start_line, len( rows ) ):
            if ( len(rows[ i ]) >= 2 ):
                if ( rows[i][1] == '-' ):       # check for głosiciel 1
                    print( rows[i][0] )
                
                if ( rows[i][2] == '-' ):       # check for głosiciel 2
                    print( rows[i][0] )

    return



#=======================================================
#	TESTING:
#=======================================================

if ( __name__ == '__main__' ):
    template = generate_month_template( 'grafik.csv', ls_weekdays, month, year, display_result=True )

    test_func( weekday='sobota', start_line=202, reader_file='grafik.csv', dyspozycyjnosc=csv_dyspozycyjnosc_reader )

    # assign_people_01( 'wtorek', 'dyspozycyjnosc.csv' )

    # person_availability = get_person_availability( csv_dyspozycyjnosc_reader )

    # for row in csv_grafik_writer:
    #     print( row )

    # print( dir( csv.DictReader ) )



#=======================================================
#	END
#=======================================================