To use the project, first download the following libraries using pip in the command prompt-
pyautogui and
psutil.
After you are done downloading, locate the zip file you have downloaded and create shortcuts for the mouse and support file. Cut the shortcuts and paste them into the startup folder of your computer.
NOTE: Works only in Windows 11.
How it works:
The program lowers the brightness and volume of the computer when it reaches 20 percent or lower.
It uses pyautogui to move the mouse to change the brightness and volume and uses psutil to check the battery percentage.
A function checks and returns true if the battery percentage is 20 percent or lower.
An if statement checks if the function is returning a true bool and if it does, then it shows a message and moves the mouse.
Tkinter is used to show the message.
The mouse file has the .pyw extension so that the script can run continuously in the background 
A text file is used to keep track of how many times the program has been run because when the computer reaches 20 percent or lower, it executes the program but since it is running continuously in the background, it constantly runs over and over again.
The support file is used to change the contents of the text file to zero because, before shutdown of device, the text file's content can above zero, so if the computer again reaches 20 percent or lower, the program won't run because the file's contents are above 0
If anyone has any suggestions or problems, please comment
