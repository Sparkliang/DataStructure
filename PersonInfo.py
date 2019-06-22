# Ch2 abstract data type and Python class
# PersonInfo
# Liang Xing

import datetime

class Person:
    _num = 0
    def __init__(self, name, sex, birthday, ident):
        if not (isinstance(name, str) and sex in ("male", "female")):
            raise PersonValueError(name, sex)
        try:
            birth = datetime.date(*birthday)
        except:
            raise PersonValueError("Wrong date:", birthday)
        self._name = name
        self._sex = sex
        self._birthday = birth
        self._id = ident
        Person._num += 1

    def id(self): return self._id
    def name(self): return self._name
    def sex(self): return self._sex
    def birthday(self):return self._birthday
    def age(self): return (datetime.date.today().year - self._birthday.year())

    def set_name(self, name):
        if not isinstance(name, str):
            raise PersonValueError("set_name", name)
        self._name = name

    def __lt__(self, another):
        if not isinstance(another, Person):
            raise PersonTypeError(another)
        return self._id < another._id

    @classmethod
    def num(cls): return Person._num

    def __str__(self):
        return " ".join((self._id, self._name,
                         self._sex, str(self._birthday)))

    def details(self):
        return ", ".join(("number: " + self._id,
                          "name: " + self._name,
                          "gender: " + self._sex,
                          "birthday: " + str(self._birthday)))

class Student(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return "1{:04}{:05}".format(year, cls._id_num)

    def __init__(self, name, sex, birthday, department):
        Person.__init__(self, name, sex, birthday,
                        Student._id_gen())
        self._department = department
        self._enroll_date = datetime.date.today()
        self._courses = {}

    def set_course(self, course_name):
        self._courses[course_name] = None

    def set_score(self, course_name, score):
        if course_name not in self._courses:
            raise PersonValueError("No this course selected:",
                                   course_name)
        self._courses[course_name] = score

    def scores(self):
        return [(cname, self._courses[cname]) for cname in self._courses]


    def details(self):
        return ", ".join((Person.details(self),
                          "Entrance Time: " + str(self._enroll_date),
                          "College: " + self._department,
                          "Course List: " + str(self.score())))

class Staff(Person):
    _id_num = 0
    @classmethod
    def _id_gen(cls, birthday):
        cls._id_num += 1
        birth_year = datetime.date(*birthday).year
        return "0{:04}{:05}".format(birth_year, cls._id_num)

    def __init__(self, name, sex, birthday, entry_date=None):
        super().__init__(name, sex, birthday,
                         Staff._id_gen(birthday))
        if entry_date:
            try:
                self._entry_date = datetime.date(*entry_date)
            except:
                raise PersonValueError("Wrong date:",
                                       entry_date)
            else:
                self._entry_date = datetime.date.today()
            self._salary = 1720
            self._department = "undefined"
            self._position = "undefined"

    def set_salary(self, amount):
        if not type(amount) is int:
            raise TypeError
        self._salary = amount

    def set_position(self, position):
        self._position = position
    def set_department(self, department):
        self._department = department

    def details(self):
        return ", ".join((super().details(),
                         "Entry Time: " + str(self._entry_date),
                         "College: " + self._department,
                         "Position: " + self._position,
                         "Salary: " + str(self._salary)))


    
