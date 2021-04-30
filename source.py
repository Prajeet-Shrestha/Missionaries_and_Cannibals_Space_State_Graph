
# Author: Prajeet Shrestha
# Roll Number: 43
# prazzeettstha@gmail.com
# Computer Science Batch 2017

from queue import Queue
from node import Node
from treelib import Tree
import numpy as np


def TreeGenerator(initial_state,isDetailed):
    tree  = Tree()
    start_node = Node(initial_state, None, None,0)
    if start_node.goal_test():
        return start_node.find_solution()
    q = Queue()
    q.put(start_node)
    explored=[]
    killed=[]
    display_state = '(Initial state)' if isDetailed else ''
    tree.create_node(str(start_node.state)+ display_state ,str(start_node.state))
    while not(q.empty()):
        node=q.get()
        explored.append(node.state)
        if node.parent:
            diff=np.subtract(node.parent.state,node.state)
            if node.parent.state[2]==0:
                diff[0],diff[1]=-diff[0],-diff[1]
        children=node.generate_child()
        if not node.is_killed():
            for child in children:
                if child.state not in explored:
                    if(child.state[0]<=3 and child.state[1] <= 3):
                        if(child.state[0] < child.state[1]):
                            display_state = '(Killed)' if isDetailed else ''
                        elif(child.state[0] == 0 and  child.state[1] == 0):
                            display_state = '(Final state)' if isDetailed else ''
                        else:
                            display_state = '(No more feasible states)' if isDetailed else ''
                        tree.create_node(str(child.state) + display_state,str(child.state),parent = str(node.state))
                    if child.goal_test():
                        diff = np.subtract(node.parent.state, node.state)
                        if node.parent.state[2] == 0:
                            diff[0], diff[1] = -diff[0], -diff[1]

                        tree.show()
                        return child.find_solution()
                    if child.is_valid():
                        q.put(child)
                        explored.append(child.state)
        else:
            killed.append("\""+str(node.state)+"\"")
    return

initial_state= [3,3,1]
final_state = [0,0,0]
print()
detailedGraph = input('Do you want a detailed Graph?(y/n)')
detailedGraphBool = True if (detailedGraph.upper() == 'Y' or detailedGraph.upper() == 'YES' or detailedGraph.upper() == 'YA' or detailedGraph.upper() == 'OK') else False
print()
print('::::The Following is the space state graph of the game called Missionaries and Cannibals::::  \n ')
print('Initial State:',initial_state)
print('Final State:',final_state,'\n')
Node.num_of_instances=0
solution=TreeGenerator(initial_state,detailedGraphBool)



