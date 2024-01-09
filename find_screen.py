

import time
from pynput import mouse







print("Click on the top-left corner of the game window.")
print("Click on the bottom-right corner of the game window.")
print("Click on the position of the dinosaur.")



Click_list = []
def on_click(x, y, button, pressed):
    if pressed:
        print(f'Mouse Pressed at ({x}, {y}) with {button}')
        Click_list.append((x, y))

listener = mouse.Listener(on_click=on_click)

# Start the listener
listener.start()

try:
    # Your code here
    while len(Click_list) < 3:
        time.sleep(0.1)  # Adjust sleep duration as needed

    print("Reached 3 clicks. Stopping the listener.")

except KeyboardInterrupt:
    # Handle keyboard interrupt (Ctrl+C) gracefully
    pass
finally:
    # Stop the listener
    listener.stop()
    listener.join()


