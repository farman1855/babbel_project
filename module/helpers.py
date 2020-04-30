from datetime import datetime

myFile = open("/home/farman_ali/append.txt", "a")
myFile.write("\nAccessed on " + str(datetime.now()))
