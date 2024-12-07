# C S 153 - Python Programming
# Documentation for Custom Tikinter:  https://customtkinter.tomschimansky.com/documentation/

import os
import datetime # for data entries
import json # For saving data
import customtkinter as ctk # For UI
from PIL import Image

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

                                                   
                                                            #  main dashboard menu/window loop
def displayDashboard():
    for widget in dashboard.winfo_children():                    # Clear the frame
        widget.destroy()

    
    # Button definitions with corrected commands
    moodButton = ctk.CTkButton(dashboard, text="Mood Tracker", command=lambda: trackMood())
    moodButton.pack(pady=5)
    
    foodButton = ctk.CTkButton(dashboard, text="Food Tracker", command=lambda: trackFood())
    foodButton.pack(pady=5)  
    
    waterButton = ctk.CTkButton(dashboard, text="Water Tracker", command=lambda: trackWater())
    waterButton.pack(pady=5)

    sleepButton = ctk.CTkButton(dashboard, text="Sleep Tracker", command=lambda: trackSleep())
    sleepButton.pack(pady=5)

    exerciseButton = ctk.CTkButton(dashboard, text="Exercise Tracker", command=lambda: trackExercise())
    exerciseButton.pack(pady=5)

    badgeButton = ctk.CTkButton(dashboard, text="See Current Badge", command=lambda: doBadgeSystem())
    badgeButton.pack(pady=5)

    saveProgressButton = ctk.CTkButton(dashboard, text="Save Daily Progress", command=saveDailyProgress)
    saveProgressButton.pack(pady=5)

    journalButton = ctk.CTkButton(dashboard, text="Journal", command=lambda: openMoodJournal())
    journalButton.pack(pady=5)

    logoutButton = ctk.CTkButton(dashboard, text="Log Out", command=lambda: logout() or dashboard.quit())  # Logout and close the window
    logoutButton.pack(pady=20)


 
# End Dashboard Loop

# Start trackMood
def trackMood():
    for widget in dashboard.winfo_children():                    # Clear the frame
        widget.destroy()

                                                            # Create Mood Tracker widgets
    moodLabel = ctk.CTkLabel(dashboard, text="On a scale of 1-5, how do you feel today?")
    moodLabel.pack(pady=20)

    def saveMood():
        global moodEntry
        moodTrack = int(moodSlider.get())

        # Checking mood and updating goal status
        if moodTrack > 5:
            moodLabel.configure(text="That is not on the scale", fg_color="purple")
        elif moodTrack < 3:
            moodLabel.configure(text="Remember: things will always get \nbetter with consistent effort!", text_color="Yellow")
            goalAchieved = 1
        else:
            moodLabel.configure(text="That's fantastic!", text_color="Light Green")
            goalAchieved = 1

        # Create entry based off of data using a dictionary
        moodEntry = {
            "moodTracked": moodTrack,
            "goalAchieved": goalAchieved
        }


    def updateMoodLabel():
        currentMood = int(moodSlider.get())
        moodValueLabel.configure(text=f"Mood: {currentMood}")

                                                                                    # Slider to track mood
    moodSlider = ctk.CTkSlider(dashboard, from_=1, to=5, number_of_steps=4, command=lambda x: updateMoodLabel())
    moodSlider.pack(pady=20)

    moodValueLabel = ctk.CTkLabel(dashboard, text="Mood: 3", font=("Aptos", 14))
    moodValueLabel.pack()
                                                                                # Save progress
    saveButton = ctk.CTkButton(dashboard, text="save", command=saveMood)
    saveButton.pack(pady=20)
                                                                                #return to dashboard
    backButton = ctk.CTkButton(dashboard, text="Back", command=displayDashboard)
    backButton.pack(pady=10)



# End trackMood

# Start Food Tracker
def trackFood():

    for widget in dashboard.winfo_children():                    # Clear the frame
        widget.destroy()
            # Prompt to get food groups
    foodLabel = ctk.CTkLabel(dashboard, text="What food groups have you eaten today?")
    foodLabel.pack(pady=10)

    # Food categories and variables to track checks
    foods = ['Fruits', 'Vegetables', 'Grains', 'Protein', 'Dairy']
    checkListDictionary = {food: ctk.BooleanVar() for food in foods}    # Creates a BooleanVar to track the state of a checkbox (True or False)
                                                                        # Typically handles the states of widgets
    # displays checklist
    def checkListOptions():
        global foodEntry

        # Gets checked items
        checkedItems = [food for food, var in checkListDictionary.items() if var.get()]
        goalAchieved = int(len(checkedItems) == 5)                      # True if at least 5 groups are checked

        # moves selected options to the global variable
        foodEntry = {
            "foods": checkedItems,
            "goalAchieved": goalAchieved
        }

                                                                            # Confirms food logging
        foodLabel.configure(text="Food groups logged successfully!", text_color="Light Green")
        ctk.CTkLabel(dashboard, text="Remember: Try to eat at least two\nmeals with all of these daily!", text_color="Light Blue").pack(pady=5)
        
    # Generate checkboxes for each food group
    for food in foods:
        ctk.CTkCheckBox(dashboard, text=food, variable=checkListDictionary[food]).pack(anchor="w", padx=20)

    # Save button
    ctk.CTkButton(dashboard, text="Save", command=checkListOptions).pack(pady=20)

    # keeps dashboard popped up until closed
    backButton = ctk.CTkButton(dashboard, text="Back", command=displayDashboard)
    backButton.pack(pady=10)
    
