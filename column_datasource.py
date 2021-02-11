import pandas as pd
import colorcet as cc
from numpy import linspace
from scipy.stats.kde import gaussian_kde

from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, FixedTicker, PrintfTickFormatter, HoverTool
from bokeh.plotting import figure
from bokeh.models.tools import HoverTool
from bokeh.sampledata.perceptions import probly

#Save our figure with .html extension
ouput_file = ('hitpredictormodel.html')

#Insert the absolute path of csv into method
df = pd.read_csv('/Users/Valerie/dataset-of-00s.csv')

#Group track per hit factors
grouped = df.groupby('Track')[ 'artist', 'danceability', 'energy', 'speechiness', 'liveness', 'valence', 'target'].sum() * 100


#Random sample in df
sample = df.sample(50)

#Pass data into columndatasource and store sample in source
source = ColumnDataSource(sample)

