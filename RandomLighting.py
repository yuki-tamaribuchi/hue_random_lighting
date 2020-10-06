from phue import Bridge
import time
import random

class RandomLighting():

    def __init__(self,ip_addr,light_no,interval=0.05):
        self.b=Bridge(ip_addr)
        self.light_no=light_no
        self.interval=interval
        self.b.set_light(light_no,'on',True)

    def lighting(self):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)

        r_direction=0 if random.random() < 0.5 else 1
        g_direction=0 if random.random() < 0.5 else 1
        b_direction=0 if random.random() < 0.5 else 1

        while True:
            red = pow((r + 0.055) / (1.0 + 0.055), 2.4) if r > 0.04045 else (r / 12.92)
            green = pow((g + 0.055) / (1.0 + 0.055), 2.4) if g > 0.04045 else (g / 12.92)
            blue =  pow((b + 0.055) / (1.0 + 0.055), 2.4) if b > 0.04045 else (b / 12.92)

            x = red * 0.649926 + green * 0.103455 + blue * 0.197109
            y = red * 0.234327 + green * 0.743075 + blue * 0.022598
            z = green * 0.053077 + blue * 1.035763

            x = x / (x + y + z)
            y = y / (x + y + z)
            xy=[x,y]

            cmd={
                'xy':xy,
                'transitiontime':0,
            }

            self.b.set_light(self.light_no,cmd)

            if r_direction:
                if r==255:
                    r=254
                    r_direction=False
                else:
                    r+=1
            else:
                if r==0:
                    r=1
                    r_direction=True
                else:
                    r-=1

            if g_direction:
                if g==255:
                    g=254
                    g_direction=False
                else:
                    g+=1
            else:
                if g==0:
                    g=1
                    g_direction=True
                else:
                    g-=1

            if b_direction:
                if b==255:
                    b=254
                    b_direction=False
                else:
                    b+=1
            else:
                if b==0:
                    b=1
                    b_direction=True
                else:
                    b-=1

            r_direction = not r_direction if random.random() <0.01 else r_direction
            g_direction = not g_direction if random.random() <0.01 else g_direction
            b_direction = not b_direction if random.random() <0.01 else b_direction

            print('R=',r,'G=',g,'B=',b)
            time.sleep(self.interval)
            

    #def __del__(self):
        #self.b.set_light(self.light_no,'on',False)
