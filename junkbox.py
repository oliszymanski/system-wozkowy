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
