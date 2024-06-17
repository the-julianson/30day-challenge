## Fix don't repeat yourself violation

The Don't Repeat Yourself (DRY) principle is a coding principle that aims to
reduce repetition in code. It suggests that when writing code, you should
avoid duplicating code logic or functionality in multiple places, and instead,
create reusable code elements that can be called and reused throughout your
codebase.

For example, let's say you are creating a program that needs to convert
temperatures from Fahrenheit to Celsius in multiple places. You could write the
conversion formula each time it is needed, but this would result in repeating
the same code logic over and over again. Instead, you could create a function
that contains the conversion formula, and call that function wherever
temperature conversion is needed. This way, if you need to update the formula
or add additional functionality, you only need to make the change in one place,
and it will be reflected throughout your codebase.

One really important aspect you need to pay attention is to standardize (as strictly as possible)
the inputs and outputs of the function, so that it compatible with the data types / structures
across the various places that it will be called.

By following the DRY principle, you can make your code more efficient,
easier to maintain, and less prone to errors caused by repetition or inconsistencies.

## Challenge

For this challenge you need to refactor the given code in `dry_violation.py` in some places (you will have to figure
out which) in order to avoid code repetition.
