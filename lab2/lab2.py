# Fall 2012 6.034 Lab 2: Search
#
# Your answers for the true and false questions will be in the following form.  
# Your answers will look like one of the two below:
#ANSWER1 = True
#ANSWER1 = False

# 1: True or false - Hill Climbing search is guaranteed to find a solution
#    if there is a solution
ANSWER1 = False

# 2: True or false - Best-first search will give an optimal search result
#    (shortest path length).
#    (If you don't know what we mean by best-first search, refer to
#     http://courses.csail.mit.edu/6.034f/ai3/ch4.pdf (page 13 of the pdf).)
ANSWER2 = False

# 3: True or false - Best-first search and hill climbing make use of
#    heuristic values of nodes.
ANSWER3 = True

# 4: True or false - A* uses an extended-nodes set.
ANSWER4 = True

# 5: True or false - Breadth first search is guaranteed to return a path
#    with the shortest number of nodes.
ANSWER5 = True

# 6: True or false - The regular branch and bound uses heuristic values
#    to speed up the search for an optimal path.
ANSWER6 = False

# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph
import math

def quickSort(graph,goal,alist,sortType=0):
   quickSortHelper(graph,goal,alist,0,len(alist)-1,sortType)

def quickSortHelper(graph,goal,alist,first,last,sortType):
   if first<last:

       splitpoint = partition(graph,goal,alist,first,last)

       quickSortHelper(graph,goal,alist,first,splitpoint-1,sortType)
       quickSortHelper(graph,goal,alist,splitpoint+1,last,sortType)

def partition(graph,goal,alist,first,last):
   pivotvalue = graph.get_heuristic(alist[first][-1],goal) #- len(alist[first])

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and \
               graph.get_heuristic(alist[leftmark][-1],goal)  <= pivotvalue:
           leftmark = leftmark + 1

       while graph.get_heuristic(alist[rightmark][-1],goal) >= pivotvalue and \
               rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark


def quickSort_bnb(graph,goal,alist,sortType=0):
   quickSortHelper_bnb(graph,goal,alist,0,len(alist)-1,sortType)

def quickSortHelper_bnb(graph,goal,alist,first,last,sortType):
   if first<last:

       splitpoint = partition_bnb(graph,goal,alist,first,last)

       quickSortHelper_bnb(graph,goal,alist,first,splitpoint-1,sortType)
       quickSortHelper_bnb(graph,goal,alist,splitpoint+1,last,sortType)

def partition_bnb(graph,goal,alist,first,last):
   pivotvalue = graph.get_heuristic(alist[first][-1],goal) + path_length(graph,alist[first])

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and \
               graph.get_heuristic(alist[leftmark][-1],goal) + path_length(graph,alist[leftmark]) <= pivotvalue:
           leftmark = leftmark + 1

       while graph.get_heuristic(alist[rightmark][-1],goal) + path_length(graph,alist[rightmark]) >= pivotvalue and \
               rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark



## Optional Warm-up: BFS and DFS
# If you implement these, the offline tester will test them.
# If you don't, it won't.
# The online tester will not test them.

# def bfs(graph, start, goal):
#     pathList = [(start,)];
#     reachedGoal = False
#     if start == goal:
#         return [start]
#     while len(pathList) > 0:
#         #print pathList
#         pathToExtend = pathList[0]
#         pathList.remove(pathList[0])
#         nodeToExtend = pathToExtend[-1]
#         newNodes = graph.get_connected_nodes(nodeToExtend)
#         if goal in newNodes:
#             reachedGoal = True
#             goalPath = pathToExtend + (goal,)
#         if len(pathToExtend) > 1:
#             newNodes = [ node for node in newNodes if node not in pathToExtend ]
#         newPaths = [ pathToExtend + (node,) for node in newNodes ]
#         pathList.extend(newPaths)
#         if reachedGoal: break
#     if reachedGoal:
#         #print "goal path : " + str(goalPath)
#         return goalPath
#     else: return []

