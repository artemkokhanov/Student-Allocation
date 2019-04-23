## @file SeqADT.py
#  @author Artemiy Kokhanov
#  @brief SeqADT
#  @date 08/02/2018


## @brief An abstract data type that represents a sequence
class SeqADT:

    ## @brief SeqADT constructor
    #  @details initializes the sequence of any type
    #  param x sequence of any type
    def __init__(self, x):
        self.s = x
        self.i = 0

    ## @brief start sets the starting point of the sequence to the beginning of the sequence
    def start(self):
        self.i = 0

    ## @brief next gets the next item in the sequence
    #  @details if i is within range of the sequence then return the next item in the sequence
    #  @exception StopIteration - if i is not within the range of the sequence
    #  @return next item in the sequence
    def next(self):
        if self.i >= len(self.s):
            raise StopIteration
        else:
            self.i += 1
            return self.s[self.i - 1]

    ## @brief end checks if at the end of the sequence
    #  @return boolean True if at end of the sequence and False if not
    def end(self):
        return self.i >= len(self.s)
