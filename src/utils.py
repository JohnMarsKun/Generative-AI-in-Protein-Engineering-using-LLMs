import numpy as np
import random

def levenshtein_distance(s1, s2):
    """Compute the Levenshtein distance between two strings."""
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    distances = np.arange(len(s1) + 1)
    for index2, char2 in enumerate(s2):
        new_distances = [index2 + 1]
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                new_distances.append(distances[index1])
            else:
                new_distances.append(1 + min(distances[index1], distances[index1 + 1], new_distances[-1]))
        distances = new_distances
    return distances[-1]

def generate_random_sequence(min_length, max_length):
    """Generate a random protein sequence with a length between min_length and max_length."""
    amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
    length = random.randint(min_length, max_length)
    return ''.join(random.choices(amino_acids, k=length))
