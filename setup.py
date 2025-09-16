from setuptools import setup, find_packages

setup(
    name="insta-unfollower",
    version="0.1.0",
    description="Instagram unfollow automation using PyAutoGUI",
    author="BananaLeaf77",
    packages=find_packages(),
    install_requires=[
        "pyautogui",
        "keyboard",
    ],
    entry_points={
        "console_scripts": [
            "insta-unfollower=insta_unfollower.main:main",
        ],
    },
    python_requires=">=3.8",
)