def bfs(graph, start, goal):
    pathList = [(start,)]
    if start == goal:
      return [start]
    while len(pathList) > 0:
        #print pathList
        #print [ graph.get_heuristic(path[-1],goal) for path in pathList ]
        newPaths = []
        while len(pathList) > 0:
            pathToExtend = pathList[0]
            pathList.remove(pathList[0])
            nodeToExtend = pathToExtend[-1]
            newNodes = graph.get_connected_nodes(nodeToExtend)
            if len(pathToExtend) > 1:
                newNodes = [ node for node in newNodes if node not in pathToExtend]
            if goal in newNodes:
                goalPath = pathToExtend + (goal,)
                #print "goalPath", goalPath
                return list(goalPath)
            newPaths += [ pathToExtend + (node,) for node in newNodes ]
        pathList.extend(newPaths)
        
        # #print "newPathsList" + str(newPaths)
        # quickSort(graph,goal,newPaths,1)
        # #print "newPathsList sorted by len" + str(newPaths)
    return []


## Once you have completed the breadth-first search,
## this part should be very simple to complete.
def dfs(graph, start, goal):
    pathList = [(start,)];
    reachedGoal = False
    if start == goal:
        return [start]
    while len(pathList) > 0:
        #print pathList
        pathToExtend = pathList[0]
        pathList.remove(pathList[0])
        nodeToExtend = pathToExtend[-1]
        newNodes = graph.get_connected_nodes(nodeToExtend)
        if len(pathToExtend) > 1:
            newNodes = [ node for node in newNodes if node not in pathToExtend ]
        if goal in newNodes:
            reachedGoal = True
            goalPath = pathToExtend + (goal,)
        newPaths = [ pathToExtend + (node,) for node in newNodes ]
        newPaths.extend(pathList)
        pathList = newPaths
        if reachedGoal: break
    if reachedGoal:
        #print "goal path : " + str(goalPath)
        return goalPath
    else: return []


## Now we're going to add some heuristics into the search.  
## Remember that hill-climbing is a modified version of depth-first search.
## Search direction should be towards lower heuristic values to the goal.
def hill_climbing(graph, start, goal):
    pathList = [(start,)];
    reachedGoal = False
    if start == goal:
        return [start]
    while len(pathList) > 0:
        #print pathList
        #print [ graph.get_heuristic(path[-1],goal) for path in pathList ]
        pathToExtend = pathList[0]
        pathList.remove(pathList[0])
        nodeToExtend = pathToExtend[-1]
        newNodes = graph.get_connected_nodes(nodeToExtend)
        if len(pathToExtend) > 1:
            newNodes = [ node for node in newNodes if node not in pathToExtend]
        if goal in newNodes:
            reachedGoal = True
            goalPath = pathToExtend + (goal,)
        newPaths = [ pathToExtend + (node,) for node in newNodes ]
        ##print "newPaths" + str(newPaths)
        quickSort(graph,goal,newPaths)
        ##print "sortedPaths" + str(newPaths)
        newPaths.extend(pathList)
        pathList = newPaths
        if reachedGoal: break
    if reachedGoal:
        #print "goal path : " + str(goalPath)
        return list(goalPath)
    else: return []

## Now we're going to implement beam search, a variation on BFS
## that caps the amount of memory used to store paths.  Remember,
## we maintain only k candidate paths of length n in our agenda at any time.
## The k top candidates are to be determined using the 
## graph get_heuristic function, with lower values being better values.
def beam_search(graph, start, goal, beam_width):
    #print "beam_width %d", beam_width
    pathList = [(start,)]
    reachedGoal = False
    if start == goal:
      return [start]
    while len(pathList) > 0:
        pathList = pathList[:beam_width]
        #print pathList
        #print [ graph.get_heuristic(path[-1],goal) for path in pathList ]
        newPaths = []
        while len(pathList) > 0:
            pathToExtend = pathList[0]
            pathList.remove(pathList[0])
            nodeToExtend = pathToExtend[-1]
            newNodes = graph.get_connected_nodes(nodeToExtend)
            if len(pathToExtend) > 1:
                newNodes = [ node for node in newNodes if node not in pathToExtend]
            if goal in newNodes:
                goalPath = pathToExtend + (goal,)
                #print "goalPath", goalPath
                return list(goalPath)
            newPaths += [ pathToExtend + (node,) for node in newNodes ]
        pathList.extend(newPaths)
        quickSort(graph,goal,pathList)
        #print "sortedPathsList" + str(pathList)
        #print [graph.get_heuristic(path[-1],goal) for path in pathList]
        
        # #print "newPathsList" + str(newPaths)
        # quickSort(graph,goal,newPaths,1)
        # #print "newPathsList sorted by len" + str(newPaths)
    return []


