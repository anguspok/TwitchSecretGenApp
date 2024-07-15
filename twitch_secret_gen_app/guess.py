class Guess:
    '''
    Class with methods for handling chat guesses

    Methods
    -------
    guess_validator(chat_input, secret):
        Compares chat guess with secret word
    
    user_updater:
        Updates new users and their number of attempts made

    guess_attempts:
        Writes all guess attempts into attempts.txt file
    '''
    # secret word to be guessed
    secret = "STRING"

    def guess_validator(self, chat_input, secret) -> bool:
        '''
        Compares chat guess with secret word

        Parameters:
            chat_input (str): word/phrase argument used with !guess command
            secret (str): word/phrase to be guessed

        Returns:
            result (bool): True if correct word/phrase guessed, False if not
        '''
        # comparing chat input to arbitrary secret word 
        if chat_input.lower() == secret.lower():
            return True
        else:
            return False
        

        def user_updater(self):
            pass