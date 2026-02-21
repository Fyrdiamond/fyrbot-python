from dotenv import load_dotenv
import os
from discord.discord_adapter import DiscordAdapter
from commands.role import Role
from commands.ping import Ping
from command_register import CommandRegister
from message_handler import MessageHandler

if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("DISCORD_BOT_TOKEN")

    message_handler = MessageHandler()

    adapter = DiscordAdapter(token, message_handler)

    command_register = CommandRegister(adapter)

    for command in [Role, Ping]:
        command_instance = command(adapter)
        adapter.register_command(command_instance)

    adapter.run()
