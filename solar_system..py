import pygame

<<<<<<< HEAD

SCREEN_SIZE = (800, 800)


class Menu(): 
    def menufunc(self, clock, events): # функция меню 
        done = False
        while not done: #обработка событий
            clock.tick(30)
    
            for event in events.get():
                if event.type == pg.QUIT:
                    done = True 
                    """ нажимаем кнопку чтобы начать"""
                elif event.type == pg.KEYDOWN: 
                    return Level_1(clock, events)
                """теперь обрабатывать события будет функция start класса level"""
            pg.display.flip()
            
            
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
            print(int(acceleration * cos))
            print(int(acceleration * sin))
    


        
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


=======
pygame.init()


class Sun():
    """
    Устанавливает параметры Солнца и рисует его
    """
    pass


class Planet():
    """
    Управляет движением планет, устанавливает их параметры и рисует их
    """
    def __init__(self, number):
        """
        Рассчитывает скорость планет, их координаты и ускорения
        Параметр number выбирает планету из файла
        """
        pass
    pass



class StartButton():
   """
   Рисует стартовую кнопку, проверяет, нажата ли она и начинает симуляцию
   """
   pass


class PauseButton():
   """
   Рисует кнопку паузы, проверяет, нажата ли она и останавливает симуляцию
   """
   pass


class ResetButton():
   """
   Рисует кнопку перезагрузки, проверяет, нажата ли она и перезапускает симуляцию
   """
   pass


>>>>>>> parent of 6c46d38... Update solar_system..py
class Processing():
    """
    Обрабатка
    """
<<<<<<< HEAD
    pass

        self.start(clock,events)
     #функция обрабатывает запуск ракеты  
    def start(self, clock, events):            
        done = False
        while not done: #обработка событий
            clock.tick(30)
            screen.fill((0,0,0))
            for event in events.get():
                if event.type == pg.QUIT:
                    done = True
                elif event.type == pg.KEYDOWN:
                    self.planet.velocity = [0, 20]
                    #теперь обрабатывать события будет функция process
                    self.process(clock, events)
            self.drawthemall()
            pg.display.flip()
    def process(self, clock, events):
        #функция обрабатывает полет ракеты    
        done = False
        while not done: #обработка событий
            clock.tick(30)
            screen.fill((0,0,0))
            for event in events.get():
                if event.type == pg.QUIT:
                    done = True
            self.planet.gravity(self.stars)
            self.movethemall()
            self.drawthemall()
            pg.display.flip()
        
    def drawthemall(self):

        
        for star in self.stars:
            star.draw()
    

        self.planet.draw()
        
        
    def movethemall(self):
        self.planet.motion()
    
    
screen = pg.display.set_mode(SCREEN_SIZE)


clock = pg.time.Clock()

"""создаем объект меню """
menu = Menu()     

""" функция выкидывает нам тип уровня:"""
level = menu.menufunc(clock, pg.event)




pg.quit()
=======
    pass
>>>>>>> parent of 6c46d38... Update solar_system..py
