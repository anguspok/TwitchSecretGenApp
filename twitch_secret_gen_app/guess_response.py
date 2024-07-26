from abc import ABC,  abstractmethod
from pathlib import Path
from random import randint
from guess_user import User
from file_manager import ResponseFile

class Guess:
    '''
    Class represents a guess made by a user of the !guess command

    Methods
    -------
    verify_guess():
        Compares chat guess with secret word
    
    user_updater:
        Updates new users and their number of attempts made

    guess_attempts:
        Writes all guess attempts into attempts.txt file
    '''
    # secret word/phrase to be guessed
    secret = "SECRET"

    def __init__(self, input_from_chat: str, is_verified=False) -> None:
        self.input_from_chat = input_from_chat
        self.is_verified = is_verified

    def verify_guess(self) -> bool:
        '''
        Compares chat guess with secret word

        Parameters
        ----------
        input_from_chat (str): word/phrase argument used with !guess command
        secret (str): word/phrase to be guessed

        Returns
        ------- 
        result (bool): True if correct word/phrase guessed, False if not
        '''
        # comparing chat input to arbitrary secret word 
        if self.input_from_chat.lower() == Guess.secret.lower():
            self.is_verified = True
            return True # word matches
        else:
            self.is_verified = False
            return False # word does not match 

class Response:
    '''
    Class with methods for reading chat guesses and returning a response

    Methods
    -------
    response_reader(response_filepath):
        Reads from response.txt
    
    response_gen(responses):
         Generates a random number corresponding to index of elements in responses list

    give_response(response):
        Receives input from chat and gives a suitable response
    '''
    def generate_response(self, responses: list) -> str:
        '''
        Generates a random number corresponding to index of elements in responses
        
        Parameters
        ----------
        responses (list): List of responses
        
        Returns
        -------
        gen_response (str): Randomly chosen response
        '''
        # get random integer between range
        gen_num = randint(0, len(responses) - 1)

        # get response from response_list
        gen_response = responses[gen_num]

        return gen_response
    

    def give_response(self, input_from_chat: str) -> str:
        '''
        Receives input from chat and gives a suitable response

        Parameters
        ----------
        input_from_chat (str): word/phrase argument used with !guess command

        Returns
        -------
        response_to_chat (str): response that chatbot will send to chat
        '''
        # validate word by calling validator
        result = Guess.verify_guess(input_from_chat)

        if result:
            pass
        else:
            pass