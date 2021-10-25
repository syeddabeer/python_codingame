import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

w_max=w-1
h_max=h-1
w_min=0
h_min=0

x=x0
y=y0

visited = []
step=0
# game loop
while True:
    bomb_dir = input()  # Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    x_new=x
    y_new=y
    
    visited.append([x,y])
    
    if bomb_dir=="UNKNOWN":
        if (w_max-w_min)>(h_max-h_min):
            x_new=w_max+w_min-x
            y_new=y0
        else:
            y_new=h_max+h_min-y
            x_new=x0
        
    elif bomb_dir=="SAME":
        if x_prev==x and y_prev==y:
           if w_max!=w_min: x_new=w_max  
           else: y_new=h_max
        elif y_prev==y:
            x_new=round((x_prev+x)/2.)
            w_max=x_new
            w_min=x_new
        else:
            y_new=round((y_prev+y)/2.)
            h_max=y_new
            h_min=y_new
        if w_min==w_max: x_new=w_min
        if h_min==h_max: y_new=h_min
    elif bomb_dir=="WARMER":
#        print (x_prev, y_prev, x, y)
        if x_prev==x:
            if y_prev>y:
                h_max=min(h_max,math.floor((y_prev+y)/2.))
            else:
                h_min=max(h_min,math.ceil((y_prev+y)/2.))
            xt=x_new=w_max+w_min-x
            if xt>w-1: xt=w-1
            if xt<0:xt=0
            if w_max!=w_min: x_new=xt
            else: y_new=math.floor((h_max+h_min)/2.)
        else:
            if x_prev>x:
                w_max=min(math.floor((x_prev+x)/2.),w_max)
            else:
                w_min=max(math.ceil((x_prev+x)/2.),w_min)
            yt=h_max+h_min-y
            if yt>h-1: yt=h-1
            if yt<0:yt=0
            if h_max!=h_min: y_new=yt
            else: x_new=math.floor((w_max+w_min)/2.)
    elif bomb_dir=="COLDER":
        if x_prev==x:
            if y_prev<y:
                h_max=min(math.floor((y_prev+y)/2.-0.5),h_max)
                yt=h_min+h_max-y+1
                if yt<0: y_new=0
                else: y_new=yt
            
            
            else:
                h_min=max(math.ceil((y_prev+y)/2.+0.5),h_min)
                yt=h_min+h_max-y-1
                if yt>h-1: 
                    y_new=h-1
                    #y_new=y
                else:
                    y_new=yt
                x_new=x_prev
        elif y_prev==y:
            if x_prev<x:
                w_max=min(math.floor((x_prev+x)/2.-0.5),w_max)
                xt=w_min+w_max-x+1
                if xt<w: x_new=0
                else: x_new=xt
            else:
                w_min=max(math.ceil((x_prev+x)/2.+0.5),w_min)
                xt=w_min+w_max-x-1
                if xt>w-1: x_new=w-1
                else: x_new=xt
            y_new=y_prev


    if x_new==x and h_min==h_max:
       y_new=h_min

    if y_new==y and w_min==w_max:
       x_new=w_max


    print(w_min,w_max,h_min,h_max, file=sys.stderr)
    if step>0:
        if [x_new,y_new] == [x_prev,y_prev]: 
            print("visited",file=sys.stderr)
            if x_new==x:
                if y_new>y and y_new>h_min+1:y_new-=1
                elif y_new<y and y_new<h_max-1:y_new+=1
            else:
                if x_new>x and x_new>w_min+1:x_new-=1
                elif x_new<x and x_new<w_max-1:x_new+=1
        if [x_new,y_new]==[x,y]:
            print("repeat",file=sys.stderr)
            if y_new<h_max: y_new+=1
            elif y_new>h_min: y_new-=1 
            elif x_new<w_max: x_new+=1
            elif x_new>w_min: x_new-=1
    
    if bomb_dir=="UNKNOWN":
        if (w_max-w_min)>(h_max-h_min):
            x_new=w_max+w_min-x
            y_new=y0
        else:
            y_new=h_max+h_min-y
            x_new=x0
    elif bomb_dir=="SAME":
        print("SAME",file=sys.stderr)
    else:
        
        dx=math.floor(abs((w_max+w_min)/2.-x)) 
        
        if x>(w_max+w_min)/2.:
            xt=math.ceil((w_max+w_min)/2.)-dx
        else:
            xt=math.floor((w_max+w_min)/2.)+dx
            
        
        dy=math.floor(abs((h_max+h_min)/2.-y)) 
        
        if y>(h_max+h_min)/2.:
            yt=math.ceil((h_max+h_min)/2.)-dy
        else:
            yt=math.floor((h_max+h_min)/2.)+dy
        
        #xt=w_max+w_min-x
        #yt=h_max+h_min-y
        
        
        if xt>w-1: xt=w-1
        if xt<0: xt=0  
        if xt==x: xt+=1
        if yt>h-1: yt=h-1
        if yt<0: yt=0
        if yt==y: yt+=1
        
        
        d1=abs(w_max+w_min-x-xt)
        d2=abs(h_max+h_min-y-yt)
        if d2<=(h_max-h_min) or d1<=(w_max-w_min):
            if d2*(w_max-w_min)>=d1*(h_max-h_min):
                y_new=y
                x_new=xt
            else:
                x_new=x
                y_new=yt
        else: 
            print("too far",file=sys.stderr)
#            y_new=math.floor((h_min+h_max)/2.)
#            x_new=math.floor((w_min+w_max)/2.)
            if h_min>(h-h_max): 
                y_new=h_min
            else:
                y_new=h_max
            if w_min>(w-w_max):
                x_new=w_min
            else:
                x_new-w_max
                
    if step>0:
        if [x_new,y_new] == [x_prev,y_prev]: 
            print("visited",file=sys.stderr)
            #if x_new==x:
            #    if y_new>y and y_new>h_min+1:y_new-=1
            #    elif y_new<y and y_new<h_max-1:y_new+=1
            #else:
            #    if x_new>x and x_new>w_min+1:x_new-=1
            #    elif x_new<x and x_new<w_max-1:x_new+=1
            
#            y_new=math.floor((h_min+h_max)/2.)
#            x_new=math.floor((w_min+w_max)/2.)

            if h_min<(h-h_max): 
                y_new=h_min
            else:
                y_new=h_max
            if w_min<(w-w_max):
                x_new=w_min
            else:
                x_new-w_max
     
            #y_new=h_max
            #x_new=w_max
    
    #if h_min==h_max:
    #   y_new=h_min

    #if w_min==w_max:
    #   x_new=w_max
    
    if [x_new,y_new]==[x,y]:
            print("repeat",file=sys.stderr)
            if y_new<h_max: y_new+=1
            elif y_new>h_min: y_new-=1 
            elif x_new<w_max: x_new+=1
            elif x_new>w_min: x_new-=1
    
            
    if h_max==h_min and w_max==w_min:
        x_new=w_max
        y_new=h_min
    
    print(str(x_new)+" "+str(y_new))
    
    x_prev=x
    y_prev=y
    x=x_new
    y=y_new
    step+=1