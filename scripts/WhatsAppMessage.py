import pywhatkit
# write the 10 digit mobile number inplace of xxx.. 
# (+91) is country code (add your country code accordingly)
# "This is a message" is the message you want to send
# the last 2 parameters 15, 54 represents hours and minutes (eg, send message at 15hours and 54 minutes)
pywhatkit.sendwhatmsg("+91xxxxxxxxxx", "This is a message", 15, 54)
