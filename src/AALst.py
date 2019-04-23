## @file AALst.py
#  @author Artemiy Kokhanov
#  @brief AALst
#  @date 08/02/2018

from StdntAllocTypes import *


## @brief An abstract data type for storing students in departments
class AALst:

    s = []

    ## @brief init initial data structure
    #  @details Adds all departments to data structure and a list for students to be added to
    @staticmethod
    def init():
        AALst.s = []

        for i in DeptT:
            AALst.s.append((i, []))

    ## @brief add_stdnt adds students to specified department
    #  @param dep department name
    #  @param m student name
    @staticmethod
    def add_stdnt(dep, m):
        for i in range(len(AALst.s)):
            if dep == AALst.s[i][0]:
                AALst.s[i][1].append(m)

    ## @brief lst_alloc gets list of students in specified department
    #  @param d department name
    #  @return list of students
    @staticmethod
    def lst_alloc(d):
        for i in range(len(AALst.s)):
            if d == AALst.s[i][0]:
                return AALst.s[i][1]

    ## @brief num_alloc gets the number of students in specified department
    #  @param d department name
    #  @return number of students in specified department
    @staticmethod
    def num_alloc(d):
        for i in range(len(AALst.s)):
            if d == AALst.s[i][0]:
                return len(AALst.s[i][1])
