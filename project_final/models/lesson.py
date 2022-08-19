class Lesson:

    def __init__(self, name, time, date, location, instructor, capacity, id=None):
        self.name = name
        self.time = time
        self.date = date
        self.location = location
        self.instructor = instructor
        self.capacity = capacity
        self.id = id