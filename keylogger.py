import win32console
import win32gui
import win32clipboard
import pythoncom
import pyWinhook as pyHook


class Keylogger:
    def __init__(self, model_call):
        self.t = ""

        self.keep_running = True
        self.ctrl_pressed = False
        self.shift_pressed = False

        self.model_call = model_call

    def start(self):
        hook = pyHook.HookManager()
        hook.KeyDown = self.OnKeyboardEvent
        hook.HookKeyboard()

        while self.keep_running:
            # Detect pause after typing
            if self.t != "":
                self.model_call(self.t)
                self.t = ""
            pythoncom.PumpWaitingMessages()

    def hide(self):
        win = win32console.GetConsoleWindow()
        win32gui.ShowWindow(win, 0)

    def OnKeyboardEvent(self, event):
        # check quit
        if self.check_combination(event, 81):
            self.keep_running = False

        # check model call
        if self.check_combination(event, 76):
            win32clipboard.OpenClipboard()
            self.t = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

        return True
    
    def check_combination(self, event, key):
        """
        Check if ctrl + shift + key is pressed
        """

        if event.KeyID in (162, 163):
            self.ctrl_pressed = event.MessageName == 'key down'
        elif event.KeyID in (160, 161):
            self.shift_pressed = event.MessageName == 'key down'
        
        if self.ctrl_pressed and self.shift_pressed and event.KeyID == key:
            self.ctrl_pressed = False
            self.shift_pressed = False
            return True
    
        return False
