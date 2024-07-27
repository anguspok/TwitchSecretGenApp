class User:
    '''
    Class represents a user of the !guess command

    Methods
    -------
    handle_user():
        Returns a response to the user for an incorrect guess made
    '''
    # key: username, value: [is_locked, num_of_attempts]
    users = {}

    # all repeat users
    repeat_users = list(users.keys())

    def __init__(self, user: str) -> None:
        self.user = user
    

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
    

    def check_for_new_user(self) -> str:
        '''
        Checks if user is repeat user

        Parameters
        ----------
        user (str): username

        Returns
        -------
        str: indicates if user is repeated or new
        '''
        if self.user in User.repeat_users:
            return "repeat" # is repeat user
        else:
            return "new" # is new user
        
    @classmethod
    def new_user_updater(self) -> None:
        '''
        Class method: adds new user to user_dict as key, 
        gives default value of user key
        '''
        # default value: [is_locked=False, num_of_attempts=1]
        User.users[self.user] = [False, 1]

    
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