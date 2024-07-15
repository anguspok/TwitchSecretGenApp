import twitchio
from twitchio.ext import commands
from response import Response

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token='ACCESS_TOKEN', prefix='!')

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')


    async def event_command_error(self, context: commands.Context, error: Exception):
            if isinstance(error, commands.CommandNotFound):
                return

            elif isinstance(error, commands.ArgumentParsingFailed):
                await context.send(error.message)

            elif isinstance(error, commands.MissingRequiredArgument):
                await context.send("You're missing an argument: " + error.name)

            elif isinstance(error, commands.CheckFailure): # we'll explain checks later, but lets include it for now.
                await context.send("Sorry, you cant run that command: " + error.args[0])

            elif isinstance(error, MissingGuessWord):
                await context.send()

            else:
                print(error)


    @commands.command()
    # command guess, invoke command with prefix and command name and phrase
    # eg. !guess phrase
    async def guess(self, ctx: commands.Context, guess_phrase: str = None):
        if guess_phrase is None:
            raise("No guess word/phrase was entered")

        # retrieve response
        response = Response.give_response(guess_phrase)
        
        # send response to chat
        await ctx.send(f'@{ctx.author.name} {response}')


bot = Bot()
bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.