#%%

from pyvis import network as net
from IPython.core.display import display, HTML

ids=['C', 'N', 'C', 'N', 'C', 'C', 'C', 'O', 'N', 'C', 'O', 'N', 'C', 'C']
xs=[2.776, 1.276, 0.3943, -1.0323, -1.0323, 0.3943, 0.7062, 2.1328, -0.4086, -1.8351, -2.9499, -2.147, -3.5736, -0.0967]
ys=[0.0, 0.0, 1.2135, 0.75, -0.75, -1.2135, -2.6807, -3.1443, -3.6844, -3.2209, -4.2246, -1.7537, -1.2902, -5.1517]
bonds=[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [6, 8], [8, 9], [9, 10], [9, 11], [11, 12], [8, 13], [5, 1], [11, 4]]
g3=net.Network(height='400px', width='80%',heading='')
g3.set_options('''
var options = {
    "nodes": {
    "borderWidth": 2,
    "borderWidthSelected": 4
  },
  "edges":{
    "width":24
  },
  "physics": {
    "barnesHut": {
      "gravitationalConstant":-2000,
      "centralGravity": 0,
      "springLength": 60,
      "springConstant": 0.545,
      "damping": 0.1,
      "avoidOverlap": 0.52
    },
    "maxVelocity:":50,
    "minVelocity": 0.75,
    "timestep": 0.5
  }
}
''')
for atomo in range(14): 
  g3.add_node(atomo,label=ids[atomo],x=int(100*xs[atomo]),y=int(100*ys[atomo]),physics=True,size=30)

g3.add_edges(bonds)
# show_graph(g3,'g3.html')
g3.show('d3graph.html')
