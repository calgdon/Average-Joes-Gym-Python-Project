from models.location import Location
import repositories.location_repository as location_repository

from models.instructor import Instructor
import repositories.instructor_repository as instructor_repository

from models.lesson import Lesson
import repositories.lesson_repository as lesson_repository

from models.member import Member
import repositories.members_repository as members_repository

from models.visit import Visit
import repositories.visit_repository as visit_repository


# Adding in a location

location1 = Location("Red Room", 10)
location_repository.save(location1)

location2 = Location("Blue Room", 20)
location_repository.save(location2)

location3 = Location("Green Room", 30)
location_repository.save(location3)

location4 = Location("Orange Room", 5)
location_repository.save(location4)

location5 = Location("Pink Room", 10)
location_repository.save(location5)

location6 = Location("Yellow Room", 15)
location_repository.save(location6)

# Adding in an instructor

instructor1 = Instructor("Arnold Schwarzenegger")
instructor_repository.save(instructor1)

instructor2 = Instructor("Olivia Newton-John")
instructor_repository.save(instructor2)

instructor3 = Instructor("Jane Fonda")
instructor_repository.save(instructor3)

instructor4 = Instructor("Patches O'Houlihan")
instructor_repository.save(instructor4)

instructor5 = Instructor("Mr Motivator")
instructor_repository.save(instructor5)

instructor6 = Instructor("Kris Kringle")
instructor_repository.save(instructor6)

# Adding in a lesson

lesson1 = Lesson("Yoga", "09:00", "2022/08/25", location1, instructor1, 20)
lesson_repository.save(lesson1)

lesson2 = Lesson("Pilates", "10:00", "2022/08/25", location2, instructor2, 15)
lesson_repository.save(lesson2)

lesson3 = Lesson("Arobics", "12:00", "2022/08/25", location3, instructor1, 10)
lesson_repository.save(lesson3)

lesson4 = Lesson("Wrench Dodging", "14:00", "2022/08/25", location1, instructor4, 12)
lesson_repository.save(lesson4)

lesson5 = Lesson("Wrench Ducking", "09:00", "2022/08/26", location5, instructor5, 20)
lesson_repository.save(lesson5)

lesson6 = Lesson("Wrench Dipping", "10:00", "2022/08/26", location6, instructor4, 26)
lesson_repository.save(lesson6)

lesson7 = Lesson("Wrench Diving", "11:00", "2022/08/26", location4, instructor5, 30)
lesson_repository.save(lesson7)

lesson8 = Lesson("Dodgeball", "14:00", "2022/08/26", location3, instructor6, 50)
lesson_repository.save(lesson8)

#  Adding in a member

member1 = Member("Ross", "Geller", "1980/01/01", "19 Grove Street, New York", "07770123456", "ross.geller@gmail.com", True)
members_repository.save(member1)

member2 = Member("Joey", "Tribbiani", "1984/03/31", "121 Love Street, New York", "07770987654", "joey.tribbiani@gmail.com", False)
members_repository.save(member2)

member3 = Member("Rachel", "Green", "1983,06/04", "71 The Bowery, New York", "07788648723", "rachel.green@gmail.com", True)
members_repository.save(member3)

member4 = Member("Chandler", "Bing", "1984/08/12", "53 High Road, New York", "07755234876", "chandler.bing@gmail.com", False)
members_repository.save(member4)

member5 = Member("Monica", "Geller", "1985/03/25", "12 Central Perk, New York", "07653743298", "monica.geller@gmail.com", False)
members_repository.save(member5)

member6 = Member("Phoebe", "Buffay", "1985/03/25", "12 Central Perk, New York", "07653743298", "monica.geller@gmail.com", False)
members_repository.save(member6)

member7 = Member("Fun", "Bobby", "1985/03/25", "12 Central Perk, New York", "07653743298", "monica.geller@gmail.com", False)
members_repository.save(member7)

