from gym import spaces
import numpy as np
from copy import deepcopy


class ProteinEnv():

    def __init__(self):
        self.action_space = spaces.Discrete(4)    # 0:L, 1:U, 2:R, 3:D
        self.protein="HPHPPHHPHPPHPHHPPHPH"
        self.locs = [(0,0)]        #stores locations of each amino acid in the protein
        self.state = (self.protein, self.locs)   #we initialise by placing the first amino acid at origin
        
       
    
    def transition(self, x_t, a_t):    #x_t = state, a_t = action
        current_state = deepcopy(x_t)
        x_coord = current_state[1][-1][0]        #x-coordinate of the last amino acid
        y_coord = current_state[1][-1][1]        #y-coordinate of the last amino acid
        
        if a_t == 0:    #left
            new_coords = (x_coord-1, y_coord)
        elif a_t == 1:     #up
            new_coords = (x_coord, y_coord+1)
        elif a_t == 2:     #right
            new_coords = (x_coord+1 , y_coord)        
        elif a_t == 3:     #down
            new_coords = (x_coord, y_coord-1)
        
        locs = current_state[1]
        locs.append(new_coords)
        new_state = (current_state[0], locs)
        return new_state

    def calculate_E(self, x_t_1):
        next_state = deepcopy(x_t_1)
        h_coords =[]

        for ix in range(len(next_state[0])):
            if next_state[0][ix] == 'H':
                h_coords.append((ix, next_state[1][ix]))
        
        E = 0
        #print('h_coords ', h_coords)
        for ix in h_coords:
            for iy in h_coords:
                if (abs(ix[1][0] - iy[1][0]) + abs(ix[1][1] - iy[1][1])) == 1 and abs(ix[0] - iy[0]) != 1:
                    E -= 0.5    #because it counts a pair twice
        print(' energy ',E)
       
        return E
    
    
    def invalid_action(self, x_t_1): 
        next_state = deepcopy(x_t_1)
        #print('state ',next_state) 
        invalid = False
        #OVERLAP
        for ix in range(len(next_state[1])-1):
            #print('i ', ix)
            #for fx in range(len(next_state[1])):

            #print('next_state[1][-1] ', next_state[1][-1])
            #print('ix ', ix, ' next_state[1][ix] ', next_state[1][ix])
            #if (fx !=ix and next_state[1][fx] == next_state[1][ix]):
            if (next_state[1][-1] == next_state[1][ix]):

                invalid = True   
       
        return invalid
    
    
    def reward(self, x_t_1):     #x_t_1 = next_state, a_t = action        
        next_state = deepcopy(x_t_1)
        r=0
        is_invalid = self.invalid_action(next_state)
        if is_invalid == True:                              #action is invalid
            r = 0.01
        elif is_invalid == False: 
            if len(next_state[0]) == len(next_state[1]):              #reached terminal state
                r = -self.calculate_E(next_state)
                print('energy as reward valid ',r)
            else:
                r = 0.1        
        return r, is_invalid


    def step(self, x_t, a_t):   
        assert self.action_space.contains(a_t)  
        
        current_state = deepcopy(x_t)                               
        action = deepcopy(a_t)

        next_state = self.transition(current_state, action)       #next_state

        reward1, valid = self.reward(next_state)

        return next_state, reward1, valid

