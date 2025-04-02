from tkinter import Tk, BOTH, Canvas

class Cell:
    def __init__(self, 
                 x1, y1, 
                 x2, y2, 
                 win=None, 
                 has_left_wall=True, 
                 has_right_wall=True, 
                 has_top_wall=True, 
                 has_bottom_wall=True
                 ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.visited = False

    def draw(self, window, fill_color='white', no_fill_color='black'):
        
        if self.has_bottom_wall:
            bottom_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            window.draw_line(bottom_line, fill_color)
        else:
            bottom_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            window.draw_line(bottom_line, no_fill_color)

        if self.has_top_wall:
            top_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            window.draw_line(top_line, fill_color)
        else:
            top_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            window.draw_line(top_line, no_fill_color)


        if self.has_left_wall:  
            left_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            window.draw_line(left_line, fill_color)
        else:
            left_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            window.draw_line(left_line, no_fill_color)
        if self.has_right_wall:
            right_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            window.draw_line(right_line, fill_color)
        else:
            right_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            window.draw_line(right_line, no_fill_color)
    
    def draw_move(self, to_cell, undo=False):
        fill_color = 'gray' if undo else 'red'
        start_x = (self._x1 + self._x2) // 2
        start_y = (self._y1 + self._y2) // 2
        end_x = (to_cell._x1 + to_cell._x2) // 2
        end_y = (to_cell._y1 + to_cell._y2) // 2

        line = Line(Point(start_x, start_y), Point(end_x, end_y))
        self._win.draw_line(line, fill_color)
 

class Window(Tk):
    def __init__(self, width, height):
        super().__init__() 
        self.title('Maze Solver')
        self.geometry(f'{width}x{height}')
        self.__canvas = Canvas(self)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__running = False 
        self.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__canvas.update() 
        self.update_idletasks()
        self.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            try:
                self.redraw()
            except:
                # If there's an error (like the window being destroyed), 
                # exit the loop
                self.__running = False
                break

    def close(self):
        self.__running = False
        self.destroy()
    
    def draw_line(self, line, fill_color='black'):
        line.draw(self.__canvas, fill_color)
        

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color='black'):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
