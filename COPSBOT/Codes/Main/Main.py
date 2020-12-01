# Unofficial discord bot for critical ops.
# Made by Senpai_Desi#8565 and J. Pisser#3258
# Date created: 03-06-2020
# LAst modification 16-11-2020
# Version: V0.4.4 Alpha
# Copyrighted 2020-2030 Under the GNU license.
# This project is free to alter aslong as credit is givin
# Copy and pasting some code is permitted as long as the user DOES NOT copy the entire project and alters 1 or 2 signatures.
# Any projects alterd like above is in fight with the license and will result in deleting the app or asking the developer to change it.
# Only current exception is for employees working at CF Studio or Critical ops.


# This one is for you developers :)
# Love Your game.
# Keep up the good work as you are all doing an amazing job!
# This game is great and under your supervision it will stay so.
# Greets from the Netherlands ~Senpai_Desi 03-06-2020


# Importing libraries.
import discord                                          #Imports the discord.py library found at :https://github.com/Rapptz/discord.py
from discord.ext import commands, tasks                 #Imports the commands and task library from discord 
from itertools import cycle                             #imports the cycle library from itertools
import time                                             #Imports the time library


# Getting login details and making a description.
TOKEN = 'CENSORED'
description = '''The unofficial critical ops bot made by Senpai_Desi#8565'''


# Making the bot description to the description  given one line up.
bot = commands.Bot(command_prefix='/', description=description)


# Setting the status cycle.
status = cycle(['Use /commands to get  help', 'Respecting devs', 'Watching operatives.',
                'c-ops api', 'Opening cases', 'Watching 115,000+ members', 'Helping new operatives'])


#Removes the help command.
bot.remove_command('help')

# Initialising the status cycle.

#Starts the presence loop.
@tasks.loop(minutes=3)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))


# Logging in and selecting the first status for the status cycler to use.
@bot.event
async def on_ready():
    change_status.start()
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Respecting devs'))
    print('Welcome to the critical ops bot console :)')
    print('Logged in sucsesfully!')
    print(bot.user.name)
    print(bot.user.id)
    print('-------------------------------------')
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------


#Frequently asked question commands.


@bot.command()
async def elite(ctx):
    await ctx.send('<https://criticalopsgame.com/leaderboards/ranked-elite/>')  #


@bot.command()
async def ranked(ctx):
    await ctx.send('<https://criticalopsgame.com/leaderboards/ranked>')


@bot.command()
async def casual(ctx):
    await ctx.send('<https://criticalopsgame.com/leaderboards/casual/>')


@bot.command()
async def clan(ctx):
    await ctx.send('<https://criticalopsgame.com/leaderboards/clan>')


@bot.command()
async def websitecops(ctx):
    await ctx.send('<https://criticalopsgame.com/>')


@bot.command()
async def cfe(ctx):
    await ctx.send('<https://criticalforce.fi>')


@bot.command()
async def updates(ctx):
    await ctx.send('<https://criticalopsgame.com/updates/>')


@bot.command()
async def news(ctx):
    await ctx.send('<https://criticalopsgame.com/news/>')


@bot.command()
async def maps(ctx):
    await ctx.send('<https://criticalopsgame.com/maps/>')


@bot.command()
async def influencer(ctx):
    await ctx.send('<https://criticalopsgame.com/influencer/>')


@bot.command()
async def coc(ctx):
    await ctx.send('<https://www.criticalopsgame.com/code-conduct/>')


@bot.command()
async def faq(ctx):
    await ctx.send('<https://critical-force.helpshift.com/a/critical-ops/>')



# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------



# Basic moderation commands

@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f' Banned {member.mention}')


@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')                                       # WHy would you split that IDIOT?

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
        return


@bot.command()
async def ping(ctx):
    '''
    check ping for the bot aka latency.
    '''
    latency = bot.latency
    await ctx.send('Ping = {0} ms'.format(round(bot.latency, 1)))

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Link to the official youtube command of critical ops


@bot.command()          
async def copsyt(ctx):
    await ctx.send('The offical C-ops youtube channel:')
    await ctx.send('<https://www.youtube.com/user/CriticalForceEnt>')
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------


#channel commands


@bot.command()
async def clear(ctx, amount=40000000):                                                #Don't you think that is too much?
    '''Clears the chat by 30 messages or more.'''
    await ctx.channel.purge(limit=amount)

@bot.command()
async def guildcount(ctx):
    """Bot Guild Count"""
    await ctx.send("**I'm in {} C-ops related servers!**".format(len(bot.guilds)))
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------



