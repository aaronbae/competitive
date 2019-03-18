import math

class Sphere:
    def __init__(self, c_x, c_y, c_z, c_r):
        self.x = c_x
        self.y = c_y
        self.z = c_z
        self.r = c_r
    def center(self):
        return [self.x, self.y, self.z]
    def radius(self):
        return self.r

class Line:
    def __init__(self, ray_x, ray_y, ray_z, dir_x, dir_y, dir_z):
        self.x0 = ray_x
        self.y0 = ray_y
        self.z0 = ray_z
        self.x = dir_x
        self.y = dir_y
        self.z = dir_z

    def point(self, t):
        return [self.x0+t*self.x, self.y0+t*self.y, self.z0+t*self.z]


def mag(v):
    return math.sqrt(math.pow(v[0],2)+math.pow(v[1],2)+math.pow(v[2],2))

def dot(v1, v2):
    return v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2];

def subtract(v1, v2):
    return [v1[0] - v2[0],v1[1] - v2[1],v1[2] - v2[2]]

def dist_points(p1, p2):
    return math.sqrt(math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1],2)+math.pow(p1[2]-p2[2],2))

def distance(sphere, line, t):
    sp = sphere.center
    lp = line.point(t)
    return dist_points(sp, lp)

def find_intersections():
    [c_x, c_y, c_z, c_r,ray_x, ray_y, ray_z, dir_x, dir_y, dir_z] = [2.0, 2.0, 1.0, 3.0, -1.0, 0.0, 0.0, 1.0, 0.0, 0.0]
    """
    Args:
        c_x, c_y, c_z (float): coordinates of center point of the sphere.
        c_r (float): radius of the sphere.
        ray_x, ray_y, ray_z (float): coordinates of the origin of the ray.
        dir_x, dir_y, dir_z (float): direction vector of the ray.

    Returns:
        [] or list of floats

    """
    # Write your code here
    s = Sphere(c_x, c_y, c_z, c_r)
    l = Line(ray_x, ray_y, ray_z, dir_x, dir_y, dir_z)
    dl = [dir_x, dir_y, dir_z]
    det = math.pow(dot(dl, subtract(l.point(0), s.center())),2)-(math.pow(mag(subtract(l.point(0), s.center())),2)-math.pow(s.radius(),2))
    print(det)

    -2

find_intersections();
