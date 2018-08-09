"""
Implementation of Interstripation for restore vertical stripes using standard interstripation

@author: oleksii.slavik
"""


class VerticalInterstripation:

    @staticmethod
    def restore(surface, stripe):
        """
        Restore given vertical stripe data in given surface

        Parameters
        ----------
        surface: Surface
            surface data
        stripe: Stripe
            stripe data
        """
        startAt = stripe.startAt - 1
        endAt = stripe.endAt

        for i in range(surface.matrix.shape[0]):
            for j in range(startAt, endAt):
                surface.matrix[i, j] = \
                    (j - endAt) * surface.matrix[i, startAt] / (startAt - endAt) - \
                    (j - startAt) * surface.matrix[i, endAt] / (startAt - endAt)
