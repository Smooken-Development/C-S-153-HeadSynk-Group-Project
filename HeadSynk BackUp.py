# C S 153 - Python Programming
# Documentation for Custom Tikinter:  https://customtkinter.tomschimansky.com/documentation/

import os
import datetime # for data entries
import json # For saving data
import customtkinter as ctk # For UI
from PIL import Image

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

moodEntry = {}
foodEntry = {}
waterEntry = {}
sleepEntry = {}
exerciseEntry = {}
journalEntry = {}
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

# This is the global variable that stores the dictionary dump
twoWeekData = {}
# This is to keep track of data for 2 weeks
dataTemplate = {
    "week1": {
        "monday": tempUserData, "tuesday": tempUserData, "wednesday": tempUserData, "thursday": tempUserData, "friday": tempUserData, "saturday": tempUserData, "sunday": tempUserData
    },
    "week2": {
        "monday": tempUserData, "tuesday": tempUserData, "wednesday": tempUserData, "thursday": tempUserData, "friday": tempUserData, "saturday": tempUserData, "sunday": tempUserData
    }
}

dataFile = "user_data.json"

#_Start_HeadSynk_______________________________________________

# Side Notes:
#   We might need to make a user class, so that we can populate things when the user wants them
# or, we can just load the sections after they click on them for more complex stuff (i.e analytics)

# Starts the program with a user login
def doLogIn():
    return  # DELETE ME: Remove when doLogIn() is complete
    logFile = "login.txt"
    regFile = "register.txt"
    
    def write_file(name):
        try:
            with open(name, 'w') as f:
                user = input("Enter username: ")
                pw = input("Enter password: ")
                f.write(f"{user}\n{pw}")                                   #writes username & password to file
    
        except IOError:
            print("Permission denied")
        except Exception as e:
            print(f"Error: {e}")
    
    
    def read_file(name):
        try:
            with open(name, 'r') as f:
                return f.read().strip().split('\n')  			#reads each line separate, returns a list
    
        except FileNotFoundError:
            print(f"File {name} not found")
        except IOError:
            print(f"You don't have permission to read {name}")
        except Exception as e:
            print(f"Error: {e}")
        return None
    
    def check_info(log, reg):
        return log== reg
    
    # Main loop
    logged_in = False
    while not logged_in:
        write_file(logFile)
        log_info = read_file(logFile)
        reg_info = read_file(regFile)
        if log_info and reg_info:
            if check_info(log_info, reg_info):
                logged_in = True
                print("Login successful")
            else:
                print("Wrong info")
        else:
            print("access denied")


# The main dashboard menu/window loop
# Start Dashboard Loop
# The main dashboard menu/window loop
# Start Dashboard Loop
def displayDashboard():
    dashboard = ctk.CTk()
    dashboard.title("HeadSynk")
    dashboard.geometry("600x400")
    
    # Button definitions with corrected commands
    moodButton = ctk.CTkButton(dashboard, text="Mood Tracker", command=trackMood)
    moodButton.pack(pady=5)
    
    foodButton = ctk.CTkButton(dashboard, text="Food Tracker", command=trackFood)
    foodButton.pack(pady=5)
    
    waterButton = ctk.CTkButton(dashboard, text="Water Tracker", command=trackWater)
    waterButton.pack(pady=5)

    sleepButton = ctk.CTkButton(dashboard, text="Sleep Tracker", command=trackSleep)
    sleepButton.pack(pady=5)

    exerciseButton = ctk.CTkButton(dashboard, text="Exercise Tracker", command=trackExercise)
    exerciseButton.pack(pady=5)

    badgeButton = ctk.CTkButton(dashboard, text="See Current Badge", command=doBadgeSystem)
    badgeButton.pack(pady=5)

    saveProgressButton = ctk.CTkButton(dashboard, text="Save Daily Progress", command=saveDailyProgress)
    saveProgressButton.pack(pady=5)

    journalButton = ctk.CTkButton(dashboard, text="Journal", command=openMoodJournal)
    journalButton.pack(pady=5)

    logoutButton = ctk.CTkButton(dashboard, text="Log Out", command=lambda: logout() or dashboard.quit())  # Logout and close the window
    logoutButton.pack(pady=20)

    # Start the window loop
    dashboard.mainloop()

    print("Goodbye!")
