from raylib import *


def main():
    screenWidth = 800
    screenHeight = 800

    InitWindow(screenWidth, screenHeight, b"raython [core] example - keyboard input")

    ballPosition = Vector2(screenWidth / 2, screenHeight / 2)

    SetTargetFPS(60)

    while not WindowShouldClose():
        if IsKeyDown(Key.KEY_RIGHT.value):
            ballPosition.x += 2.0
        if IsKeyDown(Key.KEY_LEFT.value):
            ballPosition.x -= 2.0
        if IsKeyDown(Key.KEY_UP.value):
            ballPosition.y -= 2.0
        if IsKeyDown(Key.KEY_DOWN.value):
            ballPosition.y += 2.0

        BeginDrawing()

        ClearBackground(RAYWHITE)

        DrawText(b"move the ball with arrow keys", 10, 10, 20, DARKGRAY)

        DrawCircleV(ballPosition, 50, MAROON)

        EndDrawing()

    CloseWindow()


if __name__ == "__main__":
    main()
