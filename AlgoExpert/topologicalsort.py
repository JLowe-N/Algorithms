'''
Given an array of jobs identified by distinct integer values, and an an array of
dependencies, where each dependency is represented by a subarray where the 1st 
element is the prerequisite job for the 2nd element:  return a new array with a 
valid order to complete the jobs.  If no valid order exists, return an empty array.
'''

# Solution 1 - Depth First Traversal Of Grpah
# Complexity - Time O(j + d) | Space O(j + d)
# Where j is # of jobs and d is # of dependencies

def topologicalSort(jobs, deps):
    jobGraph = createJobGraph(jobs, deps)
    return getOrderedJobs(jobGraph)

def createJobGraph(jobs, deps):
    graph = JobGraph(jobs)
    for prereq, job in deps:
        graph.addPrereq(job, prereq)
    return graph

def getOrderedJobs(graph):
    orderedJobs = []
    nodes = graph.nodes
    while len(nodes):
        node = nodes.pop()
        containsCycle = depthFirstTraverse(node, orderedJobs)
        if containsCycle:
            return []
    return orderedJobs

def depthFirstTraverse(node, orderedJobs):
    if node.visited:
        return False
    if node.visiting:
        return True
    node.visiting = True
    for prereqNode in node.prereqs:
        containsCycle = depthFirstTraverse(prereqNode, orderedJobs)
        if containsCycle:
            return True
    node.visited = True
    node.visiting = False
    orderedJobs.append(node.job)
    return False


class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.addNode(job)

    def addPrereq(self, job, prereq):
        jobNode = self.getNode(job)
        prereqNode = self.getNode(prereq)
        jobNode.prereqs.append(prereqNode)

    def addNode(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]

class JobNode:
    def __init__(self, job):
        self.job = job
        self.prereqs = []
        self.visited = False
        self.visiting = False

########################################
# Solution #2 - Removing Edges as dependencies fulfilled
########################################
# Complexity:  O(j + d) Time O(j + d) Space
# Where j is # of jobs and d is # of dependencies
# def topologicalSort(jobs, deps):
#     jobGraph = createJobGraph(jobs, deps)
#     return getOrderedJobs(jobGraph)


# def createJobGraph(jobs, deps):
#     graph = JobGraph(jobs)
#     for job, dep in deps:
#         graph.addDep(job, dep)
#     return graph


# def getOrderedJobs(graph):
#     orderedJobs = []
#     nodesWithNoPrereqs = list(
#         filter(lambda node: node.numOfPrereqs == 0, graph.nodes))
#     while len(nodesWithNoPrereqs):
#         node = nodesWithNoPrereqs.pop()
#         orderedJobs.append(node.job)
#         removeDeps(node, nodesWithNoPrereqs)
#     graphHasEdges = any(node.numOfPrereqs for node in graph.nodes)
#     return [] if graphHasEdges else orderedJobs


# def removeDeps(node, nodesWithNoPrereqs):
#     while len(node.deps):
#         dep = node.deps.pop()
#         dep.numOfPrereqs -= 1
#         if dep.numOfPrereqs == 0:
#             nodesWithNoPrereqs.append(dep)


# class JobGraph:
#     def __init__(self, jobs):
#         self.nodes = []
#         self.graph = {}
#         for job in jobs:
#             self.addNode(job)

#     def addDep(self, job, dep):
#         jobNode = self.getNode(job)
#         depNode = self.getNode(dep)
#         jobNode.deps.append(depNode)
#         depNode.numOfPrereqs += 1

#     def addNode(self, job):
#         self.graph[job] = JobNode(job)
#         self.nodes.append(self.graph[job])

#     def getNode(self, job):
#         if job not in self.graph:
#             self.addNode(job)
#         return self.graph[job]


# class JobNode:
#     def __init__(self, job):
#         self.job = job
#         self.deps = []
#         self.numOfPrereqs = 0