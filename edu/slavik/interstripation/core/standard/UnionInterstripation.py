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
        endV = region.x2 + 1
        endH = region.y2 + 1

        for i in range(startV, endV):
            for j in range(startH, endH):
                surface.matrix[i, j] = \
                    (i - endH) / (startH - endH) * surface.matrix[startH, j] - \
                    (i - startH) / (startH - endH) * surface.matrix[endH, j] + \
                    (j - endV) / (startV - endV) * surface.matrix[i, startV] - \
                    (j - startV) / (startV - endV) * surface.matrix[i, endV] - \
                    (i - endH) / (startH - endH) * (j - endV) / (startV - endV) * surface.matrix[startH, startV] + \
                    (i - endH) / (startH - endH) * (j - startV) / (startV - endV) * surface.matrix[startH, endV] + \
                    (i - startH) / (startH - endH) * (j - endV) / (startV - endV) * surface.matrix[endH, startV] - \
                    (i - startH) / (startH - endH) * (j - startV) / (startV - endV) * surface.matrix[endH, endV]
