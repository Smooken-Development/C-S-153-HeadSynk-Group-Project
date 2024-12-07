# Developed for CS 153: Python Programming at New Mexico State University Alamogordo
# HeadSynk: A habit tracker for personal use

Professor:
    Ayman Alzaid - alzaida@nmsu.edu

Main Developers:
    Zachary A. Carmichael - https://github.com/Smooken-Development
    Shabhan Andrew George - https://github.com/dravidian117

Contributers:
    Raena Martinez        - https://github.com/Raenamartinne
    William Jones         - https://github.com/WaveBurnt
    Jason Edgington       - https://github.com/jedge09

---

# Overview
    HeadSynk is a Python-based application designed to track and analyze personal data over two weeks.
It features tools for tracking mood, food intake, water consumption, sleep, exercise, and journaling,
helping users maintain consistency and meet their wellness goals.

This project uses:
- `customtkinter` for an intuitive graphical user interface (GUI)
- `PIL` for image handling
- `datetime` for timestamping entries
- `json` for saving and loading user data

---

# Features
    1. Mood Tracker 
- Allows users to rate their daily mood on a scale from 1 to 5.
- Offers motivational messages and allows users to track how they are feeling over time.

    2. Food Tracker 
- Lets users log their intake of major food groups (Fruits, Vegetables, Grains, Protein, Dairy).
- Encourages balanced eating habits by reminding user to eat at least two meals with all of the above.

    3. Water Tracker 
- Tracks daily water intake in liters.
- Provides feedback to encourage meeting a recommended daily goal of 2.7 liters or more.

    4. Sleep Tracker 
- Logs hours of sleep per night.
- Advises users to aim for 7+ hours for optimal rest.

    5. Journal 
- A space for users to write down anything they wish to remember for the day.

    6. Badge System 
- Unfinished. Currently displays a picture as a badge.

    7. Data Persistence
- Data is saved in `user_data.json` with nested dictionaries

---

# Requirements
- Python 3.10 or newer
- Modules:
  - `customtkinter`
  - `PIL` (Python Imaging Library)
  - `datetime`
  - `json`

---

# Usage
    Initial Setup
1. Clone or download the project files.
2. Install the required dependencies using pip:
    Command Prompt:
    pip install customTkinter, pillow
