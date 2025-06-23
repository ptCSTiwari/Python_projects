import socket

try:
    # Creating socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Socket created successfully")

    ip_add = "192.168.137.176"  # IP of the receiver (no extra space)
    port = 8888
    target_add = (ip_add, port)

    # Input and send message
    body = input("Enter message body: 😒 ")
    encoded_msg = body.encode("ascii")
    s.sendto(encoded_msg, target_add)
    print("Message sent successfully")

    s.close()

except Exception as e:
    print("An error occurred:", e)