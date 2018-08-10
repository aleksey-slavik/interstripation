from edu.slavik.interstripation.surface.Surface import Surface
from edu.slavik.interstripation.surface.LinearEdgesSurface import LinearEdgesSurface
from edu.slavik.interstripation.core.standard.HorizontalInterstripation import HorizontalInterstripation
"""
Contains example of restore vertical stripes using standard horizontal interstripation

@author: oleksii.slavik
"""

# remove horizontal stripes
surface = LinearEdgesSurface('../../resources/test.jpeg', 0, 5, 5, 5)
surface.removeStripes()
surface.save('../../resources/standard/corrupted/horizontal.png')

# restore horizontal stripes
for i in range(len(surface.horizontalStripes)):
    HorizontalInterstripation.restore(surface, surface.horizontalStripes[i])

surface.save('../../resources/standard/restored/horizontal.png')

# compare with original
origin = Surface('../../resources/test.jpeg')
error = origin.compare(surface)
error.save('../../resources/standard/error/horizontal.png')