# End Dashboard Loop

# Start trackMood
def trackMood():
    # Create Mood Tracker Window
    moodWindow = ctk.CTkToplevel()
    moodWindow.title("Mood Tracker")
    moodWindow.geometry("600x400")

    def saveMood():
        global moodEntry
        moodTrack = int(moodSlider.get())

        # Checking mood and updating goal status
        if moodTrack > 5:
            print("That is not on the scale")
        elif moodTrack < 3:
            print("Things will get better")
            goalAchieved = 1
        else:
            print("That's great.")
            goalAchieved = 1

        # Create entry based off of data using a dictionary
        moodEntry = {
            "moodTracked": moodTrack,
            "goalAchieved": goalAchieved
        }

        ctk.CTkLabel(moodWindow, text="Mood logged successfully!", fg_color="green").pack(pady=5)
        moodWindow.after(2000, moodWindow.destroy)  # Close the window after 2 seconds

    def updateMoodLabel():
        currentMood = int(moodSlider.get())
        moodValueLabel.configure(text=f"Mood: {currentMood}")

    # Slider to track mood
    moodSlider = ctk.CTkSlider(moodWindow, from_=1, to=5, number_of_steps=4, command=lambda x: updateMoodLabel())
    moodSlider.pack(pady=20)

    moodValueLabel = ctk.CTkLabel(moodWindow, text="Mood: 3", font=("Aptos", 14))
    moodValueLabel.pack()

    # Save Button
    saveButton = ctk.CTkButton(moodWindow, text="Save", command=saveMood)
    saveButton.pack(pady=20)

    moodWindow.wait_window()
# End trackMood

# Start Food Tracker
def trackFood():

    # Initializes the foodWindow
    foodWindow = ctk.CTkToplevel()
    foodWindow.title("Food Tracker")
    foodWindow.geometry("600x400")  # consistent window geometry

    # Food categories and variables to track checks
    foods = ['Fruits', 'Vegetables', 'Grains', 'Protein', 'Dairy']
    checkListDictionary = {food: ctk.BooleanVar() for food in foods}    # Creates a BooleanVar to track the state of a checkbox (True or False)
                                                                        # Typically handles the states of widgets
    # displays checklist
    def checkListOptions():
        global foodEntry

        # Gets checked items
        checkedItems = [food for food, var in checkListDictionary.items() if var.get()]
        goalAchieved = int(len(checkedItems) == 5)  # True if at least 5 groups are checked

        # moves selected options to the global variable
        foodEntry = {
            "foods": checkedItems,
            "goalAchieved": goalAchieved
        }

        # Confirms food logging
        ctk.CTkLabel(foodWindow, text="Food groups logged successfully!", fg_color="green").pack(pady=5)
        ctk.CTkLabel(foodWindow, text="Remember: Try to eat at least two meals with all of these daily!").pack(pady=5)
        
        # Closes popup window after some time
        foodWindow.after(2000, foodWindow.destroy)

    # Prompt to get food groups
    ctk.CTkLabel(foodWindow, text="What food groups have you eaten today?").pack(pady=10)

    # Generate checkboxes for each food group
    for food in foods:
        ctk.CTkCheckBox(foodWindow, text=food, variable=checkListDictionary[food]).pack(anchor="w", padx=20)

    # Save button
    ctk.CTkButton(foodWindow, text="Save", command=checkListOptions).pack(pady=20)

    # keeps foodWindow popped up until closed
    foodWindow.wait_window()
# End Food Tracker

