import discord
from discord.commands import Option

class DiscordAdapter:
    def __init__(self, token, message_handler):
        self.token = token
        self.message_handler = message_handler
        self.bot = discord.Bot(intents=discord.Intents.all())

        @self.bot.event
        async def on_ready():
            print(f'Logged in as {self.bot.user}')

        @self.bot.event
        async def on_message(message):
            if message.author == self.bot.user:
                return

            if message.content.startswith('!'):
                await self.message_handler.handle_message(message)

    def register_command(self, command):
        async def wrapper(ctx, options=Option(str, description="command options", required=False)):
            await command.run(ctx, options)

        self.bot.slash_command(
            name=command.name,
            description=command.description
        )(wrapper)

    def run(self):
        self.bot.run(self.token)

    async def send_message(self, channel_id, content):
        channel = self.bot.get_channel(channel_id)
        if channel:
            await channel.send(content)

    async def reply_to_message(self, message, content):
        await message.reply(content)

    async def send_response(self, ctx, content):
        await ctx.respond(content)

    async def send_ephemeral_response(self, ctx, content):
        await ctx.respond(content, ephemeral=True)
