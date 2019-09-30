from game.war import War


def start():
    war = War()
    war.add_small_enemy(6)
    war.start()


if __name__ == '__main__':
    start()