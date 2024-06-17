## Simplify inheritance relationship | Introduce polymorphishm

In the previous challenge we introduced multiple levels of abstraction to reduce code coupling.
We created the `HttpClient`, `RequestsClient` and `WeatherApi` to manage access to the api service.
With this implementation the `WeatherApi` is agnostic to the library (approach) we use to connect to the api 
service of `OpenWeatherMap`. This way it becomes very easy to replace `requests` librady with a different one if needed.

## Challenge

For this challenge you need to refactor the given code so that the inheritance relationship is simplified.
There's many ways to do so, but a good approach would be to further decouple the `WeatherApi` to work with any
`HttpClient` object and not only with `RequestClient` which is a subclass of the former. 

Hint: Try using a higher order function to avoid the need to pass the an http_client in the WeatherApi constructor.





