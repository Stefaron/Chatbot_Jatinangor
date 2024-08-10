import aiml
import time

# Buat kernel dan pelajari berkas AIML
kernel = aiml.Kernel()
kernel.learn("start.xml")
kernel.respond("aiml a")

while True:
    user_input = input("USER > ")
    response = kernel.respond(user_input)
    if response:
        print("Bot > ", response)
    else:
        print("Bot > Maaf, saya kurang mengerti.")
