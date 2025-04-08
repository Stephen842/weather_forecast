# Weather Now

__Overview__

This is a weather forecast web application built using Django, HTML, CSS, TailwindCSS, and the OpenWeather API. The app allows users to search for any city or town in the world and get real-time weather data, including temperature, humidity, pressure, and weather conditions. The background images dynamically change based on the time of day, enhancing the user experience.

__Features__

1. City Search: Users can search for any city or town to get its current weather conditions.

2. Responsive Design: The app is fully responsive, providing a smooth experience across devices (desktop, tablet, mobile).

3. Dynamic Background: Background images change dynamically based on the time of day, creating an immersive experience.

4. Real-Time Data: Fetches live weather data from the OpenWeather API, ensuring accurate and up-to-date information.

5. Version Control: The project uses Git and GitHub for version control, enabling easy collaboration and version management.

__Technologies Used__

1. Backend: Django (Python)

2. Frontend: HTML, CSS, TailwindCSS

3. API: OpenWeather API for weather data

4. Version Control: Git, GitHub

__Installation__

To get started with this project locally, follow these steps:

**Prerequisites**

1. Python 3.x

2. Django 4.x or above

3. A GitHub account for version control (optional)

__Steps__

*Clone the repository:*

    git clone https://github.com/your-username/weather-forecast-app.git

    cd weather-forecast-app

*Set up a virtual environment:*

    python3 -m venv venv

    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

*Install the required dependencies:*

    pip install -r requirements.txt

*Set up environment variables:*

    Create a .env file and add your OpenWeather API key:

        OPENWEATHER_API_KEY=your-api-key-here

*Run the Django migrations:*

    python manage.py migrate

*Start the development server:*

    python manage.py runserver

Open your browser and go to http://127.0.0.1:8000 to access the app.


__Usage__

1. Open the app in your browser.

2. Enter the name of a city or town in the search bar.

3. The weather information for that location will be displayed, including:

    Current temperature

    Humidity

    Pressure

    Sunrise/Sunset times

    Weather conditions (e.g., sunny, cloudy)

4. The background will automatically adjust based on the time of day (morning, afternoon, evening).

__Limitations__

The app uses the OpenWeather API, which has limitations for free accounts (only one city allowed). To work around this limitation, cities are stored in the database, and the search feature dynamically replaces the city stored in the database to fetch weather data for any city worldwide.

Extended weather forecasts (future forecasts) are available only with a paid OpenWeather account. Currently, only current weather conditions are fetched.

__Future Improvements__

Upgrade to a paid OpenWeather API account to include extended forecasts.

__License__

This project is licensed under the MIT License - see the LICENSE file for details.

__Acknowledgements__

The app uses the OpenWeather API for weather data.

Thanks to Django, TailwindCSS, and all contributors who make web development easier and more enjoyable.