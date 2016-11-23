import sys
import math

class Polynomial(object):

    def __init__(self, polynomial):
        self.tup_poly = tuple(polynomial)

    def get_polynomial(self):
        print self.tup_poly

    def __neg__(self):
        newList = [(-x,y) for x,y in self.tup_poly]
        return Polynomial(newList)

    def __add__(self, other):
        newL=[]
        for i in self.tup_poly:
            newL.append(i)
        for i in other.tup_poly:
            newL.append(i)
        return Polynomial(newL)

    def __sub__(self, other):
        other = -other
        newObj = self + other
        return newObj

    def __mul__(self, other):
        pass

    def __call__(self, x):


     def simplify(self):
        pass

    def __str__(self):
        first_term = str(self.tup_poly[0][0]) + 'x'
        return first_term + '+' + str(self.tup_poly[1][0])


def main():
    p = Polynomial([(2, 1), (1, 0)])
    q = Polynomial([(4, 3), (3, 2)])
    #q.get_polynomial()
    s = p-q
    s.get_polynomial()
if __name__ == '__main__':
    main()