# Read the docs!

@bot.command()
async def commands(ctx):
    await ctx.send("You can find all commands at:")
    await ctx.send("<https://docs.google.com/document/d/1jsjsWy7wNyiuuVCXg95UxBIDznk6iqIgpffjC3W0iVs/edit?usp=sharing>")


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

# Communtiy support commands.


@bot.command()
async def crerror(ctx, member: discord.Member):
    await ctx.channel.purge(limit=2)
    await ctx.send("Critical errors are automatticly send to [D]evelopers. Restarting your game should make you able to play.")
    await ctx.send("If you want to help out contact the support like following:")
    await ctx.send("Open the game> Settings> General > contact support> Chose any topic > Choose not helpfull. > describe your issue in english. If you got an error code tell what happen before it.")
    await ctx.send(f' {member.mention}.')


@bot.command()
async def nadebug(ctx, member: discord.Member):
    await ctx.channel.purge(limit=2)
    await ctx.send(f' The nade bug is being fixed. Please check <#210339508204339200>s channel for furtur updates. {member.mention}')


@bot.command()
async def permban(ctx, member: discord.Member):
    await ctx.channel.purge(limit=2)
    await ctx.send(f' A permanent ban is issued when both the anti cheat and the developers confirm violation of the terms of service.')
    await ctx.send(f' Please read through them to find out what you did wrong at <https://criticalopsgame.com/terms>')
    await ctx.send(f' Under no circumstances are unbans issued due to confirmation of violation {member.mention}')


@bot.command()
async def lag(ctx, member: discord.Member):
    await ctx.channel.purge(limit=2)
    await ctx.send(f' If you are experiencing peformance issues goto: <https://critical-force.helpshift.com/a/critical-ops/?s=game-performance&f=why-is-my-game-lagging-or-crashing&l=en> {member.mention}')


@bot.command()
async def whenpass(ctx, member: discord.Member):
    await ctx.channel.purge(limit=2)
    await ctx.send(f' This channel is NOT meant for:')
    await ctx.send(f'- When update/pass/whatever comes; this is NOT a support issue. Move to <#210338479068938240> for that. ')
    await ctx.send(f'- Suggestions/feedback/complaining; send suggestions on Reddit and/or anything else to in-game support ')
    await ctx.send(f'- Reporting of any kind (hack, bug, and so on); read <#494053962618765312>')
    await ctx.send(f'- Sharing media; go to <#210339764862320641>')
    await ctx.send(f'- Begging for credits or anything else; just do not do this anywhere in this server')
    await ctx.send(f'- Discord related (nicknames, slowmode, whatever); move to <#210338479068938240> for that')
    await ctx.send(f'- Reloaded related: go to support of Reloaded.')
    await ctx.send(f'  ')
    await ctx.send(f'You may get warned and/or muted without warning if you ignore these rules. {member.mention}')
    time.sleep(10)
    await ctx.channel.purge(limit=11)





@bot.command()
async def beta(ctx,):
    await ctx.channel.purge(limit=1)
    await ctx.send("For new releases, we usually offer a limited-time beta, where players can participate in a beta test of an upcoming release giving you access to the upcoming content while giving us valuable information about the state of the build.")
    await ctx.send("For Android devices, the easiest way is to simply go to the Google Play store, head to the Critical Ops app page, and simply scroll to the bottom of the page and opt into the beta program.")
    await ctx.send("Alternatively, you can use this link:")
    await ctx.send("<https://play.google.com/apps/testing/com.criticalforceentertainment.criticalops>")
    await ctx.send("For Apple devices, we have a selection based process, where selected users can participate in testing using the Testflight program. Apply through this link:")
    await ctx.send("<https://testflight.apple.com/join/xoziEUBr>")


