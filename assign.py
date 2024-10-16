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

_DBG0_ = False
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

    
    
    def generate_month_schedule( self, ls_weekdays : list, display_result=True ):

        """
        input:
            ls_weekdays:        list of weekdays;

        output:
            dict_calendar:      dictionary with dates and weekdays;
        """

        dict_calendar = {}

        year = self.year

        for weekday_name in ls_weekdays:
            weekday = list( calendar.day_name ).index( dict_days[ weekday_name ] )
            cal = calendar.monthcalendar( year, self.month )

            for week in cal:
                if ( week[ weekday ] != 0 ):
                    day = week[ weekday ]
                    dict_calendar[f"{ day }/{ self.month }/{ year }"] = weekday_name

        dict_calendar = dict( sorted( dict_calendar.items(), key=lambda x: tuple(map(int, x[0].split('/'))) ) ) # sorting by date
        
        with open( self.grafik, 'w', newline='' ) as csv_file_writer:
            line_number_counter = 1
            csv_file_writer.truncate()
            csv_file_writer.write( templates.header )

            for date, weekday_name in dict_calendar.items():
                if ( display_result ): print( f"{ date } - { weekday_name }" )

                if ( weekday_name == 'wtorek' ):
                    csv_file_writer.write( f'wtorek { date }\n' + templates.day_wtorek )
                    self.assign_people( self.grafik, 'wtorek', line_number_counter ) # not working
                    line_number_counter += len( templates.day_wtorek.splitlines() ) + 1

                if ( weekday_name == 'czwartek' ):
                    csv_file_writer.write( f'czwartek { date }\n' + templates.day_czwartek )
                    self.assign_people( self.grafik, 'czwartek', line_number_counter )
                    line_number_counter += len( templates.day_czwartek.splitlines() ) + 1
                
                if ( weekday_name == 'piątek' ):
                    csv_file_writer.write( f'piątek { date }\n' + templates.day_piatek )
                    self.assign_people( self.grafik, 'piątek', line_number_counter )
                    line_number_counter += len( templates.day_piatek.splitlines() ) + 1
                
                if ( weekday_name == 'sobota' ):
                    csv_file_writer.write( f'sobota { date }\n' + templates.day_sobota )
                    self.assign_people( self.grafik, 'sobota', line_number_counter )
                    line_number_counter += len( templates.day_sobota.splitlines() ) + 1

            if ( display_result ):
                print( f'{ dict_calendar }' )


            if ( display_result ): print( f'number of lines in file: { line_number_counter }')


            return dict_calendar



    def assign_people( self, filename: str, weekday: str, start_line: int ):
    
        '''
        input:
            weekday:        day of the week,
            start_line:     where to start typing in;

        output:

        '''

        print( 'assign_people function called' )
        print(f"Processing weekday: {weekday}, starting at line: {start_line}")

        with open( self.grafik, 'r' ) as grafik_file:
            reader = csv.reader( grafik_file )
            read_rows = list( reader )

        with open( self.dyspozycyjnosc, 'r' ) as dyspozycyjnosc_file:
            csv_dyspozycyjnosc = csv.DictReader( dyspozycyjnosc_file )


        if ( _DBG0_ ):
            ls_matching_disposal_rows = [ disposal_row for disposal_row in csv_dyspozycyjnosc if ( '7:30' in disposal_row[ weekday ] ) ]
            print( f'ls_matching_disposal_rows: { ls_matching_disposal_rows }' )


        if ( start_line < len( read_rows ) ): 
            print( 'assiging people' )
            for i in range( start_line, len( read_rows ) ):

                if ( len( read_rows[ i ] ) == 3 ):
                    print( f'row 0: { read_rows[ i ][ 0 ] }' )

                    with open( self.dyspozycyjnosc, 'r' ):
                        csv_dyspozycyjnosc = csv.DictReader( open( self.dyspozycyjnosc, 'r' ) )
                        ls_matching_disposal_rows = [ disposal_row for disposal_row in csv_dyspozycyjnosc if ( read_rows[i][0] in disposal_row[ weekday ] ) ]

                    if ( ls_matching_disposal_rows ):
                        st_assigned_people = set()

                        # first publisher
                        name_01 = choice( ls_matching_disposal_rows )[ 'imię i nazwisko' ]
                        read_rows[ i ][ 1 ] = name_01
                        st_assigned_people.add( name_01 )
                        if (_DBG1_): print( f'first publisher: { read_rows[ i ][ 1 ] }' )

                        available_names = [ row['imię i nazwisko'] for row in ls_matching_disposal_rows if ( row['imię i nazwisko'] not in st_assigned_people ) ]
                        
                        # second publisher
                        if ( available_names ):
                            name_02 = choice( available_names )
                            read_rows[ i ][ 2 ] = name_02
                            if (_DBG1_): print( f'second publisher: {read_rows[ i ][ 2 ]}' )

                            try:
                                with open( filename, 'w', newline='' ) as csv_file_writer:
                                    csv_writer = csv.writer( csv_file_writer )
                                    csv_writer.writerows( read_rows )

                            except Exception as e:
                                print(f'error writing to file: {e}')

                        else: print( 'No available names' )
                    
                    print( 'written data rows' )

        return None



    def assign_people_to_schedue( self, start_line : int ):
        
        with open( self.grafik, 'r' ) as grafik_file:
            reader = csv.reader( grafik_file )
            read_rows = list( reader )

        with open( self.dyspozycyjnosc, 'r' ) as dyspozycyjnosc_file:
            csv_dyspozycyjnosc = csv.DictReader( dyspozycyjnosc_file )


        if ( start_line < len( read_rows ) ): 
            for i in range( start_line, len( read_rows ) ):

                if ( (len( read_rows[ i ] ) == 1) and ( 'sobota' in read_rows[i][0] ) ):
                    print( f'row 0: { read_rows[ i ][ 0 ] }' )

        return