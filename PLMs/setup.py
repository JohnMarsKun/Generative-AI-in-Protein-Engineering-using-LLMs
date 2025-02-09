from setuptools import setup, find_packages

setup(
    name='PLMs',
    version='0.1.0',
    description='Generative AI in protein engineering using LLMs',
    author='John Maris',
    author_email='gianismaris13@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'esm==2.0.1',
        'torch==2.3.1',
        'numpy==1.26.4',
        'umap-learn==0.5.6',
        'transformers==4.42.3',
        'wandb==0.17.9',
        'tqdm==4.67.1',
        'pandas==2.2.3',
        'ml-collections==0.1.1',
        'matplotlib==3.8.3',
        'scipy==1.11.2',
        'torch_geometric==2.6.0',
        'biotite==0.41.2'
    ],
    entry_points={
        'console_scripts': [
        ],
    },
)
