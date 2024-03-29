import time
from pynput import mouse
def findscreen():
    Topleft = None
    bottomright = None
    dinosaur_viewbox_Topleft = None
    dinosaur_viewbox_bottomright = None

    Click_list = []
    def on_click(x, y, button, pressed):
        if pressed:
            print(f'Mouse Pressed at ({x}, {y}) with {button}')
            Click_list.append((x, y))

    listener = mouse.Listener(on_click=on_click)

    listener.start()

    try:
        
        while len(Click_list) < 4:
            if len(Click_list) == 0:
                print("Click on the top-left corner of the game window.")
            elif len(Click_list) == 1:
                print("Click on the bottom-right corner of the game window.")
            elif len(Click_list) == 2:
                print("Click on the top-left corner of the dinosaur.")
            elif len(Click_list) == 3:
                print("Click on the bottom-right corner of the dinosaur.")
            time.sleep(0.1)
        print("Reached 4 clicks")
    except KeyboardInterrupt:
        pass
    finally:
        
        Topleft = Click_list[0]
        bottomright = Click_list[1]
        dinosaur_viewbox_Topleft = Click_list[2]
        dinosaur_viewbox_bottomright = Click_list[3]
        listener.stop()
        listener.join()
        return Topleft, bottomright,dinosaur_viewbox_Topleft,dinosaur_viewbox_bottomright

