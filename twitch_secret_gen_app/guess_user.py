class User:
    '''
    Class represents a user of the !guess command

    Methods
    -------
    handle_user():
        Returns a response to the user for an incorrect guess made
    '''
    # holds users and attempts made
    user_dict = {}

    def __init__(self, user: str, is_locked=False, is_repeat=False) -> None:
        self.user = user
        self.is_locked = is_locked
        self.is_repeat = is_repeat


    @classmethod
    def new_user_updater(self) -> None:
        '''
        Class method: adds new user to user_dict as key, 
        sets value of new user as 1
        '''
        # add user and record attempts as 1
        User.user_dict[self.user] += 1

        # modify user status to repeat user
        self.is_repeat = True
    

    @classmethod
    def repeat_user_updater(self) -> None:
        '''
        Class method: updates value of user key by +1
        '''
        # update number of attempts made by user by 1
        User.user_dict[self.user]+=1


    @classmethod
    def check_user_attempts(self) -> None:
        '''
        Class method: checks number of attempts made, 
        removes user from user_dict if 3 attempts used, 
        updates is_locked status
        '''
        # check for number of attempts made by user
        attempts = User.user_dict[self.user]
        
        if attempts == 3:
            # remove users with 3 attempts
            User.user_dict.pop(self.user)

            # modify user status to locked
            self.is_locked = True
    
    
    def handle_user(self) -> str:
        '''
        Checks if user is locked, 
        adds new user into user_dict,
        updates attempts made for new and repeat users,
        returns a response to the user for an incorrect guess made
        
        Returns
        -------
        str: response to user 
        '''
        # check for number of attempts made by user
        attempts = User.user_dict[self.user]

        # user is locked
        if self.is_locked:
            return " you have used all 3 attempts"

        # user is not locked
        else:
            # user is a repeat user
            if self.is_repeat:
                # update user_dict
                User.repeat_user_updater(self.user)
            
            # user is a new user
            else:
                # update user_dict
                User.new_user_updater(self.user)

            return f" incorrect guess, you have {3-attempts} left"