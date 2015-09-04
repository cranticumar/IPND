import os, urllib

def read_file():
    text = open(os.path.join(os.getcwd(), 'TextFile1.txt'))
    content = text.read()
    print content
    text.close()
    profanity_check(content)

def profanity_check(text):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text)
    profanity = connection.read()
    if "true" in profanity:
        print "Profanity Alert!!"
    print "Good to Go!!"
    connection.close()

read_file()