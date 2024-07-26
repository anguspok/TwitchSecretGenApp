from abc import ABC, abstractmethod

# class Filepath(ABC):
#     '''
#     '''
#     def retrieve_absolute_filepath(self, filepath: str) -> str:
#         '''
#         '''
#         return Path(filepath)


class FileManager(ABC):
    '''
    Class with methods for managing files
    '''
    @abstractmethod
    def file_reader(self):
        '''
        '''
        pass

    @abstractmethod
    def file_writer(self):
        '''
        '''
        pass


class ResponseFile(FileManager):
    response_filepath = 'data/response.txt'

    def file_reader(self):
        with open(ResponseFile.response_filepath, 'rt') as responsetxt_file:
            # initialize empty list
            responses = []

            # read all lines in response.txt
            lines = responsetxt_file.readlines()

            # add each line from response.txt as an item into responses list
            for line in lines:
                responses.append(line.strip()) #remove whitespaces

            responsetxt_file.close()

            return responses