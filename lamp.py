#!/usr/bin/python

from boxes import Boxes

class Lamp(Boxes):
    def __init__(self):
        Boxes.__init__(self, width=1000, height=800)
        self.fingerJointSettings = (5, 5)

    def ring(self, r, w):
        self.ctx.save()
        d = 2*(r+w)
        self.roundedPlate(d, d, r)

        self.moveTo(r+w, w)
        self.corner(360, r)
        self.ctx.restore()

    def base(self, r, w):
        self.ctx.save()
        d = 2*(r+w)
        self.roundedPlate(d, d, r)
        self.moveTo(w/2.0, w/2.0)
        self.hexHolesPlate(d-w, d-w, r-w/2.0)
        self.ctx.restore()

    def render(self, r, w, x, y, h):
        """
        r : radius of lamp
        w : width of surrounding ring
        """
        d = 2*(r+w)
        self.ctx.save()
        self.moveTo(20, 20)
        self.ring(r, w)
        self.moveTo(2*(r+w)+20, 0)
        self.base(r, w)

        self.ctx.restore()
        self.moveTo(10, 2*(r+w)+40)
        self.surroundingWall(d, d, r, 150, top='h', bottom='h')
        self.moveTo(0, 150+20)

        self.rectangularWall(x, y, edges="ffff")
        self.moveTo(x+20, 0)
        self.rectangularWall(x, y, edges="ffff")
        self.moveTo(10, 10)
        self.hexHolesRectangle(x-20, y-20)


        #self.hexHolesHex(200)
        #self.hexHolesRectangle(400, 200)

        self.ctx.stroke()
        self.surface.flush()


l = Lamp()
l.render(100, 20, 250, 140, 120)