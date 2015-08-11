from __future__ import division

import numpy

class Geometry():

    def _validate(self, vec):
        return True if isinstance(vec, numpy.ndarray) else False

    def _get_norm(self, vec):
        return numpy.linalg.norm(vec)

    def _get_inner_product(self, vec1, vec2):
        return numpy.dot(vec1, vec2)

    def get_cosine(self, vec1, vec2):
        if self._validate(vec1) and self._validate(vec2):
            norm1 = self._get_norm(vec1)
            norm2 = self._get_norm(vec2)
            inner_product = self._get_inner_product(vec1, vec2)
            return inner_product / (norm1 * norm2)
        else:
            return 0

    @classmethod
    def get_distance(self, vec1, vec2):
        return numpy.linalg.norm(vec1-vec2)