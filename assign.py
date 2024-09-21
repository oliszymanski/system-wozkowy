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

month = 9                                   
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
#	CLASSES:
#=======================================================

class AssignPublishers():

    def __init__(self, grafik: str, dyspozycyjnosc: str, month: int, year: int ):

        self.grafik = grafik
        self.dyspozycyjnosc = dyspozycyjnosc

        self.month = month
        self.year = year

        return None

    
    
    def generate_month_template( self, ls_weekdays : list, display_result=True ):

        """
        input:
            ls_weekdays:        list of weekdays with templates;

        output:
            dict_calendar:      dictionary with dates and weekdays;
        """

        dict_calendar = {}

        for weekday_name in ls_weekdays:
            weekday = list( calendar.day_name ).index( dict_days[ weekday_name ] )
            cal = calendar.monthcalendar( year, self.month )

            for week in cal:
                if ( week[ weekday ] != 0 ):
                    day = week[ weekday ]
                    dict_calendar[f"{ day }/{ self.month }/{ year }"] = weekday_name


        dict_calendar = dict( sorted( dict_calendar.items(), key=lambda x: tuple(map(int, x[0].split('/'))) ) ) # sorting by date
        csv_file_writer = open( self.grafik, 'w', newline='' )

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
                self.assign_people( 'piątek', line_number_counter )
                line_number_counter += len( templates.day_piatek.splitlines() ) + 1
            
            if ( weekday_name == 'sobota' ):
                csv_file_writer.write( f'sobota { date }\n' + templates.day_sobota )
                line_number_counter += len( templates.day_sobota.splitlines() ) + 1

        if ( display_result ):
            print( f'{ dict_calendar }' )


        if ( display_result ): print( f'number of lines in file: { line_number_counter }')


        return dict_calendar



    def assign_people( self, weekday: str, start_line: int ):
    
        '''
        input:
            weekday:        day of the week,
            start_line:     where to start typing in;

        output:

        '''


        reader = csv.reader( open( self.grafik, 'r' ) )
        csv_dyspozycyjnosc = csv.DictReader( open( self.dyspozycyjnosc, 'r' ) )

        rows = list( reader )


        if ( _DBG0_ ):
            ls_matching_disposal_rows = [ disposal_row for disposal_row in csv_dyspozycyjnosc if ( '7:30' in disposal_row[ weekday ] ) ]
            print( f'ls_matching_disposal_rows: { ls_matching_disposal_rows }' )


        if ( start_line < len( rows ) ): 
            for i in range( start_line, len( rows ) ):

                if ( len( rows[ i ] ) == 3 ):
                    print( f'row 0: { rows[ i ][ 0 ] }' )

                    csv_dyspozycyjnosc = csv.DictReader( open( self.dyspozycyjnosc, 'r' ) )
                    ls_matching_disposal_rows = [ disposal_row for disposal_row in csv_dyspozycyjnosc if ( rows[i][0] in disposal_row[ weekday ] ) ]

                    if (ls_matching_disposal_rows):
                        st_assigned_people = set()

                        # first publisher
                        name_01 = choice( ls_matching_disposal_rows )[ 'imię i nazwisko' ]
                        rows[ i ][ 1 ] = name_01
                        st_assigned_people.add( name_01 )
                        print( f'publisher 1: { rows[ i ][ 1 ] }' )

                        available_names = [ row['imię i nazwisko'] for row in ls_matching_disposal_rows if ( row['imię i nazwisko'] not in st_assigned_people ) ]
                        
                        # second publisher
                        if ( available_names ):
                            name_02 = choice( available_names )
                            rows[ i ][ 2 ] = name_02
                            print( f'publisher 2: {rows[ i ][ 2 ]}' )

                        else: print( 'No available names' )


        return None



#=======================================================
#	TESTING:
#=======================================================

if ( __name__ == '__main__' ):
    assigning = AssignPublishers( 'grafik.csv', 'dyspozycyjnosc.csv', month, year )
    
    assigning.generate_month_template( ls_weekdays )
    assigning.assign_people( 'sobota', 202  )