# Start trackWater
def trackWater():
    # Create Water Tracker Window
    waterWindow = ctk.CTkToplevel()
    waterWindow.title("Water Tracker")
    waterWindow.geometry("600x400")

    def saveWater():
        global waterEntry
        waterAmount = float(waterSlider.get())

        if waterAmount > 2.7:
            print("You have drunk the required amount for today")
            goalAchieved = 1
        else:
            print("You should drink some more water")
            goalAchieved = 0

        # Create entry based off of data using a dictionary
        waterEntry = {
            "waterAmount": waterAmount,
            "goalAchieved": goalAchieved
        }

        ctk.CTkLabel(waterWindow, text="Water logged successfully!", fg_color="green").pack(pady=5)
        waterWindow.after(2000, waterWindow.destroy)  # Close the window after 2 seconds

    def updateWaterLabel():
        currentWater = float(waterSlider.get())
        waterValueLabel.configure(text=f"Water: {currentWater:.2f} L")

    # Slider to track water intake
    waterSlider = ctk.CTkSlider(waterWindow, from_=0, to=5, number_of_steps=50, command=lambda x: updateWaterLabel())
    waterSlider.pack(pady=20)

    waterValueLabel = ctk.CTkLabel(waterWindow, text="Water: 0.00 L", font=("Aptos", 14))
    waterValueLabel.pack()

    # Save Button
    saveButton = ctk.CTkButton(waterWindow, text="Save", command=saveWater)
    saveButton.pack(pady=20)

    waterWindow.wait_window()
# End trackWater

# Start Track Sleep
def trackSleep():
    def saveSleep():
        # gets sleep hours 
        global sleepEntry
        sliderValue = int(slider.get())

        # if sleep is greater than 7, then the goal has been achieved
        if sliderValue > 7:
            goalAchieved = 1
        else:
            goalAchieved = 0

        # Saves it to the sleepEntry dictionary
        sleepEntry = {"sleepAmount": sliderValue, "goalAchieved":goalAchieved}
        sleepWindow.destroy()

    def updateLabel():  # This is to make the number pop below the slider
        currentValue = int(slider.get())
        if currentValue > 9:
            sliderValueLabel.configure(text="SleepHours: 9+")
        else:
            sliderValueLabel.configure(text=f"SleepHours: {currentValue}")

    sleepWindow = ctk.CTkToplevel()
    sleepWindow.title("Sleep Tracker")
    sleepWindow.geometry("600x400")

    label = ctk.CTkLabel(sleepWindow, text="How many hours did you sleep last night?", font=("Aptos", 16))
    label.pack(side="top", pady = 20)

    slider = ctk.CTkSlider(sleepWindow, from_=0, to=10, number_of_steps=10, command=lambda x: updateLabel())
    slider.pack(pady=20)

    sliderValueLabel = ctk.CTkLabel(sleepWindow, text="SleepHours: 5", font=("Aptos", 14))
    sliderValueLabel.pack()

    saveButton = ctk.CTkButton(sleepWindow, text="Confirm", command=saveSleep)
    saveButton.pack(pady=20)

    sleepWindow.wait_window()
# End Track Sleep

# Start Track Exercise
def trackExercise():
    # Create Exercise Tracker Window
    exerciseWindow = ctk.CTkToplevel()
    exerciseWindow.title("Exercise Tracker")
    exerciseWindow.geometry("600x400")

    exerciseTypes = {1: "Cardio", 2: "Yoga", 3: "Weights", 4: "Sports/Recreation", 5: "Walking"}
    selectedExercise = ctk.IntVar()  # Variable to store user's choice

    def saveExercise():
        global exerciseEntry
        try:
            choice = selectedExercise.get()
            if choice not in exerciseTypes:
                ctk.CTkLabel(exerciseWindow, text="Please select a valid exercise type.", fg_color="red").pack(pady=5)
                return

            # Get duration
            try:
                duration = int(durationEntry.get())
                if duration <= 0:
                    raise ValueError("Duration must be a positive integer.")
                elif duration < 30:
                    goalAchieved = 0
                elif duration >= 30:
                    goalAchieved = 1
            except ValueError as ve:
                ctk.CTkLabel(exerciseWindow, text=str(ve), fg_color="red").pack(pady=5)
                return

            # Log entry
            exerciseEntry = {
                "exerciseType": exerciseTypes[choice],
                "duration": duration,
                "goalAchieved": goalAchieved
            }

            ctk.CTkLabel(exerciseWindow, text="Exercise logged successfully!", fg_color="green").pack(pady=5)
            exerciseWindow.after(2000, exerciseWindow.destroy)  # Close the window after 2 seconds
        except Exception as e:
            ctk.CTkLabel(exerciseWindow, text=f"Error: {e}", fg_color="red").pack(pady=5)

    # Prompt user to select exercise type
    ctk.CTkLabel(exerciseWindow, text="Select the type of exercise:", font=("Aptos", 16)).pack(pady=10)

    for key, value in exerciseTypes.items():
        ctk.CTkRadioButton(exerciseWindow, text=value, variable=selectedExercise, value=key).pack(anchor="w", padx=20)

    # Prompt user to enter duration
    ctk.CTkLabel(exerciseWindow, text="Enter duration in minutes:", font=("Aptos", 16)).pack(pady=10)
    durationEntry = ctk.CTkEntry(exerciseWindow, width=200)
    durationEntry.pack(pady=10)

    # Save button
    saveButton = ctk.CTkButton(exerciseWindow, text="Save", command=saveExercise)
    saveButton.pack(pady=20)

    exerciseWindow.wait_window()
