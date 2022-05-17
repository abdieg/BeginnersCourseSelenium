DEMO: https://youtu.be/IomEm9EuzP4

GITHUB: https://github.com/abdieg/BeginnersCourseSelenium

Common folder contains CommonFunctions, Constant and Locators files.
- Constant.py has the general configuration files like users, passwords and timeouts.
- Locators.py has the XPATH of all elements in the page. Although it is not a fully implemented Page Object Model, it makes the scenarios easier to read.
- CommonFunctions.py has general functions used through all test cases such as clicking, writing or waiting for elements.

Under Tests folder there are 3 files: Launch, Scenarios and Suite.
- Launch.py has a general class which contains the logic to set webdriver configuration to be executed on each test scenario.
- Scenarios.py contains all test cases to be executed.
- Suite.py has the capability to load different clases and run specific files

To use in console:
1. Install Python
2. Execute "pip install selenium"
3. In a CMD run "python Suite.py"