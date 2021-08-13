from datetime import datetime
class Booking:

    def __init__(self, booking_time, capacity) -> None:
        self._booking_time = booking_time
        self._capacity = int(capacity)
    
    def get_ordered_capacity(self):
        return self._capacity
    
    def get_booking_time(self):
        return self._booking_time
