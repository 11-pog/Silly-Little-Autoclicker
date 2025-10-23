from typing import List
import mouse
import keyboard
import asyncio

from pydantic import InstanceOf


class SimpleAutoClicker:
    def __init__(self, delay = 0.01, trigger_key = 'F8', execute_key = "click", *, loop=None):
        self.delay = delay
        self.execute_key = execute_key
        self.trigger_key = trigger_key
        
        self.clicking = False
        self.click = self.get_corresponding_key_function(execute_key)
        
        self.loop = loop or asyncio.new_event_loop()
    
    
    
    def begin(self):
        keyboard.on_press_key(self.trigger_key, self.on_keyboard_press)
        print("Started")
        self.loop.run_forever()
    
    
    def get_corresponding_key_function(self, key):
        match key:
            case 'lclick' | 'click':
                return lambda: mouse.click(mouse.LEFT)
            
            case 'rclick':
                return lambda: mouse.click(mouse.RIGHT)
            
            case 'mclick':
                return lambda: mouse.click(mouse.MIDDLE)
            
            case _:
                return lambda: keyboard.press_and_release(self.execute_key)
    
    
    def on_keyboard_press(self, event):
        print("Toggeld")
        asyncio.run_coroutine_threadsafe(self.toggle_clicker(), self.loop)
    
    
    async def toggle_clicker(self):
        self.clicking = not self.clicking
        
        print(f"Now clicking: {self.clicking}")
        
        if self.clicking:
            await self.click_loop()
    
    
    async def click_loop(self):
        while self.clicking:
            self.click()
            await asyncio.sleep(self.delay)



class MacroClicker():
    class Tap:
        __slots__ = ['key']
        
        def __init__(self, key):
            self.key = key
    
    class Hold(Tap):
        __slots__ = ['hold', 'key']
        
        def __init__(self, key, hold = 0):
            self.hold = hold
            self.key = key
    
    class Rest:
        __slots__ = ['time']
        
        def __init__(self, time):
            self.time = time
    
    
    def __init__(self, *, trigger_key = 'F8', tempo = 0.1, execution_map: List[Hold | Rest], loop=None):
        self.trigger_key = trigger_key
        self.clicking = False
        
        self.tempo = tempo
        self.function_map = self.get_function_map(execution_map)
        
        for key in execution_map:
            self.execution_map[key] = [execution_map[key],  None]
            self.execution_map[key][1] = self.get_corresponding_key_function(key)
        
        print(self.execution_map)
        
        self.loop = loop or asyncio.new_event_loop()
    
    
    
    def begin(self):
        keyboard.on_press_key(self.trigger_key, self.on_keyboard_press)
        print("Started")
        self.loop.run_forever()
    
    
    def get_function_map(self, execution_map):
        function_map = []
        
        for key in execution_map:
            match key:
                case MacroClicker.Rest():
                    function_map.append(lambda: asyncio.sleep(key.time))
        
        return function_map
    
    
    def get_corresponding_key_function(self, key, mode = "click"):
        """
        press = only presses
        
        release = only releases
        
        click = presses and releases
        """
        match key:
            case 'left' | 'right' | 'middle':
                return lambda: mouse.click(key)
            
            case None:
                return None
            
            case _:
                return lambda: keyboard.press_and_release(self.execution_map)
    
    
    
    def on_keyboard_press(self, event):
        print("Toggeld")
        asyncio.run_coroutine_threadsafe(self.toggle_clicker(), self.loop)
    
    async def toggle_clicker(self):
        self.clicking = not self.clicking
        
        print(f"Now clicking: {self.clicking}")
        
        if self.clicking:
            for key in self.execution_map:
                pass
    
    async def click_loop(self):
        while self.clicking:
            self.click()
            await asyncio.sleep(self.delay)



if __name__ == "__main__":
    auto_clicker = MacroClicker(execution_map={
        'w': [0, 1],
        's': [0, 1]
    })
    auto_clicker.begin()