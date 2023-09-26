# """From Bradley, Hax, and Magnanti, 'Applied Mathematical Programming', figure 8.1."""

from __future__ import print_function
from ortools.graph import pywrapgraph

def main():
  """MinCostFlow simple interface example."""

  # Define four parallel arrays: start_nodes, end_nodes, capacities, and unit costs
  # between each pair. For instance, the arc from node 0 to node 1 has a
  # capacity of 15 and a unit cost of 4.

  start_nodes = [4,10,7,10,2,4,5,10,2,7,4,8,2,5,7,8,1,4,1,7,5,8,2,6,6,10,9,10,1,5,3,4,6,8,1,6,3,7,2,9,3,5,1,10,8,9,3,10,4,6,4,9,2,10,7,9,3,6,8,10,1,9,2,3,6,9,5,9,3,9,3,8,5,6,1,3,6,7,4,7,4,5,1,2,1,8,2,8,5,7]
  end_nodes   = [10,4,10,7,4,2,10,5,7,2,8,4,5,2,8,7,4,1,7,1,8,5,6,2,10,6,10,9,5,1,4,3,8,6,6,1,7,3,9,2,5,3,10,1,9,8,10,3,6,4,9,4,10,2,9,7,6,3,10,8,9,1,3,2,9,6,9,5,9,3,8,3,6,5,3,1,7,6,7,4,5,4,2,1,8,1,8,2,7,5]
  capacities  = [479,389,429,302,429,272,353,341,458,321,235,491,343,368,220,477,313,341,366,364,216,392,476,464,493,444,463,248,221,328,227,286,248,429,241,255,280,254,400,459,340,407,296,280,205,468,211,350,407,268,358,333,344,220,403,261,381,421,338,444,447,308,311,224,332,349,348,300,480,329,475,462,410,244,393,472,455,224,376,379,401,327,428,478,279,306,416,232,429,397]
  unit_costs  = [0,-311.6959523,-311.6959523,-283.3973928,-283.3973928,-277.1018595,-277.1018595,-273.4763749,-273.4763749,-267.5914084,-267.5914084,-258.8548069,-258.8548069,-249.3092992,-249.3092992,-246.1719094,-246.1719094,-239.2905571,-239.2905571,-231.5968898,-231.5968898,-228.8443,-228.8443,-228.6726052,-228.6726052,-226.0959849,-226.0959849,-220.1366203,-220.1366203,-212.5159544,-212.5159544,-208.4631389,-208.4631389,-205.0540507,-205.0540507,-197.4937533,-197.4937533,-186.9392277,-186.9392277,-176.4579843,-176.4579843,-172.802348,-172.802348,-163.6249926,-163.6249926,-158.0728736,-158.0728736,-154.9346814,-154.9346814,-153.2946234,-153.2946234,-150.853229,-150.853229,-147.9968449,-147.9968449,-145.8447219,-145.8447219,-140.9032815,-140.9032815,-138.9535928,-138.9535928,-138.8583162,-138.8583162,-138.3402673,-138.3402673,-132.3031775,-132.3031775,-124.8940769,-124.8940769,-115.7772894,-115.7772894,-114.3822347,-114.3822347,-112.2357562,-112.2357562,-111.7482741,-111.7482741,-111.5078279,-111.5078279,-98.15913963,-98.15913963,-91.49648287,-91.49648287,-87.92154685,-87.92154685,-76.21600484,-76.21600484,-74.22911793,-74.22911793,-73.22644148,-73.22644148]

  # Define an array of supplies at each node.

  supplies = [0,0,524,0,0,0,0,0,-524]

  # Instantiate a SimpleMinCostFlow solver.
  min_cost_flow = pywrapgraph.SimpleMinCostFlow()

  # Add each arc.
  for i in range(0, len(start_nodes)):
    min_cost_flow.AddArcWithCapacityAndUnitCost(start_nodes[i], end_nodes[i],
                                                capacities[i], unit_costs[i])

  # Add node supplies.

  for i in range(0, len(supplies)):
    min_cost_flow.SetNodeSupply(i, supplies[i])


  # Find the minimum cost flow between node 0 and last node.
  if min_cost_flow.Solve() == min_cost_flow.OPTIMAL:
    print('Minimum cost:', min_cost_flow.OptimalCost())
    print('')
    print('  Arc    Flow / Capacity  Cost')
    for i in range(min_cost_flow.NumArcs()):
      cost = min_cost_flow.Flow(i) * min_cost_flow.UnitCost(i)
      print('%1s -> %1s   %3s  / %3s       %3s' % (
          min_cost_flow.Tail(i),
          min_cost_flow.Head(i),
          min_cost_flow.Flow(i),
          min_cost_flow.Capacity(i),
          cost))
  else:
    print('There was an issue with the min cost flow input.')

if __name__ == '__main__':
  main()
