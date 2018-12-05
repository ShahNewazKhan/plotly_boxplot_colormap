from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

x_data = ['Henrik Sedin', 'Daniel Sedin',
          'Brock Boeser', 'Elias Pettersen',
          'Bo Horvat', 'Pavel Bure',]

y0 = np.random.randn(50)+4
y1 = np.random.randn(50)+4
y2 = np.random.randn(50)+2
y3 = np.random.randn(50)+2
y4 = np.random.randn(50)+1
y5 = np.random.randn(50)+3

y_data = [y0,y1,y2,y3,y4,y5]

traces = []

df = pd.DataFrame(y_data)
vmin, vmax = df.min().min(), df.max().max()

norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)
cmap = matplotlib.cm.get_cmap('GnBu')

for xd, yd in zip(x_data, y_data):
        median = np.median(yd)
        color = 'rgb' + str(cmap(norm(median))[0:3])
        
        traces.append(go.Box(
            y=yd,
            name=xd,
            boxpoints='all',
            jitter=0.5,
            whiskerwidth=0.2,
            fillcolor=color,
            marker=dict(
                size=2,
                color='rgb(0, 0, 0)'
            ),
            line=dict(width=1),
        ))

layout = go.Layout(
    title='Canucks all time +/- per game',
    yaxis=dict(
        autorange=True,
        showgrid=True,
        zeroline=True,
        dtick=5,
        gridcolor='rgb(255, 255, 255)',
        gridwidth=1,
        zerolinecolor='rgb(255, 255, 255)',
        zerolinewidth=2,
    ),
    margin=dict(
        l=40,
        r=30,
        b=80,
        t=100,
    ),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
    showlegend=False,
    shapes= [{
      'type': 'line',
      'x0': -1,
      'y0': 2,
      'x1': 6,
      'y1': 2,
      'line': {
        'color': 'rgb(50, 171, 96)',
        'width': 4,
        'dash': 'dashdot'
      }
    }]
)

fig = go.Figure(data=traces, layout=layout)
plot(fig)