## Now we're going to try optimal search.  The previous searches haven't
## used edge distances in the calculation.

## This function takes in a graph and a list of node names, and returns
## the sum of edge lengths along the path -- the total distance in the path.
def path_length(graph, node_names):
   i=0
   length=False
   while i < len(node_names) - 1:
      if graph.are_connected(node_names[i],node_names[i+1]):
            length+= graph.get_edge(node_names[i],node_names[i+1]).length
      i+=1
   return length


def branch_and_bound(graph, start, goal):
    pathList = [(start,)];
    goalPath = False
    if start == goal:
        return [start]
    while len(pathList) > 0:
        #print pathList
        #print [ graph.get_heuristic(path[-1],goal) + path_length(graph,path) for path in pathList ]
        pathToExtend = pathList[0]
        pathList.remove(pathList[0])
        nodeToExtend = pathToExtend[-1]
        newNodes = graph.get_connected_nodes(nodeToExtend)
        if len(pathToExtend) > 1:
            newNodes = [ node for node in newNodes if node not in pathToExtend]
        if goal in newNodes and goalPath:
         newGoalPath = pathToExtend + (goal,)
         if path_length(graph,newGoalPath) <= path_length(graph,goalPath):
            goalPath = newGoalPath
            #print 'newgoalpath : ', newGoalPath
        elif goal in newNodes and not goalPath: 
         goalPath = pathToExtend + (goal,)
         #print 'goalpath : ', goalPath
        newPaths = [ pathToExtend + (node,) for node in newNodes ]
        newPaths.extend(pathList)
        pathList = newPaths
        quickSort_bnb(graph,goal,pathList)
        #print "sortedPaths" + str(pathList)
    if goalPath:
        #print "final goal path : " + str(goalPath)
        return list(goalPath)
    else: return []

def a_star(graph, start, goal):
    pathList = [(start,)];
    goalPath = False
    if start == goal:
        return [start]
    while len(pathList) > 0 and not goalPath:
        #print pathList
        #print [ graph.get_heuristic(path[-1],goal) + path_length(graph,path) for path in pathList ]
        pathToExtend = pathList[0]
        pathList.remove(pathList[0])
        nodeToExtend = pathToExtend[-1]
        newNodes = graph.get_connected_nodes(nodeToExtend)

        if len(pathToExtend) > 1:
            newNodes = [ node for node in newNodes if node not in pathToExtend]

        if goal in newNodes:
            goalPath = pathToExtend + (goal,)

        newPaths = [ pathToExtend + (node,) for node in newNodes ]
        newPaths.extend(pathList)
        pathList = newPaths

        for path in pathList:
            #print 'checking if ',path[-1], "is in", newNodes
            if path[-1] in newNodes:
                    if path_length(graph,pathToExtend + (path[-1],)) < path_length(graph, path):
                        #print 'removing path terminating at same node: ',path
                        pathList.remove(path)        

        quickSort_bnb(graph,goal,pathList)
        #print "sortedPaths" + str(pathList)
    if goalPath:
        #print "final goal path : " + str(goalPath)
        return list(goalPath)
    else: return []


## It's useful to determine if a graph has a consistent and admissible
## heuristic.  You've seen graphs with heuristics that are
## admissible, but not consistent.  Have you seen any graphs that are
## consistent, but not admissible?

def is_admissible(graph, goal):
    admissible = True
    # print 'goal is',goal
    for node in graph.nodes:
    	# print "checking ", node, " for admissibility"
    	pathToGoal = a_star(graph,node,goal)
    	if len(pathToGoal) > 0:
    	    distanceToGoal = path_length(graph,pathToGoal)
            if graph.get_heuristic(node,goal) > distanceToGoal:
    	        # print "is not admissible"
                admissible = False
    return admissible

def is_consistent(graph, goal):
    consistent = True
    for edge in graph.edges:
        if abs(graph.get_heuristic(edge.node2,goal) - graph.get_heuristic(edge.node1,goal)) > edge.length:
            consistent = False
    return consistent

HOW_MANY_HOURS_THIS_PSET_TOOK = '6'
WHAT_I_FOUND_INTERESTING = 'a star'
WHAT_I_FOUND_BORING = 'nothing'
