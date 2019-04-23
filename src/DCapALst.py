## @file DCapALst.py
#  @author Artemiy Kokhanov
#  @brief DCapALst
#  @date 08/02/2018


## @brief An abstract data type for storing department data
class DCapALst:

    s = []

    ## @brief init initial data structure
    @staticmethod
    def init():
        DCapALst.s = []

    ## @brief add adds a department to the data structure
    #  @exception throws KeyError if department is already in the data structure
    #  @param d department name added to the data structure
    #  @param n capacity of department added to the data structure
    @staticmethod
    def add(d, n):
        if (d, n) in DCapALst.s:
            raise KeyError
        else:
            DCapALst.s.append((d, n))

    ## @brief remove removes a deparment from the data structure
    #  @exception throws KeyError if department is not in data structure
    #  @param d department name
    @staticmethod
    def remove(d):
        if True in [d == i[0] for i in DCapALst.s if d == i[0]]:
            for i in DCapALst.s:
                if d == i[0]:
                    elem = i
        else:
            raise KeyError

        DCapALst.s.remove(elem)

    ## @brief elm checks if the department is in the data structure
    #  @param d department name
    #  @return True if department in datastructure and False if not
    @staticmethod
    def elm(d):
        if len(DCapALst.s) != 0:
            if True in [d == i[0] for i in DCapALst.s if d == i[0]]:
                return True
            else:
                return False
        else:
            return False

    ## @brief capacity checks the capacity of the department
    #  @exception throws KeyError if department is not in the data structure
    #  @param d department name
    #  @return capacity of the department
    @staticmethod
    def capacity(d):
        if True in [d == i[0] for i in DCapALst.s if d == i[0]]:
            for i in DCapALst.s:
                if d == i[0]:
                    return i[1]
        else:
            raise KeyError
