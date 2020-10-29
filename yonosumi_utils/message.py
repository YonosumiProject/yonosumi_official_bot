import discord
from discord.ext import commands
from yonosumi_utils.embed import YonosumiEmbed
from asyncio import TimeoutError

class YonosumiMsg:
    
    @staticmethod
    async def waiting(ctx):
        return await ctx.send(f"{ctx.author.mention}->処理中です...")
    
    @staticmethod
    async def no_permission(ctx):
        return await ctx.send(f"{ctx.author.mention}->このコマンドを実行する権限がありません！")

    @staticmethod
    async def custom_waiting(ctx, *, arg :str):
        return await ctx.send(f"{ctx.author.mention}->{arg}です...")

    @staticmethod
    async def startup_process(ctx):
        return await ctx.send(f"{ctx.author.mention}->起動処理中です...再度お試しください...")

    @staticmethod
    async def question(bot :commands.Bot, ctx :commands.Context, title :str) -> discord.Message:
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        question = await ctx.send(content = title)
        try:
            msg = await bot.wait_for(
                'message',
                check=check,
                timeout=60.0
                )
        except TimeoutError:
            await question.edit(content=f"{ctx.author.mention}->入力待機時間内に応答がありませんでした！")
            return False
        return msg
