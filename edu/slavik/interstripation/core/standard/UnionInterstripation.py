"""
Contains method for restore union stripes using standard interstripation

@author: oleksii.slavik
"""


class UnionInterstripation:

    @staticmethod
    def restore(surface, region):
        """
        Restore given region data in given surface

        Parameters
        ----------
        surface: Surface
            surface data
        region: Region
            region data
        """
        startV = region.x1 - 1
        startH = region.y1 - 1
        endV = region.x2
        endH = region.y2

        for i in range(startV, endV):
            for j in range(startH, endH):
                surface.matrix[i, j] = \
                    (i - endV) / (startV - endV) * surface.matrix[startV, j] - \
                    (i - startV) / (startV - endV) * surface.matrix[endV, j] + \
                    (j - endH) / (startH - endH) * surface.matrix[i, startH] - \
                    (j - startH) / (startH - endH) * surface.matrix[i, endH] - \
                    (i - endV) / (startV - endV) * (j - endH) / (startH - endH) * surface.matrix[startV, startH] + \
                    (i - endV) / (startV - endV) * (j - startH) / (startH - endH) * surface.matrix[startV, endH] + \
                    (i - startV) / (startV - endV) * (j - endH) / (startH - endH) * surface.matrix[endV, startH] - \
                    (i - startV) / (startV - endV) * (j - startH) / (startH - endH) * surface.matrix[endV, endH]
