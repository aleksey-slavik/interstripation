"""
Contains method for restore horizontal stripes using standard interstripation

@author: oleksii.slavik
"""


class HorizontalInterstripation:

    @staticmethod
    def restore(surface, stripe):
        """
        Restore given horizontal stripe data in given surface

        Parameters
        ----------
        surface: Surface
            surface data
        stripe: Stripe
            stripe data
        """
        startAt = stripe.startAt - 1
        endAt = stripe.endAt

        for i in range(startAt, endAt):
            for j in range(surface.matrix.shape[1]):
                surface.matrix[i, j] = \
                    (i - endAt) * surface.matrix[startAt, j] / (startAt - endAt) - \
                    (i - startAt) * surface.matrix[endAt, j] / (startAt - endAt)
