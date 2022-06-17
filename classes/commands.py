class Commands:
    def __init__(self, bot, db):
        @bot.command(name="commands")
        async def commands(ctx):
            await ctx.message.delete()
            await ctx.send("**Commands:**\n`$clear <x>` - Clear x messages from the chat.;\n`$level` - Shows your "
                           "level;\n`$myid` - Shows your Dircord ID;\n`$legend` - Check if you're a legend;\n`$mv33` "
                           "- Shows the best Formula 1 driver;", delete_after=120)

        @bot.command(name="clear")
        async def clear(ctx, amount):
            await ctx.channel.purge(limit=int(amount) + 1)
            await ctx.send(f"Cleared {amount} message in this chat! :broom:", delete_after=5)

        @bot.command(name="level")
        async def level(ctx):
            await ctx.message.delete()
            if ctx.author.id not in db.get_levels():  # todo: create members database
                db.set_level(int(ctx.author.id), 0)

            lv = db.get_level(int(ctx.author.id))
            await ctx.send(f"{ctx.author.mention} you're in level {lv}! :zap:", delete_after=10)

        @bot.command(name="myid")
        async def myid(ctx):
            await ctx.message.delete()
            await ctx.send(f"{ctx.author.mention}, your ID is {ctx.author.id}! :label:", delete_after=10)

        @bot.command(name="legend")
        async def legend(ctx):
            await ctx.message.delete()
            if ctx.author.id in db.get_legends():
                await ctx.send(f"You're a legend, {ctx.author.mention}! :rocket:", delete_after=10)
            else:
                await ctx.send(f"You're not a legend, {ctx.author.mention}! :confused:", delete_after=10)

        @bot.command(name="mv33")
        async def test(ctx):
            await ctx.message.delete()
            await ctx.send("Max Verstappen, you are the world champion! The world champion! :trophy:", delete_after=10)
            await ctx.send("https://c.tenor.com/AOZecKy-muIAAAAd/max-verstappen-max.gif", delete_after=10)
