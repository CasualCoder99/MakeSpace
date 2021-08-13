from MakeSpace.Bookings.bookings import Booking
from MakeSpace.BookingTime.bookingtime import BookingTime
import unittest, sys, os

class TestBooking(unittest.TestCase):
      
    booking_time = BookingTime("10:00","12:00")
    ordered_capacity = 10
    booking = Booking(booking_time, ordered_capacity)
  
    # Returns True if the booking capacity returned is correct.
    def test_get_order_capacity(self):
        print("\nStart get_order_capacity test\n")
        self.assertEqual(self.booking.get_ordered_capacity(), self.ordered_capacity)
    
    def test_get_booking_time(self):
        print("\nStart get_booking_time test\n")
        self.assertEqual(vars(self.booking_time), vars(self.booking.get_booking_time()))
    
  
if __name__ == '__main__':
    unittest.main()