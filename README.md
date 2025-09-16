# 🚀 Insta-Unfollower

This project automates **unfollowing Instagram users** using Python + PyAutoGUI.
It reads usernames from a JSON file and simulates mouse/keyboard actions to unfollow each account automatically.

⚠️ **Disclaimer**: Use this tool at your own risk. Instagram may block or restrict your account for automation activity.
This project is for **educational purposes only**.

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/BananaLeaf77/insta-unfollower.git
cd insta-unfollower
```

### 2. Install Dependencies

If you’re using pip:

```bash
pip install -r requirements.txt
```

Or install as a package (editable mode):

```bash
pip install -e .
```

---

## ⚙️ Setup

1. Make sure you are **logged in to Instagram** in your default browser.
2. Your browser window must be **maximized** and the **Instagram tab visible**.
3. Prepare your unfollow list in `to_unfollow.json`:

   ```json
   [
       "username1",
       "username2",
       "username3"
   ]
   ```

---

## ▶️ Usage

Run the script:

```bash
insta-unfollower
```

Or if running directly:

```bash
python -m insta_unfollower.main
```

---

## 🖱️ How It Works

* Opens each Instagram profile from your `to_unfollow.json` list.
* Clicks the **Following** button (using screen coordinates).
* Confirms the **Unfollow** action.
* Moves to the next user until all are processed.
* You can **abort anytime** by moving your mouse to the **top-left corner** of your screen.

---

## ⚙️ Configuration

In `main.py`, adjust the **coordinates** if your screen resolution or browser layout is different:

```python
FOLLOWING_BUTTON_COORDS = (1081, 142)
UNFOLLOW_BUTTON_COORDS = (707, 679)
```

You can also tweak delays:

```python
delay_between_actions = 1      # seconds between actions
unfollow_confirmation_wait = 3 # seconds to wait after clicking unfollow
```

---

## 📂 Project Structure

```
insta-unfollower/
 ├── insta_unfollower/
 │   ├── __init__.py
 │   └── main.py              # main script
 ├── to_unfollow.json         # usernames to unfollow
 ├── setup.py                 # package installer
 ├── requirements.txt
 └── README.md
```

---

## 📘 Requirements

* Python 3.8+
* [PyAutoGUI](https://pyautogui.readthedocs.io)
* [keyboard](https://github.com/boppreh/keyboard)

Install all with:

```bash
pip install -r requirements.txt
```

---

## ⚠️ Notes

* If Instagram is **slow to load**, increase delays in `main.py`.
* Coordinates may need **manual calibration** if the layout changes.
* Always test with a dummy account before using your real account.

---

## 👨‍🎓 Author

* **Name**: Your Name
* **Project**: College Project (Educational Use Only)
* **Goal**: Demonstrate desktop automation with Python

---
