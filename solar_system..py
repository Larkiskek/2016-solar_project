import pygame as pg
import math
pg.init()
pg.font.init()
SCREEN_SIZE = (800, 800)

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (87, 160, 211)
GREEN = (140, 207, 127)
ORANGE = (240, 136, 0)


class Menu():
    def menufunc(self, clock, events): #функция меню
        self.sb = StartButton()
        self.pb = PauseButton()
        self.rb = ResetButton()
        done = False
        while not done: #обработка событий
            clock.tick(30)
            self.sb.draw(screen, BLACK)
            self.pb.draw(screen, BLACK)
            self.rb.draw(screen, BLACK)
            done = False
            for event in events.get():
                if event.type == pg.QUIT:
                    done = True
                    """ нажимаем кнопку чтобы начать"""
                elif event.type==pg.MOUSEBUTTONDOWN:
                    self.sb.react(pg.mouse.get_pos())
                    self.pb.react(pg.mouse.get_pos())
                    self.rb.react(pg.mouse.get_pos())
                    if (self.sb.phrase) == "Start":
                        return Level_1(clock, events)
                """теперь обрабатывать события будет функция start класса level"""
            pg.display.flip()



class Button():
    """
    Содержит основные свойства любой кнопки.
    """
    def __init__(self, coord=[20, 20], color=BLUE, width=100, height=45, phrase=""):
        self.coord = coord
        self.color = color
        self.width = width
        self.height = height
        self.phrase = phrase
        self.font = pg.font.SysFont("dejavusansmono", 40)
        self.font_loc = [self.coord[0] + 10, self.coord[1] + 10]
        self.font_color = BLACK

    def draw(self, screen, font_color, phrase=""):
        pg.draw.rect(screen, self.color, (self.coord[0], self.coord[1], self.width, self.height))
        screen.blit(self.font.render(phrase, True, self.font_color), self.font_loc)


    def react(self, mouse_pos, phrase=""):
        if ((mouse_pos[0] > self.coord[0]) and (mouse_pos[0] < (self.coord[0] + self.width)) and
            (mouse_pos[1] > self.coord[1]) and (mouse_pos[1] < (self.coord[1] + self.height))):
            screen.blit(self.font.render(phrase, True, RED), self.font_loc)
            self.phrase = phrase


class StartButton(Button):
    """
    Рисует стартовую кнопку, проверяет, нажата ли она и начинает симуляцию
    """
    def __init__(self, coord=[20, 85], color=GREEN, width=100, height=45):
        super().__init__(coord=[20, 85], color=GREEN, width=100, height=45)

    def draw(self, screen, font_color, phrase="Start"):
        super().draw(screen, font_color, phrase="Start")
    
    def react(self, mouse_pos, phrase="Start"):
        super().react(mouse_pos, phrase = "Start")


class PauseButton(Button):
    """
    Рисует кнопку паузы, проверяет, нажата ли она и останавливает симуляцию
    """
    def __init__(self, coord=[20, 150], color=ORANGE, width=100, height=45):
        super().__init__(coord=[20, 150], color=ORANGE, width=100, height=45)

    def draw(self, screen, font_color, phrase = "Pause"):
        super().draw(screen, font_color, phrase = "Pause")
    
    def react(self, mouse_pos, phrase="Pause"):
        if ((mouse_pos[0] > self.coord[0]) and (mouse_pos[0] < (self.coord[0] + self.width)) and
            (mouse_pos[1] > self.coord[1]) and (mouse_pos[1] < (self.coord[1] + self.height))):
            screen.blit(self.font.render(phrase, True, RED), self.font_loc)
            self.phrase = phrase
            if self.font_color==BLACK:
                self.font_color = RED
            else:
                self.font_color = BLACK



class ResetButton(Button):
    """
    Рисует кнопку перезагрузки, проверяет, нажата ли она и перезапускает симуляцию
    """
    def __init__(self, coord=[20, 20], color=BLUE, width=100, height=45):
        super().__init__(coord=[20, 20], color=BLUE, width=100, height=45)


    def draw(self, screen, font_color, phrase = "Reset"):
        super().draw(screen, font_color, phrase = "Reset")

    def react(self, mouse_pos, phrase="Reset"):
        super().react(mouse_pos, phrase = "Reset")
    