# End Track Exercise

#__Shabhan's__Badge_System#_____________________________________
def doBadgeSystem():
    # FINISH ME:

    


    badgeWindow = ctk.CTkToplevel()
    badgeWindow.title("Congratulations!")
    badgeWindow.geometry("600x400")

        #TODO: if save data == satisfactory :


    badge_img_path = "D:\\1 - Computer Science Classes\\Headsynk\\Screenshot 2024-10-31 231643.png"
    badge_img = ctk.CTkImage(dark_image=Image.open(badge_img_path), size=(200, 200))
    badge_label = ctk.CTkLabel(badgeWindow, image=badge_img)
    badge_label.pack(pady=20)

    ctk.CTkLabel(badgeWindow, text="Congratulations!\nYou earned a badge!", font=("Aptos", 16)).pack(pady=20)

    exitButton = ctk.CTkButton(badgeWindow, text="Close", command=badgeWindow.destroy)
    exitButton.pack(pady=5)

    badgeWindow.wait_window()
#_______________________________________________________________

# Start Mood Journal
def openMoodJournal():
    def saveEntry():
        global journalEntry
        # dictionary to stay consistent
        journalEntry = {"journalEntry": textBox.get("1.0", "end-1c")}   # 1.0 gets the textBox entry at column 1,
                                                                        # row 1. end-1c removes any lines after the last character
        journalWindow.destroy()

    # Create a new window
    journalWindow = ctk.CTkToplevel()
    journalWindow.title("Mood Journal")
    journalWindow.geometry("600x400")

    # Add a label to the top of the window
    label = ctk.CTkLabel(journalWindow, text="Please write anything you'd like to remember from today!\nPlease make sure to press 'save' before exiting.", font=("Aptos", 16))
    label.pack(side="top", pady = 20)

    # Add a text box for multi-line input
    textBox = ctk.CTkTextbox(journalWindow, width=380, height=200)
    textBox.pack(pady=10)

    # Add a save button
    saveButton = ctk.CTkButton(journalWindow, text="Save", command=saveEntry)
    saveButton.pack(pady=10)

    journalWindow.wait_window()
# End Mood Journal

