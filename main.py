from __future__ import division
from email import message
import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print('Start {0.user}'.format(client))

@client.event
async def on_message(message):


    if message.author == client.user:
        return

    if message.content.startswith('$help'):
        await message.channel.send('Hello, this is the CalculationBot, written by Sven Lobbes!')
        await message.channel.send('This bot supports these arithmetic operations: +, -, *, /')
        await message.channel.send('Examples:')
        await message.channel.send('$c 3+3-2')
        await message.channel.send('$c 4/2')
        await message.channel.send('$c 2*(3+6)')
        await message.channel.send('Negative Numbers are also available!')
        await message.channel.send('Example:')
        await message.channel.send('$c -5+1')
        await message.channel.send('For all calculations use "$c" with a space')
        await message.channel.send('Thank you for using my first Discord bot and have fun :)')

    if message.content.startswith('$c'): ####CALCULATOR ################
        InputStr = message.content
        SyntaxError = 'Your Command contains Syntax Error'
        
        ###If Syntax is good then calculation
        if InputStr[2] == ' ': #Syntax == good
            plus = '+'  ###Check if there are too many operators 
            minus = '-'
            times = '*'
            division = '/'

            k = len(InputStr)
            i = 3
            t = 0

            while i != k:
               # if InputStr[i] and InputStr[i + 1] == plus or minus or times or division: 
                #    t = 1   # t is a check var

                i = i + 1 

            if t == 0: # Syntax Still good! 
                i = 3
                CalcString = ''

                while i != k:
                    CalcString = CalcString + InputStr[i]
                    i = i + 1

                RESULT = eval(CalcString)

                await message.channel.send(RESULT)

            else: #Syntax bad 
                await message.channel.send(SyntaxError)


        else: #Syntax == bad
            await message.channel.send(SyntaxError)

client.run('') #INSERT TOKEN OF BOT




