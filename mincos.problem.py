# """From Bradley, Hax, and Magnanti, 'Applied Mathematical Programming', figure 8.1."""

from __future__ import print_function
from ortools.graph import pywrapgraph

def main():
  """MinCostFlow simple interface example."""

  # Define four parallel arrays: start_nodes, end_nodes, capacities, and unit costs
  # between each pair. For instance, the arc from node 0 to node 1 has a
  # capacity of 15 and a unit cost of 4.

  start_nodes = [0,1,2,3,4,5,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21]
  end_nodes   = [1,2,3,4,5,6,1,2,1,3,1,4,1,5,1,6,2,3,2,4,2,5,2,6,3,4,3,5,3,6,4,5,4,6,5,6]
  capacities  = [10000,524,524,524,524,524,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000]
  unit_costs  = [0,0,0,0,0,0,-124.8940769,0,-172.802348,0,-112.2357562,0,-249.3092992,0,-73.22644148,0,-115.7772894,0,-132.3031775,0,-176.4579843,0,-145.8447219,0,-140.9032815,0,-138.3402673,0,-186.9392277,0,-228.6726052,0,-111.5078279,0,-267.5914084,0]

  # Define an array of supplies at each node.

  supplies = [0,-430,-593,-1118,-1218,-1852,430,350,356,360,357,243,391,219,418,371,377,414,262,210,453]

  # Instantiate a SimpleMinCostFlow solver.
  min_cost_flow = pywrapgraph.SimpleMinCostFlow()

  # Add each arc.
  for i in range(1, len(start_nodes)):
    min_cost_flow.AddArcWithCapacityAndUnitCost(start_nodes[i], end_nodes[i],
                                                capacities[i], unit_costs[i])

  # Add node supplies.

  for i in range(1, len(supplies)):
    min_cost_flow.SetNodeSupply(i, supplies[i])


  # Find the minimum cost flow between node 0 and node 4.
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
