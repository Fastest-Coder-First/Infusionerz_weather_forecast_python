# Infusionerz_weather_forecast_python
This weather forecasting tool is a Python application that fetches weather data from the OpenWeatherMap API and displays the current temperature, humidity, pressure, and other relevant information for a specified location, github copilot helped us a lot like 90% of our code suggestions was done by it and that too very accurate on that part, that enhanced our code to run well and on time too.

## Uniqueness in our project:-
### Backend -> We made our own api using Model fast Api -> that itself uses 3 api from OpenWeatherMap API.
### Frontend -> We made frontend part using CustomTkinter
### Prerequisites
### To run this application, you need to have the following installed on your system:
- Python 3 (version 3.7 or higher)
- Requests library (can be installed using `pip install requests`)

### Architectural flow
![image](https://github.com/Fastest-Coder-First/Infusionerz_weather_forecast_python/assets/114357685/d27e5688-e5f8-4869-a16c-0ac43e5996c6)

  
1. When prompted, enter the location for which you want to fetch the weather data. You can enter the country name   (e.g., "india").
2.  The application will connect to our own API.
3.  our own api is: url = f"{base_url}/weather?city_name={city_name}&country_code={country_code}", where base_url = http://localhost:8000
4.  The fetched weather data, including the current temperature, humidity, pressure, and other relevant information, will be displayed on Our Command line,
    which is made using  customtkinter. 
5. 1 own backend api parameters passed: city_name, country_code


get_city_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&limit=1&appid={api_key}"

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

6. The application will terminate after displaying the weather information. If you want to fetch the weather data for another location, you can run the application again and follow the same steps.


### GitHub Copilot
This project was developed with the assistance of GitHub Copilot, an AI-powered code completion tool.it helps automate the writing of code by providing suggestions for whole lines or blocks of code based on the context and patterns it has learned from vast amounts of publicly available code.
1. it provide suggestions for making HTTP requests using the requests library. It helped in generating code snippets for handling API endpoints, query parameters, and API key authentication.
2. Copilot suggested docstrings for functions, including the route handler function in FastAPI.
3. it has provide suggestions for error handling and exception handling. It can help generate code snippets for handling network errors, JSON parsing errors.

## Screenshots and Video of our command line tools :-

https://drive.google.com/file/d/1Oe3EEPG6OW5YrDTY8w37vL8Eo7xrUCQP/view?usp=drive_link
https://drive.google.com/file/d/1oFq7hi7l--iWbepLrXNt9e-4oRJDIfQg/view?usp=drive_link

![image](https://github.com/Fastest-Coder-First/Infusionerz_weather_forecast_python/assets/64723994/318d65a2-be2d-41e7-a4d6-f609d7321890)
![image](https://github.com/Fastest-Coder-First/Infusionerz_weather_forecast_python/assets/64723994/9321b2a9-2a02-4391-839b-7ad0a9c867bb)


## link of the video:-
https://drive.google.com/file/d/1SCA468pKQyg2mipZw1gJTfa8ewDI2VQd/view?usp=drive_link


https://github.com/Fastest-Coder-First/Infusionerz_weather_forecast_python/assets/64723994/4297d94a-a321-455c-9035-e12390ec9f62