member8 = Member("Janice", "Hosenstein", "1985/03/25", "12 Central Perk, New York", "07653743298", "monica.geller@gmail.com", False)
members_repository.save(member8)

member9 = Member("Richard", "Burke", "1985/03/25", "12 Central Perk, New York", "07653743298", "monica.geller@gmail.com", False)
members_repository.save(member9)

member10 = Member("Charlie", "Wheelar", "1985/03/25", "12 Central Perk, New York", "07653743298", "monica.geller@gmail.com", False)
members_repository.save(member10)

member11 = Member("Ursula", "Buffay", "1985/03/25", "12 Central Perk, New York", "07653743298", "monica.geller@gmail.com", False)
members_repository.save(member11)

member12 = Member("Amy", "Green", "1985/03/25", "12 Central Perk, New York", "07653743298", "monica.geller@gmail.com", False)
members_repository.save(member12)

member13 = Member("Mr", "Heckles", "1985/03/25", "12 Central Perk, New York", "07653743298", "monica.geller@gmail.com", False)
members_repository.save(member13)

member14 = Member("Roy The", "Stripper", "1985/03/25", "12 Central Perk, New York", "07653743298", "monica.geller@gmail.com", False)
members_repository.save(member14)

member15 = Member("Gunther", "Gunther", "1985/03/25", "12 Central Perk, New York", "07653743298", "monica.geller@gmail.com", False)
members_repository.save(member15)

# Adding in a member to a class

class_member1 = Visit(member1, lesson1)
visit_repository.save(class_member1)

class_member2 = Visit(member1, lesson2)
visit_repository.save(class_member2)

class_member3 = Visit(member2, lesson2)
visit_repository.save(class_member3)

class_member4 = Visit(member3, lesson3)
visit_repository.save(class_member4)

class_member5 = Visit(member3, lesson4)
visit_repository.save(class_member5)

class_member6 = Visit(member4, lesson4)
visit_repository.save(class_member6)

class_member7 = Visit(member5, lesson4)
visit_repository.save(class_member7)

class_member8 = Visit(member6, lesson6)
visit_repository.save(class_member8)

class_member9 = Visit(member7, lesson8)
visit_repository.save(class_member9)

class_member10 = Visit(member8, lesson7)
visit_repository.save(class_member10)

class_member11 = Visit(member9, lesson5)
visit_repository.save(class_member11)


# Select all members

print(members_repository.select_all())


# Select a single member

member = members_repository.select(1)
print(member.__dict__)

# Select all instructors

print(instructor_repository.select_all())

# Select a single instructor

instructor = instructor_repository.select(1)
print(instructor.__dict__)

# Select all lessons

print(lesson_repository.select_all())

# Select a single lesson

lesson = lesson_repository.select(1)
print(lesson)


# Select a single location

location = location_repository.select(1)
print(location.__dict__)


# View all members in a certain lesson

attendees = visit_repository.select_all_members_in_lesson(lesson4)
print(attendees)


#  Get the capacity of a lesson

capacity = lesson_repository.get_capacity(lesson4)
print(capacity)


# Check the number of members in a lesson

members_in_lesson = visit_repository.number_of_members_in_lesson(lesson4)
print(members_in_lesson)


# Check if member can be added to lesson

check_to_add_member_to_lesson = visit_repository.check_if_member_can_be_added_to_lesson(lesson4)
print(check_to_add_member_to_lesson)

# Check the number of spaces available per lesson

number_of_spaces_available = visit_repository.number_of_spaces_available_per_lesson(lesson4)
print(number_of_spaces_available)


# Get all classes that the member is in

all_classes_member1_in = visit_repository.get_all_classes_member_in(member1)
print(all_classes_member1_in)


# Check which classes have spaces

classes = visit_repository.check_which_classes_have_spaces()
print(classes)


# 

result = visit_repository.find_visits_id(member1, lesson1)
print(result)
