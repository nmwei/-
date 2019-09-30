import pygame

import constants
from game.plane import Plane


class Enemy(Plane):
    # 图片
    images_src = constants.SMALL_ENEMY_PLANE_IMG_LIST
    # 摧毁图片
    destroy_images_src = constants.SMALL_ENEMY_DESTROY_IMG_LIST
    # 摧毁音效
    destroy_sound_src = constants.SMALL_ENEMY_PLANE_DOWN_SOUND

    def __init__(self, screen, speed=10):
        super().__init__(screen, speed)

    def init_rect(self):
        pass

