import constants
from game.enemeyplane import EnemyPlane


class MiddleEnemyPlane(EnemyPlane):
    # 图片
    images_src = constants.MIDDLE_ENEMY_PLANE_IMG_LIST
    # 被击中后图片
    images_hit_src = constants.MIDDLE_ENEMY_PLANE_HIT_IMG_LIST
    # 摧毁图片
    destroy_images_src = constants.MIDDLE_ENEMY_DESTROY_IMG_LIST
    # 摧毁音效
    destroy_sound_src = constants.MIDDLE_ENEMY_PLANE_DOWN_SOUND
    # 飞机最大血量
    max_blood = 3

    def blit_image(self, war):
        """ 渲染视图 """
        if self.hit:
            self.screen.blit(self.images_hit[0], self.rect)
        else:
            self.screen.blit(self.images[0], self.rect)

