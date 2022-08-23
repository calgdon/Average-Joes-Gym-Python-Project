class Lesson:

    def __init__(self, name, time, date, location, instructor, capacity, id=None):
        self.name = name
        self.time = time
        self.date = date
        self.location = location
        self.instructor = instructor
        self.capacity = capacity
        self.id = id

    def __eq__(self, other):
        if not isinstance(other, Lesson):
            return NotImplemented

        return self.name==other.name and self.time==other.time and self.date==other.date and self.location==other.location and self.instructor==other.instructor and self.capacity==other.capacity and self.id==other.id
