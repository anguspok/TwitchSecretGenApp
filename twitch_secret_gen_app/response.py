from pathlib import Path
from random import randint
from guess import Guess


class Response:
    '''
    Class with methods for reading chat guesses and returning a response

    Methods
    -------
    response_reader(filepath):
        Reads from response.txt
    
    response_gen(response_list):
         Generates a random number corresponding to index of elements in response_list

    give_response(response):
        Receives input from chat and gives a suitable response
    '''
    filepath = Path(r'FILEPATH')

    def response_reader(self, filepath: str) -> list:
        '''
        Reads from response.txt
        
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

        response_file.close()

        return response_list

    
    def response_gen(self, response_list) -> str:
        '''
        Generates a random number corresponding to index of elements in response_list
        
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
    

    def give_response(self, chat_input) -> str:
        '''
        Receives input from chat and gives a suitable response

        Parameters:
            chat_input (str): word/phrase argument used with !guess command

        Returns:
            response_str (str): response that chatbot will send to chat
        '''
        # validate word by calling validator
        result = Guess.guess_validator(chat_input, secret=Guess.secret)

        if result:
            pass
        else:
            pass