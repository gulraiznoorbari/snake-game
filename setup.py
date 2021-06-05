# Converting our SNAKE_GAME.py script into a executable file:
import cx_Freeze

executables = [cx_Freeze.Executable("Snake_Game.py")]
cx_Freeze.setup(
    name = "Snake Game",
    options = {"build_exe":{"packages":["pygame"],"include_files":["apple.png","SnakeHead.png"]}},
    description = "Snake Game Tutorial",
    executables = executables
    )
