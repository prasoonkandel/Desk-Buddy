import pyautogui
import time

print("Starting... Press Ctrl+C to stop.")

try:
    while True:
        pyautogui.press('e')  # Presses the 'e' key
        print("Pressed 'e'")
        time.sleep(15)  # Wait for 15 seconds (5 minutes)
except KeyboardInterrupt:
    print("\nStopped by user.")
