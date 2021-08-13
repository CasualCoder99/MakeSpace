from datetime import datetime


class BookingTime:

    open_time = datetime.strptime("0000", "%H%M") # opening time of office
    close_time = datetime.strptime("2345", "%H%M") # closing time of office
    buffers = [("0900", "0915"),("1315", "1345"),("1845", "1900")] #buffer times of office
    buffer_times = []
    for buffer in buffers:
            buffer_start, buffer_end = datetime.strptime(buffer[0],"%H%M"), datetime.strptime(buffer[1],"%H%M")
            buffer_times.append((buffer_start,buffer_end))

    def __init__(self, start_time, end_time) -> None:
        self._start_time_object = datetime.strptime(start_time, "%H:%M")
        self._end_time_object = datetime.strptime(end_time, "%H:%M")
    
    def get_time_object(self) -> tuple:
        return (self._start_time_object,self._end_time_object)
    
    def meeting_during_buffer(self) -> bool: #is the meeting scheduled during buffer time?
        for buffer in self.buffer_times:
            buffer_start, buffer_end = buffer
            if(self._start_time_object >= buffer_start and self._start_time_object < buffer_end):  
                return True
            elif((self._end_time_object > buffer_start and self._end_time_object <= buffer_end)):
                return True
        return False

    def is_valid_time_object(self) -> bool:
        time_interval_permit = 15 # only intervals of 15 mins allowed
        if(self._end_time_object <= self._start_time_object): 
            return False
        elif((self._end_time_object.minute % time_interval_permit != 0 or self._start_time_object.minute % time_interval_permit != 0)): # not in 15 minute intervals
            return False
        elif(self._start_time_object < self.open_time and self._start_time_object >= self.close_time):
            return False
        elif(self._end_time_object > self.close_time and self._end_time_object <= self.open_time):
            return False
        else:
            return True