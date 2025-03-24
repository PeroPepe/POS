import curses

# User credentials
USER_ID = "1"
PASSWORD = "2014"

# Product list
PRODUCTS = {
    "1": "Pringles Sour Cream",
    "2": "LAYS MEGA PACK XL"
}

def login_screen(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    stdscr.refresh()
    
    # Dark theme colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    stdscr.attron(curses.color_pair(1))
    
    h, w = stdscr.getmaxyx()
    
    stdscr.addstr(h//2 - 3, w//2 - 10, "POS LOGIN", curses.A_BOLD)
    stdscr.addstr(h//2 - 1, w//2 - 15, "User ID: ")
    stdscr.addstr(h//2 + 1, w//2 - 15, "Password: ")
    stdscr.refresh()
    
    user_id = ""
    password = ""
    keypress = 0
    
    while True:
        keypress = stdscr.getch()
        
        if keypress in range(48, 58):  # Numeric keys 0-9
            if len(user_id) < 4:
                user_id += chr(keypress)
                stdscr.addstr(h//2 - 1, w//2 - 5, user_id)
        
        elif keypress == 10:  # Enter key
            if user_id == USER_ID:
                stdscr.addstr(h//2 + 1, w//2 - 5, "*" * len(password))  # Hide password
                break
        
    while True:
        keypress = stdscr.getch()
        
        if keypress in range(48, 58):  # Numeric keys 0-9
            if len(password) < 4:
                password += chr(keypress)
                stdscr.addstr(h//2 + 1, w//2 - 5, "*" * len(password))
        
        elif keypress == 10:  # Enter key
            if password == PASSWORD:
                stdscr.clear()
                return True
            else:
                stdscr.addstr(h//2 + 3, w//2 - 10, "INVALID LOGIN!", curses.A_BOLD)
                stdscr.refresh()
                curses.napms(1000)
                return False

def pos_screen(stdscr):
    stdscr.clear()
    stdscr.refresh()
    
    h, w = stdscr.getmaxyx()
    stdscr.addstr(h//2 - 3, w//2 - 10, "POINT OF SALE", curses.A_BOLD)
    stdscr.addstr(h//2 - 1, w//2 - 20, "[1] Pringles Sour Cream")
    stdscr.addstr(h//2, w//2 - 20, "[2] LAYS MEGA PACK XL")
    stdscr.addstr(h//2 + 2, w//2 - 20, "Press 1 or 2 to add a product")
    
    selected_products = []
    
    while True:
        keypress = stdscr.getch()
        
        if keypress == ord('1'):
            selected_products.append("Pringles Sour Cream")
        elif keypress == ord('2'):
            selected_products.append("LAYS MEGA PACK XL")
        elif keypress == ord('q'):  # Quit
            break
        
        # Display added products
        stdscr.addstr(h//2 + 4, w//2 - 20, "Cart: " + ", ".join(selected_products)[:w-30])
        stdscr.refresh()

def main(stdscr):
    while True:
        if login_screen(stdscr):
            pos_screen(stdscr)
        else:
            break

curses.wrapper(main)
