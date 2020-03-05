import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import os

Bot = commands.Bot(command_prefix = "//")
token = 'NjgzMzY1NTI3NTE0OTA2NjI0.XlwLBQ.cf684knUdyioOMuBpWPBCE3js9k'
client = discord.Client()



@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Game(name='Impact 1.12.2'))
    print('Всё мы запустились, {0.user}'.format(Bot))



@Bot.command(pass_context=True)
async def grole(ctx, role1, member: discord.Member=None):
    role = discord.utils.get(member.guild.roles, name = role1)
    member1 = member
    msg21 = ("Была выдана роль ** "+ str(role) +" ** участнику сервера **" + str(member1)+ "**")
    await ctx.send(msg21)
    await member.add_roles(role, member)

@Bot.command(pass_context=True)
async def clear(ctx, amount):
    await ctx.channel.purge(limit = int(amount) + 1)
    await ctx.send("Было удалено " + amount + " сообщений")

@Bot.command(pass_context=True)
async def kick(ctx,member: discord.Member = None):
    await member.kick()

    await ctx.send("***ВНИМАНИЕ*** участник клана **" + str(member) + "** был кикнут из клана" )

@Bot.command(pass_context=True)
async def helps(ctx):
    await ctx.send("""```Перечень команд бота T-BOT: \n **//grole** (роль которую вы хотите выдать без @) (ник участника сервера нп TToMoIIIHUK#1485) \n **//Clear** (количевство сообщений которые вы хотите удалить)\n **//kick** (никнейм участника нп. TToMoIIIHUK#1485) \n\n\n\n T-BOT created by TToMoIIHUK```""")




@Bot.event
async def on_member_join(ctx):
    await ctx.send("***Приветствыю в клане Freedom/Ария. \n Чтобы узнать больше команд пищи //helps в канале для ботов!***")
    role = discord.utils.get(ctx.guild.roles, name = "Testing")
    await ctx.add_roles(role)

token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))
