from consts import *


class MainWindow:
    def __init__(self, x: int, y: int, z: int):
        self.bg = pygame.image.load('data/map.png')
        self.size = self.bg.get_size()

        pygame.init()
        pygame.display.set_caption('Yandex Map')
        self.screen = pygame.display.set_mode(self.size)

        self.x = x
        self.y = y
        self.z = z

        self.get_image()
        self.running = False
        self.mainloop()


    def get_image(self):
        import requests
        size = self.x, self.y, self.z
        response = 0
        if size != 0:
            map_request = f"""http://static-maps.yandex.ru/1.x/?ll={size[1]},{size[0]}&spn={size[2]},{size[2]}&l=map"""
            response = requests.get(map_request)
        else:
            map_request = 'Неверные координаты'
        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)
        map_file = "data/map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        self.bg = pygame.image.load('data/map.png')
        self.size = self.bg.get_size()

    def mainloop(self):
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_PAGEDOWN:
                        print("Hhhhhh")
                    elif event.key == pygame.K_PAGEUP:
                        print("sggrgrr")
            self.screen.blit(self.bg, [0,0])
            pygame.display.flip()
