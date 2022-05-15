import datetime
import time

now = datetime.datetime.now()

class Talons():
    def __init__(self, number, email):
        self.hasATalon = "True"
        self.listOfReminders = []
        self.listOfEvents = []

        if type(number) is str:
            self.numberSet = number
        if type(email) is str:
            self.emailSet = email

        self.hourNow = None
        self.minuteNow = None
        self.secondNow = None

        self.hourSetForTimer = None
        self.minuteSetForTimer = None
        self.secondsSetForTimer = None
        self.messageSetForTimer = ""

        self.breakTime = 0
        self.workTime = 0

        self.statsForToday = 0

    def setPhoneNumber(self, number):
        self.numberSet = number

    def setEmailAddress(self, email):
        self.emailSet = email

    def setBreakAndWorkTime(self, workTime, breakTime):
        self.workTime = workTime
        self.breakTime = breakTime

    def appendReminder(self, reminder):
        if type(reminder) is not tuple:
            print("The reminder is not of type Tuple")
        else:
            if reminder not in self.listOfReminders:
                self.listOfReminders.append(reminder)
                return 1
            else:
                return -1

    def removeReminder(self, reminder):
        if type(reminder) is not tuple:
            print("The reminder is not of type Tuple")
        else:
            try:
                self.listOfReminders.remove(reminder)
            except Exception as e:
                print(e)

    def appendEvent(self, event):
        if type(event) is not tuple:
            print("The event is not of type Tuple")
        else:
            if event not in self.listOfEvents:
                self.listOfEvents.append(event)
                return 1
            else:
                return -1

    def removeEvent(self, event):
        if type(event) is not tuple:
            print("The event is not of type Tuple")
        else:
            try:
                self.listOfEvents.remove(event)
            except Exception as e:
                print(e)


    def __str__(self):
        return "Phone Number: " + self.numberSet + ", Email: " + self.emailSet