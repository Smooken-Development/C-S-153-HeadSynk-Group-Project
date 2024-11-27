# C S 153 - Python Programming
# Documentation for Custom Tikinter:  https://customtkinter.tomschimansky.com/documentation/

import os
import datetime # for data entries
import json # For saving data
import customtkinter as ctk # For UI

# TODO
# - make all function display a helpful message
# - make all user interactable functions happen in CTK windows
# - make all popup windows disappear after a few seconds

# This is to keep track of data for 2 weeks
mondayData1 = {};       mondayData2 = {}
tuesdayData1 = {};      tuesdayData2 = {}
wednesdayData1 = {};    wednesdayData2 = {}
thursdayData1 = {};     thursdayData2 = {}
fridayData1 = {};       fridayData2 = {}
saturdayData1 = {};     saturdayData2 = {}
sundayData1 = {};       sundayData2 = {}


moodEntry = {"moodTracked": 0,"goalAchieved": False}
foodEntry = {"foods": "N/A","goalAchieved": False}
waterEntry = {"waterAmount": 0.0,"goalAchieved": False}
sleepEntry = {"sleepAmount": 0,"goalAchieved": False}
exerciseEntry = {"exerciseType": "N/A","duration": 0,"goalAchieved": False}
journalEntry = {"journalEntry": "N/A"}
entryTimestamp = datetime.datetime.now().strftime("%Y-%m-%d")
tempUserData = {
    "moodEntry": moodEntry,
    "foodEntry": foodEntry,
    "waterEntry": waterEntry,
    "sleepEntry": sleepEntry,
    "exerciseEntry": exerciseEntry,
    "journalEntry": journalEntry,
    "entryTimestamp": entryTimestamp
}
'''
moodEntry = {"moodTracked": 5,"goalAchieved": True}
foodEntry = {"foods": "All","goalAchieved": True}
waterEntry = {"waterAmount": 3.1,"goalAchieved": True}
sleepEntry = {"sleepAmount": 8,"goalAchieved": True}
exerciseEntry = {"exerciseType": "Cardio","duration": 30,"goalAchieved": True}
journalEntry = {"journalEntry": "journal input"}
entryTimestamp = datetime.datetime.now().strftime("%Y-%m-%d")
tempUserData = {
    "moodEntry": moodEntry,
    "foodEntry": foodEntry,
    "waterEntry": waterEntry,
    "sleepEntry": sleepEntry,
    "exerciseEntry": exerciseEntry,
    "journalEntry": journalEntry,
    "entryTimestamp": entryTimestamp
}
'''

def saveDailyProgress():
    global tempUserData

    # TODO - Save tempUserData to a seperate variable depending on the week day
    match datetime.datetime.now().weekday():
        case 0:
            pass

    tempUserData = {
        "moodEntry": moodEntry,
        "foodEntry": foodEntry,
        "waterEntry": waterEntry,
        "sleepEntry": sleepEntry,
        "exerciseEntry": exerciseEntry,
        "journalEntry": journalEntry,
        "entryTimestamp": entryTimestamp
    }
    try:
        with open("user_data.json", "w") as file:
            json.dump(tempUserData, file, indent=4)
        print("Daily progress saved successfully.")
    except Exception as e:
        print(f"Error {e} has occured")
# End Save Function

# Start Load Function
def loadDailyProgress():
    global tempUserData
    try:
        with open("user_data.json", "r") as file:
            tempUserData = json.load(file)
        print("Daily progress loaded successfully.")    # DELETE ME: Temporary to confirm loaded data
    except FileNotFoundError:
        print("No saved data found. Starting fresh.")
        tempUserData = {}
    except Exception as e:
        print(f"An error occurred while finding data: {e}")
# End Load Function

def checkDayofWeek():
    global mondayData1;     global mondayData2
    global tuesdayData1;    global tuesdayData2
    global wednesdayData1;  global wednesdayData2
    global thursdayData1;   global thursdayData2
    global fridayData1;     global fridayData2
    global saturdayData1;   global saturdayData2
    global sundayData1;     global sundayData2

    # Figure out how to switch from week 1 to week 2

    day = datetime.datetime.now().weekday()
    '''if (True) & (True): A&A
       if (True) & (False): A&B
       // Only True & True will be execute'''
    twoWeeksAgo = datetime.datetime.now() - datetime.timedelta(days=14)
    dayNow = datetime.datetime.now()

    numA = int(datetime.datetime.now().strftime("%d"))
    if (dayNow >= twoWeeksAgo):
        print("yes")
    else:
        print("no")

    print(dayNow)
    



# loadDailyProgress()
checkDayofWeek()
# print(tempUserData)