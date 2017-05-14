#! /usr/bin/env python3

import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

class Maze:
    def __init__(self, mazefilename):
        rowInMaze = 0
        x_translate = 0
        y_translate = 0
        row_in_maze = 0
        col_in_maze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFile = open(mazefilename, 'r')
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.start_row = rowInMaze
                    self.start_col = col
                col = col + 1
            rowInMaze = rowInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

        self.row_in_maze = rowInMaze
        self.col_in_maze = columnsInMaze
        self.x_translate = -columnsInMaze / 2
        self.y_translate = rowInMaze / 2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-(columnsInMaze-1)/2-.5,\
                -(rowInMaze-1)/2-.5,\
                (columnsInMaze-1)/2+.5,\
                (rowInMaze-1)/2+.5)

        #setup(width=600, height=600)
        #setworldcoordinates(-(columnsInMaze - 1)/2-0.5,\
        #        -(rowsInMaze-1)/2-0.5,\
        #        (clumnsInMaze-1)/2+0.5,\
        #        (rowsInMaze-1)/2+0.5\
        #        )
        
    def draw_maze(self):
        for y in range(self.row_in_maze):
            for x in range(self.col_in_maze):
                if self.mazelist[y][x] == OBSTACLE:
                    self.draw_center_box(x+self.x_translate,\
                            -y+self.y_translate,'tan')
        self.t.color('black', 'blue')

    def draw_center_box(self, x, y, color):
        self.t.speed(10)
        self.wn.tracer(0)
        self.t.up()
        self.t.goto(x-.5,y-.5)
        self.t.color('black', color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
        self.wn.update()
        self.wn.tracer(1)
    
    def move_turtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x+self.x_translate, -y+self.y_translate))
        self.t.goto(x+self.x_translate, -y+self.y_translate)

    def drop_breadcrumb(self, color):
        self.t.dot(color)

    def update_position(self, row, col, val = None):
        if val:
            self.mazelist[row][col] = val
        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.drop_breadcrumb(color)

    def is_exit(self, row, col):
        return (row == 0 or
                row == self.row_in_maze - 1 or
                col == 0 or
                col == self.col_in_maze - 1)

    def __getitem__(self, idx):
        return self.mazelist[idx]



