import json
import time
import pyautogui
import keyboard
import webbrowser

# Load the usernames from the JSON file
with open('../igsource/to_unfollow.json', 'r') as f:
    usernames = json.load(f)

# Settings
delay_between_actions = 1  # seconds
unfollow_confirmation_wait = 3  # seconds

# Coordinates (using your provided values)
FOLLOWING_BUTTON_COORDS = (1081, 142)
UNFOLLOW_BUTTON_COORDS = (707, 679)

# Safety feature - failsafe
pyautogui.PAUSE = 0.5  # Add small delay between pyautogui actions
pyautogui.FAILSAFE = True  # Move mouse to top-left to abort

def focus_address_bar():
    """Focus the browser address bar using Ctrl+L (works in most browsers)"""
    keyboard.press_and_release('ctrl+l')
    time.sleep(delay_between_actions)
    print("Address bar focused")

def navigate_to_profile(username):
    """Navigate to Instagram profile"""
    focus_address_bar()
    pyautogui.write(f'https://www.instagram.com/{username}')
    keyboard.press_and_release('enter')
    time.sleep(delay_between_actions * 3)  # Wait longer for page load
    print(f"Navigated to {username}'s profile")

def click_following_button(name_length):
    """Click the Following button at specific coordinates"""
    pyautogui.click(FOLLOWING_BUTTON_COORDS[0]+name_length*8, FOLLOWING_BUTTON_COORDS[1])
    print(name_length*8)
    time.sleep(delay_between_actions)
    print("Clicked Following button")

def confirm_unfollow():
    """Click the Unfollow confirmation at specific coordinates"""
    pyautogui.click(UNFOLLOW_BUTTON_COORDS[0], UNFOLLOW_BUTTON_COORDS[1])
    time.sleep(unfollow_confirmation_wait)
    print("Confirmed unfollow")

def unfollow_user(username):
    """Unfollow a single user"""
    print(f"\nStarting to unfollow {username}...")
    navigate_to_profile(username)
    username_length = len(username)
    click_following_button(username_length)
    time.sleep(1)
    confirm_unfollow()
    print(f"Successfully unfollowed {username}")

def main():
    print("Instagram Unfollow Automation")
    print("Make sure:")
    print("1. You're logged in to Instagram in your default browser")
    print("2. The browser window is maximized")
    print("3. You have the Instagram tab open and visible")
    input("Press Enter when ready to start...")
    
    # Countdown before starting
    print("Starting in 3 seconds... Move mouse to top-left corner to abort")
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    for username in usernames:
        unfollow_user(username)
    
    print("\nUnfollow process completed!")

if __name__ == "__main__":
    main()