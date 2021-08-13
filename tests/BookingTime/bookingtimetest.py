from datetime import datetime
from MakeSpace.Bookings.bookings import Booking
from MakeSpace.BookingTime.bookingtime import BookingTime
import unittest

class BookingTimeTest(unittest.TestCase):
    booking_time = BookingTime("16:00","18:00")
    start_time_object = datetime.strptime("16:00","%H:%M")
    end_time_object = datetime.strptime("18:00","%H:%M")
  
    # Returns True if the booking capacity returned is correct.
    def test_get_time_object(self):
        print("\nStart get_time_object test\n")
        self.assertEqual(vars(self.start_time_object), vars(datetime.strptime("16:00","%H:%M")))
        self.assertEqual(vars(self.end_time_object), vars(datetime.strptime("18:00","%H:%M")))
  
if __name__ == '__main__':
    unittest.main()