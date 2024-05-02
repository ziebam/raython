import platform

from ctypes import *
from enum import Enum

raylib = CDLL("./raylib.dll" if platform.system() == "Windows" else "./raylib.so")


class Color(Structure):
    _fields_ = [
        ("r", c_char),
        ("g", c_char),
        ("b", c_char),
        ("a", c_char),
    ]


DARKGRAY = Color(80, 80, 80, 255)
MAROON = Color(190, 33, 55, 255)
RAYWHITE = Color(245, 245, 245, 255)


class Key(Enum):
    KEY_RIGHT = 262
    KEY_LEFT = 263
    KEY_DOWN = 264
    KEY_UP = 265


class Vector2(Structure):
    _fields_ = [("x", c_float), ("y", c_float)]


InitWindow = raylib.InitWindow
InitWindow.argtypes = [c_int, c_int, c_char_p]

SetTargetFPS = raylib.SetTargetFPS
SetTargetFPS.argtypes = [c_int]

WindowShouldClose = raylib.WindowShouldClose
WindowShouldClose.restype = c_bool

IsKeyDown = raylib.IsKeyDown
IsKeyDown.argtypes = [c_int]
IsKeyDown.restype = c_bool

BeginDrawing = raylib.BeginDrawing

ClearBackground = raylib.ClearBackground
ClearBackground.argtypes = [Color]

DrawCircleV = raylib.DrawCircleV
DrawCircleV.argtypes = [Vector2, c_float, Color]


DrawText = raylib.DrawText
DrawText.argtypes = [c_char_p, c_int, c_int, c_int, Color]

EndDrawing = raylib.EndDrawing

CloseWindow = raylib.CloseWindow
