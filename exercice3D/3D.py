import math

class Point3D:
    Npts = 0
    Mx = float('-inf')
    My = float('-inf')
    Mz = float('-inf')

    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z
        Point3D.Npts += 1
        Point3D.Mx = max(Point3D.Mx, x)
        Point3D.My = max(Point3D.My, y)
        Point3D.Mz = max(Point3D.Mz, z)

    def afficher(self):
        print(self)

    def deplacer(self, dx, dy, dz):
        self.__x += dx
        self.__y += dy
        self.__z += dz
        Point3D.Mx = max(Point3D.Mx, self.__x)
        Point3D.My = max(Point3D.My, self.__y)
        Point3D.Mz = max(Point3D.Mz, self.__z)

    def distance(self, autre_point):
        return math.sqrt(
            (self.__x - autre_point.__x) ** 2 +
            (self.__y - autre_point.__y) ** 2 +
            (self.__z - autre_point.__z) ** 2
        )

    def __repr__(self):
        return f"Point3D(x={self.__x}, y={self.__y}, z={self.__z})"

    def __str__(self):
        return f"Point({self.__x}, {self.__y}, {self.__z})"

    @classmethod
    def getNpts(cls):
        return cls.Npts

    @classmethod
    def getMaxX(cls):
        return cls.Mx

    @classmethod
    def getMaxY(cls):
        return cls.My

    @classmethod
    def getMaxZ(cls):
        return cls.Mz

    @staticmethod
    def est_diagonale(x, y, z):
        return x == y == z


a3D = Point3D(1, 2, 3)
b3D = Point3D(4, 5, 6)
c3D = Point3D(7, 7, 7)

print("Coordonnées initiales :")
a3D.afficher()
b3D.afficher()
c3D.afficher()

try:
    print(a3D.__x)
except AttributeError as e:
    print("Erreur d'accès direct :", e)

a3D.deplacer(1, 1, 1)
b3D.deplacer(-1, -1, -1)

print("\nAprès déplacement :")
a3D.afficher()
b3D.afficher()

print("\nDistance entre a3D et b3D :", a3D.distance(b3D))

print("\nNombre total de points créés :", Point3D.getNpts())
print("Max X :", Point3D.getMaxX())
print("Max Y :", Point3D.getMaxY())
print("Max Z :", Point3D.getMaxZ())

print("\nTest diagonale :")
print("Point(7,7,7) est sur la diagonale ?", Point3D.est_diagonale(7, 7, 7))
print("Point(1,2,3) est sur la diagonale ?", Point3D.est_diagonale(1, 2, 3))
