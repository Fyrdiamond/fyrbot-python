class MessageHandler:
    def __init__(self):
        pass

    async def handle_message(self, message):
        content = message.content
        if not content.startswith("!"):
            return

        elif content.startswith("!ping"):
            await message.reply("Pong!")
