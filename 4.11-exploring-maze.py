#! /usr/bin/env python3
from Maze import Maze

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

def search_from(maze, startrow, startcoloumn):
    maze.update_position(startrow, startcoloumn)
    #Check for base cases:
    #1.We have run into an obstacle, return false
    if maze[startrow][startcoloumn] == OBSTACLE:
        return False
    #2. We have found a square that has already been explored
    if maze[startrow][startcoloumn] == TRIED:
        return False
    #3. Success, an outside edge not occupied by an obstacle
    if maze.is_exit(startrow, startcoloumn):
        maze.update_position(startrow, startcoloumn, PART_OF_PATH)
        return True
    maze.update_position(startrow, startcoloumn, TRIED)
    
    #Otherwise, use Logical short circuiting to try each
    #direction in turn (if needed)
    found = search_from(maze, startrow-1, startcoloumn) or \
            search_from(maze, startrow+1, startcoloumn) or \
            search_from(maze, startrow, startcoloumn-1) or \
            search_from(maze, startrow, startcoloumn+1)
    if found:
        maze.update_position(startrow, startcoloumn, PART_OF_PATH)
    else:
        maze.update_position(startrow, startcoloumn, DEAD_END)

    return found


my_maze = Maze('maze2.txt')
my_maze.draw_maze()
my_maze.update_position(my_maze.start_row, my_maze.start_col)

search_from(my_maze, my_maze.start_row, my_maze.start_col)