class Planet():
    def __init__(self):
        self.coord = [100, 400]
        self.velocity = [0,10]

    def motion(self): #функция движения
        self.coord[0] += self.velocity[0]
        self.coord[1] += self.velocity[1]


    def draw(self): #рисуем ракету каждый clock.tick
        pg.draw.circle(screen, (33, 150, 243),
                     self.coord, 5)
    def gravity(self, stars):
        """ гравитация. принимаем на вход массив звёзд"""
        G = 0.1
        for star in stars:

            distance = math.sqrt((self.coord[0] - star.coord[0])**2 +
                                 (self.coord[1] - star.coord[1])**2)
            cos = (self.coord[0] - star.coord[0]) / distance
            acceleration = G * star.mass / distance**2
            sin = (self.coord[1] - star.coord[1]) / distance
            self.velocity[0] -= round(acceleration * cos)
            self.velocity[1] -= round(acceleration * sin)

class Star():
    def __init__(self, x, y, rad, mass):
        self.coord = [x,y]
        self.rad = rad
        self.mass = mass
    def draw(self):
        pg.draw.circle(screen, (255, 235, 59),
                       self.coord, self.rad)


class Level():
    pass

class Level_1(Level):
    def __init__(self,clock, events):
        self.planet = Planet()
        self.stars = []
        self.stars.append(Star(400, 400, 20, 1000000))
        self.start(clock,events)

     #функция обрабатывает начало движения планеты
    def start(self, clock, events):
        self.sb = StartButton()
        self.pb = PauseButton()
        self.rb = ResetButton()
        done = False
        while not done: #обработка событий
            clock.tick(30)
            screen.fill((0,0,0))
            self.sb.draw(screen, BLACK)
            self.pb.draw(screen, BLACK)
            self.rb.draw(screen, BLACK)
            for event in events.get():
                if event.type == pg.QUIT:
                    done = True

                elif event.type==pg.MOUSEBUTTONDOWN:
                    self.sb.react(pg.mouse.get_pos())
                    self.pb.react(pg.mouse.get_pos())
                    self.rb.react(pg.mouse.get_pos())
                    if (self.sb.phrase) == "Start":
                        self.planet.velocity = [0, 20]

                        #теперь обрабатывать события будет функция process
                        self.process(clock, events)


            self.drawthemall()
            pg.display.flip()

    def process(self, clock, events):
        #функция обрабатывает полет планеты
        self.sb = StartButton()
        self.pb = PauseButton()
        self.rb = ResetButton()
        done = False

        while not done: #обработка событий
            clock.tick(30)
            screen.fill((0,0,0))
            self.sb.draw(screen, BLACK)
            self.pb.draw(screen, BLACK)
            self.rb.draw(screen, BLACK)
            for event in events.get():
                if event.type == pg.QUIT:
                    done = True
                elif event.type==pg.MOUSEBUTTONDOWN:
                    self.sb.react(pg.mouse.get_pos())
                    self.pb.react(pg.mouse.get_pos())
                    self.rb.react(pg.mouse.get_pos())
            if (self.pb.phrase) != "Pause":
                self.planet.gravity(self.stars)
                self.movethemall()
                self.drawthemall()
                pg.display.flip()

            if (self.rb.phrase) == "Reset":
                done = True
                return Level_1(clock, events)

            if ((self.pb.phrase) == "Pause"):
                i = 0
                self.pb.phrase = ""
                while i < 1:
                    done = True
                    for event in events.get():
                        if event.type == pg.QUIT:
                            i = 1
                        elif event.type==pg.MOUSEBUTTONDOWN:
                            self.sb.react(pg.mouse.get_pos())
                            self.pb.react(pg.mouse.get_pos())
                            self.rb.react(pg.mouse.get_pos())

                    if (self.pb.phrase) == "Pause":
                        i = 1
                        done = False
                        self.pb.phrase = ""

                    if (self.rb.phrase) == "Reset":
                        i = 1
                        return Level_1(clock, events)


    def drawthemall(self):
        for star in self.stars:
            star.draw()
        self.planet.draw()

    def movethemall(self):
        self.planet.motion()




screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("Solar system model")
clock = pg.time.Clock()
"""создаем объект меню """
menu = Menu()
""" функция выкидывает нам тип уровня:"""
level = menu.menufunc(clock, pg.event)


pg.quit()


