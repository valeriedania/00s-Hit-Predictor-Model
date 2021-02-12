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

#From ridgeplot.py template
def ridge(category, data, scale=20):
    return list(zip([category]*len(data), scale*data))

cats = list(reversed(probly.keys()))
palette = [cc.rainbow[i*15] for i in range(17)]
x = linspace(-20,110, 500)

#Insert the absolute path of csv into method
df = pd.read_csv('/Users/Valerie/dataset-of-00s.csv')

#Group track per hit factors
grouped = df.groupby(['track'])[ ['artist', 'danceability', 'energy', 'speechiness', 'liveness', 'valence', 'target']].mean() 

#Pass data into columndatasource and store sample in source
source = ColumnDataSource(grouped)

p = figure(y_range=cats, plot_width=900, x_range=(-5, 105), toolbar_location=None)

#Also from Bokeh's ridgeplot documentation
for i, cat in enumerate(reversed(cats)):
    pdf = gaussian_kde(probly[cat])
    y = ridge(cat, pdf(x))
    source.add(y, cat)
    p.patch('x', cat, color=palette[i], alpha=0.6, line_color="black", source=source)

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
p.xaxis.axis_label = Hit Likelihood
p.yaxis.axis_label = Average

#Add hovertool
hover = HoverTool()
hover.tooltips = [
    ('track', '@track'),
    ('artist', '@artist'),
    ('danceability' '@danceability'), 
    ('energy', '@energy'), 
    ('speechiness' '@speechiness'), 
    ('liveness', '@liveness'), 
    ('valence', '@valence')
    ('target', '@target')


show(p)
