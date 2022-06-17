class Events:
    def __init__(self, bot):
        @bot.event
        async def on_ready():
            print(f"Connected to {bot.user.name}, ID: {bot.user.id}!")

        @bot.event
        async def on_message(message):
            if message.author == bot.user:
                return

            await bot.process_commands(message)
