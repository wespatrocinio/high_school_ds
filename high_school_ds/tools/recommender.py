import numpy
from collections import defaultdict

from dataset import user_preferences
from high_school_ds.high_school_math.geometry import Geometry


def generate_ratings_arrays(rating_dict):
    ratings_array = defaultdict()
    for key, ratings in rating_dict.iteritems():
        ratings_array[key] = numpy.array([rating for _, rating in ratings.iteritems()])
    return ratings_array

def get_nearest(sample, ratings_array):
    similarity_scores = defaultdict()
    for key, ratings in ratings_array.iteritems():
        similarity_scores[key] = Geometry.get_cosine(sample, ratings)
    return max(similarity_scores, similarity_scores.get)

def find_unrated_items(sample, nearest):
    return [key for key in sample.keys() if sample.get(key) == 0 and nearest.get(key) != 0]