#
# wymuszenie skorzystania z dekodera polskich znaków
# coding=utf-8


#
# import biblioteki PyGame
#
import pygame


#
# ZMIENNE GLOBALNE
#


#
# Inicjalne ustawienie szerokości ekranu, wysokość zostaje wyliczona automatycznie przez funkcję calculateScaleFactor().
# Funkcja ta oblicza i przypisuje także wartość ScaleFactor i przypisuje ją do zmiennej giScaleFactor.
# Szerokość maksymalna 1280;
#
giScreenWidth = 700;


#
# Definicja jednowymiarowej tablicy "gaWalkLeft" zawierającej pliki graficzne w formacie PNG animacji głównej postaci - ruch w prawo
#
gaWalkRight = [
                    pygame.image.load('character-02/character-right-01.png'),
                    pygame.image.load('character-02/character-right-02.png'),
                    pygame.image.load('character-02/character-right-03.png'),
                    pygame.image.load('character-02/character-right-04.png'),
                    pygame.image.load('character-02/character-right-05.png'),
                    pygame.image.load('character-02/character-right-06.png'),
                    pygame.image.load('character-02/character-right-07.png'),
                    pygame.image.load('character-02/character-right-08.png')
              ]


#
# Definicja jednowymiarowej tablicy "gaWalkLeft" zawierającej pliki graficzne w formacie PNG animacji głównej postaci - ruch w lewo
#
gaWalkLeft = [
                    pygame.image.load('character-02/character-left-01.png'),
                    pygame.image.load('character-02/character-left-02.png'),
                    pygame.image.load('character-02/character-left-03.png'),
                    pygame.image.load('character-02/character-left-04.png'),
                    pygame.image.load('character-02/character-left-05.png'),
                    pygame.image.load('character-02/character-left-06.png'),
                    pygame.image.load('character-02/character-left-07.png'),
                    pygame.image.load('character-02/character-left-08.png')
             ]


