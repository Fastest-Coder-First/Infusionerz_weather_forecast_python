import tkinter as tk
import customtkinter
import requests
customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.geometry("700x550")

def login():
    print("Test")

frame = customtkinter.CTkFrame(master=root)

frame.pack(pady=20, padx=60, fill="both", expand= True)
label = customtkinter.CTkLabel(master=frame, text="Weather Forecasting Tool", font=('Robot', 24))
label.pack(pady=12, padx=10)
# entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="City")
# entry1.pack(pady=12, padx=10)
Country_combobox_var = customtkinter.StringVar(value="Enter Country")  # set initial value
Country_combobox = customtkinter.CTkComboBox(master=frame,
                                     values=["option 1", "option 2"],
                                     variable=Country_combobox_var,
                                     )
Country_combobox.pack(padx=20, pady=10)

City_combobox_var = customtkinter.StringVar(value="Enter City")  # set initial value


City_combobox = customtkinter.CTkComboBox(master=frame,
                                     values=["option 1", "option 2"],
                                     variable=City_combobox_var)
City_combobox.pack(padx=20, pady=10)

def button_event():

    base_url = "http://localhost:8000"

    # Parameters
    city_name = "Delhi"
    country_code = "IN"

    print(Country_combobox_var, City_combobox_var)

    # Build the URL
    url = f"{base_url}/weather?city_name={city_name}&country_code={country_code}"

    # Send GET request
    response = requests.get(url)
    data = response.json()

    temperature_label.configure(text=f"Temperature is: {data['temperature']}")
    min_temperature_label.configure(text=f"Min Temperature is: {data['temp_min']}")
    max_temperature_label.configure(text=f"Max Temperature is: {data['temp_max']}")
    humidity_label.configure(text=f"Humidity is: {data['humidity']}")
    description_label.configure(text=f"Current weather is: {data['description']}")
    wind_speed.configure(text=f"Wind Speed: {data['wind_speed']}")
    sunrisetime.configure(text=f"Sunrise Time is: {data['sunrisetime']}")
    sunsettime.configure(text=f"Sunset Time is: {data['sunsettime']}")
    
    
    

button = customtkinter.CTkButton(master=frame, text="Get Weather", command=button_event)
button.pack(padx=20, pady=10)

description_label = customtkinter.CTkLabel(master=frame, text="Current weather is: ", font=('Robot', 16), justify = "left")
description_label.pack(pady=10, padx=10)

temperature_label = customtkinter.CTkLabel(master=frame, text="Temperature is: ", font=('Robot', 16), justify = "left")
temperature_label.pack(pady=10, padx=10)

min_temperature_label = customtkinter.CTkLabel(master=frame, text="min_temperature is: ", font=('Robot', 16), justify = "left")
min_temperature_label.pack(pady=10, padx=10)

max_temperature_label = customtkinter.CTkLabel(master=frame, text="max_temperature is: ", font=('Robot', 16), justify = "left")
max_temperature_label.pack(pady=10, padx=10)

humidity_label = customtkinter.CTkLabel(master=frame, text="Humidity is: ", font=('Robot', 16), justify = "left")
humidity_label.pack(pady=10, padx=10)


wind_speed = customtkinter.CTkLabel(master=frame,text="Wind speed is: ", font=('Robot', 16), justify = "left")
wind_speed.pack(pady=10, padx=10)


sunrisetime = customtkinter.CTkLabel(master=frame,text="sunrise time is: ", font=('Robot', 16), justify = "left")
sunrisetime.pack(pady=10, padx=10)


sunsettime = customtkinter.CTkLabel(master=frame,text="sunset time is: ", font=('Robot', 16), justify = "left")
sunsettime.pack(pady=10, padx=10)

root.mainloop()