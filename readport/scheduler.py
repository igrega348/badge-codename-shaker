# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 19:11:24 2018

@author: Ivan
"""
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

def messg(argument):
    if argument == True:
        print('now')

def run():
    scheduler = BackgroundScheduler()
    scheduler.start()
    
    scheduler.add_job(messg, trigger = 'interval', seconds=5, start_date = datetime.now(), args = [True])

    while True:
        try:
            k = 0
            high = 2**26
            for i in range(high):
                k += 1
                if k == high-1:
                    print('end')
        except:
            print('first interrupt')
            scheduler.shutdown()
            break

        
if __name__ == "__main__":
    run()