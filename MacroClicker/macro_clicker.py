from typing import List
import keyboard
import asyncio


from base_actions import *
from abstract import Action
from MacroClicker.commands.structure import MacroSequence


class MacroClicker():
    def __init__(self, *, toggle_key = 'F8', tempo = 0.1, actions: List[Action | MacroSequence], loop=None, restart_on_toggle = True):
        self.toggle_key = toggle_key
        self.executing = False
        
        self.actions = self._decompose(actions)
        
        self.tempo = tempo
        self.current_step = 0
        
        self.restart_on_toggle = restart_on_toggle
        
        print([str(a) for a in self.actions])
        
        self.loop = loop or asyncio.new_event_loop()
    
    
    def _decompose(self, actions):
        flat_list = []
        for act in actions:
            if isinstance(act, MacroSequence):
                flat_list.extend(self._decompose(act.actions))
            else:
                flat_list.append(act)
        return flat_list
    
    
    def begin(self):
        keyboard.on_press_key(self.toggle_key, self.on_keyboard_press)
        print("Started")
        self.loop.run_forever()
    
    
    def on_keyboard_press(self, event):
        print("Toggeld")
        asyncio.run_coroutine_threadsafe(self.toggle_clicker(), self.loop)
    
    
    async def toggle_clicker(self):
        self.executing = not self.executing
        
        print(f"Now executing: {self.executing}")
        
        if self.executing:
            await self.click_loop()
    
    
    def get_next_step(self):
        return (self.current_step + 1) % len(self.actions)
    
    
    def peek(self):
        index = self.get_next_step()
        return self.actions[index]
    
    
    async def click_loop(self):
        while self.executing:
            action = self.actions[self.current_step]
            
            await action.act(self)
            
            await asyncio.sleep(self.tempo)
            
            if not self.executing:
                break
            
            self.current_step = self.get_next_step()
        
        if self.restart_on_toggle:
            self.current_step = 0