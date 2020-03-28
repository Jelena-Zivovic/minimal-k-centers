import math
import numpy as np
import random





class Graph:
    def __init__(self, adjacency_list: dict, weights: list, vertices: list):
        self.adjacency_list = adjacency_list
        self.weights = weights
        self.vertices = vertices
        self.cardV = len(vertices)
        self.cardE = len(weights)
        
    def __str__(self):
        return str(self.adjacency_list)


    def get_neighbours(self, n):
        return self.adjacency_list[n]





        
        
    

