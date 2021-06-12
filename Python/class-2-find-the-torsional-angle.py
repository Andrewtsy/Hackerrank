
        
class Points:      
    def __init__(self, x, y, z):
        self.x, self.y, self.z = map(float, [x, y, z])
        
    def __sub__(self, p2):
        return Points(p2.x - self.x, p2.y - self.y, p2.z - self.z)
        
    def cross(self, v2):
        return Points(self.y*v2.z - self.z*v2.y, self.z*v2.x - self.x*v2.z, self.x*v2.y - self.y*v2.x)
        
    def dot(self, v2):
        return self.x*v2.x + self.y*v2.y + self.z*v2.z
    
    def absolute(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'



