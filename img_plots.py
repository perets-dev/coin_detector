import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from typing import Callable


def make_badge_scatter(
    df: pd.DataFrame,
    img_provider:Callable[[str], OffsetImage],
    **subplot_kwargs
) -> tuple:
    REQ_COLS = {'x', 'y', 'keys'}
    if len(set(df.columns).union(REQ_COLS)) > len(df.columns):
        raise ValueError(f'Required cols for the input dataframe {REQ_COLS}')
        
    fig, ax = plt.subplots(**subplot_kwargs)
    ax.scatter(df['x'], df['y'])
    for index, row in df.iterrows():
        ab = AnnotationBbox(img_provider(row['keys']), (row['x'], row['y']),
                            frameon=False)
        ax.add_artist(ab)
    plt.grid(True)
    return fig, ax