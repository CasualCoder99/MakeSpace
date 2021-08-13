from MakeSpace.Bookings.bookings import Booking
from MakeSpace.Rooms.rooms import Room, CCave, DTower, GMansion
from datetime import datetime
from MakeSpace.BookingTime.bookingtime import BookingTime
import unittest


class BookingTimeTest(unittest.TestCase):
    booking_time = BookingTime("16:00","18:00")
    start_time_object = datetime.strptime("16:00","%H:%M")
    end_time_object = datetime.strptime("18:00","%H:%M")
    bookings = []
    room = GMansion()
  
    # Returns True if the start and end time objects returned are correct.
    def test_get_time_object(self):
        print("\nStart get_time_object test\n")
        self.assertEqual(vars(self.start_time_object), vars(datetime.strptime("16:00","%H:%M")))
        self.assertEqual(vars(self.end_time_object), vars(datetime.strptime("18:00","%H:%M")))
    
    # Returns True if the booking added is correct.
    def test_add_booking(self):
        booking_time = BookingTime("15:00","16:30")
        capacity = 7
        booking = Booking(booking_time, capacity)
        self.bookings.append(booking)
        self.room.add_booking(booking)
        self.assertEqual(vars(self.room.get_bookings[-1]), vars(self.bookings[-1]))

if __name__ == '__main__':
    unittest.main()