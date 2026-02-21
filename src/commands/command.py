from abc import ABC, abstractmethod

class Command(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    async def run(self, ctx, options=None):
        pass

    def __init__(self, adapter):
        self.ds_adapter = adapter
