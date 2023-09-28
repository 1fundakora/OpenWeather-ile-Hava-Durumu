from tkinter import *           # sayfa açmak için kullanılan kütüphane
from PIL import ImageTk,Image   #Görüntü işlemek için kullanılan kütüphane
import requests                 # web sayfalarına istek yollayıp kodları almamızı sağlayan kütüphane
from tkinter import messagebox

url= 'https://api.openweathermap.org/data/2.5/weather'
api_key= 'b2baa95fd5c677bc1aec407c1803d0ff'
iconUrl ='https://openweathermap.org/img/wn/{}@2x.png'

def getweather(city):
    try:
        params = {'q':city,'appid':api_key,'lang':'tr'}
        data = requests.get(url,params=params).json()
        
        if data:city = data['name'].capitalize() #şehir bilgisi almak için
        
        country = data['sys']['country'] #ülke bilgisi almak için
        temp = int(data ['main']['temp'] - 273.15) #sıcaklık almak için
        icon = data['weather'][0]['icon'] 
        condition = data['weather'][0]['description']
        return (city,country,temp,icon,condition)
    
    except Exception as e:
        messagebox.showerror("Hava Durumu","Hatalı Giriş!!")
def main():
    city = cityEntry.get()
    weather = getweather(city)
    if weather:
        locationLabel['text'] = '{} , {}'.format(weather[0],weather [1])
        templabel['text']='{}°C'.format(weather[2])
        conditionLabel['text'] = weather[4]
        icon = ImageTk.PhotoImage(Image.open(requests.get(iconUrl.format(weather [3]),stream = True).raw))
        iconlabel.configure(image=icon)
        iconlabel.image = icon


app = Tk()
app.geometry('450x500')
app.title('HAVA DURUMU')
cityEntry = Entry(app,justify='center')
cityEntry.pack(fill=BOTH,ipady=8,ipadx=25,pady=4)
cityEntry.focus()

#arama kutusu
searchButton = Button(app,text='Arama',font=('Times New Roman',15),command=main)
searchButton.configure(background="#88dd08")
searchButton.pack(fill=BOTH,ipady=10,ipadx=20)

#icon resim işlemi
iconlabel = Label(app)
iconlabel.pack()

#lokasyon ve şehir seçim
locationLabel = Label(app,font=('Times New Roman',40))
locationLabel.pack()

#sıcaklık almak için 
templabel = Label(app,font=('Times New Roman',50,'bold'))
templabel.pack()

#condition tutmak için
conditionLabel = Label(app,font=('Times New Roman',20))
conditionLabel.pack()

app.mainloop()