#
# Definicja dwu wymiarowej tablicy "gaRoomElements" zawierającej opis wyglądu każdego pokoju
#
gaRoomElements = [
                        # pokój - 0 / przyroda
                        [0,    0, 550, pygame.image.load("rooms/floor-01.png"), -1],
                        [0,   22, 257, pygame.image.load("rooms/bricks-01.png"), -1],
                        [0,  351, 326, pygame.image.load("rooms/bricks-01.png"), -1],
                        [0,  739, 137, pygame.image.load("rooms/bricks-01.png"), -1],
                        [0, 1161, 292, pygame.image.load("rooms/bricks-03.png"), -1],
                        [0, 1134, 434, pygame.image.load("rooms/bricks-03.png"), -1],
                        [0,  920,  74, pygame.image.load("rooms/arms.png"), -1],
                        [0,  844, 189, pygame.image.load("rooms/door-01.png"), -1],
                        [0,  157,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [0,  562,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [0,  964,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [0,   52, 373, pygame.image.load("rooms/desk.png"), -1],
                        [0,  136, 235, pygame.image.load("rooms/exponat-01.png"), -1],
                        [0,  230, 237, pygame.image.load("rooms/exponat-02.png"), -1],
                        [0,  620, 199, pygame.image.load("rooms/skeleton.png"), -1],
                        [0,  485, 367, pygame.image.load("rooms/flower-01.png"), -1],
                        # pokój - 1/ przyroda
                        [1,    0, 550, pygame.image.load("rooms/floor-01.png"), -1],
                        [1,    5, 332, pygame.image.load("rooms/bricks-03.png"), -1],
                        [1,    5, 460, pygame.image.load("rooms/bricks-01.png"), -1],
                        [1,  818, 433, pygame.image.load("rooms/bricks-03.png"), -1],
                        [1, 1108,  62, pygame.image.load("rooms/bricks-01.png"), -1],
                        [1,  157,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [1,  562,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [1,  964,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [1,  208, 199, pygame.image.load("rooms/skeleton.png"), -1],
                        [1,  434, 373, pygame.image.load("rooms/desk.png"), -1],
                        [1,  448, 213, pygame.image.load("rooms/exponat-03.png"), -1],
                        [1,  583, 235, pygame.image.load("rooms/exponat-01.png"), -1],
                        [1,  699, 336, pygame.image.load("rooms/billboard-02.png"), -1],
                        [1,  823, 160, pygame.image.load("rooms/picture-01.png"), -1],
                        [1,  902, 301, pygame.image.load("rooms/picture-02.png"), -1],
                        [1, 1024, 235, pygame.image.load("rooms/picture-01.png"), -1],
                        [1, 1143, 175, pygame.image.load("rooms/picture-02.png"), -1],
                        [1, 1113, 367, pygame.image.load("rooms/flower-01.png"), -1],
                        [1, 1184, 367, pygame.image.load("rooms/flower-01.png"), -1],
                        # pokój - 3 / sala gimnastyczna
                        [3,    0, 550, pygame.image.load("rooms/floor-01.png"), -1],
                        [3,   90, 434, pygame.image.load("rooms/bricks-01.png"), -1],
                        [3,   60, 216, pygame.image.load("rooms/bricks-03.png"), -1],
                        [3,  786,  65, pygame.image.load("rooms/bricks-03.png"), -1],
                        [3, 1108,  65, pygame.image.load("rooms/bricks-01.png"), -1],
                        [3,  638, 189, pygame.image.load("rooms/door-01.png"), -1],
                        [3,  210, 135, pygame.image.load("rooms/climbing-frame.png"), -1],
                        [3,  380, 135, pygame.image.load("rooms/climbing-frame.png"), -1],
                        [3,  940, 135, pygame.image.load("rooms/climbing-frame.png"), -1],
                        [3, 1120, 135, pygame.image.load("rooms/climbing-frame.png"), -1],
                        [3,  157,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [3,  562,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [3,  964,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [3,   67, 503, pygame.image.load("rooms/football-01.png"), -1],
                        [3,  135, 509, pygame.image.load("rooms/ball-01.png"), -1],
                        [3,  286, 396, pygame.image.load("rooms/horse.png"), -1],
                        # pokój - 4 / sala gimnastyczna
                        [4,    0, 550, pygame.image.load("rooms/floor-01.png"), -1],
                        [4,   19,  30, pygame.image.load("rooms/bricks-03.png"), -1],
                        [4,  404, 103, pygame.image.load("rooms/bricks-01.png"), -1],
                        [4,  665,  30, pygame.image.load("rooms/bricks-03.png"), -1],
                        [4,  864,  40, pygame.image.load("rooms/bricks-01.png"), -1],
                        [4,    5, 135, pygame.image.load("rooms/climbing-frame.png"), -1],
                        [4,  175, 135, pygame.image.load("rooms/climbing-frame.png"), -1],
                        [4,  367,   0, pygame.image.load("rooms/rope-ring.png"), -1],
                        [4,  425,   0, pygame.image.load("rooms/rope-ring.png"), -1],
                        [4, 1173,   0, pygame.image.load("rooms/rope.png"), -1],
                        [4,  731, 118, pygame.image.load("rooms/basket.png"), -1],
                        [4,  157,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [4,  562,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [4,  964,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [4,  167, 503, pygame.image.load("rooms/football-01.png"), -1],
                        [4,  543, 509, pygame.image.load("rooms/ball-01.png"), -1],
                        [4,  613, 509, pygame.image.load("rooms/ball-01.png"), -1],
                        [4,  580, 464, pygame.image.load("rooms/football-01.png"), -1],
                        [4,  753, 488, pygame.image.load("rooms/basketball-01.png"), -1],
                        [4,  831, 488, pygame.image.load("rooms/basketball-01.png"), -1],
                        [4,  788, 426, pygame.image.load("rooms/basketball-01.png"), -1],
                        # pokój - 5 / korytarz
                        [5,    0, 550, pygame.image.load("rooms/floor-01.png"), -1],
                        [5,   23, 120, pygame.image.load("rooms/bricks-01.png"), -1],
                        [5,  254,  78, pygame.image.load("rooms/bricks-01.png"), -1],
                        [5,  493, 431, pygame.image.load("rooms/bricks-03.png"), -1],
                        [5,  494, 256, pygame.image.load("rooms/bricks-02.png"), -1],
                        [5,  684, 364, pygame.image.load("rooms/bricks-03.png"), -1],
                        [5,  859,  41, pygame.image.load("rooms/bricks-01.png"), -1],
                        [5, 1143, 497, pygame.image.load("rooms/bricks-02.png"), -1],
                        [5,  183, 189, pygame.image.load("rooms/door-01.png"), -1],
                        [5,  844, 189, pygame.image.load("rooms/door-01.png"), -1],
                        [5,  157,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [5,  562,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [5,  964,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [5,  593, 358, pygame.image.load("rooms/sink-01.png"), -1],
                        [5, 1149, 280, pygame.image.load("rooms/billboard-01.png"), -1],
                        [5,  229, 294, pygame.image.load("rooms/label-mathematics.png"), -1],
                        [5,  897, 294, pygame.image.load("rooms/label-science.png"), -1],
                        [5,   29, 367, pygame.image.load("rooms/flower-01.png"), -1],
                        [5,  100, 367, pygame.image.load("rooms/flower-01.png"), -1],
                        # pokój - 6 / korytarz
                        [6,    0, 550, pygame.image.load("rooms/floor-01.png"), -1],
                        [6,   39, 430, pygame.image.load("rooms/bricks-01.png"), -1],
                        [6,  338, 101, pygame.image.load("rooms/bricks-01.png"), -1],
                        [6,  484, 331, pygame.image.load("rooms/bricks-03.png"), -1],
                        [6,  594, 255, pygame.image.load("rooms/bricks-02.png"), -1],
                        [6, 1156, 312, pygame.image.load("rooms/bricks-03.png"), -1],
                        [6, 1143, 493, pygame.image.load("rooms/bricks-02.png"), -1],
                        [6,  212, 189, pygame.image.load("rooms/door-01.png"), -1],
                        [6,  157,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [6,  562,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [6,  964,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [6,   61, 138, pygame.image.load("rooms/picture-of-the-king-04.png"), -1],
                        [6,  311, 294, pygame.image.load("rooms/label-wc.png"), -1],
                        [6,  741, 259, pygame.image.load("rooms/cupboard-01.png"), -1],
                        [6,  844, 259, pygame.image.load("rooms/cupboard-01.png"), -1],
                        [6,  945, 259, pygame.image.load("rooms/cupboard-01.png"), -1],
                        [6, 1045, 259, pygame.image.load("rooms/cupboard-01.png"), -1],
                        [6,  766, 291, pygame.image.load("rooms/label-01.png"), -1],
                        [6,  867, 291, pygame.image.load("rooms/label-02.png"), -1],
                        [6,  973, 291, pygame.image.load("rooms/label-03.png"), -1],
                        [6, 1066, 291, pygame.image.load("rooms/label-04.png"), -1],
                        [6,  769, 214, pygame.image.load("rooms/ball-01.png"), -1],
                        [6,  958, 214, pygame.image.load("rooms/ball-01.png"), -1],
                        # pokój - 7 / korytarz
                        [7,    0, 550, pygame.image.load("rooms/floor-01.png"), -1],
                        [7,  324,  54, pygame.image.load("rooms/bricks-01.png"), -1],
                        [7,  296, 484, pygame.image.load("rooms/bricks-01.png"), -1],
                        [7,  577, 186, pygame.image.load("rooms/bricks-02.png"), -1],
                        [7, 1140, 495, pygame.image.load("rooms/bricks-02.png"), -1],
                        [7,  527, 350, pygame.image.load("rooms/bricks-03.png"), -1],
                        [7,  802, 189, pygame.image.load("rooms/door-01.png"), -1],
                        [7,  157,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [7,  562,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [7,  964,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [7,  411, 136, pygame.image.load("rooms/picture-of-the-king-01.png"), -1],
                        [7,  638, 358, pygame.image.load("rooms/sink-01.png"), -1],
                        [7, 1120, 275, pygame.image.load("rooms/billboard-01.png"), -1],
                        [7,   17, 259, pygame.image.load("rooms/cupboard-01.png"), -1],
                        [7,   40, 289, pygame.image.load("rooms/label-05.png"), -1],
                        [7,  127, 256, pygame.image.load("rooms/cupboard-02.png"), -1],
                        [7,  223, 259, pygame.image.load("rooms/cupboard-01.png"), -1],
                        [7,  254, 294, pygame.image.load("rooms/label-06.png"), -1],
                        [7,  158, 206, pygame.image.load("rooms/ball-01.png"), -1],
                        [7,  844, 295, pygame.image.load("rooms/label-computer-science.png"), -1],
                        [7,   42,  64, pygame.image.load("rooms/flower-01.png"), -1],
                        # pokój - 8 / korytarz
                        [8,    0, 550, pygame.image.load("rooms/floor-01.png"), -1],
                        [8,   10, 240, pygame.image.load("rooms/bricks-01.png"), -1],
                        [8,  280, 420, pygame.image.load("rooms/bricks-01.png"), -1],
                        [8,  523, 484, pygame.image.load("rooms/bricks-01.png"), -1],
                        [8, 1162, 493, pygame.image.load("rooms/bricks-02.png"), -1],
                        [8, 1003, 428, pygame.image.load("rooms/bricks-03.png"), -1],
                        [8,  638, 189, pygame.image.load("rooms/door-01.png"), -1],
                        [8,  157,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [8,  562,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [8,  964,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [8,  332, 173, pygame.image.load("rooms/picture-of-the-king-02.png"), -1],
                        [8,  451, 173, pygame.image.load("rooms/picture-of-the-king-03.png"), -1],
                        [8,  935, 352, pygame.image.load("rooms/sink-01.png"), -1],
                        [8,  690, 295, pygame.image.load("rooms/label-gym.png"), -1],
                        [8,   64, 360, pygame.image.load("rooms/flower-01.png"), -1],
                        [8,  133, 360, pygame.image.load("rooms/flower-01.png"), -1],
                        [8, 1123, 360, pygame.image.load("rooms/flower-01.png"), -1],
                        # pokój - 11 / wc
                        [11,    0, 550, pygame.image.load("rooms/floor-01.png"), -1],
                        [11,  388, 140, pygame.image.load("rooms/bricks-02.png"), -1],
                        [11,   12, 194, pygame.image.load("rooms/bricks-01.png"), -1],
                        [11,  107, 410, pygame.image.load("rooms/bricks-03.png"), -1],
                        [11,  553, 373, pygame.image.load("rooms/tiles-01.png"), -1],
                        [11,  755, 352, pygame.image.load("rooms/tiles-01.png"), -1],
                        [11, 1113, 249, pygame.image.load("rooms/tiles-01.png"), -1],
                        [11,  934, 191, pygame.image.load("rooms/tiles-02.png"), -1],
                        [11,  212, 189, pygame.image.load("rooms/door-01.png"), -1],
                        [11,  157,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [11,  562,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [11,  964,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [11,  562, 190, pygame.image.load("rooms/mirror.png"), -1],
                        [11,  615, 310, pygame.image.load("rooms/sink-02.png"), -1],
                        [11,  815, 267, pygame.image.load("rooms/towels.png"), -1],
                        [11,  953, 293, pygame.image.load("rooms/urinal.png"), -1],
                        [11, 1099, 293, pygame.image.load("rooms/urinal.png"), -1],
                        [11,   35, 360, pygame.image.load("rooms/flower-01.png"), -1],
                        # pokój - 15 / matematyka
                        [15,    0, 550, pygame.image.load("rooms/floor-01.png"), -1],
                        [15,   29, 299, pygame.image.load("rooms/bricks-01.png"), -1],
                        [15,   27, 430, pygame.image.load("rooms/bricks-03.png"), -1],
                        [15,  469, 412, pygame.image.load("rooms/bricks-03.png"), -1],
                        [15,  963, 191, pygame.image.load("rooms/bricks-01.png"), -1],
                        [15,  260,  74, pygame.image.load("rooms/arms.png"), -1],
                        [15,  183, 189, pygame.image.load("rooms/door-01.png"), -1],
                        [15,  157,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [15,  562,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [15,  964,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [15,  470, 204, pygame.image.load("rooms/ruler-02.png"), -1],
                        [15,  560, 263, pygame.image.load("rooms/ruler-01.png"), -1],
                        [15,  674, 373, pygame.image.load("rooms/desk.png"), -1],
                        [15,  688, 273, pygame.image.load("rooms/figure-01.png"), -1],
                        [15,  785, 253, pygame.image.load("rooms/figure-02.png"), -1],
                        [15,  906, 273, pygame.image.load("rooms/figure-03.png"), -1],
                        [15, 1085, 196, pygame.image.load("rooms/computer-02.png"), -1],
                        # pokój - 16 / matematyka
                        [16,    0, 550, pygame.image.load("rooms/floor-01.png"), -1],
                        [16,   24,  60, pygame.image.load("rooms/bricks-01.png"), -1],
                        [16,  123, 254, pygame.image.load("rooms/bricks-03.png"), -1],
                        [16,   76, 459, pygame.image.load("rooms/bricks-01.png"), -1],
                        [16,  630, 360, pygame.image.load("rooms/bricks-03.png"), -1],
                        [16,  223, 148, pygame.image.load("rooms/blackboard.png"), -1],
                        [16,  157,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [16,  562,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [16,  964,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [16,  768, 139, pygame.image.load("rooms/picture-of-einstein.png"), -1],
                        [16, 1000, 360, pygame.image.load("rooms/flower-01.png"), -1],
                        [16, 1080, 360, pygame.image.load("rooms/flower-01.png"), -1],
                        [16, 1160, 360, pygame.image.load("rooms/flower-01.png"), -1],
                        # pokój - 17 / informatyka
                        [17,    0, 550, pygame.image.load("rooms/floor-01.png"), -1],
                        [17,   72, 230, pygame.image.load("rooms/bricks-01.png"), -1],
                        [17,   25, 411, pygame.image.load("rooms/bricks-03.png"), -1],
                        [17,  680, 421, pygame.image.load("rooms/bricks-03.png"), -1],
                        [17, 1133,  44, pygame.image.load("rooms/bricks-02.png"), -1],
                        [17,  880,  74, pygame.image.load("rooms/arms.png"), -1],
                        [17,  802, 189, pygame.image.load("rooms/door-01.png"), -1],
                        [17,  157,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [17,  562,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [17,  964,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [17,  182, 193, pygame.image.load("rooms/computer-02.png"), -1],
                        [17, 1095, 193, pygame.image.load("rooms/computer-02.png"), -1],
                        [17,  395, 375, pygame.image.load("rooms/desk.png"), -1],
                        [17,  416, 262, pygame.image.load("rooms/computer-01.png"), -1],
                        [17,  485, 262, pygame.image.load("rooms/computer-01.png"), -1],
                        [17,  560, 239, pygame.image.load("rooms/computer-screen.png"), -1],
                        # pokój - 18 / informatyka
                        [18,    0, 550, pygame.image.load("rooms/floor-01.png"), -1],
                        [18,   36,  18, pygame.image.load("rooms/bricks-01.png"), -1],
                        [18,  337,  96, pygame.image.load("rooms/bricks-03.png"), -1],
                        [18,  748, 140, pygame.image.load("rooms/bricks-03.png"), -1],
                        [18,  905,  46, pygame.image.load("rooms/bricks-01.png"), -1],
                        [18,  157,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [18,  562,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [18,  964,   0, pygame.image.load("rooms/lamp-01.png"), -1],
                        [18,   20, 193, pygame.image.load("rooms/computer-02.png"), -1],
                        [18,  200, 193, pygame.image.load("rooms/computer-02.png"), -1],
                        [18,  445, 375, pygame.image.load("rooms/desk.png"), -1],
                        [18,  503, 262, pygame.image.load("rooms/computer-01.png"), -1],
                        [18,  591, 239, pygame.image.load("rooms/computer-screen.png"), -1],
                        [18,  853, 375, pygame.image.load("rooms/desk.png"), -1],
                        [18,  916, 262, pygame.image.load("rooms/computer-01.png"), -1],
                        [18, 1000, 239, pygame.image.load("rooms/computer-screen.png"), -1],
                        [18,  372, 360, pygame.image.load("rooms/flower-01.png"), -1],
                        [18,  782, 360, pygame.image.load("rooms/flower-01.png"), -1],
                        [18, 1189, 360, pygame.image.load("rooms/flower-01.png"), -1]
                    ]


#
# Definicja dwu wymiarowej tablicy "gaRoomTransition" zawierającej opis przejść pomiędzy pokojami, kolory tłą poszczególnego pokoju.
#
gaRoomTransition = [
                     # pokój - 0 / przyroda
                     [0, False, True, [111, 170, 127], [825, 1055, 5]],
                     # pokój - 1 / przyroda
                     [1, True, False, [111, 170, 127], [-1]],
                     # pokój - 2 / brak pokoju
                     [2, False, False, [0, 0, 0], [-1]],
                     # pokój - 3 / sala gimnastyczna
                     [3, False, True, [207, 142, 49], [650, 880, 8]],
                     # pokój - 4 / sala gimnastyczna
                     [4, True, False, [207, 142, 49], [-1]],
                     # pokój - 5 / korytarz
                     [5, False, True, [174, 174, 174], [195, 425, 15, 855, 1085, 0]],
                     # pokój - 6 / korytarz
                     [6, True, True, [174, 174, 174], [225, 455, 11 ]],
                     # pokój - 7 / korytarz
                     [7, True, True, [174, 174, 174], [815, 1050, 17]],
                     # pokój - 8 / korytarz
                     [8, True, False, [174, 174, 174], [650, 880, 3]],
                     # pokój - 9 / brak pokoju
                     [9, False, False, [0, 0, 0], [-1]],
                     # pokój - 10 / brak pokoju
                     [10, False, False, [0, 0, 0], [-1]],
                     # pokój - 11 / wc
                     [11, False, False, [82, 115, 231], [225, 455, 6]],
                     # pokój - 12 / brak pokoju
                     [12, False, False, [0, 0, 0], [-1]],
                     # pokój - 13 / brak pokoju
                     [13, False, False, [0, 0, 0], [-1]],
                     # pokój - 14 / brak pokoju
                     [14, False, False, [0, 0, 0], [-1]],
                     # pokój - 15 / matematyka
                     [15, False, True, [239, 74, 74], [195, 425, 5]],
                     # pokój - 16 / matematyka
                     [16, True, False, [239, 74, 74], [-1]],
                     # pokój - 17 / informatyka
                     [17, False, True, [191, 120, 195], [815, 1050, 7]],
                     # pokój - 18 / informatyka
                     [18, True, False, [191, 120, 195], [-1]],
                     # pokój - 19 / brak pokoju
                     [19, False, False, [0, 0, 0], [ -1 ]]
                   ]


#
# Parametr odpowiedzialny za aktualnie wyświetlany pokój
#
giRoomNumber = 6


#
#
#
giMainCharacterWidth = 192
giMainCharacterHeight= 256


#
# Definicja klasy c_MainCharacter
#
class c_MainCharacter(object):
    def __init__(self, iX, iY, iWidth, iHeight):
        self.iX = iX
        self.iY = iY
        self.iWidth = iWidth
        self.iHeight = iHeight
        self.bLeft = False
        self.bRight = False
        self.bJump = False
        self.walkCount = 0
        self.jumpCount = 12
        self.vel = 4/giScaleFactor #10 #2

    def setX (self, iX):
        self.iX = iX

    def getWalkCount(self):
        return self.walkCount

    def draw(self, gpyDisplay):
        # Ponieważ mamy 8 klatek animacji głównego bohatera - 8 klatek  chód w prawo, 8 klatek chód w lewo.
        # Chcemy pokazać tą samą klatkę animacji dwa razy podczas odświeżenia ekranu. Dlatego wartością maksymalną dla
        # zmiennej iWalkCounter jest liczba 16, bo 16 / 2 = 8
        if self.walkCount + 1 >= 16:
            self.walkCount = 0
        #
        if self.bLeft:
            gpyDisplay.blit(pygame.transform.smoothscale(gaWalkLeft[self.walkCount // 2], (round(gaWalkLeft[self.walkCount // 2].get_width()/giScaleFactor), round(gaWalkLeft[self.walkCount // 2].get_height()/giScaleFactor))), (self.iX, self.iY))
            self.walkCount += 1
        #
        elif self.bRight:
            gpyDisplay.blit(pygame.transform.smoothscale(gaWalkRight[self.walkCount // 2], (round(gaWalkRight[self.walkCount // 2].get_width()/giScaleFactor), round(gaWalkRight[self.walkCount // 2].get_height()/giScaleFactor))), (self.iX, self.iY))
            self.walkCount += 1
        #
        else:
            gpyDisplay.blit(pygame.transform.smoothscale(pStandingCharacter, (round(pStandingCharacter.get_width()/giScaleFactor), round(pStandingCharacter.get_height()/giScaleFactor))), (self.iX, self.iY))


#
# Funkcja calculateScaleFactor()
# Oblicza szerokość (giScreenWidth), wysokość (giScreenHeight) oraz współczynnikk skalowania (giScaleFactor).
# Maksymalna możliwa rozdzielczość to szerokość 1280 pikseli. W oparciu o wyliczoną wartość zmiennej GiScaleFactor, pozycjonowane i skalowane są
# wszystkie obiekty w grze
#
def calculateScaleFactor():
    global giScreenWidth
    global giScreenHeight
    global giScaleFactor
    #
    if giScreenWidth < 1280:
        giScaleFactor = 1280/giScreenWidth
        giScreenHeight = round(640/giScaleFactor)
    #
    else:
        giScreenWidth = 1280
        giScreenHeight = 640
        giScaleFactor = 1


#
# Funkcja redrawRoom(iRoomNumber)
#
def redrawRoom(iRoomNumber, aColour):
    pygame.draw.rect(gpyDisplay, (aColour[0], aColour[1], aColour[2]), (0, 0, giScreenWidth, giScreenHeight))
    for aRowRoomElements in gaRoomElements:
        if aRowRoomElements[0] == iRoomNumber:
            gpyDisplay.blit(pygame.transform.smoothscale(aRowRoomElements[3], (round(aRowRoomElements[3].get_width()/giScaleFactor), round(aRowRoomElements[3].get_height()/giScaleFactor))), (round(aRowRoomElements[1]/giScaleFactor), round(aRowRoomElements[2]/giScaleFactor)))


#
# Funkcja redrawGameWindow()
#
def redrawGameWindow():
    # Rysowanie pokoju - wywołanie funkcji "redrawRoom" / jako parametr przesyłamy numer pokoju oraz tablicę z wartościami RGB - kolor tła
    redrawRoom (giRoomNumber, [gaRoomTransition[giRoomNumber][3][0], gaRoomTransition[giRoomNumber][3][1], gaRoomTransition[giRoomNumber][3][2]])
    # Rysowanie postaci - wywołanie metody "draw" obiektu "o_MainCharacter"
    o_MainCharacter.draw(gpyDisplay)
    # update screen
    pygame.display.update()


#
# Wywołanie funkcji calculateScaleFactor()
#
calculateScaleFactor()


#
# Inicjacja biblioteki PyGame
#
pygame.init()
#
pygame.display.set_caption("adventure game")
# Ustalenie trybu pracy ekranu w trybie FULLSCREEN o wymiarach ustalonych przez wywołanie funkcji calculateScaleFactor()
gpyDisplay = pygame.display.set_mode((giScreenWidth, giScreenHeight), pygame.FULLSCREEN)
# Utworzenie obiektu pozwalającego śledzić czas
gpyTimeClock = pygame.time.Clock()
# Załadowanie obrazka odpowiadającego za postać głównego bohatera w momencie kiedy stoi bez ruchu
pStandingCharacter = pygame.image.load('standing.png')
# Utworzenie obiektu na podstawie wczytanego pliku dźwiękowego
#pSoundWalk = pygame.mixer.Sound('sounds/walk-01.wav')
pSoundJump = pygame.mixer.Sound('sounds/jump-01.wav')
pSoundDoor = pygame.mixer.Sound('sounds/door-01.wav')
# Załadowanie muzki, która będzie odgrywana w tle w czasie gry
#pMusic = pygame.mixer.music.load('sounds/music-01.mp3')
#pygame.mixer.music.play(-1, 0.0)
# Ponieważ używamy trybu pełnego ekranu (FULLSCREEN) ukrywamy kursor myszy
pygame.mouse.set_visible(False)


#
# Utworzenie obiektu o_MainCharacter
# Obiekt odpowiada za postać głównego bohatera, przechowuje położenie, rozmiar, aktualnie wyświetlaną fazę animacji
# a także ustala kierunek (ruch w prawo, lewo) oraz skok
#
o_MainCharacter = c_MainCharacter(giScreenWidth/2, giScreenHeight/2-6, round(giMainCharacterWidth/giScaleFactor), round(giMainCharacterHeight/giScaleFactor))


#
# Główna pętla programu
#
bMainGameLoop = True
while bMainGameLoop:

    #
    # Aktualizacja częstotliwości obiektu odpowiedzialnego za zegar
    gpyTimeClock.tick(60)

    #
    #
    for event in pygame.event.get():
        #
        #
        if event.type == pygame.QUIT:
            bMainGameLoop = False
        #
        #
        elif event.type == pygame.KEYDOWN:
            #
            #
            if event.key == pygame.K_ESCAPE:
                bMainGameLoop = False
            #
            #
            elif event.key == pygame.K_UP:
                #
                #
                iTemp = 0
                iRoomTransition = len(gaRoomTransition[giRoomNumber][4])
                if gaRoomTransition[giRoomNumber][4][0] != -1:
                    while iRoomTransition > iTemp:
                        if o_MainCharacter.iX >= round(gaRoomTransition[giRoomNumber][4][iTemp]/giScaleFactor) and o_MainCharacter.iX <= round(gaRoomTransition[giRoomNumber][4][iTemp+1]/giScaleFactor):
                            giRoomNumber = gaRoomTransition[giRoomNumber][4][iTemp+2]
                            pSoundDoor.stop()
                            pSoundDoor.play()
                            break
                        iTemp += 3

    #
    #
    aKeys = pygame.key.get_pressed()

    #
    # Naciśnięty klawisz "q"
    if aKeys[pygame.K_q]:
        bMainGameLoop = False

    #
    # Naciśnięty klawisz "kursor w lewo"
    elif aKeys[pygame.K_LEFT]:
        if o_MainCharacter.iX > o_MainCharacter.vel:
            o_MainCharacter.iX -= o_MainCharacter.vel
            o_MainCharacter.bLeft = True
            o_MainCharacter.bRight = False
        else:
            if gaRoomTransition[giRoomNumber][1] == True:
                giRoomNumber -= 1
                o_MainCharacter.setX(giScreenWidth - round(giMainCharacterWidth/giScaleFactor))

    #
    # Naciśnięty klawisz "kursor w prawo"
    elif aKeys[pygame.K_RIGHT]:
        if o_MainCharacter.iX < giScreenWidth - round(o_MainCharacter.iWidth/giScaleFactor) - o_MainCharacter.vel:
            o_MainCharacter.iX += o_MainCharacter.vel
            o_MainCharacter.bRight = True
            o_MainCharacter.bLeft = False
        else:
            if gaRoomTransition[giRoomNumber][2] == True:
                giRoomNumber += 1
                o_MainCharacter.setX(0)

    #
    #
    else:
        o_MainCharacter.bRight = False
        o_MainCharacter.bLeft = False
        o_MainCharacter.walkCount = 0

    #
    # Naciśnięty klawisz "spacja"
    if not(o_MainCharacter.bJump):
        if aKeys[pygame.K_SPACE]:
            o_MainCharacter.bJump = True
            pSoundJump.stop()
            pSoundJump.play()
            #o_MainCharacter.bRight = False
            #o_MainCharacter.bLeft = False
            #o_MainCharacter.walkCount = 0

    #
    #
    else:
        if o_MainCharacter.jumpCount >= -12:
            neg = 2
            if o_MainCharacter.jumpCount < 0:
                neg = -2
            o_MainCharacter.iY -= (o_MainCharacter.jumpCount ** 2) * (0.2/giScaleFactor) * neg
            o_MainCharacter.jumpCount -= 2
        else:
            o_MainCharacter.bJump = False
            o_MainCharacter.jumpCount = 12

    #
    # Odświerzenie ekranu
    redrawGameWindow()


##
## Zakończenie programu
##
pygame.quit()