# End Food Tracker

def trackWater():
                                                            #create Water Tracker Window
    for widget in dashboard.winfo_children():                    # Clear the frame
        widget.destroy()

    waterLabel = ctk.CTkLabel(dashboard, text="How much water have you drank today?")
    waterLabel.pack(pady=20)        

    def saveWater():
        global waterEntry
        waterAmount = float(waterSlider.get())

        if waterAmount > 2.7:
            waterLabel.configure(text="Good job on reaching your intake goal!", text_color="Light Green")
            goalAchieved = 1
        else:
            waterLabel.configure(text="Make sure to drink at least 2.7 liters a day!", text_color="Yellow")
            goalAchieved = 0

                                                            #create entry based off of data using a dictionary
        waterEntry = {
            "waterAmount": waterAmount,
            "goalAchieved": goalAchieved
        }

        ctk.CTkLabel(dashboard, text="Water logged successfully!", text_color="Light Green").pack(pady=5)

    def updateWaterLabel():
        currentWater = float(waterSlider.get())
        waterValueLabel.configure(text=f"Water: {currentWater:.2f} L")

    # Slider to track water intake
    waterSlider = ctk.CTkSlider(dashboard, from_=0, to=5, number_of_steps=50, command=lambda x: updateWaterLabel())
    waterSlider.pack(pady=20)

    waterValueLabel = ctk.CTkLabel(dashboard, text="Water: 2.70 L", font=("Aptos", 14))
    waterValueLabel.pack()

    # Save Button
    saveButton = ctk.CTkButton(dashboard, text="Save", command=saveWater)
    saveButton.pack(pady=20)

    backButton = ctk.CTkButton(dashboard, text="Back", command=displayDashboard)
    backButton.pack(pady=10)

# End trackWater

# Start Track Sleep
def trackSleep():
    for widget in dashboard.winfo_children():                    # Clear the frame
        widget.destroy()
    sleepLabel = ctk.CTkLabel(dashboard, text="How many hours did you sleep last night?", font=("Aptos", 16))
    sleepLabel.pack(side="top", pady = 20)

    def saveSleep():
        # gets sleep hours 
        global sleepEntry
        sliderValue = int(slider.get())

        # if sleep is greater than 7, then the goal has been achieved
        if sliderValue >= 7:
            goalAchieved = 1
            sleepLabel.configure(text="Good job on getting a good night's rest!", text_color="Light Green")
        else:
            goalAchieved = 0
            sleepLabel.configure(text="Make sure to get enough sleep tonight\nYou need it to function!", text_color="Light Blue")

        # Saves it to the sleepEntry dictionary
        sleepEntry = {"sleepAmount": sliderValue, "goalAchieved":goalAchieved}

    def updateLabel():  # This is to make the number pop below the slider
        currentValue = int(slider.get())
        if currentValue > 9:
            sliderValueLabel.configure(text="SleepHours: 9+")
        else:
            sliderValueLabel.configure(text=f"SleepHours: {currentValue}")


    slider = ctk.CTkSlider(dashboard, from_=0, to=10, number_of_steps=10, command=lambda x: updateLabel())
    slider.pack(pady=20)

    sliderValueLabel = ctk.CTkLabel(dashboard, text="SleepHours: 5", font=("Aptos", 14))
    sliderValueLabel.pack()

    saveButton = ctk.CTkButton(dashboard, text="Confirm", command=saveSleep)
    saveButton.pack(pady=20)

    backButton = ctk.CTkButton(dashboard, text="Back", command=displayDashboard)
    backButton.pack(pady=10)
# End Track Sleep



