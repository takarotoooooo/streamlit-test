from pathlib import Path
import pandas as pd

class Dataset:
    def __init__(self):
        app_root_dir = Path(__file__).resolve().parent.parent
        self.movies = pd.read_csv(app_root_dir.joinpath('datasets/ml-latest/movies.csv'))
