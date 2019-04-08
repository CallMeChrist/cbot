import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
import asyncio
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get
import ctx


bot=commands.Bot(command_prefix='$')
see='328062252420694026'
evo='373723169091092480'
start=time.time()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('--------------------')
	await client.change_presence(game=discord.Game(name='With your dicks 🍆 | $help',type=0))
	await client.change_presence(game=discord.Game(name='Bitch Lasagna 🎶 | $help',type=1))
	
@client.command(pass_context=True)
async def info():
	embed=discord.Embed(title='Call Me Christ',description='Bot Created By <@328062252420694026>')
	embed.add_field(name='Created by Ꮯʜʀɪsᴛ with love <3',value='Note : `Some command may not work`',inline=False)
	
	await client.say(embed=embed)
	
@client.command(pass_context=True)
async def invite():
	await client.say("`Sorry this bot is not public yet`")	
			
@client.command(pass_context=True)
async def ping(ctx):
    t = await client.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await client.edit_message(t, new_content='Pong!`{}ms`'.format(int(ms)))
    	
@client.command(pass_context=True)
async def avatar(ctx,member:discord.Member):
	await client.say("{}".format(member.avatar_url))

@client.command(pass_context=True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await client.delete_message(ctx.message)
    return await client.say(mesg)
	
@client.command(pass_context=True)
async def cat():
	possible_responses=['https://tenor.com/view/ready-cat-wiggle-gif-4625114','https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif','https://tenor.com/view/cats-catporn-kitties-lick-gif-5238122','https://tenor.com/view/cat-sadface-please-gif-10136432','https://tenor.com/view/smiling-cat-creepy-cat-cat-zoom-kitty-gif-12199043','https://tenor.com/view/cat-toilet-potty-poo-gif-3696457']
	await client.say(random.choice(possible_responses))
	
@client.command(pass_context=True)
async def dog():
	possible_responses=['https://tenor.com/view/scary-angry-pissed-mad-bro-gif-10066144','https://tenor.com/view/husky-pun-dog-meme-gif-9639526','https://tenor.com/view/dog-sad-funny-animals-funny-turning-gif-10670068','https://tenor.com/view/dog-funny-funny-dog-dog-walk-gif-5003534','https://tenor.com/view/dog-eyebrow-funny-gif-13185653']
	await client.say(random.choice(possible_responses))
	
@client.command(pass_context=True)
async def girl():
	possible_responses=['https://tenor.com/view/sex-friends-with-benefits-mila-kunis-gif-4914830','https://tenor.com/view/bikini-girl-gif-10539751','https://tenor.com/view/jennie-blackpink-kpop-sad-gif-9473686','https://tenor.com/view/fitness-girl-mikebarreras-mike-tyson-gif-12636561','https://tenor.com/view/sexy-bath-time-fabulous-gif-4743104']
	await client.say(random.choice(possible_responses))
	
@client.command()
async def render(type):
    await client.say('https://growtopiagame.com/worlds/'f'{type}.png')
    
@client.command(pass_context=True)
async def number(ctx):
	possible_responses=['1','2','3','4','5','6','7','8','9','10']
	await client.say(random.choice(possible_responses))
	
@client.command(pass_context=True)
async def text(ctx):
	possible_responses=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	await client.say(random.choice(possible_responses))
	
@client.command(pass_context=True)
async def up(ctx):
	now=time.time()
	sec=int(now-start)
	mins=int(sec//60)
	await client.say(f"*Bot is online `{sec}`'s ago!*")
	
@client.command(pass_context=True)
async def play():
	await client.say("`Sorry this command is disabled for now.`")
	
@client.command(pass_context=True)
async def queue():
	await client.say("`Sorry this command is disabled for now.`'")
	
@client.command(pass_context=True)
async def nowplay():
	await client.say("`Sorry this command is disabled for now.`")
	
@client.command(pass_context=True)
async def remove():
	await client.say("`Sorry this command is disabled for now.`")
	
@client.command(pass_context=True)
async def pause():
	await client.say("`Sorry this command is disabled for now.`")
	
@client.command(pass_context=True)
async def resume():
	await client.say("`Sorry this command is disabled for now.`")
	
@client.command(pass_context=True)
async def leave():
	await client.say("`Sorry this command is disabled for now.`")
	
@client.command(pass_context=True)
async def prefix(ctx,type:int):
	if ctx.message.author.id==(see):
		await client.change_prefix(type=type)
	else:
			await client.say("***You don't have permission to use this command!***")
	
@client.command(pass_context=True)
async def purge(ctx,num:int):
	if ctx.message.author.id==(see) or ctx.message.author.id==(evo):
		await client.delete_message(ctx.message)
		return await client.purge_from(ctx.message.channel,limit=num)
		return await client.say(f'*Deleted `{num}` messages!*')
	else:
			await client.say("***You don't have permission to use this command!***")
			
@client.command(pass_context=True)
async def presence(ctx,text:str,type:int):
	if ctx.message.author.id==(see):
		await client.change_presence(game=discord.Game(name=text,type=type))
	else:
		await client.say("***You don't have permission to use this command")
		
@client.command(pass_context=True)
async def p(ctx):
	if ctx.message.author.id==(see):
		await client.say(':white_check_mark:')
	time.sleep(0)
	for i in range(0,1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
	    	await client.change_presence(game=discord.Game(name='Bitch Lasagna 🎶 | $help',type=1))
    		await client.change_presence(game=discord.Game(name='With Your Dicks 🍆 | $help',type=0))
    		await client.change_presence(game=discord.Game(name='$help for commands',type=0))
		
@client.command()
async def support():
	embed=discord.Embed(title='Support Server',description='-------------------------------------------')
	embed.add_field(name='Join this server if you have question :',value=('<https://discord.gg/Zpzd34X>'))
	
	await client.say(embed=embed)
    
@client.command(pass_context=True)
async def warn(ctx,target:discord.Member):
	if ctx.message.author.id==(see):
          await client.send_message(target,'***You have been warned !***')
          await client.say(f':white_check_mark: *User has been warned!*')
	else:
			await client.say("***You don't have permission to use this command!***")
			
@client.command(pass_context=True)
async def setnick(ctx):
	if ctx.message.author.id==(see):
		await client.say('`Sorry this command is disabled for now.`')
	else:
			await client.say("***You don't have permission to use this command!***")
          
@client.command(pass_context=True)
async def addrole(ctx,target:discord.Member):
	if ctx.message.author.id==(see):
		
		role=discord.utils.get(ctx.message.server.roles)
		await client.add_roles(target,roles)
		await client.say(':white_check_mark: `added role to user!`')
		
@client.command(pass_context=True)
async def removerole(ctx,target:discord.Member,):
	if ctx.message.author.id==(see):
		
		role=discord.utils.get(ctx.message.server.roles)
		await client.remove_roles(target,role)
		await client.say(':white_check_mark: `removed role from user!`')
          
@client.command(pass_context=True)
async def mute(ctx,target:discord.Member):
	if ctx.message.author.id==(see) or ctx.message.author.id==(evo):
		
		role=discord.utils.get(ctx.message.server.roles,name='Muted')
		
		await client.add_roles(target,role)
		await client.say(':white_check_mark: ***User has been muted***')
	else:
			await client.say("***You don't have permission to use this command!***")
		
@client.command(pass_context=True)
async def unmute(ctx,target:discord.Member):
	if ctx.message.author.id==(see) or ctx.message.author.id==(evo):
		
		role=discord.utils.get(ctx.message.server.roles,name='Muted')
		
		await client.remove_roles(target,role)
		await client.say(':white_check_mark: ***User is unmuted***')
	else:
			await client.say("***You don't have permission to use this command!***")
		
@client.command(pass_context=True)
async def kick(ctx,target:discord.Member):
	if ctx.message.author.id==(see):
         await client.kick(target)
         await client.say(':white_check_mark: ***User has been kicked!***')
	else:
			await client.say("***You don't have permission to use this command!***")

@client.command(pass_context=True)
async def ban(ctx,target:discord.Member):
	if ctx.message.author.id==(see) or ctx.message.author.id==(evo):
         await client.ban(target)
         await client.say(':white_check_mark: ***User has been banned!***')
	else:
			await client.say("***You don't have permission to use this command!***")
			
@client.command(pass_context=True)
async def unban(ctx,target:discord.Member):
	if ctx.message.author.id==(see):
         await client.remove_ban(target)
         await client.say(':white_check_mark: ***User is unbanned!***')
	else:
			await client.say("***You don't have permission to use this command!***")
			
client.remove_command('help')
	
@client.command()
async def help():
	embed=discord.Embed(title="Call Me Christ", description="Bot prefix is `$`                                                          Note : `Some command may not work`                   List of command :")
	embed.add_field(name='Help',value='Show help command list `$help`',inline=False)
	embed.add_field(name='Fun',value='Show fun command list `$fun`',inline=False)
	embed.add_field(name='Music',value='Show music command list `$music`',inline=False)
	embed.add_field(name='Utility',value='Show utility command list `$utility`',inline=False)
	embed.add_field(name='Role',value='Show role command list `$role`',inline=False)
	embed.add_field(name='Moderation',value='Show moderation command list `$moderation`',inline=False)

	await client.say(embed=embed)
	
@client.command()
async def fun():
	embed=discord.Embed(title='Fun',description='Fun command list :')
	embed.add_field(name='$ping',value='Bot will answer `Pong!`.',inline=False)
	embed.add_field(name='$avatar',value='`Give user avatar`',inline=False)
	embed.add_field(name='$say',value='`Bot will repeat what you say`',inline=False)
	embed.add_field(name='$cat',value='`Bot give cat picture/gif`',inline=False)
	embed.add_field(name='$dog',value='`Bot give dog picture/gif`',inline=False)
	embed.add_field(name='$girl',value='`Bot give sexy girl picture/gif`',inline=False)
	embed.add_field(name='$number',value='Show random number `1-10`',inline=False)
	embed.add_field(name='$text',value='Show random text `A-Z`',inline=False)
	
	await client.say(embed=embed)
	
@client.command()
async def music():
	embed=discord.Embed(title='Music',description='Music command list :')
	embed.add_field(name='$play',value='`Play a music use link or music name`',inline=False)
	embed.add_field(name='$queue',value='`Shoq music queue`',inline=False)
	embed.add_field(name='$nowplay',value='`Show current played music`',inline=False)
	embed.add_field(name='$remove',value='`Remove music from queue`',inline=False)
	embed.add_field(name='$pause',value='`Bot will pause current music`',inline=False)
	embed.add_field(name='$resume',value='`Bot will resume current music`',inline=False)
	embed.add_field(name='$leave',value='`Bot will leave current voice channel`',inline=False)
	
	await client.say(embed=embed)
	
@client.command()
async def utility():
	embed=discord.Embed(title='Utility',description='Utility command list :')
	embed.add_field(name='$up',value='`Show bot online status`',inline=False)
	embed.add_field(name='$userinfo',value='Get info about user `$userinfo <user>`',inline=False)
	embed.add_field(name='$purge',value='Clear user message `$purge <value>`',inline=False)
	
	await client.say(embed=embed)
	
@client.command()
async def role():
	embed=discord.Embed(title='Role',description='Role command list :')
	embed.add_field(name='$setnick',value='Change user nickname `$setnick <user> <name>`',inline=False)
	embed.add_field(name='$addrole',value='Add role to user `$addrole <user> <role>`',inline=False)
	embed.add_field(name='$removerole',value='Remove role from user `$removerole <user> <role>`',inline=False)
	
	await client.say(embed=embed)
	
@client.command()
async def moderation():
	embed=discord.Embed(title='Moderation',description='Moderation command list')
	embed.add_field(name='$prefix',value='Change bot prefix `$prefix <new prefix>`',inline=False)
	embed.add_field(name='$warn',value='Warn a user `$warn <user>`',inline=False)
	embed.add_field(name='$mute',value='Mute a user `$mute <user>`',inline=False)
	embed.add_field(name='$unmute',value='Unmute a user `$unmute <user>`',inline=False)
	embed.add_field(name='$kick',value='kick a user from this server `$kick <user>`',inline=False)
	embed.add_field(name='$ban',value='Ban a user from this server `$ban <user>`',inline=False)
	embed.add_field(name='$unban',value='Unban a user from this server `$unban <user>`',inline=False)

	await client.say(embed=embed)
	
@client.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    await client.say("User name is: `{}`".format(user.name))
    await client.say("User ID is: `{}`".format(user.id))
    await client.say("User status is: `{}`".format(user.status))
    await client.say("User highest role is: `{}`".format(user.top_role))
    await client.say("User joined at: `{}`".format(user.joined_at))















client.run(str(os.environ.get('TOKEN')))
