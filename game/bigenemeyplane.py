import constants
from game.enemeyplane import EnemyPlane


class BigEnemyPlane(EnemyPlane):
    # 图片
    images_src = constants.BIG_ENEMY_PLANE_IMG_LIST
    # 被击中后图片
    images_hit_src = constants.BIG_ENEMY_PLANE_HIT_IMG_LIST
    # 摧毁图片
    destroy_images_src = constants.BIG_ENEMY_DESTROY_IMG_LIST
    # 摧毁音效
    destroy_sound_src = constants.BIG_ENEMY_PLANE_DOWN_SOUND
    # 飞机最大血量
    max_blood = 5

    def blit_image(self, war):
        """ 渲染视图 """
        if self.hit:
            self.screen.blit(self.images_hit[0], self.rect)
        else:
            if war.times % 3 == 0:  # 飞机喷气效果
                self.screen.blit(self.images[0], self.rect)
            else:
                self.screen.blit(self.images[1], self.rect)

