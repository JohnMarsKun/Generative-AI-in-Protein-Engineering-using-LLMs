import umap.umap_ as umap
import matplotlib.pyplot as plt
import numpy as np

def plot_umap_2d(embeddings, labels, title="UMAP projection of embeddings", save_path=None):
    """
    Compute a 2D UMAP projection of `embeddings` and plot them, coloring points according to `labels`.
    """
    reducer = umap.UMAP()
    umap_embeddings = reducer.fit_transform(embeddings)
    
    plt.figure(figsize=(12,8))
    unique_labels = set(labels)
    for label in unique_labels:
        indices = [i for i, l in enumerate(labels) if l == label]
        plt.scatter(umap_embeddings[indices, 0], umap_embeddings[indices, 1], label=label)
    plt.legend()
    plt.title(title)
    plt.xlabel("UMAP1")
    plt.ylabel("UMAP2")
    if save_path:
        plt.savefig(save_path)
    plt.show()

def plot_umap_3d(embeddings, labels, title="3D UMAP projection of embeddings"):
    """
    Compute a 3D UMAP projection of `embeddings` and create a 3D scatter plot colored by `labels`.
    """
    reducer = umap.UMAP(n_components=3)
    umap_embeddings = reducer.fit_transform(embeddings)
    
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111, projection='3d')
    unique_labels = set(labels)
    colors = plt.cm.rainbow(np.linspace(0, 1, len(unique_labels)))
    for label, color in zip(unique_labels, colors):
        indices = [i for i, l in enumerate(labels) if l == label]
        ax.scatter(umap_embeddings[indices, 0],
                   umap_embeddings[indices, 1],
                   umap_embeddings[indices, 2],
                   label=label,
                   color=color)
    ax.legend()
    ax.set_title(title)
    ax.set_xlabel("UMAP1")
    ax.set_ylabel("UMAP2")
    ax.set_zlabel("UMAP3")
    plt.show()
