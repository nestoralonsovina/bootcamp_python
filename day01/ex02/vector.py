import operator

class Vector:
    def __init__(self, vector):
        self.values = list(vector)
        self.length = len(self.values)

    def __add__(self, v2):
        return Vector(map(operator.add, self.values, v2.values if isinstance(v2, Vector) else [v2] * self.length))

    def __radd__(self, v2):
        return Vector(map(operator.add, v2.values if isinstance(v2, Vector) else [v2] * self.length, self.values))

    def __sub__(self, v2):
        return Vector(map(operator.sub, self.values, v2.values if isinstance(v2, Vector) else [v2] * self.length))

    def __rsub__(self, v2):
        return Vector(map(operator.sub, v2.values if isinstance(v2, Vector) else [v2] * self.length, self.values))

    def __truediv__(self,v2):
        return Vector(map(operator.truediv, self.values, [v2] * self.length))

    def __rtruediv__(self, v2):
        return Vector(map(operator.truediv, [v2] * self.length, self.values))

    def __mul__(self, v2):
        if isinstance(v2, Vector):
            if v2.length != self.length:
                raise ValueError('Invalid')
            return sum(list(map(operator.mul, self.values, [v2] * self.length)))
        return Vector(map(operator.mul, self.values, [v2] * self.length))

    def __rmul__(self, v2):
        if isinstance(v2, Vector):
            if v2.length != self.length:
                raise ValueError('Invalid')
            return sum(list(map(operator.mul, [v2] * self.length, self.values)))
        return Vector(map(operator.mul, [v2] * self.length, self.values))


    def __str__(self):
        return f"Vector: {str(self.values)}"

    def __repr__(self):
        return str(self.values)








