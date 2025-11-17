# Structure commands

from typing import Union
from abstract import Action

# simple structure

class MacroSequence:
    __slots__ = ['actions']
    
    def __init__(self, actions: list[Union["Action", "MacroSequence"]]):
        self.actions = actions


class RepeatSequence(MacroSequence):
    def __init__(self, actions: list[Union["Action", "MacroSequence"]], repeat: int):
        actions = actions * repeat
        
        super().__init__(actions)


# as for the current implementation of MacroSequence (special command not derived from Actions)
# any MacroSequence is only able to be achieved at compile time and cannot change dynamically

# this is because some commands (Rest) can peek at the next Action
# and implementing this with dynamic changing list of Actions with Macro n shit would be hell (someday ill do it)
# so as for now it just decomposes the macros into the Action List