import aiml
# membuat kernel dan mempelajari berkas AIML
kernel = aiml.Kernel()
kernel.learn("mulai.xml")
kernel.respond("AIML A")
while True:
    print(kernel.respond(input("Tuliskan pesan di sini: >> ")))