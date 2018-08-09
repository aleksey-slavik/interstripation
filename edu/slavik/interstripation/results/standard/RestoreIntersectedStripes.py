from edu.slavik.interstripation.surface.Surface import Surface
from edu.slavik.interstripation.surface.LinearEdgesSurface import LinearEdgesSurface
from edu.slavik.interstripation.core.standard.IntersectionInterstripation import IntersectionInterstripation
"""
Contains example of restore intersected stripes using standard interstripation

@author: oleksii.slavik
"""

# remove stripes
surface = LinearEdgesSurface('../../resources/test.jpeg', 5, 5, 5, 5)
surface.removeStripes()
surface.save('../../resources/standard/corrupted/intersection.png')

# restore vertical stripes
for i in range(len(surface.verticalStripes)):
    for j in range(len(surface.horizontalStripes)):
        IntersectionInterstripation.restore(surface, surface.verticalStripes[i], surface.horizontalStripes[j])

surface.save('../../resources/standard/restored/intersection.png')

# compare with original
origin = Surface('../../resources/test.jpeg')
error = origin.compare(surface)
error.save('../../resources/standard/error/intersection.png')
