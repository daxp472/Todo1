import subprocess
import time
import os

def restart_bot():
    while True:
        try:
            # Get the current directory
            current_directory = os.path.dirname(os.path.abspath(file))
            # Replace 'your_bot_script.py' with the name of your bot script
            subprocess.run(['python3', os.path.join(current_directory, 'sasuke.py')], check=True)
        except subprocess.CalledProcessError as e:
            print(f'Bot crashed with error: {e}. Restarting...')
            time.sleep(5)  # Wait for 5 seconds before restarting

if name == "main":
    restart_bot()