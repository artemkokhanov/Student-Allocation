## @file SALst.py
#  @author Artemiy Kokhanov
#  @brief SALst
#  @date 08/02/2018

from AALst import *
from DCapALst import *


## @brief An abstract data type for allocating students
class SALst:

    s = []

    ## @brief init initial data structure
    @staticmethod
    def init():
        SALst.s = []

    ## @brief add adds student from data structure
    #  @exception throws KeyError if student information already in data structure
    #  @param m student macid
    #  @param i student information
    @staticmethod
    def add(m, i):
        if (m, i) in SALst.s:
            raise KeyError
        else:
            SALst.s.append((m, i))

    ## @brief remove removes student from data structure
    #  @exception throws KeyError if student is not in data structure
    #  @exception ValueError - just to make sure built-in remove function does not raise
    #             ValueError because of specification
    #  @param m student macid
    @staticmethod
    def remove(m):
        if True in [m == i[0] for i in SALst.s if m == i[0]]:
            for i in SALst.s:
                if m == i[0]:
                    elem = i
        else:
            raise KeyError

        SALst.s.remove(elem)

    ## @brief elm if the student is in the data structure
    #  @param m student macid
    #  @return True if student is in the data structure and false if not
    @staticmethod
    def elm(m):
        if len(SALst.s) != 0:
            if True in [m == i[0] for i in SALst.s if m == i[0]]:
                return True
            else:
                return False
        else:
            return False

    ## @brief info gets student information
    #  @exception throws KeyError if student is not in the data structure
    #  @param m students macid
    #  @return SInfoT
    @staticmethod
    def info(m):
        if True in [m == i[0] for i in SALst.s if m == i[0]]:
            for i in SALst.s:
                if m == i[0]:
                    return i[1]
        else:
            raise KeyError

    ## @brief sort sorts the data structure
    #  @details Sorts the data structure in decending order in terms of gpa
    #  @param f function that decides which students get sorted
    #  return sorted list of students in data structure
    @staticmethod
    def sort(f):
        sorted_list = []

        first_sort = [SALst.s[i] for i in range(len(SALst.s)) if f(SALst.s[i][1]) is True]
        second_sort = sorted(first_sort, key=lambda x: x[1].gpa, reverse=True)

        for i in range(len(second_sort)):
            sorted_list.append(second_sort[i][0])

        return sorted_list

    ## @brief average gets the average gpa of students in the data structure
    #  @details appropriate average calculated based on gender
    #  @param f function that decides for which gender to calculate average
    #  return average gpa of students
    @staticmethod
    def average(f):
        f_set = [SALst.s[i] for i in range(len(SALst.s)) if f(SALst.s[i][1]) is True]

        sum = 0
        for i in range(len(f_set)):
            sum += f_set[i][1].gpa

        return float("{0:.2f}".format(sum / len(f_set)))

    ## @brief allocate allocates students to departments
    #  @details allocated students based on freechoice and gpa
    #  @exceptions throws RuntimeError if allocation does not occur
    @staticmethod
    def allocate():
        AALst.init()
        f = SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0)
        for m in f:
            ch = SALst.info(m).choices
            AALst.add_stdnt(ch.next(), m)

        s = SALst.sort(lambda t: t.freechoice is False and t.gpa >= 4.0)
        for m in s:
            ch = SALst.info(m).choices
            alloc = False
            while alloc is not True and ch.end() is not True:
                d = ch.next()
                if AALst.num_alloc(d) < DCapALst.capacity(d):
                    AALst.add_stdnt(d, m)
                    alloc = True
            if alloc is not True:
                raise RuntimeError
