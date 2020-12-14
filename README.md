# AutomationHybridModel
Automation project with mqtt broker connection and selenium webdriver

How to run the project (Question 1) ::
1. install python version 3.9.
2. install pip as well (though it happens automatically most of the times )
3. set the python bin directoy to path environment variable.
4. Check the verion of both Python and pip.
5. install pipenv by typing pip install pipenv
6. Install pycharm (did not got much time to work on gauge as faced an issue with my mac with gauge installation)(Not required can run from commandline as well)
7. download the project and assign it to pipenv interpreter.
8. install all dependencies by typing pipenv sync (it installs everything from pipenv.lock , do not install anything from pipfile always use pipfile.lock.)
9. now run it by typing python main.py or go to the main.py from pycharm and right click and select Run

Project Structure ::
1. I have created pipfile and pipfile.lock for dependency management.
2. paho-mqtt for broker connection, selenium for webui automation, config-parser for parsing ini files and webdriver-manager for automatically driver installation 
2. setup.ini file for environment selection.
3. utilities folder with all the broker connection, base driver instantiation and browser selection .
4. webui folder with all the page related Xpaths and operations.
5. resources folder with Pem files to connect to mqtt broker server.

N.B :: Could not implement BDD framework due to shortage of time.

Question 2 ::
I have created a file with the name question2.txt and there I have mentioned the scenarios for the 2nd question of the assignment.

