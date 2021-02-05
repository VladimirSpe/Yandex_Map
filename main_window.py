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

    def mainloop(self):
        pygame.init()
        bg = pygame.image.load("data/map.png")
        size = bg.get_size()
        pygame.display.set_caption('Yandex Map')
        screen = pygame.display.set_mode(size)
        screen.blit(bg, [0, 0])
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            screen.blit(bg, [0, 0])
        pygame.quit()
