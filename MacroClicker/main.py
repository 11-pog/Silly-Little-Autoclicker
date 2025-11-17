from macro_clicker import MacroClicker

from commands.mouse import *
from commands.keyboard import *
from commands.general import *


actions = [
    KeyboardPress("ctrl"),
    #Rest(.01),
    KeyboardRelease("ctrl"),
    #Rest(.01)
]


macro = MacroClicker(
    toggle_key='F8',
    tempo=0.01,
    actions=actions
)
macro.begin()