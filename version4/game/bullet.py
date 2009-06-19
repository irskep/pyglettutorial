import physicalobject, resources, util

class Bullet(physicalobject.PhysicalObject):
    """Bullets fired by the player"""
    
    def __init__(self, *args, **kwargs):
        super(Bullet, self).__init__(*args, **kwargs)
        
        # Bullets shouldn't stick around forever
        self.age = 0.0
        self.lifespan = 0.5
    
    def update(self, dt):
        # We can measure age simply by adding up the time steps
        self.age += dt
        if self.age >= self.lifespan:
            self.dead = True
        
        super(Bullet, self).update(dt)
    
    def collides_with(self, other_object):
        """Special collision method, returns False if other_object doesn't care about bullets"""
        
        if not other_object.reacts_to_bullets:
            return False
        
        return super(Bullet, self).collides_with(other_object)
    
