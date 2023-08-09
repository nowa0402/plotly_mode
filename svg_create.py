import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

N = 20
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)

plot = [
    go.Scatter(
        mode="lines+markers",
        x=random_x,
        y=random_y0,
        name="sampleA",
        line=dict(color="blue", dash="solid"),
        marker=dict(symbol="circle-open"),
    ),
    go.Scatter(
        mode="lines+markers",
        x=random_x,
        y=random_y1,
        name="sampleB",
        line=dict(color="red", dash="solid"),
        marker=dict(symbol="circle-open"),
    ),
]

fig = go.Figure(data=plot)
pio.write_image(fig, "./output.svg", format="svg")
