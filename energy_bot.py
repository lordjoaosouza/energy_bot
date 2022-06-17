from discord.ext import commands
from classes.database import Database
from classes.events import Events
from classes.commands import Commands

bot = commands.Bot("$")
db = Database()

Events(bot)
Commands(bot, db)

bot.run(db.get_token())
