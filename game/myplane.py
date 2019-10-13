import pygame

import constants
from game.bullet import Bullet
from game.plane import Plane


class MyPlane(Plane):
    # 飞机图片
    images_src = constants.MY_PLANE_IMA_LIST
    # 摧毁图片
    destroy_images_src = constants.MY_DESTROY_IMG_LIST

    def init_rect(self):
        """ 初始化我的飞机位置 """
        width, height = self.get_screen_size()
        self.rect.bottom = height
        self.rect.centerx = width / 2

    def bind_event(self, down_key):
        """ 绑定事件 """
        if down_key == pygame.K_w or down_key == pygame.K_UP:
            self.move_up()
        elif down_key == pygame.K_s or down_key == pygame.K_DOWN:
            self.move_down()
        elif down_key == pygame.K_a or down_key == pygame.K_LEFT:
            self.move_left()
        elif down_key == pygame.K_d or down_key == pygame.K_RIGHT:
            self.move_right()

    def render(self, war):
        """ 渲染视图 """
        if war.times % 3 == 0:  # 添加子弹
            self.bullets.add(Bullet(self.screen, self, -20))
        if war.times % 5 == 0:  # 飞机喷气效果
            self.screen.blit(self.images[0], self.rect)
        else:
            self.screen.blit(self.images[1], self.rect)
        # 碰撞检测
        targets = pygame.sprite.spritecollide(self, war.enemies, False)
        if targets:
            self.hurt(war)

    def destroy(self, war):
        super().destroy(war)
        # 清空敌机
        war.enemies.empty()
        war.small_enemies.empty()
        war.middle_enemies.empty()
        war.big_enemies.empty()
        # 修改游戏状态
        war.state = war.OVER

