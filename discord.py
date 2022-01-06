from http.client import HTTPSConnection 
from sys import stderr
from json import dumps
from time import sleep

# if it doesn't work, try downloading the missing files with the 'npm install' command
# if it doesn't work, try downloading the missing files with the 'npm install' command
# if it doesn't work, try downloading the missing files with the 'npm install' command
# if it doesn't work, try downloading the missing files with the 'npm install' command
 
header_data = { 
    "content-type": "application/json", 
    "user-agent": "discordapp.com", 
    "authorization": "token", # write your account token here
    "host": "discordapp.com", 
    "referer": "https://discord.gg/8TMwJZMX" # this is irrelevant
} 
 
def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 
 
def send_message(conn, channel_id, message_data): 
    try: 
        conn.request("POST", f"/api/v6/channels/{channel_id}/messages", message_data, header_data) 
        resp = conn.getresponse() 

        if 199 < resp.status < 300: 
            print("Message sent!")
            pass 
 
        else: 
            stderr.write(f"HTTP received {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("""

            Message Failed to send!

            """) 
 
def main(): 

    id = "906665590649921558"
    message_data = { 
        "content": """

!d bump\n



        """, #if this  consists of more than one line, use '\n'
        "tts": "false", 
    } 


    send_message(get_connection(), id, dumps(message_data))

    sleep(7210) #if you want more channels, duplicate these two lines

    send_message(get_connection(), id, dumps(message_data))

    sleep(7250)

    send_message(get_connection(), id, dumps(message_data))

    sleep(7290)

    send_message(get_connection(), id, dumps(message_data))

    sleep(7276)

    send_message(get_connection(), id, dumps(message_data))

    sleep(7246)



while True:
    main()
    sleep(5)
     # 1 = 1 sec, 60 = 1 minute, 300 = 5 minutes