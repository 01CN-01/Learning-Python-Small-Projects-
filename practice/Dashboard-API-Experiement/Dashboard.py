import platform
import os
import datetime
import requests
#Datetime
#Weather locations
#Random Quote API
#System info

#Option 1
def currenttime():
    current_time = datetime.datetime.now()
    print("Current time: ",current_time.strftime("%A, %d %m %Y"))
    print("Time: ",current_time.strftime("%I %p"))

#Option 2
def weather(city):
    API_KEY = "6a2cf164c1d37bab8fc2f0564aa5d58f"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url) #Get information from the website
    data = response.json() #Turns the data into a certain format

    print("Weather in:", city)
    print("Temperature:", data["main"]["temp"], "°C")
    print("Condition:", data["weather"][0]["description"])

#Option 3
def quote(): 
    url = f"https://zenquotes.io/api/random"
    response = requests.get(url) #Get information from the website
    data = response.json() #Turns the data into a certain format

    print(data[0]["q"], "-", data[0]["a"]) #Gets the QUOTE and the AUTHOR of the first thing.

#Option 4
def system():
    print("System Information:")
    print("OS: ",platform.system())
    print("OS Version: ",platform.version())
    print("Release: ",platform.release())
    print("Machine: ",platform.machine())
    print("Processor: ",platform.processor())
    print("Python version: ",platform.python_version())

#Option Selection
def options(choice):
    if choice == 1:
        currenttime() #prints whatever i had in that function
    if choice ==2:
        city = input("Enter your city: ")
        weather(city)
    if choice == 3:
        quote()
    if choice == 4:
        system

while True:
    while True:
        try:
            print("This is your Dashboard")
            print("1 = Time")
            print("2 = Weather")
            print("3 = Quotes")
            print("4 = System Info")
            choice = int(input("Select and option: "))
            if choice in [1, 2, 3, 4]:
                options(choice) #Executes the option function and gives it the "choice" variable
                break
            else:
                print("Only use 1, 2, 3, 4")
        except ValueError:
            print("Enter a number, not text.") #Instead of printing error it loops back
    
    finished = input("Are you finished? (1 = yes/2 =no): ")
    print("Use numbers")
    if finished == "1":
        break
    elif finished == "2":
        continue  #Telling it to loop back
    else:
        print("Invalid input. Returning to dashboard.")
        continue





