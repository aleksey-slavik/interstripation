"""
Contains method for restore horizontal stripes using modified interstripation

@author: oleksii.slavik
"""


def restore(surface, stripe):
    """
    Restore given horizontal stripe data in given surface

    Parameters
    ----------
    surface: Surface
        surface data
    stripe: Stripe
        defect data
    """
    startAt = stripe.startAt - 1
    endAt = stripe.endAt

    for i in range(startAt, endAt):
        for j in range(surface.matrix.shape[1]):
            surface.matrix[i, j] = \
                (i - endAt) / (startAt - endAt) * rightDelta(surface, stripe, i, j) - \
                (i - startAt) / (startAt - endAt) * leftDelta(surface, stripe, i, j)


def distance(value, stripe):
    return min(value - stripe.startAt + 1, stripe.endAt - value)


def leftDelta(surface, stripe, x, y):
    r = distance(x, stripe)
    res = 0

    for i in range(r + 1):
        res += surface.matrix[stripe.startAt - i, y]

    return res / (r + 1)


def rightDelta(surface, stripe, x, y):
    r = distance(x, stripe)
    res = 0

    for i in range(r + 1):
        res += surface.matrix[stripe.endAt + i, y]

    return res / (r + 1)
