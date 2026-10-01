
today_done = False
streak = 0 
def on_commit():
    global today_done, streak 
    if not today_done :
        streak +=1
        today_done= True
    
    