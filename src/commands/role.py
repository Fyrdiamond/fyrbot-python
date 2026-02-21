from commands.command import Command
from database.database_adapter import DatabaseAdapter

from logic.operators import Eq, Gt, Lt, And, Or

# store role and user associations in a many to many relationship


class Role(Command):
    name = "role"
    description = "Manage roles and their members"

    async def run(self, ctx, options=None):
        options = options.split() if options else []
        if not options:
            await self.ds_adapter.send_response(
                ctx, "Please provide a subcommand (add/remove/list)"
            )
            return
        await self.ds_adapter.send_response(
            ctx, f"Role command executed with options: {options}"
        )

    async def add_role(self, role_name):
        # test if role exists
        self.db_adapter.select_from_where("id", "roles", Eq("Name", role_name))
        result = self.db_adapter.get_one()
        if result:
            return False

        # if it doesn't, create a new role entry with a name and unique id
        self.db_adapter.insert("roles", {"name": role_name})
        return True
