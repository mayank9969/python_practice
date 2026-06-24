class train:
    def __init__(mayank,traino,fro ,to ,seats ,fare,staus):
        mayank.traino =traino
        mayank.fro = fro
        mayank.to = to
        mayank.seats = seats
        mayank.fare = fare
        mayank.staus = staus
        
    
    def book_ticket(mayank):
        if mayank.seats > 0:
            mayank.seats -= 1
            print(f"ticket is booked in train no {mayank.traino} and remaing seat numbers are {mayank.seats} ")
        else :
            print("booking failed no seats are available you are in reserve categaorty if any one cancels your ticket you will get ticket and you will be notifed on in advance 48 hours ")    
    def get_staus(mayank):
        print(f" your ticket which is booked fro  {mayank.fro} and to {mayank.to} and train no is {mayank.traino} and status is {mayank.staus}")
    def fair(mayank):
        print(f"your are travelling fro {mayank.fro} to {mayank.to} so your fare is {mayank.fare}")
        
r =train(2,"A","b",5 ,1500,"booked")
r.book_ticket()
r.get_staus()    
r.fair()            

        
        
