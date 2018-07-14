# -*- coding: utf-8 -*-
import Person


class Student(Person):

    def __init__(self, name, age, average_grade):
        super(Student, self).__init__(name, age)
        self.__avg_grade = average_grade

    def get_avg_grade(self):
        return self.__avg_grade

    def set_avg_grade(self, avg_grade):
        self.__avg_grade = avg_grade