@bot.command()
async def bugrep(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    await ctx.send("You can try to file a bug support:  open the game > settings > help> chose any topic > not helpful > contact us > send a screenshot and provide as much detail as you can preferably in English.")
    await ctx.send(f'{member.mention}')


@bot.command()
async def whycopsrl(ctx, member: discord.Member,):
    await ctx.channel.purge(limit=1)
    await ctx.send(" It wasn't up to the devs to decide. NHN invested into the company and the goal was to have an Asian version of C-OPS, since current C-OPS is not a fit to the Asian market.")
    await ctx.send("Some countries have their own restrictions etc, which you need to follow and removing these features from the game would have not been cool for rest of the world. More info:")
    await ctx.send("<https://www.pocketgamer.biz/news/63892/critical-force-nhn-entertainment-partnership/>")
    await ctx.send("<https://critical-force.helpshift.com/a/critical-ops/?s=hot-topics&f=critical-ops-reloaded>")
    await ctx.send(f'{member.mention}')


@bot.command()
async def penalty(ctx,):
    await ctx.channel.purge(limit=1)
    await ctx.send("First penalty: 30 min suspension")
    await ctx.send("Second penalty: 1-day suspension")
    await ctx.send("Third penalty: 2-day suspension")
    await ctx.send("Fourth or more penalty: 7-day suspension")


@bot.command()
async def tapjoy(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    await ctx.send("Offers are managed by Tapjoy/ironSource and not by Critical Force.")
    await ctx.send("Abide by the Terms & Conditions of the offer.If you completed an offer and you're still not paid the reward, then report to Tapjoy or ironSource.")
    await ctx.send("Go to offer wall → Reward status → tap on offer → check estimate wait time.Wait until it's over, then there will be contact support button.")
    await ctx.send("Tapjoy:- <http://tapjoy.force.com/pkb_mobile#/>- <https://www.tapjoy.com/customer-support/>")
    await ctx.send("ironSource:- <http://www.ironsrc.com/contact/>")
    await ctx.send("Please review the FAQ article about this as well:- <https://critical-force.helpshift.com/a/critical-ops/?s=hot-topics&f=i-did-not-get-my-credits-for-completing-an-offer&p=all>")
    await ctx.send(f'{member.mention}')


@bot.command()
async def fbauth(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    await ctx.send("You can try the following workarounds, but make sure you know your Facebook login credentials before attempting them:")
    await ctx.send("Workaround 1: Facebook App → Account Settings → Settings & Privacy → Settings → Apps & Websites → Logged in with Facebook → Select Critical Ops → Remove → Open Critical Ops → Log in. ")
    await ctx.send("------------------------------------------------------------------------------------------------------------------------")
    await ctx.sendd("If this does not work:")
    await ctx.send("Workaround 2: On Android: delete the Critical Ops app cache and data on your device from the settings menu, under Apps category. On iOS: reinstall the Critical Ops app.")
    await ctx.send(f'Try this {member.mention}')



@bot.command()
async def fb1104(ctx, member : discord.Member):
    await ctx.channel.purge(limit=1)
    await ctx.send("Try the following:")
    await ctx.send("1. Uninstall the Facebook app from the device. Dont reinstall it back.  2. Connect your Facebook account on the browser (log in from there). 3. Go back to the game, try logging in then.")
    await ctx.send(f'^ {member.mention}')




  

# support-moderation-commands


@bot.command()
async def clutter(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    await ctx.send(f' Your message has been deleted to prevent clutter. Please move to <#210338479068938240>.{member.mention}')
    time.sleep(5)
    await ctx.channel.purge(limit=1)

@bot.command()
async def rulessup(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(" Ran into problems IN the game? Ask for support here! Read <#210339391070142464> <#210350469879562241> <#210339508204339200> <#449271903077662731> AND https://www.criticalopsgame.com/faq BEFORE asking here!")
    time.sleep(10)
    await ctx.channel.purge(limit=1)


@bot.command()
async def rules2(ctx, member: discord.Member,):
    await ctx.channel.purge(limit=2)
    await ctx.send(f'Read the rules of the channel. And move to <#210338479068938240> for that. {member.mention}')


@bot.command()
async def warn1(ctx, member: discord.Member,):
    await ctx.channel.purge(limit=2)
    await ctx.send(f'WARNING!')
    await ctx.send(f'You have recieved a warning. further continuation of these violations can result to moderation actions. {member.mention}')
    time.sleep(12)
    await ctx.channel.purge(limit=2)


@bot.command()
async def warn2(ctx, member: discord.Member,):
    await ctx.channel.purge(limit=2)
    await ctx.send("SECOND WARNING!")
    await ctx.send(f'This is your second warning {member.mention}! You have one more chance. Follow the rules.')
    time.sleep(5)
    await ctx.channel.purge(limit=2)


@bot.command()
async def warn3(ctx, member: discord.Member):
    await ctx.channel.purge(limit=2)
    await ctx.send(f'{member.mention} You failed to comply with the rules and will be muter/ kicked or banned.')


""" Features soon to come. """







































































bot.run(TOKEN)
