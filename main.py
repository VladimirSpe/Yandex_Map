def scre_pyg():
    import pygame
    pygame.init()
    getImage()
    bg = pygame.image.load("map.png")
    size = bg.get_size()
    pygame.display.set_caption('Yandex_Map_ex1')
    screen = pygame.display.set_mode(size)
    screen.blit(bg, [0, 0])
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        screen.blit(bg, [0, 0])
    pygame.quit()


def getImage():
    import requests
    import sys
    size = cord_inp()
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
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)


def cord_inp():
    import sys
    try:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        z = int(sys.argv[3])
    except Exception:
        return 0
    return str(x), str(y), str(z)


if __name__ == '__main__':
    scre_pyg()
