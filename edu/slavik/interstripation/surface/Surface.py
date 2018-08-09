import numpy
from PIL import Image
"""
Contains necessary methods for surfaces
Root class for all surfaces

@author: oleksii.slavik
"""


class Surface:

    def __init__(self, path):
        """
        Create surface from given source

        Parameters
        ----------
        path: str
            path to source data
        """
        imageData = Image.open('../resources/' + path)
        grayscale = imageData.convert('L')
        self.matrix = numpy.array(grayscale)

    def save(self, fileName, imageFormat='PNG'):
        """
        Save current data to file

        Parameters
        ----------
        fileName: str
            name of file
        imageFormat:
            file format
        """
        imageData = Image.fromarray(self.matrix, 'L')
        imageData.save('../resources/' + fileName, imageFormat)

    def compare(self, other):
        """
        Compare current surface with other

        Parameters
        ----------
        other: Surface
            other surface data

        Return
        ------
        res: Surface
            surface of difference between surfaces
        """
        res = abs(self.matrix - other.matrix)
        for i in range(res.shape[0]):
            for j in range(res.shape[1]):
                if res[i, j] == 0:
                    res[i, j] = -1
        return res

    def __repr__(self):
        return str(self.__dict__)
