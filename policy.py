def policy(protein):
    curr_state = (protein, [(0, 0)])
    
    while len(curr_state[1])<len(curr_state[0]):    
        best_action = max(Q_dict[curr_state[0], tuple(curr_state[1])],key=Q_dict[curr_state[0], tuple(curr_state[1])].get)
        next_state = env.transition(curr_state, best_action)
        print('Q_dict currecnt action', Q_dict[curr_state[0], tuple(curr_state[1])])
        print('Q_dict best', Q_dict[curr_state[0], tuple(curr_state[1])][best_action])

        print('next state ',next_state)
        print('best action ',best_action)


        curr_state = next_state
        #print('Q_dict after', Q_dict[curr_state[0], tuple(curr_state[1])][curr_action])

    
    x_h_coords = []
    y_h_coords = []
    x_p_coords = []
    y_p_coords = []
    
    x_inter_coords = []
    y_inter_coords = []
    

    for ix in range(len(next_state[0])):
        x_inter_coords.append(next_state[1][ix][0])
        y_inter_coords.append(next_state[1][ix][1])
        if next_state[0][ix] == 'H':
            x_h_coords.append(next_state[1][ix][0])
            y_h_coords.append(next_state[1][ix][1])
        if next_state[0][ix] == 'P':
            x_p_coords.append(next_state[1][ix][0])
            y_p_coords.append(next_state[1][ix][1])
        
        
        
    
    plt.scatter(x_h_coords, y_h_coords, s=300,marker = 'o', color = 'black')
    plt.scatter(x_p_coords, y_p_coords,s=300, marker = 'o', facecolors='none', edgecolors='black')
    plt.plot(x_inter_coords, y_inter_coords, color='green', linestyle='dashed')
    plt.show()
  
    
    print(x_h_coords)
    print(y_h_coords)
    print(x_p_coords)
    print(y_p_coords)
    print(x_inter_coords)
    print(y_inter_coords)