import matplotlib.pyplot as plt

def plot_amp_histogram(file_path, model_name: str = ''):
    """
    Reads a file and plots a histogram of the count of sequences categorized as AMPs
    (with probability >= 0.5) against their sequence lengths.

    Parameters:
    - file_path (str): The path to the input file.

    The input file is expected to have the following tab-separated format:
    Seq. ID.	Class	AMP Probability
    LENGTH_X_SEQ_Y	[AMP/NAMP]	[Probability]

    Example:
    LENGTH_5_SEQ_1	NAMP	0.26
    """
    # Dictionary to hold counts of AMPs per length
    amp_counts = {}
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    # Skip the header
    lines = lines[1:]
    
    for line in lines:
        # Skip empty or malformed lines
        if not line.strip():
            continue
        # Split the line into components
        parts = line.strip().split()
        if len(parts) != 3:
            continue  # Skip lines that don't have exactly 3 parts
        seq_id, class_label, prob_str = parts
        try:
            prob = float(prob_str)
        except ValueError:
            continue  # Skip lines where probability is not a float
        if prob >= 0.5:
            # Extract length from seq_id
            # The seq_id is in the format LENGTH_X_SEQ_Y
            # We can split by '_'
            seq_id_parts = seq_id.split('_')
            if len(seq_id_parts) >= 2:
                length_str = seq_id_parts[1]
                try:
                    length = int(length_str)
                except ValueError:
                    continue  # Skip if length is not an integer
                # Accumulate counts
                if length in amp_counts:
                    amp_counts[length] += 1
                else:
                    amp_counts[length] = 1
    # Now we have amp_counts mapping lengths to counts
    # Let's sort the lengths
    lengths = sorted(amp_counts.keys())
    counts = [amp_counts[length] for length in lengths]
    
    # Plotting
    plt.bar(lengths, counts, color='skyblue')
    plt.xlabel('Length of Sequences')
    plt.ylabel('Count of AMPs (Probability >= 0.5)')
    plt.title('AMPs by Sequence Length ' + model_name)
    plt.xticks(lengths)  # Set x-ticks to be the lengths
    plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)
    plt.tight_layout()
    #plt.savefig("/home/johnny/Downloads/CAMP-rankings/RankingHist-CAMP-OA_DM-RF.pdf")
    plt.show()

# CAMP-rank-D3PM-RF.txt
file_path = '/home/johnny/Downloads/CAMP-rankings/CAMP-RF_500n_5-50-5-lenStep-OA_DM_640M.txt' #  file_path = '/home/johnny/Downloads/EvoDiff-AMPs/CAMP-rank-D3PM-ANN.txt'
plot_amp_histogram(file_path, '(RF) - OA_DM640M')


# from Bio import Phylo
# import matplotlib.pyplot as plt


# # Define the path to the uploaded tree file
# tree_path = '/home/johnny/Downloads/Fire-Prot-ASR/results_xilpzk_462-PETH_PISS1/results/tree.tre'

# # Read the phylogenetic tree from the file
# tree = Phylo.read(tree_path, "newick")

# # Plot the phylogenetic tree
# plt.figure(figsize=(10, 8))
# Phylo.draw(tree, do_show=False)
# plt.title("Phylogenetic Tree from ASR Analysis")
# plt.show()
