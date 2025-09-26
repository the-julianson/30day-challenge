import os
from importlib.util import module_from_spec, spec_from_file_location
from typing import Protocol
from decimal import Decimal

# Define what a Plugin looks like 

# Define a way to import plugins from modules, even if they are not yet created

# Define methods to load plugins, show plugins, and get a specific plug in 


class PaymentPlugin(Protocol):
    # Writing a class with abstract methods (meaning it doesn't need an instance)
    # Is similar to have a module with 2 methods
    @staticmethod
    def get_payment_method() -> str: ...

    @staticmethod
    def process_payment(total: Decimal) -> None: ...

PLUGINS: dict[str, PaymentPlugin] = {}


def import_module(name: str, path: str) -> PaymentPlugin:
    """This uses importlib to import a module from file"""

    # 1. Get the "Blueprint" for the module
    spec = spec_from_file_location(name, path)
    if not spec:
        raise ImportError(f"Could not import {name} from {path}")
    # 2. Create an empty module object from the blueprint
    module: PaymentPlugin = module_from_spec(spec)  # type: ignore
    # 3. Execute the code from the file to populate the module
    spec.loader.exec_module(module)  # type: ignore
    return module


def load_plugins_from_folder(folder: str) -> None:
    """Helper function to loads all modules from a folder"""
    # 1. Scan the directory recursevely using walk
    for root, _, files in os.walk(folder):
        for file in files:
            if not file.endswith(".py"):
                continue

            # remove .py en the module
            module_name = file[:-3] 
            # 2. Import the file as a module
            module_path = os.path.join(root, file)
            module = import_module(module_name, module_path)
            # 3. Registering the Plugin
            PLUGINS[module.get_payment_method()] = module

 
def get_plugin(name: str) -> PaymentPlugin:
    """Gets a plugin by name"""
    return PLUGINS[name]

def plugin_exists(name: str) -> bool:
    """Checks that plugin exists"""
    return name in PLUGINS

def all_plugins() -> list[str]:
    """Gets all plugins names."""
    return list(PLUGINS.keys())
