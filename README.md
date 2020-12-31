# Python Automated WhatsApp Messages Sender

This script sends WhatsApp messages automatically from WhatsApp web application to contacts. The name of the contact, their phone number and the message you want to send to all of them at once are saved in an excel file.

## Prerequisites

In order to run this script, you’ll need to have the following packages installed on your computer. 
* Python 3.8
* Selenium Web Driver
* Google Chrome
* Pandas
* Xlrd
* Selenium
You will also need an excel file that contains 3 columns- the name of your contact, their phone number and the message we want to send to all of them


## Approach
* User scans web QR code to log in into the WhatsApp web application.
* The script reads a customized message from excel sheet.
* The script reads rows one by one and searches that contact number in the web search box if the contact number found on WhatsApp then it will send a configured message otherwise It reads next row. 
* Loop execute until and unless all rows complete.


https://medium.com/@insecurecoders/how-to-automate-whatsapp-to-send-personalized-messages-to-100-contacts-using-python-e7cac37dd7




http://labs.brotherli.ch/vcfconvert/
