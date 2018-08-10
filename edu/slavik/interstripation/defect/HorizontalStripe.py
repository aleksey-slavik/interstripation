from edu.slavik.interstripation.defect.Stripe import Stripe
"""
Implementation of Stripe class for horizontal stripes, edges of which are parallel to abscissa axis 

@author: oleksii.slavik 
"""


class HorizontalStripe(Stripe):

    def __init__(self, startAt, endAt):
        """
        Setup initial data

        Parameters
        ----------
        startAt: int
            left edge of defect
        endAt: int
            right edge of defect
        """
        self.startAt = startAt
        self.endAt = endAt

    def removeStripe(self, surface):
        """
        Remove current horizontal stripe from surface

        Parameters
        ----------
        surface: Surface
            initial statement of surface

        Return
        ------
        surface: Surface
            surface without current horizontal defect
        """
        width = surface.matrix.shape[0]

        for i in range(self.startAt, self.endAt):
            for j in range(width):
                surface.matrix[i, j] = -1

        return surface
