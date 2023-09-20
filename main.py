import threading
import serial
import serial.tools.list_ports
import time
import sys

def discover_com_ports():
    """Discover and print all available COM ports."""
    ports = serial.tools.list_ports.comports()
    if not ports:
        print("No COM ports available.")
        return 0
    else:
        print("Available COM ports:")
        for port in ports:
            print(port.device)
        return len(ports)

def write_to_serial(port, data):
    """Thread function to write data to the serial port."""
    try:
        ser = serial.Serial(port, baudrate=9600, timeout=1)
        while True:
            ser.write(data.encode())
            time.sleep(1)
    except serial.SerialException as e:
        print(f"Failed to write to serial port: {e}")

def read_from_serial(port):
    """Thread function to read data from the serial port."""
    try:
        ser = serial.Serial(port, baudrate=9600, timeout=1)
        while True:
            data = ser.readline().decode().strip()
            print(f"Received data: {data}")
    except serial.SerialException as e:
        print(f"Failed to read from serial port: {e}")

def main():
    n_devices = discover_com_ports()
    if n_devices == 0:
        sys.exit(1)

    # Assuming there are at least 2 COM ports available, 
    # modify the port names as needed (22->23 in my case)
    port1 = sys.argv[1]
    port2 = sys.argv[2]

    # Create threads for writing and reading serial data
    write_thread = threading.Thread(target=write_to_serial, args=(port1, f"Hello from port {port1}!"))
    read_thread = threading.Thread(target=read_from_serial, args=(port2,))

    # Start the threads
    write_thread.start()
    read_thread.start()

    # Wait for threads to complete
    write_thread.join()
    read_thread.join()

if __name__ == "__main__":
    main()