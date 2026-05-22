import eel
import os
from queue import Queue
import traceback

class ChatBot:

    started = False
    userinputQueue = Queue()

    def isUserInput():
        return not ChatBot.userinputQueue.empty()

    def popUserInput():
        return ChatBot.userinputQueue.get()

    def close_callback(route, websockets):
        # if not websockets:
        #     print('Bye!')
        exit()

    @eel.expose
    def getUserInput(msg):
        ChatBot.userinputQueue.put(msg)
        print(msg)
    
    def close():
        ChatBot.started = False
    
    def addUserMsg(msg):
        eel.addUserMsg(msg)
    
    def addAppMsg(msg):
        eel.addAppMsg(msg)

    def start():
        path = os.path.dirname(os.path.abspath(__file__))
        eel.init(path + r'\web', allowed_extensions=['.js', '.html'])
        start_options = dict(
            host='localhost',
            port=27005,
            block=False,
            size=(350, 480),
            position=(10,100),
            disable_cache=True,
            close_callback=ChatBot.close_callback
        )
        try:
            try:
                eel.start('index.html', mode='chrome', **start_options)
            except Exception:
                print("Chrome launch failed. Falling back to the default browser.")
                traceback.print_exc()
                eel.start('index.html', mode='default', **start_options)

            ChatBot.started = True
            while ChatBot.started:
                try:
                    eel.sleep(10.0)
                except Exception:
                    break
        except Exception:
            print("Failed to start the Proton UI.")
            traceback.print_exc()
