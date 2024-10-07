class MyCalendar:

    def __init__(self):
        self.intervals = []
        

    def book(self, start: int, end: int) -> bool:
        add = True
        for a,b in self.intervals:
            if start<b and end>=a:
                add = False
                break
        if add:
            self.intervals.append([start, end])
        return add
    
        


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
for start, end in [[10, 20], [15, 25], [20, 30]]:
    print(obj.book(start,end))
    