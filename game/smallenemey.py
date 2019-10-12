import constants
from game.enemeyplane import EnemyPlane


class SmallEnemyPlane(EnemyPlane):
    # 图片
    images_src = constants.SMALL_ENEMY_PLANE_IMG_LIST
    # 摧毁图片
    destroy_images_src = constants.SMALL_ENEMY_DESTROY_IMG_LIST
    # 摧毁音效
    destroy_sound_src = constants.SMALL_ENEMY_PLANE_DOWN_SOUND
    # 飞机最大血量
    max_blood = 1

