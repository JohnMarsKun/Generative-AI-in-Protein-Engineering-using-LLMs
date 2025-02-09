import pandas as pd
import matplotlib.pyplot as plt

### Visit https://loschmidt.chemi.muni.cz/fireprotasr/ for more ###

class FireProtASR_AminoAcid_Analysis:
    def __init__(self, file_path: str):
        """
        Initialize the AminoAcidAnalysis class with a file path.

        Args:
        - file_path (str): Path to the CSV file containing ancestral data.
        """
        self.file_path = file_path
    
    def plot_amino_acid_distribution(self, node: int, position: int):
        """
        Plots the amino acid probability distribution for a specific node and position.
        """
        data = pd.read_csv(self.file_path)
        row = data[(data['node'] == node) & (data['position'] == position)]
        
        if row.empty:
            print(f"No data found for node {node} at position {position}.")
            return
        
        # Extract amino acids and probabilities
        amino_acids = row.columns[3:]  # Skipping node, position, and '-'
        probabilities = row.iloc[0, 3:].astype(float)  # Convert probabilities to float
        
        # Ensure alignment of amino acids with probabilities
        amino_acid_probs = dict(zip(amino_acids, probabilities))
        amino_acid_probs = {aa: prob for aa, prob in amino_acid_probs.items() if prob > 0}
        
        # Sort amino acids by probability for cleaner plotting
        amino_acid_probs = dict(sorted(amino_acid_probs.items(), key=lambda x: x[1], reverse=True))
        
        # Plotting
        plt.figure(figsize=(10, 6))
        plt.bar(amino_acid_probs.keys(), amino_acid_probs.values(), color='bisque', edgecolor='black')
        plt.xlabel('Amino Acids')
        plt.ylabel('Probability')
        plt.title(f'Probability Distribution for Node {node}, Position {position}')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


    def find_most_probable_amino_acid(self, node: int, position: int):
        """
        Finds the most probable amino acid for a given node and position.
        Returns a tuple of the amino acid and its probability.
        """
        data = pd.read_csv(self.file_path)
        row = data[(data['node'] == node) & (data['position'] == position)]
        
        if row.empty:
            print(f"No data found for node {node} at position {position}.")
            return None
        
        amino_acids = row.columns[3:]  # Skipping node, position, and '-'
        probabilities = row.iloc[0, 3:]
        max_index = probabilities.idxmax()
        max_value = probabilities[max_index]
        
        return max_index, max_value

    def plot_most_probable_amino_acids(self, node: int, stop: int = None, threshold: float = None):
        """
        Plots the most probable amino acid and highlights those above a given threshold.
        """
        data = pd.read_csv(self.file_path)
        node_data = data[data['node'] == node]
        
        if node_data.empty:
            print(f"No data found for node {node}.")
            return
        
        positions = []
        amino_acids = []
        probabilities = []
        
        for _, row in node_data.iterrows():
            position = int(row['position'])
            
            if stop is not None and position > stop:
                break
            
            position_probs = row.iloc[3:].replace('-', 0).astype(float)
            most_probable_amino_acid = position_probs.idxmax()
            max_probability = position_probs.max()
            positions.append(position)
            amino_acids.append(most_probable_amino_acid)
            probabilities.append(max_probability)
        
        if threshold is not None:
            bar_colors = ['ForestGreen' if prob > threshold else 'bisque' for prob in probabilities]
            green_count = sum(1 for prob in probabilities if prob > threshold)
            green_percentage = (green_count / len(probabilities)) * 100
        else:
            bar_colors = 'bisque'
            green_percentage = 0
        
        plt.figure(figsize=(30, 8))
        plt.bar(positions, probabilities, color=bar_colors, edgecolor='black')
        
        if threshold is not None:
            plt.axhline(y=threshold, color='red', linestyle='--', label=f'Threshold = {threshold}')
            plt.legend(loc='upper right')
            plt.text(
                0.935, 0.86, 
                "$\mathbf{Green}$ $\mathbf{Bars}$: " + f"{green_percentage:.2f}% (Above Threshold)", 
                ha='right', transform=plt.gcf().transFigure, fontsize=12, color='ForestGreen'
            )
        
        for pos, aa, prob in zip(positions, amino_acids, probabilities):
            plt.text(pos, prob + 0.01, str(aa), ha='center', fontsize=10)
        
        plt.xlabel('Position')
        plt.ylabel('Probability')
        plt.title(f'Most Probable Amino Acids for Node {node} (Up to Position {stop if stop else "Full Length"})')
        plt.xticks(positions, rotation=45)
        plt.tight_layout()
        plt.show()

    def masked_amino_acids(self, node: int, threshold: float):
        """
        Returns a list of positions for the given node where the most probable amino acid's
        probability is NOT above the specified threshold.
        """
        data = pd.read_csv(self.file_path)
        node_data = data[data['node'] == node]
        
        if node_data.empty:
            print(f"No data found for node {node}.")
            return []
        
        positions_below_threshold = []
        
        for _, row in node_data.iterrows():
            position = int(row['position'])
            position_probs = row.iloc[3:].replace('-', 0).astype(float)
            max_probability = position_probs.max()
            
            if max_probability <= threshold:
                positions_below_threshold.append(position)
        
        return positions_below_threshold

    def get_node_sequence(self, node: int) -> str:
            """
            Returns the amino acid sequence for the given node.

            Args:
            - node (int): The node to analyze.

            Returns:
            - str: The sequence of the most probable amino acids for the node.
            """
            data = pd.read_csv(self.file_path)
            node_data = data[data['node'] == node]
            
            if node_data.empty:
                print(f"No data found for node {node}.")
                return ""
            
            sequence = []
            for _, row in node_data.iterrows():
                position_probs = row.iloc[3:].replace('-', 0).astype(float)
                most_probable_amino_acid = position_probs.idxmax()
                sequence.append(most_probable_amino_acid)
            
            return "".join(sequence)