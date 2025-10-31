from typing import Union
from abstract import Action


class MacroSequence:
    __slots__ = ['actions']
    
    def __init__(self, actions: list[Union["Action", "MacroSequence"]]):
        self.actions = actions