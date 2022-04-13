



from field import Field


class BoundingBall:
    def __init__(self,x,y,field :Field):
        self.x=x
        self.y=y
        self.vx=4
        self.vy=4
        self.field = field

    def tick(self):
        self.x+=self.vx
        self.y+=self.vy
        self.update_x_bounce()
        self.update_y_bounce()
    
    def update_x_bounce(self):
        if self.x < 0:
            self.vx = abs(self.vx)
        elif self.x >self.field.width:
            self.vx = -abs(self.vx)

    def update_y_bounce(self):
        if self.y < 0:
            self.vy = abs(self.vy)
        elif self.y >self.field.height:
            self.vy = -abs(self.vy)
