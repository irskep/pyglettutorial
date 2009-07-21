import pyglet
import physicalobject, resources

class Bullet(physicalobject.PhysicalObject):
    """Bullets fired by the player"""
    
    def __init__(self, *args, **kwargs):
        super(Bullet, self).__init__(resources.bullet_image, *args, **kwargs)
        
        # Bullets shouldn't stick around forever
        pyglet.clock.schedule_once(self.die, 0.5)
        
        # Flag as a bullet
        self.is_bullet = True
    
    def die(self, dt):
        self.dead = True
    
    def collides_with(self, other_object):
        """Special collision method, returns False if other_object doesn't care about bullets"""
        
        if not other_object.reacts_to_bullets:
            return False
        else:
            return super(Bullet, self).collides_with(other_object)
    
