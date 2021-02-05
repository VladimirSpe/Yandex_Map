from consts import *


class MainWindow:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

        self.get_image()
        self.mainloop()

    def get_image(self):
        import requests
        size = self.x, self.y, self.z
        response = 0
        if size != 0:
            map_request = f"""http://static-maps.yandex.ru/1.x/?ll={size[0]},{size[1]}&spn={size[2]},{size[2]}&l=map"""
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

    def mainloop(self):
        pygame.init()
        bg = pygame.image.load("data/map.png")
        size = bg.get_size()
        pygame.display.set_caption('Yandex Map')
        screen = pygame.display.set_mode(size)
        screen.blit(bg, [0, 0])
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                x, y = 0, 0
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        y += 1
                    if event.key == pygame.K_DOWN:
                        y -= 1
                    if event.key == pygame.K_LEFT:
                        x -= 1
                    if event.key == pygame.K_RIGHT:
                        x += 1
                    if x != 0 or y != 0:
                        self.x += x
                        self.y += y
                        self.get_image()
                        bg = pygame.image.load("data/map.png")
                        screen.blit(bg, [0, 0])
                        pygame.display.flip()
                    print(x, y)

        pygame.quit()
