from edu.slavik.interstripation.surface.Surface import Surface
from edu.slavik.interstripation.surface.LinearEdgesSurface import LinearEdgesSurface
from edu.slavik.interstripation.core.standard.VerticalInterstripation import VerticalInterstripation
"""
Contains example of restore vertical stripes using standard vertical interstripation

@author: oleksii.slavik
"""

# remove vertical stripes
surface = LinearEdgesSurface('../../resources/test.jpeg', 5, 0, 5, 5)
surface.removeStripes()
surface.save('../../resources/standard/corrupted/vertical.png')

# restore vertical stripes
for i in range(len(surface.verticalStripes)):
    VerticalInterstripation.restore(surface, surface.verticalStripes[i])

surface.save('../../resources/standard/restored/vertical.png')

# compare with original
origin = Surface('../../resources/test.jpeg')
error = origin.compare(surface)
error.save('../../resources/standard/error/vertical.png')
