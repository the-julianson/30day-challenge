## Introduce abstraction to reduce coupling

Introducing (levels of) abstraction allows the code (classes) to be more agnostic with each other, thus reducing
coupling, which makes code overall more readable, maintainable and understood better both in depth, but also from a
higher (conceptual) level.

For running the current code, you will need to have a free API key from openweathermap.org platform. That requires
creating an account and you automatically receive one after you confirm your e-mail address. You can follow
instructions here: https://openweathermap.org/appid#signup. Caution, it might take some few minutes before the API key
is activated on their servers.

You will also need to install `requests` package in your python environment.

*For now I have left my own personal API key in the run script for testing purposes.

## Challenge

For this challenge you need to refactor the given code class so that the `WeatherService` becomes agnostic to the
`requests` library.

In the current setup the `WeatherService` fetches the current weather forecast of a given city using the OpenWeatherMap API.
However, the `WeatherService` class is coupled to the `requests` library and the specific API endpoint of OpenWeatherMap.
This makes it hard to change the library or the API provider in the future. To reduce coupling and improve encapsulation,
we can use abstraction to separate the `WeatherService` class from the requests library and the OpenWeatherMap API.


Hint: We can create a separate `HttpClient` class that defines the get method for fetching data from an API,
and a `WeatherApi` class that defines the specific API endpoint and data parsing logic.

*The hint can either be included or omitted, depending how challenging we wish to make this.






