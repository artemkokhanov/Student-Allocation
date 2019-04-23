## @file Read.py
#  @author Artemiy Kokhanov
#  @brief functions for retrieving data from files
#  @date 08/02/2018

from StdntAllocTypes import *
from DCapALst import *
from SALst import *


## @brief load_stdnt_data reads in student data from a file, storing it in SALst
#  @param s the name of the file to be read
def load_stdnt_data(s):
    with open(s, 'r') as stdnt_data:
        contents = stdnt_data.readlines()

    SALst.init()

    for line in contents:
        id_to_gpa = line.split(', ', 5)[0:5]
        choices = line.split(', ', 5)[5:][0].rstrip().split('], ')[0].lstrip('[').split(', ')
        freechoice = line.split(', ', 5)[5:][0].rstrip().split('], ')[1]

        if id_to_gpa[3] == 'male':
            id_to_gpa[3] = GenT.male
        elif id_to_gpa[3] == 'female':
            id_to_gpa[3] = GenT.female

        if freechoice == 'True':
            freechoice = True
        elif freechoice == 'False':
            freechoice = False

        for i in range(len(choices)):
            if choices[i] == 'civil':
                choices[i] = DeptT.civil
            elif choices[i] == 'chemical':
                choices[i] = DeptT.chemical
            elif choices[i] == 'electrical':
                choices[i] = DeptT.electrical
            elif choices[i] == 'mechanical':
                choices[i] = DeptT.mechanical
            elif choices[i] == 'software':
                choices[i] = DeptT.software
            elif choices[i] == 'materials':
                choices[i] = DeptT.materials
            elif choices[i] == 'engphys':
                choices[i] = DeptT.engphys

        fname = id_to_gpa[1]
        lname = id_to_gpa[2]
        gender = id_to_gpa[3]
        gpa = float(id_to_gpa[4])

        sinfo = SInfoT(fname, lname, gender, gpa, SeqADT(list(choices)), freechoice)
        SALst.add(id_to_gpa[0], sinfo)


## @brief load_dcap_data reads in department data from a file, storing it in DCapALst
#  @param s the name of the file to be read
def load_dcap_data(s):
    with open(s, 'r') as stdnt_data:
        contents = stdnt_data.readlines()

    DCapALst.init()

    for line in contents:
        depts = line.split(', ')

        if depts[0] == 'civil':
            depts[0] = DeptT.civil
        elif depts[0] == 'chemical':
            depts[0] = DeptT.chemical
        elif depts[0] == 'electrical':
            depts[0] = DeptT.electrical
        elif depts[0] == 'mechanical':
            depts[0] = DeptT.mechanical
        elif depts[0] == 'software':
            depts[0] = DeptT.software
        elif depts[0] == 'materials':
            depts[0] = DeptT.materials
        elif depts[0] == 'engphys':
            depts[0] = DeptT.engphys

        depts[1] = int(depts[1].rstrip())

        DCapALst.add(depts[0], depts[1])
