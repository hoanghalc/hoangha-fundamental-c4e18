map_sokoban = {
    "size_x": 5,
    "size_y": 5,
}
player = {
    "x": 4,
    "y": 0 
}   

boxes = [
    {"x": 1,"y": 1},
    {"x": 2, "y": 2},
    {"x": 3, "y": 3}   
]

destination = [
    {"x": 2,"y": 1},
    {"x": 3, "y": 2},
    {"x": 4, "y": 3}   
]

playing = True    
while playing:
    for y in range(map_sokoban["size_y"]):
        for x in range(map_sokoban["size_x"]):
            
            box_is_here = False                         #Thêm biến để lưu trạng thái
            for box in boxes:
                if  x == box["x"] and y == box["y"]:
                    box_is_here = True
            
            player_is_here = False
            if y == player["y"] and x == player["x"]:
                player_is_here = True

            destination_is_here = False
            for des in destination:
                if x == des["x"] and y == des["y"]:
                    destination_is_here = True    

            if player_is_here:
                print("P ", end="")
            elif box_is_here:
                print("B ", end="")
            elif destination_is_here:
                print("D ", end="") 
            else:
                print("- ", end="")      
            
        print()


    ### End of print map

    #Check
    win = True
    for box in boxes:
        if box not in destination:
            win = False

    if win == True:
        print("win")
        break


    #Moving
    move = input("your move: ").upper()

    dx = 0
    dy = 0

    if move == "W":
        dy = -1
    elif move == "S":
        dy = 1
    elif move == "A":
        dx = -1
    elif move == "D":
       dx = 1
    else:
        playing = False

    #Move Player
    if 0 <= player["x"] + dx < map_sokoban['size_x'] \
        and 0 <= player["y"] + dy < map_sokoban['size_y']:
            player['x'] += dx
            player['y'] += dy
    
    #Move box
    for box in boxes:
        if box['x'] == player['x'] and box['y'] == player['y']:
            box['x'] += dx
            box['y'] += dy 



