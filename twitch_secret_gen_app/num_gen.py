from random import randint
from ResponseClass import *

class NumGenClass:
    '''
    class with methods for generating a random number

    Attributes
    ----------

    Methods
    -------
    num_gen():
        generates a random number corresponding to index of elements in response_list
    '''
    def __init__(self, ):


    def num_gen(self):
        '''
        generates a random number corresponding to index of elements in response_list
            Parameters:

            Returns:
                gen_num (int): Integer which corresponds to index of elements in response_list
        '''
        # response_end_index is the larger end point of random int range
        response_end_index = len(ResponseClass.response_list) - 1

        # get random integer between range
        gen_num = randint(0, response_end_index)

        return gen_num