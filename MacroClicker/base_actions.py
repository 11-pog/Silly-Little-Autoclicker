from abstract import *
import asyncio


class Tap(Action, Pressables):
    __slots__ = ['key']
    
    def __init__(self, key):
        self.key = key
    
    async def act(self):
        await self.tap(self.key)


class Hold(Action, Pressables):
    __slots__ = ['hold', 'key']
    
    def __init__(self, key, time):
        self.time = time
        self.key = key
    
    async def act(self):
        await self.hold(self.key, self.time)


class Press(Action, Pressables):
    __slots__ = ['key']
    
    def __init__(self, key):
        self.key = key
    
    async def act(self):
        await self.tap(self.key)


class Release(Action, Pressables):
    __slots__ = ['key']
    
    def __init__(self, key):
        self.key = key
    
    async def act(self):
        await self.tap(self.key)