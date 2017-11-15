import schedule
import time
import AkshadaTweetExtractor

def job(t):
    print ("I'm working...", t)
    AkshadaTweetExtractor.main()
    print ("Execution completed")
    return

#Set the time here in 24 hour format.  Run it everytime the system boots.
schedule.every().day.at("20:33").do(job,"It is 8:33 PM")

while True:
    schedule.run_pending()
    time.sleep(60)
