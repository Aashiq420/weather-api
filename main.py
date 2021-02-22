import requests
from datetime import *
from tkinter import *
from tkinter import messagebox as mb

root = Tk()
root.title("Weather App")
root.geometry("750x370")
root.resizable(0, 0) 
try:
    #gif background
    frame_count = 24
    frames = [PhotoImage(file='logo.gif',format = 'gif -index %i' %(i)) for i in range(frame_count)]
    
    #function to animate gif
    def backimg(ind):
        frame = frames[ind]
        ind += 1
        if ind == frame_count:
            ind = 0
        gif_label.configure(image=frame)
        root.after(100, backimg, ind)

    #label for gif background
    gif_label = Label(root)
    gif_label.place(x=-20,y=-50)
    root.after(0, backimg, 0)
except:
    pass

#Class which contains program
class app:
    def __init__(self):
        #Label, Entry, button
        self.city = Entry(root)
        city_label = Label(root, text='Enter country/city name:', bg='gold')
        update_btn = Button(root, text="Update", command=self.weather)
        self.name_label = Label(root, bg='gold')
        self.temp_label = Label(root, bg='gold')
        self.humidity_label = Label(root, bg='gold')
        self.wind_label = Label(root, bg='gold')
        self.cloud_label = Label(root, bg='gold')

        #placements
        city_label.place(x=5,y=5)
        self.city.place(x=175,y=5)
        update_btn.place(x=10,y=50)
        self.name_label.place(x=25,y=90)
        self.temp_label.place(x=25,y=130)
        self.humidity_label.place(x=25,y=170)
        self.wind_label.place(x=25, y=210)
        self.cloud_label.place(x=25,y=250)

    #Program
    def weather(self):
        #using a try-except to catch any exception and display a message
        try:
            #trying to get information from weather API
            #if successful it continues and accesses the json info and tries to fetch some data
            url = 'https://api.openweathermap.org/data/2.5/weather?q='+self.city.get()+'&appid=25df487fad985da2ed650781b96f1b10'
            req = requests.get(url)
            req_j = req.json()
            temp = req_j['main']['temp']
            temp = round(float(temp)-273, 2)
        except Exception as e:
            mb.showerror('Error ','An error has occured.\nCheck your input or connection')
                
        #fetching specific data from the API

        humid = req_j['main']['humidity']

        wind = req_j['wind']['speed']

        cloud = req_j['weather'][0]['description']

        #timezone calculations to display time in different countries
        time = int(req_j['timezone']/3600)
        delta = time-2
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        new_time = now + timedelta(hours=delta)
        new_time = new_time.strftime("%H:%M")

        #updating labels with necessary information
        self.name_label['font'] = 'bold',15
        self.name_label['text'] = 'Current weather for '+self.city.get()+' at '+new_time
        self.temp_label['text'] = '• Temperature: '+str(temp)+'°C'
        self.humidity_label['text'] = '• Humidity: '+str(humid)
        self.wind_label['text'] = '• Wind speed: '+str(wind)+'km/h'
        self.cloud_label['text'] = '• Cloud cover: '+str(cloud)

#Running the program class and looping the tkinter window
run = app()
root.mainloop()
