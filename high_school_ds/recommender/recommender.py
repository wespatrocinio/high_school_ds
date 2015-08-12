import numpy
from collections import defaultdict

from dataset import user_preferences
from high_school_ds.high_school_math.geometry import Geometry

ratings_vectors = defaultdict()
for name, ratings in user_preferences.RATINGS:
    ratings_vectors[album] = numpy.array([rating for _, rating in ratings.iteritems()])