from models.publisher import Publisher
from models.schedule_entry import Schedule_entry
from datetime import datetime, time

if ( __name__ == '__main__' ):
    marian = Publisher("Marian")
    marian.add_availability(6, time(7,0))
    marian.add_availability(6, time(8,0))
    
    shift_time1=datetime(2024,9,1,7,0)
    shift_time2=datetime(2024,9,1,9,0)
    shift_time3=datetime(2024,9,2,7,0)
    
    print(marian.is_available(shift_time1))
    print(marian.is_available(shift_time2))
    print(marian.is_available(shift_time3))
