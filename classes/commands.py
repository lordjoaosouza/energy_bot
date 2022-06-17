class Commands:
    def __init__(self, bot, db):
        @bot.command(name="legend")
        async def legend(ctx):
            if ctx.author.id in db.get_legends():
                await ctx.send(f"You're a legend, {ctx.author.mention}! :rocket:")
            else:
                await ctx.send(f"You're not a legend, {ctx.author.mention}! :confused:")

        @bot.command(name="mv33")
        async def test(ctx):
            await ctx.send("Max Verstappen, you are the world champion! The world champion! :trophy:")
            await ctx.send("https://c.tenor.com/AOZecKy-muIAAAAd/max-verstappen-max.gif")
