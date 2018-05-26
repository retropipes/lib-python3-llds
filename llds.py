'''
Created on Feb 8, 2015

@author: ericahnell
'''

class LLDS(object):
    '''
    The LLDS class represents a low-level data store of variable size.
    The size of the store is set upon creation and cannot be changed.
    '''

    def __init__(self, shape):
        '''
        Constructor
        '''
        self.__shape = shape
        self.__inter_prod = list()
        product = 1
        for entry in self.__shape:
            self.__inter_prod.append(product)
            product = product * entry
        self.__data_store = list()
        for x in range(0, product):  # @UnusedVariable
            self.__data_store.append(None)
            
    def __ravel_location(self, loc):
        res = 0
        # Sanity check 1
        if len(loc) != len(self.__inter_prod):
            raise IndexError("Location length and shape length do not match")
        for index in range(0, len(self.__inter_prod)):
            # Sanity check 2
            if loc[index] < 0 or loc[index] >= self.__shape[index]:
                raise IndexError("Index out of bounds: " + str(loc[index]))
            res = res + (loc[index] * self.__inter_prod[index])
        return res
    
    def get_shape(self):
        return self.__shape
    
    def get_cell(self, loc):
        aloc = self.__ravel_location(loc)
        return self.__data_store[aloc]
    
    def set_cell(self, loc, value):
        aloc = self.__ravel_location(loc)
        self.__data_store[aloc] = value
        
    def fill(self, value):
        for x in range(0, len(self.__data_store)):
            self.__data_store[x] = value
    
    def _get_raw_cell(self, rawloc):
        return self.__data_store[rawloc]

    def _set_raw_cell(self, rawloc, value):
        self.__data_store[rawloc] = value
    
    def _get_raw_length(self):
        return len(self.__data_store)