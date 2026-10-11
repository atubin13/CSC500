# Three dictionaries, each using the course number as the key
course_rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411",
}

course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee",
}

course_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m.",
}


def get_course_info(course_number):
    """Return (room, instructor, time) for a course, or None if not found."""
    if course_number in course_rooms:
        return (
            course_rooms[course_number],
            course_instructors[course_number],
            course_times[course_number],
        )
    return None


def main():
    print("=== Course Information System ===")

    while True:
        entry = input("\nEnter a course number (e.g., CSC101) or 'quit' to exit: ")
        course_number = entry.strip().upper()

        if course_number == "QUIT":
            print("Goodbye!")
            break

        info = get_course_info(course_number)

        if info is not None:
            room, instructor, time = info
            print(f"\nCourse:     {course_number}")
            print(f"Room:       {room}")
            print(f"Instructor: {instructor}")
            print(f"Meets at:   {time}")
        else:
            print(f"\nSorry, '{entry.strip()}' was not found.")
            print("Valid courses are: " + ", ".join(course_rooms.keys()))


main()