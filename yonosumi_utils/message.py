from asyncio import TimeoutError
from typing import Union

import discord
from discord.ext import commands

from yonosumi_utils.embed import YonosumiEmbed


class YonosumiMsg:

    @staticmethod
    async def waiting(ctx):
        return await ctx.send(f"{ctx.author.mention}->処理中です...")

    @staticmethod
    async def no_permission(ctx):
        return await ctx.send(f"{ctx.author.mention}->このコマンドを実行する権限がありません！")

    @staticmethod
    async def custom_waiting(ctx, *, arg: str):
        return await ctx.send(f"{ctx.author.mention}->{arg}です...")

    @staticmethod
    async def startup_process(ctx):
        return await ctx.send(f"{ctx.author.mention}->起動処理中です...再度お試しください...")

    @staticmethod
    async def question(bot: commands.Bot, main_object: Union[commands.Context, discord.Message], member: discord.Member, title: str) -> Union[dict, bool]:

        def check(m):
            return m.author == member and m.channel == main_object.channel
        question = await main_object.channel.send(content=title)

        try:
            msg = await bot.wait_for(
                'message',
                check=check,
                timeout=60.0
            )

        except TimeoutError:
            await question.edit(content=f"{member.mention}->入力待機時間内に応答がありませんでした！")
            return False

        return {
            'result': msg,
            'question': question
        }
