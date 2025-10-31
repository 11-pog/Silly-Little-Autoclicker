import mouse
import keyboard


class _MouseMixin:
    async def press(self, button):
        mouse.press(button)
    
    async def release(self, button):
        mouse.release(button)
    
    async def tap(self, button):
        mouse.click(button)


class _KeyboardMixin:
    async def press(self, button):
        keyboard.press(button)
    
    async def release(self, button):
        keyboard.release(button)
    
    async def tap(self, button):
        keyboard.press_and_release(button)