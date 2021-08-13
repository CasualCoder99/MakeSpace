from MakeSpace.Bookings.bookings import Booking
from MakeSpace.BookingTime.bookingtime import BookingTime
from datetime import datetime

class Room:


    def __init__(self) -> None:
        self._capacity = 0 #total capacity of a room
        self._bookings = [] #all bookings made for a room
        self.name = "Room"
        
    
    def is_room_available(self,booking_time) -> bool:
        start_time_object, end_time_object = BookingTime.get_time_object(booking_time)
        for booking in self._bookings:
            booking_time_object = Booking.get_booking_time(booking)
            booking_start, booking_end = BookingTime.get_time_object(booking_time_object)
            if((start_time_object >= booking_start and end_time_object < booking_end)): # if booking time in between previous booking
                return False
            elif((start_time_object <= booking_start and end_time_object > booking_start)): # if booking overlaps with another
                return False
            elif((start_time_object < booking_end and end_time_object >= booking_end)):  # if booking overlaps with another
                return False
        return True

    def add_booking(self, booking) -> None:
        self._bookings.append(booking)
        print(self.name)
    
    def is_capacity_available(self, booking) -> bool:
        if(Booking.get_ordered_capacity(booking) <= self._capacity):
            return True
        else:
            return False
    
    def can_be_booked(self, booking):
        return self.is_capacity_available(booking) and self.is_room_available(Booking.get_booking_time(booking))
    
    def get_bookings(self):
        return self._bookings
        

class CCave(Room):
    
    def __init__(self) -> None:
        super(CCave,self).__init__()
        self._capacity = 3
        self.name = "C-Cave"

class DTower(Room):

    def __init__(self) -> None:
        super(DTower,self).__init__()
        self._capacity = 7
        self.name = "D-Tower"

class GMansion(Room):

    def __init__(self) -> None:
        super(GMansion,self).__init__()
        self._capacity = 20
        self.name = "G-Mansion"


