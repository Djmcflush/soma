import socket
import os
import argparse
from multiprocessing import Process

BUFFER_SIZE = 4096

# Function to act as the source of the data
# Simulates streaming from Point A (Source)
def data_source(file_path, host='localhost', port=5000):
    # Create a socket to send data
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f"Source: Waiting for connection on {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print(f"Source: Connected to {addr}")
            with open(file_path, 'rb') as f:
                while chunk := f.read(BUFFER_SIZE):
                    conn.sendall(chunk)
    print("Source: Finished streaming the file")

# Function to act as the receiver of the data
# Simulates streaming to Point B (Destination)
def data_destination(save_path, host='localhost', port=5000):
    # Create a socket to receive data
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f"Destination: Connected to {host}:{port}")
        
        with open(save_path, 'wb') as f:
            while True:
                data = s.recv(BUFFER_SIZE)
                if not data:
                    break
                f.write(data)
    print("Destination: File received successfully")

def main():
    parser = argparse.ArgumentParser(description="Soma: Stream data from one place to another.")
    parser.add_argument('source', help='Path to the source file')
    parser.add_argument('destination', help='Path to save the received file')
    parser.add_argument('--host', default='localhost', help='Host address')
    parser.add_argument('--port', type=int, default=5000, help='Port number')

    args = parser.parse_args()

    source_file_path = args.source
    destination_file_path = args.destination
    host = args.host
    port = args.port

    # Validate source file exists
    if not os.path.exists(source_file_path):
        print(f"Error: Source file '{source_file_path}' does not exist.")
        return

    # Start the source and destination processes to stream data
    p1 = Process(target=data_source, args=(source_file_path, host, port))
    p2 = Process(target=data_destination, args=(destination_file_path, host, port))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

    # Verify if the streamed data is identical
    if os.path.exists(destination_file_path):
        with open(source_file_path, 'rb') as f1, open(destination_file_path, 'rb') as f2:
            if f1.read() == f2.read():
                print("Success: The data was streamed correctly from Point A to Point B")
            else:
                print("Error: Data mismatch detected")

if __name__ == "__main__":
    main()
