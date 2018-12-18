# lab_7b

Quick Instructions:
Open the code with Arduino. and make sure the hardware is connected correctly with no loose pins.
Make sure GPIO_0 is plugged to ground and the Arduino has its reset pin set to ground, so that the ESP8266 can be flashed.

Setup:
In Arduino preferences, make sure to add "http://arduino.esp8266.com/stable/package_esp8266com_index.json" to "Additional Boards Manager URLs" to pull the library from esp8266 github. Then in Tools/Board/Boards_Manager, look for esp8266 and install the 2.4.2 version. Once complete, close it, and go back to Tools/Board and make sure to select "Generic ESP8285 Module" and set the flash baud rate to 115200. Open serial monitor and set it to 9600 baud and both "NL & CR".

Running:
Once setup, upload the code. After flashing, the serial monitor will start outputting data recieved from the board. To hook it with the Xbee, connect the TX of the ESP to the TX of the Xbee and the RX of the ESP to the RX Xbee. With that, the Xbee will now be sending data to the server every 5 seconds.


Video 1: https://drive.google.com/open?id=1jEZNCM8rESPkEd-ywBBBTYvadp-8cXUD
Video 2: https://drive.google.com/open?id=1xCJQUs-lTScGYBAcP4b6jp-TAsxHhnFD
