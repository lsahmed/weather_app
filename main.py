# Create a weather app using api's
import requests

api_key = '5b18ca7cf1df4a78a42155718242007'
city = input("Enter city: ")
country = input("Enter Country: ")
response = requests.get(f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city},{country}")
status = response.status_code
data = response.json()

if(status==200):
    # All inputs from API
    city = data["location"].get("name")
    region = data["location"].get("region")
    country = data["location"].get("country")
    # Weather inputs
    temp = data["current"].get("temp_c")
    condition = data["current"]["condition"].get("text")
    humidity = data["current"].get("humidity")
    last_updated = data["current"].get("last_updated")

    def dayornight():
            diurnal = ""
            if(data["current"].get("is_day")==0):
                diurnal = "Night"
            elif(data["current"].get("is_day")==1):
                diurnal = "Day"

            return diurnal
    
    diu = dayornight()
    print(f"\nShowing current weather for {city},{region},{country}")
    print(f"temprature: {temp}\ncondition: {condition}\nhumidity: {humidity}\nDiural_cycle: {diu}\nlast updated on {last_updated}")

else:
     raise Exception("Failed to fetch weather data")
