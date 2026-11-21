class MyCalendar:
    
    def __init__(self):
        self.cal=[]

    def book(self, startTime: int, endTime: int) -> bool:
        print(self.cal)
        for booking in self.cal:
            if max(booking[1],endTime)-min(booking[0],startTime)<booking[1]-booking[0]+endTime-startTime:
                return False
        self.cal.append([startTime,endTime])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)