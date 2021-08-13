from MakeSpace.BookingTime.bookingtime import BookingTime
from MakeSpace.Bookings.bookings import Booking
import sys
from MakeSpace.Rooms.rooms import  CCave, DTower, GMansion

def book_room(booking):
    if(room1.can_be_booked(booking)):
        room1.add_booking(booking)
    elif(room2.can_be_booked(booking)):
        room2.add_booking(booking)
    elif(room3.can_be_booked(booking)):
        room3.add_booking(booking)
    else:
        print("NO_VACANT_ROOM")

def find_vacancy(booking_time):
    noVacancy = True
    if(room1.is_room_available(booking_time)):
        print("C-Cave",end=' ')
        noVacancy = False
    if(room2.is_room_available(booking_time)):
        print("D-Tower",end=' ')
        noVacancy = False
    if(room3.is_room_available(booking_time)):
        print("G-Mansion",end=' ')
        noVacancy = False
    if(not noVacancy):
        print()
    else:
        print("NO_VACANT_ROOM")

room1 = CCave()
room2 = DTower()
room3 = GMansion()

def main():
    input_file = sys.argv[1]
    # parse the file and process the command
    # print the output
    file = open(input_file,'r')
    lines = file.readlines()
    query_map = {'VACANCY': find_vacancy,'BOOK': book_room,}
    for line in lines:
        inputs = line.split()
        query = inputs[0]
        booking_time = BookingTime(inputs[1],inputs[2])
        if(not booking_time.is_valid_time_object()):
            print("INCORRECT_INPUT")
        elif(booking_time.meeting_during_buffer()):
            print("NO_VACANT_ROOM")
        elif(query == 'VACANCY'):
            query_map['VACANCY'](booking_time)
        elif(query == "BOOK"):
            booking = Booking(booking_time, inputs[3])
            query_map['BOOK'](booking)
        else:
            print("INCORRECT_INPUT")
            

if __name__ == "__main__":
    main()