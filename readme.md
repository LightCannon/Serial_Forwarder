# Serial Port Forwarder
## Requirements:
1-Python 3.7+
2-Virtual COM emulator (I used VSPD, download from https://www.eltima.com/products/vspdxp/)

## Steps to run
1- Open VSPD and create a serial port bundle (of type Pair). Pair means that whatever sent on any of paired ports will be forwarded to the other. Name the ports COM22 and COM23
2- Install the requirements by running:
    pip install -r requirements.txt

3- run: python main.py COM22 COM23

## Sample output
Message "Received data: Hello from port COM22" should be continously printed on the screen.
