from abstract import *


class Tap(Pressables):
    __slots__ = ['key']
    
    def __init__(self, key: str):
        self.key = key
    
    async def act(self, context):
        await self.tap(self.key)


class Hold(Pressables):
    __slots__ = ['time', 'key']
    
    def __init__(self, key: str, time: float):
        self.time = time
        self.key = key
    
    async def act(self, context):
        await self.hold(self.key, self.time)


class Press(Pressables):
    __slots__ = ['key']
    
    def __init__(self, key: str):
        self.key = key
    
    async def act(self, context):
        await self.press(self.key)


class Release(Pressables):
    __slots__ = ['key']
    
    def __init__(self, key: str):
        self.key = key
    
    async def act(self, context):
        await self.release(self.key)