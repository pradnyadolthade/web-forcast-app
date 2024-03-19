import datetime
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim,Photon
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root = Tk()
root.title("Weather APP")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False,False)

def getWeather():
    city = textfield.get()
    geolocator = Photon(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)}N,{round(location.longitude,4)}E")
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    #weather
    api="https://api.openweathermap.org/data/2.8/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)\
          +"&units=metric&exclude=hourly&appid={api_key}"
    #removed api for security purpose

    json_data = requests.get(api).json()

    #current
    temp = json_data['current']['temp']
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']
    t.config(text=(temp,"C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hPa"))
    w.config(text=(wind,"m/s"))
    d.config(text=description)

    firstdayimage = json_data['daily'][0]['weather'][0]['icon']
    photo1 = ImageTk.PhotoImage(file=f"Images/{firstdayimage}.png")
    firstimage.config(image=photo1)
    firstimage.image=photo1


    tempday1 = json_data['daily'][0]['temp']['day']
    tempnight1 = json_data['daily'][0]['temp']['night']
    day1Item.config(text=f"Day:{tempday1}\n Night:{tempnight1}")


    seconddayimage = json_data['daily'][1]['weather'][0]['icon']
    img = (Image.open(f"Images/{seconddayimage}.png"))
    resized_img = img.resize((50,50))
    photo2 = ImageTk.PhotoImage(resized_img)
    secondimage.config(image=photo2)
    secondimage.image = photo2


    tempday2 = json_data['daily'][1]['temp']['day']
    tempnight2 = json_data['daily'][1]['temp']['night']
    day2Item.config(text=f"Day:{tempday2}\n Night:{tempnight2}")


    thirddayimage = json_data['daily'][2]['weather'][0]['icon']
    img = (Image.open(f"Images/{thirddayimage}.png"))
    resized_img = img.resize((50, 50))
    photo3 = ImageTk.PhotoImage(resized_img)
    thirdimage.config(image=photo3)
    thirdimage.image = photo3


    tempday3 = json_data['daily'][2]['temp']['day']
    tempnight3 = json_data['daily'][2]['temp']['night']
    day3Item.config(text=f"Day:{tempday3}\n Night:{tempnight3}")



    fouthdayimage = json_data['daily'][3]['weather'][0]['icon']
    img = (Image.open(f"Images/{fouthdayimage}.png"))
    resized_img = img.resize((50, 50))
    photo4 = ImageTk.PhotoImage(resized_img)
    fouthimage.config(image=photo4)
    fouthimage.image = photo4


    tempday4 = json_data['daily'][3]['temp']['day']
    tempnight4 = json_data['daily'][3]['temp']['night']
    day4Item.config(text=f"Day:{tempday4}\n Night:{tempnight4}")


    fifthdayimage = json_data['daily'][4]['weather'][0]['icon']
    img = (Image.open(f"Images/{fifthdayimage}.png"))
    resized_img = img.resize((50, 50))
    photo5 = ImageTk.PhotoImage(resized_img)
    fifthimage.config(image=photo5)
    fifthimage.image = photo5


    tempday5 = json_data['daily'][4]['temp']['day']
    tempnight5 = json_data['daily'][4]['temp']['night']
    day5Item.config(text=f"Day:{tempday5}\n Night:{tempnight5}")


    sixdayimage = json_data['daily'][5]['weather'][0]['icon']
    img = (Image.open(f"Images/{sixdayimage}.png"))
    resized_img = img.resize((50, 50))
    photo6 = ImageTk.PhotoImage(resized_img)
    sixthimage.config(image=photo6)
    sixthimage.image = photo6


    tempday6 = json_data['daily'][5]['temp']['day']
    tempnight6 = json_data['daily'][5]['temp']['night']
    day6Item.config(text=f"Day:{tempday6}\n Night:{tempnight6}")


    seddayimage = json_data['daily'][6]['weather'][0]['icon']
    img = (Image.open(f"Images/{seddayimage}.png"))
    resized_img = img.resize((50, 50))
    photo7 = ImageTk.PhotoImage(resized_img)
    sevenimage.config(image=photo7)
    sevenimage.image = photo7


    tempday7 = json_data['daily'][6]['temp']['day']
    tempnight7 = json_data['daily'][6]['temp']['night']
    day7Item.config(text=f"Day:{tempday7}\n Night:{tempnight7}")


    thirddayimage = json_data['daily'][2]['weather'][0]['icon']

    fouthdayimage = json_data['daily'][3]['weather'][0]['icon']

    fifthdayimage = json_data['daily'][4]['weather'][0]['icon']
    sixthdayimage = json_data['daily'][5]['weather'][0]['icon']
    seventhdayimage = json_data['daily'][6]['weather'][0]['icon']

    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fouth = first+timedelta(days=3)
    day4.config(text=fouth.strftime("%A"))

    fifth= first+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth= first+timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first+timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))

##icon
image_icon = ImageTk.PhotoImage(file="Images/logo.jpg")
root.iconphoto(False, image_icon)

Round_box = ImageTk.PhotoImage(file="Images/rounded_rectangle.jpg")
Label(root, image = Round_box, bg = "#57adff").place(x=30,y=110)


#label
label1 = Label(root, text = "Temperature", font=('Helvetica',11), fg='white', bg="black").place(x=50, y=120)
label2 = Label(root, text = "Humidity", font=('Helvetica',11), fg='white', bg="black").place(x=50, y=140)
label3 = Label(root, text = "Pressure", font=('Helvetica',11), fg='white', bg="black").place(x=50, y=160)
label4 = Label(root, text = "Wind Speed", font=('Helvetica',11), fg='white', bg="black").place(x=50, y=180)
label5 = Label(root, text = "Description", font=('Helvetica',11), fg='white', bg="black").place(x=50, y=200)



