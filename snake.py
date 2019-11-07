import random
import curses

# store = {
#     'products': [
#         {'product_name': 'Luck', 'price': 20, 'enabled': False, 'description': 'Give you a higher chance to guess the right number'}
#
#     ]
# }
#
# leader_board = {
#      'players': [
#         { 'name': 'Anthony', 'points': 12, 'guesses_taken': 9 },
#         { 'name': 'Bob', 'points': 5, 'guesses_taken': 45 },
#         { 'name': 'Macy', 'points': 9, 'guesses_taken': 19 },
#         { 'name': 'Joe', 'points': 1, 'guesses_taken': 3 }
#      ]
# }
#
# point_system = {
#     'gained_points': 0,
#     'lossed_points': 0
# }
#
# settings = {
#     'rounds': 10,
#     'available_numbers': {'min': 0, 'max': 10},
#     'players': 1,
#     'difficulty': ('Easy', 'Medium', 'Hard')
# }

menu = ['Play', 'Store', 'Scoreboard', 'Exit']


def print_menu(stdscr, selected_row_index):
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    for index, row in enumerate(menu):
        x = width // 2 - len(row) // 2
        y = height // 2 - len(menu) // 2 + index

        if index == selected_row_index:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row_index = 0

    print_menu(stdscr, current_row_index)

    while True:
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and current_row_index > 0:
            current_row_index -= 1
        elif key == curses.KEY_DOWN and current_row_index < len(menu) - 1:
            current_row_index += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.addstr(0,0, 'You pressed {}'.format(menu[current_row_index]))
            stdscr.refresh()
            stdscr.getch()

            if current_row_index == len(menu) - 1: # when Exit is pressed, the user breaks out of the game completely
                break

        print_menu(stdscr, current_row_index)
        stdscr.refresh()


curses.wrapper(main)
