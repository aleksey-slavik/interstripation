from edu.slavik.interstripation.stripe.Stripe import Stripe
"""
Implementation of Stripe class for vertical stripes, edges of which are parallel to ordinate axis 

@author: oleksii.slavik 
"""


class VerticalStripe(Stripe):

    def __init__(self, startAt, endAt):
        """
        Setup initial data

        Parameters
        ----------
        startAt: int
            top edge of stripe
        endAt: int
            bottom edge of stripe
        """
        self.startAt = startAt
        self.endAt = endAt

    def removeStripe(self, surface):
        """
        Remove current vertical stripe from surface

        Parameters
        ----------
        surface: Surface
            initial statement of surface

        Return
        ------
        surface: Surface
            surface without current vertical stripe
        """
        height = surface.matrix.shape[1]

        for i in range(height):
            for j in range(self.startAt, self.endAt):
                surface.matrix[i, j] = -1

        return surface