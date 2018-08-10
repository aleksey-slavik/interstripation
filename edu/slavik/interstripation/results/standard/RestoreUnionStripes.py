from edu.slavik.interstripation.surface.Surface import Surface
from edu.slavik.interstripation.surface.LinearEdgesSurface import LinearEdgesSurface
from edu.slavik.interstripation.core.standard.UnionInterstripation import UnionInterstripation
"""
Contains example of restore union stripes using standard interstripation

@author: oleksii.slavik
"""

# remove stripes
surface = LinearEdgesSurface('../../resources/test.jpeg', 5, 5, 10, 10)
surface.removeRegions()
surface.save('../../resources/standard/corrupted/union.png')

# restore stripes
for i in range(len(surface.regions)):
    UnionInterstripation.restore(surface, surface.regions[i])

surface.save('../../resources/standard/restored/union.png')

# compare with original
origin = Surface('../../resources/test.jpeg')
error = origin.compare(surface)
error.save('../../resources/standard/error/union.png')
