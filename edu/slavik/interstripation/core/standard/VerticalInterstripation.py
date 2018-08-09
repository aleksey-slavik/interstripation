from edu.slavik.interstripation.core.Interstripation import Interstripation


class VerticalInterstripation(Interstripation):

    @staticmethod
    def restore(surface, stripe):
        startAt = stripe.startAt - 1
        endAt = stripe.endAt

        for i in range(surface.matrix.shape[0]):
            for j in range(startAt, endAt):
                surface.matrix[i, j] = \
                    (j - endAt) * surface.matrix[i, startAt] / (startAt - endAt) - \
                    (j - startAt) * surface.matrix[i, endAt] / (startAt - endAt)
