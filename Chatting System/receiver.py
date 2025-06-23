import socket

try:
    # Creating socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Socket created")

    # Receiver's IP address (your own IP) and port
    ip_add = "192.168.162.115"  
    port = 8888
    complete_add = (ip_add, port)

    s.bind(complete_add)
    print(f"Socket bound to {complete_add}")

    while True:
        message, sender_address = s.recvfrom(1024)
        print("Raw message:", message)
        print("Sender address:", sender_address)
        decoded_msg = message.decode("ascii")
        print("Message:", decoded_msg)

except Exception as e:
    print("An error occurred:", e)