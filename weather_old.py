import tkinter as tk
from tkinter import messagebox
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.city_label = tk.Label(root, text="Enter city name:")
        self.city_label.pack()

        self.city_entry = tk.Entry(root, width=50)
        self.city_entry.pack()

        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack()

        self.result_label = tk.Label(root, text="", wraplength=400)
        self.result_label.pack()

    def get_weather(self):
        city = self.city_entry.get()
        if city:
            api_key = "e65bfef89b563ade7dcbe09750dd8e4c" 
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                weather_description = data['weather'][0]['description']
                temperature = data['main']['temp']
                self.result_label.config(text=f"Weather in {city}: {weather_description}, Temperature: {temperature}°C")
            else:
                messagebox.showerror("Error", "City not found.")
        else:
            messagebox.showwarning("Warning", "You must enter a city name.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
