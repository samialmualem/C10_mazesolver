from graphics import * 
from maze import Maze

def main():
    win = Window(800, 600)
    
    # p1 = Point(100, 100)    
    # p2 = Point(200, 200)
    # line = Line(p1, p2)
    
    # print(f"Drawing line from ({p1.x}, {p1.y}) to ({p2.x}, {p2.y})")
    # win.draw_line(line, "red")  # Using red to make it more visible


    # # Create two cells
    # cell1 = Cell(10, 10, 100, 100, win)
    # cell2 = Cell(110, 10, 200, 100, win)
    
    # # Draw the cells
    # cell1.draw(win, "red")
    # cell2.draw(win, "blue")
    
    # # Test draw_move between the two cells
    # cell1.draw_move(cell2)


    num_cols = 5
    num_rows = 8
    m1 = Maze(10, 10, num_rows, num_cols, 30, 30, win)
    m1._animate()
    m1._break_entrance_and_exit()
    m1._break_walls_r(1, 3)
    m1._reset_cells_visited()
    m1.solve()

    win.mainloop()
    

if __name__ == "__main__":
    main() 