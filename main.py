import socket
import pyautogui

# Anish Malla: Video on my Youtube channel

SERVER = 'irc.chat.twitch.tv' #The twitch irc chat server we want to connect to
PORT = 6667 # Port we need to connect to
NICKNAME = 'spec_he' #any nick name works
AUTH_TOKEN = '' #Request your authentification token through this: https://twitchapps.com/tmi/
CHANNEL = "#spec_he" #The channel you want to connect to

# Connecting to the server
sock = socket.socket() #create a socket object
sock.connect((SERVER, PORT)) # connecting to the server and port
sock.send(f"PASS {AUTH_TOKEN}\nNICK {NICKNAME}\nJOIN {CHANNEL}\n".encode('utf-8')) #Credentials you need to give inorder to connect

def check_for_messages():
    """"
    This function checks for any responses we get from the server.
    We need to decode the information as we get it in bytes.
    If the server send PING we need to respong with PONG inorder to let it know that we are still using the connection
    In the else statement we check if either q w e r d f have been pressed in that case we "press" that button
    """
    resp = sock.recv(1024).decode('utf-8')
    print(resp)
    if resp.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))
    else:
        message = resp.split(":")[2].split("\r\n")[0]
        message = message.lower()
        if message == "q":
            pyautogui.press('q')
        if message == "w":
            pyautogui.press('w')
        if message == "e":
            pyautogui.press('e')
        if message == "r":
            pyautogui.press('r')
        if message == "f":
            pyautogui.press('f')
        if message == "d":
            pyautogui.press('d')

def send_message(socket, message):
    """
    we send messages to the server and in order to do so we need to encode the messages and send it in a specific format
    """
    msg = f"PRIVMSG {CHANNEL} :{message}"
    socket.send((f"{msg}\n").encode('utf-8'))

send_message(sock, "The bot has joined")
send_message(sock, "Here's how it works: you can control my abilities(q, w, e, r) and by summoner spells (d, f) by typing that letter in chat and sending it")

while True:
    """
    We keep checking for messages and performing whatever the chat says until we stop the program
    """
    check_for_messages()
