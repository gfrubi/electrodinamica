# paste this code at the end of VectorFieldPlot 1.1
doc = FieldplotDocument('fig-conductor-y-campo', width=600, height=600, commons=True)
field_direction = [0.0, 1.0]
ball_radius = 1.2
field = Field({'homogeneous':[field_direction],
    'dipoles':[[0, 0, 4*pi*ball_radius**3*field_direction[0], 4*pi*ball_radius**3*field_direction[1]]]})
n = 20
for i in range(n):
    a = -3 + 6 * (0.5 + i) / n
    line = FieldLine(field, [a, 6], maxr=12, pass_dipoles=1, directions='backward')
    if abs((n - 1.) / 2. - i) > 7: off = 4 * [0.5]
    else: off = 4 * [0.25]
    doc.draw_line(line, arrows_style={'min_arrows':2, 'max_arrows':2, 'offsets':off})
# draw the superconducting ball
ball = doc.draw_object('g', {'id':'metal_ball'})
grad = doc.draw_object('radialGradient', {'id':'metal_spot', 'cx':'0.53', 'cy':'0.54',
    'r':'0.55', 'fx':'0.65', 'fy':'0.7', 'gradientUnits':'objectBoundingBox'}, group=ball)
for col, of in (('#fff', 0), ('#e7e7e7', 0.15), ('#ddd', 0.25), ('#aaa', 0.7), ('#888', 0.9), ('#666', 1)):
    doc.draw_object('stop', {'offset':of, 'stop-color':col}, group=grad)
doc.draw_object('circle', {'cx':0, 'cy':0, 'r':str(ball_radius),
    'style':'fill:url(#metal_spot); stroke:#000; stroke-width:0.02'}, group=ball)
doc.write()
