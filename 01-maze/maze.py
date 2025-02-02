import graphics as g
def draw_maze(maze):
    size = len(maze)
    win = g.GraphWin("Maze", 800, 800)
    win.setCoords(-0.5, -0.5, size + 0.5, size + 0.5)
    for row in range(size):
        for col in range(size):
            if maze[row][col] == "#":
                r = size - row - 1  # Adjust for coordinate system
                rect = g.Rectangle(g.Point(col, r), g.Point(col + 1, r + 1))
                rect.setFill("black")
                rect.draw(win)    
    win.getMouse()  
    win.close()
def read_maze_from_file(filename):
    with open(filename) as file:
        maze = [line.strip() for line in file.readlines()]
    return maze
filename = "maze10x10.txt"  
ascii_maze = read_maze_from_file(filename)
draw_maze(ascii_maze)
