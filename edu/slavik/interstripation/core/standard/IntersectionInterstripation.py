from edu.slavik.interstripation.core.standard.HorizontalInterstripation import HorizontalInterstripation
from edu.slavik.interstripation.core.standard.VerticalInterstripation import VerticalInterstripation
"""
Contains method for restore intersected stripes using standard interstripation

@author: oleksii.slavik
"""


class IntersectionInterstripation:

    @staticmethod
    def restore(surface, vertical, horizontal):
        """
        Restore given stripes data in given surface

        Parameters
        ----------
        surface: Surface
            surface data
        vertical: Stripe
            vertical defect data
        horizontal: Stripe
            horizontal defect data
        """
        HorizontalInterstripation.restore(surface, horizontal)
        VerticalInterstripation.restore(surface, vertical)
