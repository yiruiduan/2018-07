#Author:yiruidaun
import time,datetime
def time_now():
    data_show = str(datetime.date.today())
    time_show = time.strftime("%H:%M:%S")
    return "%s %s"%(data_show,time_show)

if __name__=="__main__":
    print(time_now())