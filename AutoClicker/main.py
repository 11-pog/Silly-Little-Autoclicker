import mouse
import keyboard
import asyncio


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







if __name__ == "__main__":
    auto_clicker = SimpleAutoClicker()
    auto_clicker.begin()