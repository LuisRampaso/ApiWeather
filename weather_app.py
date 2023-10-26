import requests
import json
import tkinter as tk

API_KEY = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your OpenWeather API key

def get_weather_forecast():
    # Reset the error message
    result_label.config(text="")

    city = city_entry.get()
    
    if not city:
        result_label.config(text="Please enter a valid city name.")
        return

    try:
        # Make a request to the OpenWeather API
        link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=pt_br"
        response = requests.get(link)
        data = response.json()

        if response.status_code == 200:
            # Extract weather data
            description = data['weather'][0]['description'].split(',')[0].capitalize()
            city_formatted = city.capitalize()
            temperature_kelvin = data['main']['temp']
            temperature_min_kelvin = data['main']['temp_min']
            temperature_max_kelvin = data['main']['temp_max']
            
            # Convert temperatures from Kelvin to Celsius
            temperature_celsius = temperature_kelvin - 273.15
            temperature_min_celsius = temperature_min_kelvin - 273.15
            temperature_max_celsius = temperature_max_kelvin - 273.15

            # Update the text labels in the interface
            city_label.config(text=city_formatted)
            description_label.config(text=description)
            temperature_label.config(text=f"Temperature: {temperature_celsius:.0f}°C")
            temperature_min_label.config(text=f"Min Temp: {temperature_min_celsius:.0f}°C")
            temperature_max_label.config(text=f"Max Temp: {temperature_max_celsius:.0f}°C")
        else:
            # Custom error message
            error_message = "City not found. Please check the city name."
            result_label.config(text=error_message)
    except requests.exceptions.RequestException as e:
        result_label.config(text="Network error. Please check your internet connection.")
    except json.JSONDecodeError as e:
        result_label.config(text="Error decoding the API response.")
    except Exception as e:
        result_label.config(text="An unexpected error occurred.")

# Main window configuration
window = tk.Tk()
window.title("Weather Forecast")

# Set the window's geometry (width x height)
window.geometry("400x400")

# Label for instructions
instructions_label = tk.Label(window, text="Enter the name of your city:")
instructions_label.pack()

# Text entry for the city
city_entry = tk.Entry(window)
city_entry.pack()

# Button "OK" to get the weather forecast
ok_button = tk.Button(window, text="OK", command=get_weather_forecast)
ok_button.pack()

# Labels to display the formatted weather forecast
city_label = tk.Label(window, text="", font=("Helvetica", 16))
city_label.pack()
description_label = tk.Label(window, text="", font=("Helvetica", 14))
description_label.pack()
temperature_label = tk.Label(window, text="", font=("Helvetica", 12))
temperature_label.pack()
temperature_min_label = tk.Label(window, text="", font=("Helvetica", 12))
temperature_min_label.pack()
temperature_max_label = tk.Label(window, text="", font=("Helvetica", 12))
temperature_max_label.pack()
result_label = tk.Label(window, text="", font=("Helvetica", 12))
result_label.pack()

# Start the interface
window.mainloop()
