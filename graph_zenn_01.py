import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

# データ数10のランダムな折れ線グラフを描画
# 参考:https://plotly.com/python/line-charts/
N = 19
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 5

plot = [
    go.Scatter(
        x=random_x,
        y=random_y0,
        name="sampleA",
        line=dict(color="blue", dash="solid"),
        marker=dict(symbol="circle-open"),
    ),
]


fig = go.Figure(data=plot)
pio.write_image(fig, "./output.png", format="png")
