# 2020-Pikachu-volleyball

How to run this game 

*Clone the whole file

	git clone https://github.com/NTUEE-ESLab/2020-Pikachu-volleyball.git

*Start the server

	cd 2020-Pikachu-volleyball
	
To play at the left side

	python3 ws_server_1p.py
	
Or you can play at right side

	python3 ws_server_2p.py
	
If you want to play with yuor friend, open another terminal and run both 1p & 2p. Then turn the STM32 on.

*Start the game 
You may need pixi.js to execute the program. 
Go https://github.com/pixijs/pixi.js/ to get more information. 
You need to open another terminal to start the game.
	
	cd pika
	npm start
	
Then you can open Chrome and and go to localhost http://localhost:8080/ to start it. 
If you go to the above website and see nothing, go to terminal to see where the program runs. 
If you have some problems when running the program on Chrome, you can press F12 to see more information.
Also, you can see whether your server is connected.
If the F12 console told you "WebSocket connection to 'ws://127.0.0.1:8866/' failed: Unknown reason",
you need to turn off the localhost and npm start again.
	
*STM32

1. Download mbedos 6.0.
2. Create a new program and load mbed-os-example-wifi as your active program.
3. Import sensor library to your program. ==> https://os.mbed.com/teams/ST/code/BSP_B-L475E-IOT01/#bfe8272ced90
4. Move and substitue main.cpp and mbed_app.json to your active program.
5. Change ip address, port in main.cpp and wifi-ssid, wifi-password in mbed_app.json according to your network environment.
6. Complie the program to your STM32.

If mbed-os want to change your device setting, click No.
	
	
	

