from graphics import * 


def main():
    win = Window(800, 600)
    
    # p1 = Point(100, 100)    
    # p2 = Point(200, 200)
    # line = Line(p1, p2)
    
    # print(f"Drawing line from ({p1.x}, {p1.y}) to ({p2.x}, {p2.y})")
    # win.draw_line(line, "red")  # Using red to make it more visible

    # Create two cells
    cell1 = Cell(10, 10, 100, 100, win)
    cell2 = Cell(110, 10, 200, 100, win)
    
    # Draw the cells
    cell1.draw(win, "red")
    cell2.draw(win, "blue")
    
    # Test draw_move between the two cells
    cell1.draw_move(cell2)

    win.mainloop()
    

if __name__ == "__main__":
    main()