# Start Track Exercise
def trackExercise():
    for widget in dashboard.winfo_children():                    # Clear the frame
        widget.destroy()
        # Prompt user to select exercise type
    exerciseLabel = ctk.CTkLabel(dashboard, text="Select the type of exercise:", font=("Aptos", 16))
    exerciseLabel.pack(pady=10)

    exerciseTypes = {1: "Cardio", 2: "Yoga", 3: "Weights", 4: "Sports/Recreation", 5: "Walking", 6: "Other/None"}
    selectedExercise = ctk.IntVar()  # Variable to store user's choice

    def saveExercise():
        global exerciseEntry
        try:
            choice = selectedExercise.get()
            if choice not in exerciseTypes:
                ctk.CTkLabel(dashboard, text="Please select a valid exercise type.", text_color="Red").pack(pady=5)
                return

            # Get duration
            try:
                duration = int(durationEntry.get())
                if duration < 0:
                    raise ValueError("Duration must be an integer greater than 0.")
                elif duration < 30:
                    goalAchieved = 0
                elif duration >= 30:
                    goalAchieved = 1
            except ValueError as ve:
                ctk.CTkLabel(dashboard, text=str(ve), text_color="red").pack(pady=5)
                return

            # Log entry
            exerciseEntry = {
                "exerciseType": exerciseTypes[choice],
                "duration": duration,
                "goalAchieved": goalAchieved
            }

            exerciseLabel.configure(text=f"Exercise logged successfully!", text_color="Light Green")
        except Exception as e:
            ctk.CTkLabel(dashboard, text=f"Error: {e}", fg_color="Red", text_color="Yellow").pack(pady=5)



    for key, value in exerciseTypes.items():
        ctk.CTkRadioButton(dashboard, text=value, variable=selectedExercise, value=key).pack(anchor="w", padx=20)

    # Prompt user to enter duration
    ctk.CTkLabel(dashboard, text="Enter duration in minutes:", font=("Aptos", 16)).pack(pady=10)
    durationEntry = ctk.CTkEntry(dashboard, width=200)
    durationEntry.pack(pady=10)

    # Save button
    saveButton = ctk.CTkButton(dashboard, text="Save", command=saveExercise)
    saveButton.pack(pady=20)
    
    backButton = ctk.CTkButton(dashboard, text="Back", command=displayDashboard)
    backButton.pack(pady=10)

# End Track Exercise

#__Shabhan's__Badge_System#_____________________________________
def doBadgeSystem():
    # FINISH ME:
    for widget in dashboard.winfo_children():                    # Clear the frame
        widget.destroy()
    badgeLabel= ctk.CTkLabel(dashboard, text="Congratulations!\nYou earned a badge!", text_color="Light Green", font=("Aptos", 16))
    badgeLabel.pack(pady=2)

    #TODO: if save data == satisfactory :

    # FIXME: Add New Badge Image
    badge_img_path = "D:\\1 - Computer Science Classes\\Headsynk\\Screenshot 2024-10-31 231643.png" # Change this to whatever your image is
    badge_img = ctk.CTkImage(dark_image=Image.open(badge_img_path), size=(200, 200))
    badge_label = ctk.CTkLabel(dashboard, image=badge_img)
    badge_label.pack(pady=20)

    backButton = ctk.CTkButton(dashboard, text="Back", command=displayDashboard)
    backButton.pack(pady=10)
#_______________________________________________________________

# Start Mood Journal
def openMoodJournal():
    for widget in dashboard.winfo_children():                    # Clear the frame
        widget.destroy()
    journalLabel = ctk.CTkLabel(dashboard, text="What would you like to write about today?\n(Make sure to 'save' before leaving!)", font=("Aptos", 16))
    journalLabel.pack(side="top", pady = 20)
    def saveEntry():
        global journalEntry
        # dictionary to stay consistent
        journalEntry = {"journalEntry": textBox.get("1.0", "end-1c")}   # 1.0 gets the textBox entry at column 1,
                                                                        # row 1. end-1c removes any lines after the last character
        journalLabel.configure(text="Entry saved successfully!", text_color="Light Green")


    # Add a label to the top of the window
    # Add a text box for multi-line input
    textBox = ctk.CTkTextbox(dashboard, width=380, height=200)
    textBox.pack(pady=10)

    # Add a save button
    saveButton = ctk.CTkButton(dashboard, text="Save", command=saveEntry)
    saveButton.pack(pady=10)

    backButton = ctk.CTkButton(dashboard, text="Back", command=displayDashboard)
    backButton.pack(pady=10)


# End Mood Journal

# Start loadData
def loadData():
    for widget in dashboard.winfo_children():                    # Clear the frame
        widget.destroy()
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
    progLabel = ctk.CTkLabel(dashboard, text="Saving...", font=("Aptos", 16))
    progLabel.pack()
    

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
    progLabel.after(2000, progLabel.destroy)
    
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
    dashboard = ctk.CTk()
    dashboard.title("HeadSynk")
    dashboard.geometry("600x600")
    doLogIn()
    loadData()
    displayDashboard()
    dashboard.mainloop()
