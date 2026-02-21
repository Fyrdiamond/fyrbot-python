from commands.command import Command

class Ping(Command):
    name = "ping"
    description = "Responds with Pong!"

    async def run(self, ctx, options=None):
        await self.ds_adapter.send_response(ctx, f"Pong! Options: {options}")
