from abstract import *
import asyncio


class Tap(Action):
    __slots__ = ['key']
    
    def __init__(self, key):
        self.key = key
    
    async def act(self):
        await self.tap(self.key)


class Hold(Action):
    __slots__ = ['hold', 'key']
    
    def __init__(self, key, time):
        self.time = time
        self.key = key
    
    async def act(self):
        await self.hold(self.key, self.time)


class Press(Action):
    __slots__ = ['key']
    
    def __init__(self, key):
        self.key = key
    
    async def act(self):
        await self.tap(self.key)


class Release(Action):
    __slots__ = ['key']
    
    def __init__(self, key):
        self.key = key
    
    async def act(self):
        await self.tap(self.key)


class Rest(Action):
    __slots__ = ['time']
    
    def __init__(self, time):
        self.time = time
    
    async def act(self):
        await asyncio.sleep(self.time)