import socket
import logging
import re
from datetime import datetime
import pandas as pd

class ChatLogger:
    '''
    Class that contains methods for reading and recording chat logs

    Methods
    -------
    irc_server_connect:
        Connects to irc server and decodes messages
    
    get_chat_dataframe(file):
        formats decoded messages into key components and creates a dataframe of chatlog
    
    '''
    def irc_server_connect(self):
        '''
        Connects to irc server, decodes messages and records chat logs
        '''
        # define constants for connecting to irc
        server = 'irc.twitch.tv'
        port = 6667
        nickname = 'NICKNAME'
        token = 'ouath:ACCESS_TOKEN'
        channel = '#STREAM_CHANNEL'


        # instantiate a socket
        sock = socket.socket()
        # connect this socket to Twitch with the server and port
        sock.connect((server, port))


        # send token and nickname for authentication, and the channel to connect to over the socket
        # with sockets, send() these parameters as encoded strings
        sock.send(f"PASS {token}\n".encode('utf-8'))
        sock.send(f"NICK {nickname}\n".encode('utf-8'))
        sock.send(f"JOIN {channel}\n".encode('utf-8'))
        # able to use this for other IRC, with different values

        # logging formatting
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s — %(message)s',
                            datefmt='%Y-%m-%d',
                            handlers=[logging.FileHandler('chat.log', encoding='utf-8')])

        # continuously look for new messages
        while True:
            # decode single response from chat
            resp = sock.recv(2048).decode('utf-8') #2048 buffer size, byte size of data that can be received

            # respond to twitch irc server keepalive messages
            if resp.startswith('PING'):
                sock.send("PONG\n".encode('utf-8'))


    def get_chat_dataframe(self, file):
        '''
        '''
        data = []

        with open(file, 'r', encoding='utf-8') as f:
            lines = f.read().split('\n\n\n')
            
            for line in lines:
                try:
                    time_logged = line.split('—')[0].strip()
                    time_logged = datetime.strptime(time_logged, '%Y-%m-%d_%H:%M:%S')

                    username_message = line.split('—')[1:]
                    username_message = '—'.join(username_message).strip()

                    username, channel, message = re.search(
                        ':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', username_message
                    ).groups()

                    d = {
                        'dt': time_logged,
                        'channel': channel,
                        'username': username,
                        'message': message
                    }

                    data.append(d)
                
                except Exception:
                    pass
                
        return pd.DataFrame().from_records(data)