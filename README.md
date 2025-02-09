# Generative AI in Protein Engineering using Large Language Models

This repository contains the research and implementation for **Generative AI in Protein Engineering using Large Language Models (LLMs)**, focusing on **protein sequence interpolation, synthetic antimicrobial peptide (AMP) generation, and ancestral sequence reconstruction (ASR)**.

## 🚀 **Project Overview**
This work applies **deep learning models, including ESM-2 and EvoDiff**, to generate and analyze protein sequences. The research explores:
- **Protein Interpolation:** Using embeddings from **Meta’s Evolutionary Scale Modeling (ESM-2)** to interpolate between two protein sequences.
- **AMP Generation and Ranking:** Leveraging EvoDiff to generate and rank synthetic **antimicrobial peptides (AMPs)**.
- **Ancestral Sequence Reconstruction (ASR):** Using **conditional EvoDiff** to generate ancestral sequences and analyze their evolution.

## 📂 **Repository Structure**
```
.
├── README.md
├── generated-data  
│   ├── CAMPs-Ranking 
│   ├── EVODIFFs-Conditional-Generation # conditional-generation of protein sequences using ASR
│   ├── LoRA-Logits
│   └── interpolated_sequences.csv
├── notebooks
│   ├── conditional-evodiff-gen-ASR.ipynb
│   ├── evodiff-conditional-gen-demo.ipynb # demo: cond. EvoDiff generation (mask aminoacids)
│   └── protein-interpolation.ipynb  # interpolate protein sequences using ESM ecoder-decoder
├── plots
├── requirements.txt
├── setup.py
└── src
    ├── Ranking-AMPS.py
    ├── Ranking-CAMPS.py
    ├── __init__.py
    ├── __pycache__
    ├── configurations.py 
    ├── esm_model.py 
    ├── fireprot_asr_analysis.py # main class for ASR; Ancestors tree + probs. of aminoacids
    ├── interpolations.py
    ├── utils.py
    └── visualization.py
```

## 🧬 **1. Protein Interpolation**
**Goal:** Interpolate between two protein sequences using ESM-2 embeddings and generate meaningful transitions.

**Methods:**
- **Linear Interpolation:** Computes weighted averages between two protein embeddings.
- **Sinusoidal Interpolation:** Uses a sinusoidal function for smooth transitions.
- **Arccos Interpolation:** Implements an arccosine-based transformation.

**Results:**
- Interpolated sequences are visualized using **UMAP dimensionality reduction**.
- The decoded sequences are evaluated using **Levenshtein distance analysis**.

🔹 **Output Data:** Saved in `generated-data/interpolated_sequences.csv`.

## 🔬 **2. EvoDiff for Protein Generation**
**Goal:** Use **EvoDiff**, a diffusion-based framework, for generating protein sequences in sequence space.

**Key Approaches:** 🦾
- **Order-Agnostic Autoregressive Diffusion (OADM):** Progressive masking and unmasking of amino acids.
- **Discrete Denoising Diffusion Probabilistic Models (D3PM):** Used for sequence-based protein generation.

**Models Used:**
- **OA_DM 38M & 640M** (Order-Agnostic Models)
- **D3PM BLOSUM 38M & 640M** (Denoising Models)

## 🦠 **3. Generating & Ranking Synthetic AMPs**
**Goal:** Use EvoDiff to generate **synthetic antimicrobial peptides (AMPs)** and rank them.

**Methods:**
1. **Collection of Anti-Microbial Peptides (CAMP) Database**
   - Uses **SVM & Random Forest** classifiers to rank AMPs.
2. **ESM2 Classifier with LoRA Optimization**
   - Fine-tunes ESM2 using **Low-Rank Adaptation (LoRA)** for AMP classification.

## 🌲 **4. Ancestral Sequence Reconstruction (ASR)**
**Goal:** Reconstruct ancestral protein sequences using **Conditional EvoDiff**.

**Steps:**
1. **Phylogenetic Tree Construction**
   - Built using **FireProt-ASR**.
2. **Conditional Generation with EvoDiff**
   - Uses **masked ancestral sequences** to predict missing residues.
3. **Evaluation**
   - Selected top sequences are analyzed using **AlphaFold2-3D**.

## 📊 **5. Visualization**
- **UMAP Dimensionality Reduction** (`visualization.py`)
- **3D Structure Analysis with AlphaFold2-3**

## ⚡ **Installation**
To set up the environment, install dependencies:
```bash
pip install -r requirements.txt
```

## 🏗 **Repository Workflow**
This repository is structured into three main parts:

1️⃣ **Protein Interpolation** (`protein-interpolation.ipynb`)  
   - Uses **ESM-2 embeddings** to interpolate between two protein sequences.
   - Implements **linear, sinusoidal, and arccos interpolation** techniques.
   - Outputs interpolated sequences stored in `generated-data/interpolated_sequences.csv`.

2️⃣ **Conditional Generation using EvoDiff Diffusion Models**  
   - A quick demonstration of EvoDiff-based conditional generation is available in:  
     📂 `evodiff-conditional-gen-demo.ipynb`

3️⃣ **Main: Conditional EvoDiff with ASR** (`conditional-evodiff-gen-ASR.ipynb`)  
   - Uses **Conditional EvoDiff & FireProt-ASR** to reconstruct ancestral sequences.
   - Explores **phylogenetic-based protein sequence prediction**.

## 🤝 **Contributions**
Feel free to contribute via **pull requests** or raise an **issue** if you find bugs or have suggestions.

## 📜 **References**
- [EvoDiff GitHub](https://github.com/microsoft/evodiff)
- [Meta ESM-2](https://github.com/facebookresearch/esm)
- [FireProt-ASR](https://loschmidt.chemi.muni.cz/fireprotasr/)
- [AlphaFold](https://www.deepmind.com/alphafold)

🎯 **This project aims to push the boundaries of protein design using deep learning, with applications in synthetic biology, drug discovery, and enzyme engineering.** 🚀
