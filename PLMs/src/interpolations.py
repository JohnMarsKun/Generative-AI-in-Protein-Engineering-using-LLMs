import torch
import numpy as np

def linear_interpolation(e1, e2, lamb):
    """Performs linear interpolation between two embeddings."""
    return lamb * e1 + (1 - lamb) * e2

def sinusoidal_interpolation(e1, e2, lamb):
    """Interpolates using a sinusoidal weighting."""
    return e1 * torch.sin(np.pi * (1 - lamb) / 2) + e2 * torch.sin(np.pi * lamb / 2)

def arccos_interpolation(e1, e2, lamb):
    """Interpolates using an arccos weighting."""
    interpolation_factor = np.arccos(lamb) / np.pi
    return interpolation_factor * e1 + (1 - interpolation_factor) * e2

def decode_interpolations(interpolations, encoder_model, device='cpu'):
    """
    Given a list of embeddings (interpolations) and an encoder model,
    decode each one to its corresponding protein sequence.
    """
    decoded_sequences = []
    for embedding in interpolations:
        embedding = embedding.unsqueeze(0).to(device)
        with torch.no_grad():
            decoded_seq = encoder_model.batch_decode(embedding)
        decoded_sequences.append(decoded_seq[0])
    return decoded_sequences
