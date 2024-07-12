from pathlib import Path
from random import randint


class Response:
    '''
    Class with methods for reading chat guesses and returning a response

    Methods
    -------
    response_gen(response_list):
         randomly chooses a response from response_list

    give_response(response)
    '''
    filepath = Path(r'FILEPATH')

    def response_reader(self, filepath: str) -> list:
        '''
        reads from response.txt
            Parameters:
            filepath (str): absolute file path of response.txt

            Returns:
            response_list (list): List of responses
        '''
        response_file = open(filepath, "rt")
        
        # instantiate empty list
        response_list = []

        # read all lines in response.txt
        lines = response_file.readlines()

        # add each line from response.txt as an item into response_list
        for line in lines:
            response_list.append(line.strip()) #remove whitespaces

        return response_list

    
    def response_gen(self, response_list) -> str:
        '''
        generates a random number corresponding to index of elements in response_list
            Parameters:
                response_list (list): List of responses
            Returns:
                gen_response (str): Randomly chosen response
        '''
        # upper limit of random int range
        end_index = len(response_list) - 1

        # get random integer between range
        counter = 0
        while counter < 100:
            gen_num = randint(0, end_index)
            counter+=1

        # get response from response_list
        gen_response = response_list[gen_num]

        return gen_response