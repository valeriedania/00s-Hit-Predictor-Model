import pandas as pd
import colorcet as cc
from numpy import linspace
from scipy.stats.kde import gaussian_kde

from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, FixedTicker, PrintfTickFormatter, HoverTool
from bokeh.plotting import figure
from bokeh.sampledata.perceptions import probly

#Save our figure with .html extension
ouput_file = ('hitpredictormodel.html')

#Insert the absolute path of csv into method
data = pd.read_csv('/Users/Valerie/dataset-of-00s.csv')

#Use only a subset of columns in csv file and store in df
df = pd.DataFrame(data, columns = ['Track', 'Artist', 'Danceability', 'Energy', 'Speechiness', 'Liveness', 'Valence', 'Target'])

#Random sample in df
sample = df.sample(50)

#Store sample in source
source = ColumnDataSource(sample)

#Calculate percentage
hit_factors = ['Danceabilitiy', 'Energy', 'Speechiness', 'Liveness', 'Valence', 'Target']
df['percent'] = (df[hit_factors]/ df[hit_factors].sum()) * 100

print(df)
