from macro_clicker import MacroClicker

from commands.mouse import *
from commands.keyboard import *
from commands.general import *


crouch_time = .01

actions = [
    KeyboardPress("ctrl"),
    #Rest(crouch_time),
    KeyboardRelease("ctrl"),
    #Rest(crouch_time)
]


macro = MacroClicker(
    toggle_key='F8',
    tempo=0.01,
    actions=actions
)
macro.begin()