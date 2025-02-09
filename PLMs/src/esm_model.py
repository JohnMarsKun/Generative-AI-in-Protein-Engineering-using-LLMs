import torch
from esm import pretrained
from abc import ABC, abstractmethod

# An abstract base class if you want to ensure all protein models implement these methods.
class ProteinModel(ABC):
    @abstractmethod
    def encode(self, sequence):
        pass

    @abstractmethod
    def decode(self, embedding):
        pass

def remove_special_tokens(tokens):
    """Remove tokens like <cls>, <eos>, and <pad> from a list of tokens."""
    return [token for token in tokens if token not in ['<cls>', '<eos>', '<pad>']]

class ESM2(ProteinModel):
    def __init__(self, model_name: str = "esm2_t33_650M_UR50D", device: str = None, decoder_path: str = None, max_seq_len: int = None):
        self.device = device if device else ('cuda' if torch.cuda.is_available() else 'cpu')
        self.model, self.alphabet = pretrained.esm2_t33_650M_UR50D()
        self.model.to(self.device)
        self.model.eval()
        self.max_seq_len = max_seq_len

    def encode(self, sequence: str):
        batch_converter = self.alphabet.get_batch_converter()
        data = [("seq", sequence)]
        _, _, batch_tokens = batch_converter(data)
        batch_tokens = batch_tokens.to(self.device)
        with torch.no_grad():
            results = self.model(batch_tokens, repr_layers=[33])
        embedding = results["representations"][33]
        return embedding

    def decode(self, embedding):
        with torch.no_grad():
            output_logits = self.model.lm_head(embedding)
            predicted_token_ids = output_logits.argmax(dim=-1)
        tokens = [self.alphabet.get_tok(idx) for idx in predicted_token_ids[0]]
        tokens = remove_special_tokens(tokens)
        decoded_sequence = "".join(tokens)
        return decoded_sequence

    def batch_encode(self, sequences):
        batch_converter = self.alphabet.get_batch_converter()
        data = [(str(i), seq) for i, seq in enumerate(sequences)]
        _, _, batch_tokens = batch_converter(data)
        batch_tokens = batch_tokens.to(self.device)
        with torch.no_grad():
            results = self.model(batch_tokens, repr_layers=[33])
        token_embeddings = results["representations"][33]
        return token_embeddings, batch_tokens

    def batch_decode(self, embeddings, detokenized=True):
        with torch.no_grad():
            output_logits = self.model.lm_head(embeddings)
        if detokenized:
            predicted_token_ids = output_logits.argmax(dim=-1)
            decoded_sequences = []
            for i in range(predicted_token_ids.size(0)):
                tokens = [self.alphabet.get_tok(idx) for idx in predicted_token_ids[i]]
                tokens = remove_special_tokens(tokens)
                decoded_sequence = "".join(tokens)
                decoded_sequences.append(decoded_sequence)
            return decoded_sequences
        else:
            return output_logits

class ESM2EncoderModel(ESM2):
    """
    Inherits from ESM2 and (optionally) applies normalization
    to the output embeddings.
    """
    def __init__(self, config, device, enc_normalizer=None, decoder_path=None, max_seq_len=256):
        super().__init__(model_name=config.model.hg_name, device=device, decoder_path=decoder_path, max_seq_len=max_seq_len)
        self.enc_normalizer = enc_normalizer

    def batch_encode(self, sequences):
        outputs, tokenized = super().batch_encode(sequences)
        if self.enc_normalizer is not None:
            outputs = self.enc_normalizer.normalize(outputs)
        return outputs, tokenized

    def batch_decode(self, embeddings, detokenized=True):
        if self.enc_normalizer is not None:
            embeddings = self.enc_normalizer.denormalize(embeddings)
        return super().batch_decode(embeddings, detokenized)
