# filename: snake_game.py

import random
import curses


def create_game_window(stdscr, sh, sw, w):
    # paint game border
    w.border(0)
    # Initial score
    score = 0
    # create snake and set initial direction
    snake_x = sw // 4
    snake_y = sh // 2
    snake = [[snake_y, snake_x], [snake_y, snake_x - 1], [snake_y, snake_x - 2]]
    # display snake
    for segment in snake:
        w.addch(segment[0], segment[1], curses.ACS_PI)
    # create food
    food = [sh // 2, sw // 2]
    w.addch(food[0], food[1], curses.ACS_DIAMOND)
    return [score, snake, food]


def update_game_window(w, snake, food, key, score, sh, sw):
    # determine next position of snake head
    new_head = [snake[0][0], snake[0][1]]
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    # insert new head of snake
    snake.insert(0, new_head)
    # Check if snake has run into border
    if (snake[0][0] in [0, sh]) or (snake[0][1] in [0, sw]) or (snake[0] in snake[1:]):
        return [True, score, food]
    # check if snake got food
    if snake[0] == food:
        score += 1
        food = None
        while food is None:
            nf = [random.randint(1, sh - 1), random.randint(1, sw - 1)]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_DIAMOND)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], " ")
    w.addch(snake[0][0], snake[0][1], curses.ACS_PI)
    return [False, score, food]


def game():
    stdscr = curses.initscr()
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.timeout(100)
    w.keypad(1)
    key = curses.KEY_RIGHT
    score, snake, food = create_game_window(stdscr, sh, sw, w)
    game_over = False
    while not game_over:
        next_key = w.getch()
        key = key if next_key == -1 else next_key
        game_over, score, food = update_game_window(w, snake, food, key, score, sh, sw)
        # add a delay for each round of game loop
        curses.napms(100)
    try:
        curses.endwin()
    except curses.error:
        # ignore errors on cleanup
        pass
    print(f"Game over! Your score is: {score}")


if __name__ == "__main__":
    game()
