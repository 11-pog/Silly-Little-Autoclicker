from abc import ABC, abstractmethod
import asyncio

class Action(ABC):
    @abstractmethod
    async def press(self, button): ...
    
    @abstractmethod
    async def release(self, button): ...
    
    @abstractmethod
    async def tap(self, button): ...
    
    
    async def hold(self, button, time):
        await self.press(button)
        await asyncio.sleep(time)
        await self.release(button)
    
    async def multi_press(self, buttons):
        for button in buttons:
            await self.press(button)
    
    async def multi_release(self, buttons):
        for button in buttons:
            await self.release(button)
    
    async def multi_hold(self, buttons, time):
        await self.multi_press(buttons)
        await asyncio.sleep(time)
        await self.multi_release(buttons)
    
    async def multi_tap(self, buttons):
        for button in buttons:
            await self.tap(button)
    
    
    @abstractmethod
    async def act(self): ...