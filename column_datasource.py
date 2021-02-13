import pandas as pd
import colorcet as cc
from numpy import linspace

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
grouped = df.groupby(['track'])[ ['danceability', 'energy', 'speechiness', 'liveness', 'valence', 'target']].mean() 

#Pass data into columndatasource and store sample in source
source = ColumnDataSource(grouped)
songs = source.data['track'].tolist()

#From ridgeplot.py template
def ridge(category, data, scale=20):
    return list(zip([category]*len(data), scale*data))

palette = [cc.rainbow[i*15] for i in range(17)]
x = linspace(-20,110, 500)

p = figure(y_range=songs, plot_width=900, x_range=(-5, 105), toolbar_location=None)

for i, song in enumerate(songs):
    y = ridge(songs, grouped)
    source.add(y, songs)
    p.patch('x', songs, color=palette[i], alpha=0.6, line_color="black", source=source)

p.outline_line_color = None
p.background_fill_color = "#efefef"

p.xaxis.ticker = FixedTicker(ticks=list(range(0, 101, 10)))
p.xaxis.formatter = PrintfTickFormatter(format="%d%%")

p.ygrid.grid_line_color = None
p.xgrid.grid_line_color = "#dddddd"
p.xgrid.ticker = p.xaxis.ticker

p.axis.minor_tick_line_color = None
p.axis.major_tick_line_color = None
p.axis.axis_line_color = None

p.y_range.range_padding = 0.12

#Add labels 
p.title.text = '2000s Hit Predictor Model'
p.xaxis.axis_label = 'Hit Likelihood'
p.yaxis.axis_label = 'Average' 

'''
#Add hovertool
hover = HoverTool()
hover.tooltips = [
    ('track', '@track'),
    #('artist', '@artist'),
    ('danceability' '@danceability'), 
    ('energy', '@energy'), 
    ('speechiness' '@speechiness'), 
    ('liveness', '@liveness'), 
    ('valence', '@valence'),
    ('target', '@target')
]

hover.mode = 'vline'

p.add_tools(hover)
'''
show(p)



