from random import randint
from edu.slavik.interstripation.surface.Surface import Surface
from edu.slavik.interstripation.stripe.VerticalStripe import VerticalStripe
from edu.slavik.interstripation.stripe.HorizontalStripe import HorizontalStripe
"""
Implementation of Surface class for surfaces with stripes, edges of which are are parallel to axises

@author: oleksii.slavik
"""


class LinearEdgesSurface(Surface):

    def __init__(self, path, countV, countH, maxWidth, maxHeight):
        """
        Create surface from source and remove stripes

        Parameters
        ----------
        path: str
            path to source
        countV: int
            count of vertical stripes
        countH: int
            count of horizontal stripes
        maxWidth: int
            value of maximum width of vertical stripes
        maxHeight: int
            value of maximum height of horizontal stripes
        """
        super().__init__(path)
        self.verticalStripes = self.createVerticalStripesList(countV, maxWidth)
        self.horizontalStripes = self.createHorizontalStripesList(countH, maxHeight)
        self.removeStripes()

    def removeStripes(self):
        """
        Remove stripes from surface
        """
        for i in range(len(self.verticalStripes)):
            self.verticalStripes[i].removeStripe(self)

        for i in range(len(self.horizontalStripes)):
            self.horizontalStripes[i].removeStripe(self)

    def createVerticalStripesList(self, count, maxWidth):
        """
        Create list of vertical stripes

        Parameters
        ----------
        count: int
            count of vertical stripes
        maxWidth: int
            value of maximum width of vertical stripes

        Return
        ------
        stripes: list
            list of vertical stripes
        """
        width = self.matrix.shape[0]
        stripes = []

        for i in range(count):
            step = int(width / count)
            left = randint(i * step, (i + 1) * step - maxWidth)
            stripes.append(VerticalStripe(left, left + randint(1, maxWidth)))

        return stripes

    def createHorizontalStripesList(self, count, maxHeight):
        """
        Create list of horizontal stripes

        Parameters
        ----------
        count: int
            count of vertical stripes
        maxHeight: int
            value of maximum width of horizontal stripes

        Return
        ------
        stripes: list
            list of horizontal stripes
        """
        height = self.matrix.shape[1]
        stripes = []

        for i in range(count):
            step = int(height / count)
            left = randint(i * step, (i + 1) * step - maxHeight)
            stripes.append(HorizontalStripe(left, left + randint(1, maxHeight)))

        return stripes
