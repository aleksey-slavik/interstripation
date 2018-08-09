from edu.slavik.interstripation.core.standard.HorizontalInterstripation import HorizontalInterstripation
from edu.slavik.interstripation.core.standard.VerticalInterstripation import VerticalInterstripation
from edu.slavik.interstripation.core.standard.UnionInterstripation import UnionInterstripation


class IntersectionInterstripation:

    @staticmethod
    def restore(surface, vertical, horizontal):
        HorizontalInterstripation.restore(surface, horizontal)
        VerticalInterstripation.restore(surface, vertical)