# Start loadData
def loadData():
    # Load two-week data from JSON file or create a new one if it doesn't exist
    global twoWeekData
    def assignVariables():
        global tempUserData     # Initalizes global variables within this function
        global mondayData1;     global mondayData2
        global tuesdayData1;    global tuesdayData2
        global wednesdayData1;  global wednesdayData2
        global thursdayData1;   global thursdayData2
        global fridayData1;     global fridayData2
        global saturdayData1;   global saturdayData2
        global sundayData1;     global sundayData2

        # assigns global variables with their data from the JSON file
        mondayData1 = twoWeekData["week1"]["monday"];       mondayData2 = twoWeekData["week2"]["monday"]
        tuesdayData1 = twoWeekData["week1"]["tuesday"];     tuesdayData2 = twoWeekData["week2"]["tuesday"]
        wednesdayData1 = twoWeekData["week1"]["wednesday"]; wednesdayData2 = twoWeekData["week2"]["wednesday"]
        thursdayData1 = twoWeekData["week1"]["thursday"];   thursdayData2 = twoWeekData["week2"]["thursday"]
        fridayData1 = twoWeekData["week1"]["friday"];       fridayData2 = twoWeekData["week2"]["friday"]
        saturdayData1 = twoWeekData["week1"]["saturday"];   saturdayData2 = twoWeekData["week2"]["saturday"]
        sundayData1 = twoWeekData["week1"]["sunday"];       sundayData2 = twoWeekData["week2"]["sunday"]

        # FIXME - reset data from two weeks ago to standard dictionary
        currentWeek = "week1" if datetime.datetime.now() - datetime.timedelta(days=7) < datetime.datetime.now() else "week2"
        currentDay = datetime.datetime.now().strftime("%A").lower()

        tempUserData = twoWeekData[currentWeek].get(currentDay, {})
    # Checks if dataFile exists
    if os.path.exists(dataFile):
        # if it exists, if data has week1 or week2, return data
        with open(dataFile, "r") as file:
            try:
                twoWeekData = json.load(file)
                # else, resets tempUserData to dataTemplate
                if "week1" not in twoWeekData or "week2" not in twoWeekData:
                    print("Data structure incomplete. Resetting to template.")
                    twoWeekData = dataTemplate.copy()
            except json.JSONDecodeError:
                # resets to template if the file is corrupted
                print("Corrupted JSON file. Resetting to template.")
                twoWeekData = dataTemplate.copy()
    else:
        # Return the two-week data as a dictionary
        twoWeekData = dataTemplate.copy()
    assignVariables()
# End loadData

# Start saveDailyProgress
def saveDailyProgress():
    def saveTwoWeekData(data):
        print("Saving TwoWeekData", data)
        try:
            # saves 'data' (all of the information for two weeks) by dumping it all into data file
            with open(dataFile, "w") as file:
                print("dumping data:", data)
                json.dump(data, file, indent=4)
                print("dumped data")
        except Exception as e:
            print(f"Error saving data: {e}")
        print("Data saved")
    # initializes global variables in the function
    global tempUserData
    global twoWeekData

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
        # FIXME
        # assigns currentWeek with 'week1' if today's date was more than a week ago
        print("The broken week1/week2 counters")
        currentWeek = "week1" if datetime.datetime.now() - datetime.timedelta(days=7) < datetime.datetime.now() else "week2"
        currentDay = datetime.datetime.now().strftime("%A").lower()

        print("Accessing twoWeekData:", twoWeekData[currentWeek][currentDay])
        print(tempUserData)
        twoWeekData[currentWeek][currentDay] = tempUserData
        saveTwoWeekData(twoWeekData)
        print(f"Saved data for {currentDay} in {currentWeek}.")
    except Exception as e:
        print(f"Error during saving process: {e}")
# End saveDailyProgress

#___Shabhan's__Logout()_________________________________
def logout():
    doBadgeSystem()
    saveDailyProgress()
    
#_______________________________________________________#

# Start Error Window
def showErrorPopup(errorMessage):
    
    errorWindow = ctk.CTkToplevel() # FIX ME: put in the main window varibale name here
    errorWindow.title("⚠️ Error")
    errorWindow.geometry("250x120")
    errorWindow.grab_set()

    label = ctk.CTkLabel(errorWindow, text=f"⚠️{errorMessage}", wraplength=250, font=("Aptos", 12), text_color="red")
    label.pack(pady=20)

    closeButton = ctk.CTkButton(errorWindow, text="Dismiss", command=errorWindow.destroy)
    closeButton.pack(pady=10)
    
    errorWindow.wait_window()
# End Error Window

# main "function" basically
if __name__ == "__main__":
    doLogIn()
    loadData()
    displayDashboard()
