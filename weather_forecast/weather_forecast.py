#Weather Forecast
import tkinter, requests
from tkinter import BOTH, IntVar
from PIL import ImageTk, Image
from io import BytesIO

#Define window
root = tkinter.Tk()
root.title('Weather Forecast')
root.iconbitmap('weather.ico')
root.geometry('400x400')
root.resizable(0,0)

#Define fonts and colors
sky_color = "#76c3ef"
grass_color = "#aad207"
output_color = "#dcf0fb"
input_color = "#ecf2ae"
large_font = ('SimSun', 14)
small_font = ('Simsun', 10)

#Define functions
def search():
    """Use open ewather api to look up current weather conditions given a city/ city, country"""
    global response

    #Get API response
    #URL and my api key....USE YOUR OWN API KEY!
    url = 'https://api.openweathermap.org/data/2.5/weather'
    api_key = 'c3f0bcebfb0f1fed2cc812b63dc1fda5' #USE YOUR OWN API KEY

    #Search by the appropriate query, either city name or zip
    if search_method.get() == 1:
        querystring = {"q":city_entry.get(), 'appid':api_key, 'units':'imperial'}
    elif search_method.get() == 2:
        querystring = {"zip":city_entry.get(), 'appid':api_key, 'units':'imperial'}

    #Call API
    response = requests.request("GET", url, params=querystring)
    response = response.json()
    #Example response return
    #print(response)
    '''
    {
    'coord': {'lon': 80.2785, 'lat': 13.0878}, 
    'weather': [{'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50n'}], 
    'base': 'stations', 
    'main': {'temp': 77, 'feels_like': 82.78, 'temp_min': 77, 'temp_max': 77, 'pressure': 1013, 'humidity': 83},
    'visibility': 5000, 
    'wind': {'speed': 4.61, 'deg': 70},
    'clouds': {'all': 40}, 'dt': 1613942687,
    'sys': {'type': 1, 'id': 9218, 'country': 'IN', 'sunrise': 1613955522, 'sunset': 1613997987}, 
    'timezone': 19800, 
    'id': 1264527, 
    'name': 'Chennai', 
    'cod': 200
    }
    '''
    get_weather()
    get_icon()


def get_weather():
    """Grab information from API response and update our weather labels."""
    #Gather the data to be used from the API response
    if response['cod'] == 200:
        city_name = response['name']
        country_code = str(response['sys']['country'])
        city_lat = str(response['coord']['lat'])
        city_lon = str(response['coord']['lon'])

        main_weather = response['weather'][0]['main']
        description = response['weather'][0]['description']

        temp = str(response['main']['temp'])
        feels_like = str(response['main']['feels_like'])
        temp_min = str(response['main']['temp_min'])
        temp_max = str(response['main']['temp_max'])
        humidity = str(response['main']['humidity'])
    else:
        if search_method.get() == 1:
            city_name = 'Try Zipcode'
        else:
            city_name = 'Try City,CountryCode'
        country_code,city_lat, city_lon, main_weather, description, temp, feels_like, temp_min, temp_max, humidity = '','','','','','','','','',''

    #Update output lables
    city_info_label.config(text=city_name + "," + country_code + " (" + city_lat + ", " + city_lon + ")")
    weather_label.config(text="Weather: " + main_weather + ", " + description)
    temp_label.config(text='Temperature: ' + temp + " F")
    feels_label.config(text="Feels Like: " + feels_like + " F")
    temp_min_label.config(text="Min Temperature: " + temp_min + " F")
    temp_max_label.config(text="Max Temperature: " + temp_max + " F")
    humidity_label.config(text="Humidity: " + humidity)
        

def get_icon():
    """Get the appropriate weather icon from API response"""
    global img

    #Get the icon id from API response.
    icon_id = response['weather'][0]['icon']

    #Get the icon from the correct webiste
    url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=icon_id)

    #Make a request at the url to download the icon; stream=True automatically dl
    icon_response = requests.get(url, stream=True)

    #Turn into a form tkinter/python can use
    img_data = icon_response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))

    #Update label
    photo_label.config(image=img)

#Define layout
#Create frames
sky_frame = tkinter.Frame(root, bg=sky_color, height=250)
grass_frame = tkinter.Frame(root, bg=grass_color)
sky_frame.pack(fill=BOTH, expand=True)
grass_frame.pack(fill=BOTH, expand=True)

output_frame = tkinter.LabelFrame(sky_frame, bg=output_color, width=325, height=225)
input_frame = tkinter.LabelFrame(grass_frame, bg=input_color, width=325)
output_frame.pack(pady=30)
output_frame.pack_propagate(0)
input_frame.pack(pady=15)

#Output frame layout
city_info_label = tkinter.Label(output_frame, font=large_font, bg=output_color)
weather_label = tkinter.Label(output_frame, font=small_font, bg=output_color)
temp_label = tkinter.Label(output_frame, font=small_font, bg=output_color)
feels_label = tkinter.Label(output_frame, font=small_font, bg=output_color)
temp_min_label = tkinter.Label(output_frame, font=small_font, bg=output_color)
temp_max_label = tkinter.Label(output_frame, font=small_font, bg=output_color)
humidity_label = tkinter.Label(output_frame, font=small_font, bg=output_color)
photo_label = tkinter.Label(output_frame, bg=output_color)

city_info_label.pack(pady=8)
weather_label.pack()
temp_label.pack()
feels_label.pack()
temp_min_label.pack()
temp_max_label.pack()
humidity_label.pack()
photo_label.pack(pady=8)

#Input frame layout
#Create input frame buttons and entry
city_entry = tkinter.Entry(input_frame, width=20, font=large_font)
submit_button = tkinter.Button(input_frame, text='Submit', font=large_font, bg=input_color, command=search)

search_method = IntVar()
search_method.set(1)
search_city = tkinter.Radiobutton(input_frame, text='City name[,Country Code]', variable=search_method, value=1, font=small_font, bg=input_color)
search_zip = tkinter.Radiobutton(input_frame, text="Zip[,Country Code]", variable=search_method, value=2, font=small_font, bg=input_color)

city_entry.grid(row=0, column=0, padx=10, pady=(10,0))
submit_button.grid(row=0, column=1, padx=10, pady=(10,0))
search_city.grid(row=1, column=0, pady=2)
search_zip.grid(row=1, column=1, padx=5, pady=2)


#Run root window's main loop
root.mainloop()
