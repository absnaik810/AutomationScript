import schedule
import time
import TweetExtractor   #import the task script that has to be run daily

def job(t):
    print ("I'm working...", t)
    AkshadaTweetExtractor.main()    #call the required function
    print ("Execution completed")
    return

#Set the time here in 24 hour format.  Run it everytime the system boots.
schedule.every().day.at("20:33").do(job,"It is 8:33 PM")

while True:
    schedule.run_pending()
    time.sleep(60)
