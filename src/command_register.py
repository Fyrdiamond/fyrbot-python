class CommandRegister:
    def __init__(self, adapter):
        self.adapter = adapter

    def register_command(self, command):
        self.adapter.register_command(command)
