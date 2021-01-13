import discord
import re
import math

TOKEN = "Nzk0NjI4ODM4OTY4NjU1ODgy.X-9lxg.nkF_k8LzuVU_64MbpF0tCiPjr9c"

#反応
fastHant = "/"
client = discord.Client()

@client.event
async def on_ready():

    print("The bot has logged in")
    game = discord.Game("https://prcn-dam.fin4le.com")
    await client.change_presence(activity=game)

@client.event
async def on_message(message):

    try:

        if message.author.bot:
            return

        print(message.author.name + '#' + message.author.discriminator + ' : ' + message.content)

        if message.content == fastHant + 'help':
            await message.channel.send("[/moti ボスの残HP 実際のダメージ]\nを入力することで、持ち越し時間を計算することができます。\n例として[/moti 500 900]を入力すると\nボスの残HP500、与えたダメージ900となり、持ち越し時間60秒が計算結果として吐き出されます。\n\n正しく動作しない場合は下記をご利用ください。\nhttps://prcn-dam.fin4le.com")
            return

        if message.content.startswith(fastHant + 'moti'):
            gtMsg = re.split(" |　",message.content)

            if len(gtMsg) != 3:
                await message.channel.send("入力が正しくありません。")
                return

            itMsg1 = int(gtMsg[1])
            itMsg2 = int(gtMsg[2])

            if itMsg1 >= itMsg2:
                await message.channel.send("持ち越し時間はありません。")
                return

            calcNo1 = itMsg2 - itMsg1
            calcNo2 = math.ceil(calcNo1 / itMsg2 * 90 + 20)

            if calcNo2 > 90:
                calcNo2 = 90;

            await message.channel.send("持ち越し時間は " + str(calcNo2) + " 秒です。")
            return

    except ValueError:
        await message.channel.send("入力が正しくありません。")
        return

client.run(TOKEN)
