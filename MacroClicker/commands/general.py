from abstract import Action
import asyncio

class Rest(Action):
    __slots__ = ['seconds']
    
    def __init__(self, seconds: float):
        self.seconds = seconds
    
    async def act(self, context):
        next_action = context.peek() # method already accounts for end of list btw
        
        if isinstance(next_action, Rest):
            compensation = context.tempo
        else:
            compensation = context.tempo * 2
        
        duration = max(0, self.seconds - compensation)
        
        await asyncio.sleep(duration)