## Convert payments to use the plugin architecture

The plugin architecture allows to customize an application to meet specific needs without requiring to
(necessarily) have programming knowledge or modify the application's core code. It also makes it easier for developers
to maintain and update the software application, as changes made to the core code are less likely to affect the
plugins.

## Challenge

For this challenge you need to convert the payment strategy pattern to the plugin pattern. We recommend creating a
separate folder to create all the scripts and subdirectories inside as you will need to create many new scripts.

\*Important notes:

1. Make sure the naming of the modules and the class names is consistent since it will be used as an
   argument in the `set_payment_strategy` method.
2. Add the folder where the plugins reside in your python path in order for the `importlib` to be able to import it.
   You can use the `sys.path.append` method of the `sys` library for that.
3. We also created a function to convert the module name string to the class name string for using only the module name
   string as input for the `set_payment_strategy` method. This is connected to point 1.
