## Add more payments to shopping cart with strategy pattern

The strategy pattern is a design pattern that allows you to define a family of algorithms (strategies) and make
them interchangeable within an object at runtime. In other words, it lets you define a set of related algorithms and
encapsulate each one in a separate class. The object can then use one of these algorithms (strategies) without
knowing the details of how the algorithm works or how it's implemented. This pattern promotes the principle of
"composition over inheritance", which means that behavior should be composed dynamically at runtime rather
than being hard-coded into classes through inheritance. This makes the code more flexible, extensible,
and easy to maintain.

## Challenge

For this challenge you need to add some extra functionality to the shopping cart app to allow for different types of
payments using the strategy pattern.
