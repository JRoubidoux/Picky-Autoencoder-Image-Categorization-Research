import numpy as np

class GeometricObject():
    def __init__(self, dimensionality: int):
        self.dimensionality = self.check_integer_valued_object(dimensionality, "dimensionality")
        
    def check_integer_valued_object(self, integer_object: int, attribute_name: str):
        if type(integer_object) is not int:
            raise ValueError(f"The {attribute_name} passed into point needs to be integer valued.")
        elif integer_object < 1:
            raise ValueError(f"The value of {attribute_name} should be greater than 0.")
        else:
            return integer_object
        
    def check_float_valued_object(self, float_object: float, attribute_name: str):
        if type(float_object) is not float:
            raise ValueError(f"The {attribute_name} passed into point needs to be float valued.")
        else:
            return float_object


class Vector(GeometricObject):
    """
        This class allows for a vector (geometric representation) to be represented in an n-dimensional space. 

        Arguments:
            dimensions: An integer valued number of dimensions n the vector should have.
            vector: An np.ndarray that contains each dimensional value of the vector. 
    """

    def __init__(self, dimensionality: int, vector: np.ndarray):
        super().__init__(dimensionality)
        self.set_point(vector)
        
    def print_array_shape_and_dimensions_needed(self, array: np.ndarray):
        return f"Shape: {array.shape}. Dimensions needed for point: {self.dimensionality}"

    def set_point(self, vector: np.ndarray):
        if not vector:
            raise ValueError("This cannot be None.")
        elif type(vector) is not np.ndarray:
            raise ValueError(f"The argument passed into {self.set_point.__name__} needs to np.ndarray typed.")
        elif vector.dtype is not float:
            raise ValueError(f"The vector passed into the function {self.set_point.__name__} needs to be float typed.")
        elif len(vector.shape) > 2:
            raise ValueError(f"The vector passed into the function {self.set_point.__name__} cannot be a matrix. 'Vector' shape: {vector.shape}")
        elif len(vector.shape) == 0:
            if self.dimensionality != 1:
                raise ValueError(f"Scalar valued array has only one point. {self.print_array_shape_and_dimensions_needed(vector)}")
            else:
                self.vector = vector.reshape((1, 1))
        elif len(vector.shape) == 2:
            if vector.shape[-1] > 1:
                raise ValueError(f"The vector passed in is a matrix. {self.print_array_shape_and_dimensions_needed(vector)}")
            else:
                if vector.shape[0] != self.dimensionality:
                    raise ValueError(f"The dimensionality of the vector needs to match the dimensionality of the point. {self.print_array_shape_and_dimensions_needed(vector)}")
                else:
                    self.vector = vector
        else:
            if vector.shape[0] != self.dimensionality:
                raise ValueError(f"The dimensionality of the vector needs to match the dimensionality of the point. {self.print_array_shape_and_dimensions_needed(vector)}")
            else:
                self.vector = vector.reshape((self.vector[0], 1))


class Hypersphere(GeometricObject):
    def __init__(self, dimensionality: int, radius: int):
        super().__init__(dimensionality)
        self.radius = self.check_integer_valued_object(radius, "radius")
        