#search box
search_image = ImageTk.PhotoImage(file= "Images/search bar.png")
myimage = Label(image = search_image, bg ="#57adff").place(x=318,y =120)


weat_image = PhotoImage(file = "Images/weather_imgae.png")
smaller_image = weat_image.subsample(4, 4)
weatherimage = Label(root, image = smaller_image,bg= "#203243").place(x=252, y=123)


textfield = tk.Entry(root, justify='center', width=12, font= ('poopins',25, 'bold'),bg ="#203243", border=0, fg="white")
textfield.place(x=320,y=129)
textfield.focus()


search_icon = PhotoImage(file="Images/search_icon.png")
search_icon = search_icon.subsample(3,3)

myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg = "#203243", command= getWeather)
myimage_icon.place(x=535,y=124)

#Bottom box
frame = Frame(root, width=900, height=180, bg = "#212120")
frame.pack(side=BOTTOM)

#bottom boxes
firstbox = ImageTk.PhotoImage(file="Images/rectangle 1.jpg")
secondbox = ImageTk.PhotoImage(file="Images/rectangle 2.jpg")

Label(frame, image=firstbox, bg="#212120").place(x=10,y=20)
Label(frame, image=secondbox, bg="#212120").place(x=250,y=30)
Label(frame, image=secondbox, bg="#212120").place(x=350,y=30)
Label(frame, image=secondbox, bg="#212120").place(x=450,y=30)
Label(frame, image=secondbox, bg="#212120").place(x=550,y=30)
Label(frame, image=secondbox, bg="#212120").place(x=650,y=30)
Label(frame, image=secondbox, bg="#212120").place(x=750,y=30)


#clock
clock = Label(root,font=('Helvetica',20,'bold'), fg="white",bg="#57adff")
clock.place(x=30,y=20)
#timezone
timezone = Label(root,font=('Helvetica',20), fg="white",bg="#57adff")
timezone.place(x=600,y=20)
long_lat = Label(root,font=('Helvetica',10), fg="white",bg="#57adff")
long_lat.place(x=600,y=50)

t=Label(root, font=('Helvetica',11),fg="white", bg="black")
t.place(x=150,y=120)
h=Label(root, font=('Helvetica',11),fg="white", bg="black")
h.place(x=150,y=140)
p=Label(root, font=('Helvetica',11),fg="white", bg="black")
p.place(x=150,y=160)
w=Label(root, font=('Helvetica',11),fg="white",bg="black")
w.place(x=150,y=180)
d=Label(root,font=('Helvetica',11),fg="white",bg="black")
d.place(x=150,y=200)

#first cell
firstframe = Frame(root, width=225, height=132, bg="#282829")
firstframe.place(x=15,y=315)

day1 = Label(firstframe, font="aerial 20", bg ="#282829", fg="#fff")
day1.place(x=100, y=5)

firstimage = Label(firstframe,bg="#282829")
firstimage.place(x=1,y=15)

day1Item = Label(firstframe, bg="#282829", fg="#57adff",font="arial 15 bold")
day1Item.place(x=100, y=50)
#second cell

secondframe = Frame(root, width=82, height=107, bg="#282829")
secondframe.place(x=255,y=325)

day2 = Label(secondframe,bg="#282829",fg="#fff")
day2.place(x=10, y=5)

secondimage = Label(secondframe,bg="#282829")
secondimage.place(x=7,y=20)

day2Item = Label(secondframe, bg="#282829", fg="#fff")
day2Item.place(x=10, y=70)


#Third cell
thirdframe = Frame(root, width=82, height=107, bg="#282829")
thirdframe.place(x=355,y=325)

day3 = Label(thirdframe, bg="#282829", fg="#fff")
day3.place(x=10, y=5)

thirdimage = Label(thirdframe,bg="#282829")
thirdimage.place(x=7,y=20)

day3Item = Label(thirdframe, bg="#282829", fg="#fff")
day3Item.place(x=10, y=70)

#fouth cell
fouthframe = Frame(root, width=82, height=107, bg="#282829")
fouthframe.place(x=455,y=325)

day4 = Label(fouthframe, bg ="#282829", fg="#fff")
day4.place(x=10, y=5)

fouthimage = Label(fouthframe,bg="#282829")
fouthimage.place(x=7,y=20)

day4Item = Label(fouthframe, bg="#282829", fg="#fff")
day4Item.place(x=10, y=70)

#fifth cell
fifframe = Frame(root, width=82, height=107, bg="#282829")
fifframe.place(x=555,y=325)


day5 = Label(fifframe, bg ="#282829", fg="#fff")
day5.place(x=10, y=5)

fifthimage = Label(fifframe,bg="#282829")
fifthimage.place(x=7,y=20)


day5Item = Label(fifframe, bg="#282829", fg="#fff")
day5Item.place(x=10, y=70)

#sixth cell
sixframe = Frame(root, width=82, height=107, bg="#282829")
sixframe.place(x=655,y=325)

day6=Label(sixframe, bg="#282829", fg="#fff")
day6.place(x=10, y=5)

sixthimage = Label(sixframe,bg="#282829")
sixthimage.place(x=7,y=20)


day6Item = Label(sixframe, bg="#282829", fg="#fff")
day6Item.place(x=10, y=70)
#seventh cell
seframe = Frame(root, width=82, height=107, bg="#282829")
seframe.place(x=755,y=325)


day7= Label(seframe, bg ="#282829", fg="#fff")
day7.place(x=10, y=5)

sevenimage = Label(seframe,bg="#282829")
sevenimage.place(x=7,y=20)


day7Item = Label(seframe, bg="#282829", fg="#fff")
day7Item.place(x=10, y=70)
root.mainloop()


