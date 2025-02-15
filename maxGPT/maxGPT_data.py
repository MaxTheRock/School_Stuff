import time
from colorama import Fore

# Greeting
greeting_input = ["hello", "hi", "hey", "sup","greetings and salutations my kind sir","hii","hiii","hiiii","helloo","ello there mate","hi there","hey there","hello there","hiya","howdy","howdy partner","howdy there","howdy mate","howdy friend","howdy pal","howdy buddy","howdy dude"]
greeting_output = ["Hello, what are you up to?", "Hey, how are you doing?", "Hi, how can I help you?"]

# Farewell
farewell_input = ["bye", "goodbye", "see you later", "take care", "cya","clear","exit","quit","goodbye for now","goodbye for today","goodbye for tonight",]
farewell_output = ["Goodbye, have a great day!", "See you later!", "Bye, take care!"]

# Time
time_input = ["time", "current time", "what's the time", "tell me the time","what time is it","what is the time"]
time_output = time.strftime("%H:%M:%S")

# Confermation
confirm_input = ["yes", "yep", "yeah", "sure", "ok", "okay", "correct", "right","great","thanks","ok thanks"]
confirm_output = ["Great to hear!, if you need any help then just ask", "Awesome! Let me know if you need anything else", "Perfect!, let me know if you need help with anything else"]

# Joke
joke_input = ["joke", "tell me a joke", "say something funny","make me laugh","tell a joke"]
joke_output = ["Why did the scarecrow win an award? Because he was outstanding in his field!", "What do you call a fish wearing a crown? A kingfish!", "Why couldn't the bicycle stand up by itself? It was two tired!", "What do you call a belt made out of watches? A waist of time!","Why did the math book look sad? Because it had too many problems!"]

# Food
food_input = ["jelly","jelly beans","cheese","banana","carrot","beans","potato","apple","brocoli","tomato","peach","burger","fries","chips","cheeze","cheese","cheeseburger","pasta","spaghetti","pizza","cake","ice cream","chocolate","candy","candy cane","candy corn","candy bar","candy apple","candy floss","bread","butter","jam","salad","soup","food"]
food_output = ["Yum! I love that food too!", "That sounds delicious"]

# Spanish
spanish_input = ["hola","adios","tiempo","confirmar","broma","comida","la idioma de espanol es muy carinoso"]
spanish_output = ["Hola, como estas?", "Adios, que tengas un buen dia!", "La hora actual es", "Si, si, si!", "Por que la vaca cruzo la calle? Para llegar al otro lado!", "Me encanta la comida!"]

# Random Letters
letRan_input = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","aa","bb","cc","dd","ee","ff","gg","hh","ii","jj","kk","ll","mm","nn","oo","pp","qq","rr","ss","tt","uu","vv","ww","xx","yy","zz","aaa","bbb","ccc","ddd","eee","fff","ggg","hhh","iii","jjj","kkk","lll","mmm","nnn","ooo","ppp","qqq","rrr","sss","ttt","uuu","vvv","www","xxx","yyy","zzz"]
letRan_output = ["Maybe just typing letters isnt good afterall!"]

# Clear screen
clear_input = ["cls","cl","c","clear"]

# Dumb questions
dumb_input = ["how can i break this code", "are you kaiden???","are you my friend?","fwiend?"]
dumb_output = ["No"]

# How are you?
howAreYou_input = ["how are you?","how are you","hoaw are you","how ae aeaeaeae"]
howAreYou_output = ["I'm very good, how about you!","I am feeling amazing"]