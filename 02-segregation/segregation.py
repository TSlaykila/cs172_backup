import graphics as g
import random

def draw_grid(win, grid, grid_size):
    rows, col = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(col):
            x1, y1 = j * grid_size, i * grid_size
            x2, y2 = x1 + grid_size, y1 + grid_size
            square = g.Rectangle(g.Point(x1,y1),g.Point(x2,y2))
            square.setOutline("black")

            if grid[i][j] == 0:
                square.setFill("blue")
            elif grid[i][j] == 1:
                square.setFill("red")
            else:
                square.setFill("white")

            square.draw(win)


def agent_randomizer(grid):
    """ Randomizer of Agents, indexes being assign randomly and with ruqally chances 0 or 1 
    depending on the randomizer and left on blank by chance of 10%
    First lines are the turnables to dictate percentage of appeareance, 0 to 1"""

    empty_cell = 0.1
    total_agents = 0

    #modify the divisor, increasing it reduces agent_0 and augments agent_1
    agent_0 = (1 - empty_cell) / 2

    rows, col = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(col):
            randomizer = random.random()
            if randomizer < agent_0:
                grid[i][j] = 0
                total_agents += 1
            elif randomizer > agent_0 + empty_cell:
                grid[i][j] = 1
                total_agents += 1
    return total_agents

def translocation(grid, i, j, all_agents_satisfied):
    rows, cols = len(grid), len(grid[0])
    if satisfaction_calculator(grid, i, j) < 0.3:
        for k in range(random.randint(1, 20),rows):
            for l in range(random.randint(1, 20), cols):
                if grid[k][l] == "":
                    grid[k][l],grid[i][j] = grid[i][j],grid[k][l]

                    
                    if satisfaction_calculator(grid,k,l) >= 0.3:
                        return all_agents_satisfied
                    
                    #Revert move if not satisfied
                    grid[k][l],grid[i][j] = grid[i][j],grid[k][l]

        return all_agents_satisfied
    return all_agents_satisfied + 1


def satisfaction_calculator(grid, i, j):

    friendly_squares = 0 
    enemy_squares = 0
    rows, cols = len(grid), len(grid[0])

    if grid[i][j] != "":
        agent = grid[i][j]

        # Top squares check
        if i > 0 and j > 0:  # Top-left
            if grid[i-1][j-1] == agent:
                friendly_squares += 1
            elif grid[i-1][j-1] != "":
                enemy_squares += 1

        if i > 0:  # Top
            if grid[i-1][j] == agent:
                friendly_squares += 1
            elif grid[i-1][j] != "":
                enemy_squares += 1

        if i > 0 and j < cols - 1:  # Top-right
            if grid[i-1][j+1] == agent:
                friendly_squares += 1
            elif grid[i-1][j+1] != "":
                enemy_squares += 1

        # Middle squares check (Left & Right)
        if j > 0:  # Left
            if grid[i][j-1] == agent:
                friendly_squares += 1
            elif grid[i][j-1] != "":
                enemy_squares += 1

        if j < cols - 1:  # Right
            if grid[i][j+1] == agent:
                friendly_squares += 1
            elif grid[i][j+1] != "":
                enemy_squares += 1

        # Bottom squares check
        if i < rows - 1 and j > 0:  # Bottom-left
            if grid[i+1][j-1] == agent:
                friendly_squares += 1
            elif grid[i+1][j-1] != "":
                enemy_squares += 1

        if i < rows - 1:  # Bottom
            if grid[i+1][j] == agent:
                friendly_squares += 1
            elif grid[i+1][j] != "":
                enemy_squares += 1

        if i < rows - 1 and j < cols - 1:  # Bottom-right
            if grid[i+1][j+1] == agent:
                friendly_squares += 1
            elif grid[i+1][j+1] != "":
                enemy_squares += 1

        total_squares = friendly_squares + enemy_squares

    #Satisfaction Chance 0.0 to 1.0 values calculator
        if total_squares != 0:
            return friendly_squares/total_squares
    return 0
    


            


def main():
    grid_size = 20
    grid = [["" for _ in range(grid_size)] for _ in range(grid_size)]
    win_size = grid_size * grid_size

    win = g.GraphWin("20x20 Grid", win_size, win_size)
    total_agents = agent_randomizer(grid)
    draw_grid(win, grid, grid_size)
    all_agents_satisfied = 0
    rounds = 0
    while all_agents_satisfied < total_agents:
        all_agents_satisfied = 0
        rounds += 1
        for i in range(len(grid)):
            draw_grid(win, grid, grid_size) 
            for j in range(len(grid[0])):
                if grid[i][j] != "":
                    all_agents_satisfied = translocation(grid, i, j, all_agents_satisfied)

    rounds = rounds - 1
    print("number of rounds is: " + rounds)



    
    
    win.getMouse()
    win.close()

main()

