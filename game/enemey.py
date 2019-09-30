import random

import constants
from game.plane import Plane


class SmallEnemyPlane(Plane):
    # 图片
    images_src = constants.SMALL_ENEMY_PLANE_IMG_LIST
    # 摧毁图片
    destroy_images_src = constants.SMALL_ENEMY_DESTROY_IMG_LIST
    # 摧毁音效
    destroy_sound_src = constants.SMALL_ENEMY_PLANE_DOWN_SOUND

    def __init__(self, screen, speed=10):
        super().__init__(screen, speed)
        self.init_rect()

    def init_rect(self):
        self.rect.bottom = random.randint(-self.rect.height * 5, 0)
        self.rect.left = random.randint(0, self.screen.get_width() - self.rect.width)

    def render(self, war):
        """ 渲染视图 """
        self.rect.bottom += self.speed
        if self.rect.top > self.screen.get_height():
            self.init_rect()
        self.screen.blit(self.images[0], self.rect)

