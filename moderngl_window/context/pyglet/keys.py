import pyglet
pyglet.options['shadow_window'] = False
pyglet.options['debug_gl'] = False

from pyglet.window import key

from moderngl_window.context.base import BaseKeys


class Keys(BaseKeys):
    """
    Namespace mapping pyglet specific key constants
    """
    ESCAPE = key.ESCAPE
    SPACE = key.SPACE
    ENTER = key.ENTER
    PAGE_UP = key.PAGEUP
    PAGE_DOWN = key.PAGEDOWN
    LEFT = key.LEFT
    RIGHT = key.RIGHT
    UP = key.UP
    DOWN = key.DOWN

    TAB = key.TAB
    COMMA = key.COMMA
    MINUS = key.MINUS
    PERIOD = key.PERIOD
    SLASH = key.SLASH
    SEMICOLON = key.SEMICOLON
    EQUAL = key.EQUAL
    LEFT_BRACKET = key.BRACELEFT
    RIGHT_BRACKET = key.BRACERIGHT
    BACKSLASH = key.BACKSLASH
    BACKSPACE = key.BACKSPACE
    INSERT = key.INSERT
    DELETE = key.DELETE
    HOME = key.HOME
    END = key.END
    CAPS_LOCK = key.CAPSLOCK

    F1 = key.F1
    F2 = key.F2
    F3 = key.F3
    F4 = key.F4
    F5 = key.F5
    F6 = key.F6
    F7 = key.F7
    F8 = key.F8
    F9 = key.F9
    F10 = key.F10
    F11 = key.F11
    F12 = key.F12

    NUMBER_0 = key.NUM_0
    NUMBER_1 = key.NUM_1
    NUMBER_2 = key.NUM_2
    NUMBER_3 = key.NUM_3
    NUMBER_4 = key.NUM_4
    NUMBER_5 = key.NUM_5
    NUMBER_6 = key.NUM_6
    NUMBER_7 = key.NUM_7
    NUMBER_8 = key.NUM_8
    NUMBER_9 = key.NUM_9

    A = key.A
    B = key.B
    C = key.C
    D = key.D
    E = key.E
    F = key.F
    G = key.G
    H = key.H
    I = key.I
    J = key.J
    K = key.K
    L = key.L
    M = key.M
    N = key.N
    O = key.O
    P = key.P
    Q = key.Q
    R = key.R
    S = key.S
    T = key.T
    U = key.U
    V = key.V
    W = key.W
    X = key.X
    Y = key.Y
    Z = key.Z
