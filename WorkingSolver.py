#====================================================================
# Authors:  Lidia
# Date: Dec 3rd, 2023
# Title: Recursive Maze Solver
# Program Purpose: 
#  - To find the correct path between start and end nodes in a maze. 
#====================================================================

class MazeSolver:
    def __init__(self, maze_file):
        # 2D array that represents the maze
        self.maze = []
        # Loads maze from file
        self.load_maze(maze_file)
        # Mario's starting position
        self.current_position = self.M_starting_position
        # Peach's starting position
        self.P_position = None
        # Flag that states if Peach has been rescued
        self.rescued = False

    def load_maze(self, maze_file):
        with open(maze_file) as f:
            self.width = int(next(f).strip())
            self.height = int(next(f).strip())
            row = 1
            for line in f:
                line = line.strip()
                maze_row = []
                col = 0
                for char in line:
                    if char == 'M':
                        # stores starting position of Mario
                        self.M_starting_position = (row, col)
                    if char == 'P':
                        # stores starting position of Peach
                        self.P_position = (row,col)
                    if char in ['-', '|']:
                        char = '+'
                    # adds character to maze
                    maze_row.append(char)
                    col += 1
                self.maze.append(maze_row)
                row += 1
    
    def searchForPath(self):
        # Base case
        if self.rescued:
            return

        # Recursive cases
        self.goNorth()
        if self.rescued:
            return

        self.goEast()
        if self.rescued:
            return

        self.goSouth()
        if self.rescued:
            return

        self.goWest()

        # Mark marios starting position
        self.maze[self.M_starting_position[0]][self.M_starting_position[1]] = 'M'

    def goNorth(self):
        x, y = self.current_position
        if x <= 0 or self.maze[x-1][y] in ['+', '*', '?']:
            return  # Boundary check or already visited

        if self.maze[x-1][y] == 'P':
            self.rescued = True
            return

        # Mark as maybe and move
        self.current_position = (x-1, y)
        self.maze[x-1][y] = '?'
        
        # Recursive calls
        self.searchForPath()

        if not self.rescued:
            # Backtrack if Princess not found
            self.current_position = (x, y)
            self.maze[x-1][y] = '*'  # Mark as 'no'
            
        
    def goEast(self):
        # Check if at boundary or already visited
        x, y = self.current_position
        if y >= self.width - 1 or self.maze[x][y+1] in ['+', '*', '?']:
            return

        if self.maze[x][y+1] == 'P':
            self.rescued = True
            return

        # Mark as maybe and move
        self.current_position = (x, y+1)
        self.maze[x][y+1] = '?'
        
        # Recursive calls
        self.searchForPath()

        # Backtrack if Princess not found
        if not self.rescued:
            self.current_position = (x, y)
            self.maze[x][y+1] = '*'

    def goSouth(self):
        # Check if at boundary or already visited
        x, y = self.current_position
        if x >= self.height - 1 or self.maze[x+1][y] in ['+', '*', '?']:
            return

        # Check if Princess is found
        if self.maze[x+1][y] == 'P':
            self.rescued = True
            return

        # Mark as maybe and move
        self.current_position = (x+1, y)
        self.maze[x+1][y] = '?'
        
        self.searchForPath()

        # Backtrack if Princess not found
        if not self.rescued:
            self.current_position = (x, y)
            self.maze[x+1][y] = '*'

    def goWest(self):
        # Check if at boundary or already visited
        x, y = self.current_position
        if y <= 0 or self.maze[x][y-1] in ['+', '*', '?']:
            return

        # Check if Princess is found
        if self.maze[x][y-1] == 'P':
            self.rescued = True
            return

        # Mark as maybe and move
        self.current_position = (x, y-1)
        self.maze[x][y-1] = '?'
        
        self.searchForPath()

        # Backtrack if Princess not found
        if not self.rescued:
            self.current_position = (x, y)
            self.maze[x][y-1] = '*'
        
    def display_maze(self):
        # Prints the maze
        for row in self.maze:
            print(''.join(row))



solver = MazeSolver("mazeSmall.txt")

solver.searchForPath()

solver.display_maze()

