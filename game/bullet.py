import pygame

import constants


class Bullet(pygame.sprite.Sprite):
    image_src = constants.BULLET_IMG
    sound_src = constants.BULLET_SHOOT_SOUND
    power = 1  # 子弹威力

    def __init__(self, screen, plane, step=10):
        super().__init__()
        # 游戏界面
        self.screen = screen
        # 飞机
        self.plane = plane
        # 子弹移动步长(正值表示向下移动，负值表示向上移动)
        self.step = step
        # 子弹图片资源
        self.image = pygame.image.load(self.image_src)
        # 初始化子弹位置
        self.rect = self.image.get_rect()
        self.adjust_rect()
        # 飞机发射音效
        self.sound = pygame.mixer.Sound(self.sound_src)
        self.sound.play()

    def adjust_rect(self):
        """ 初始化子弹位置 """
        plane_rect = self.plane.rect
        self.rect.centerx = plane_rect.centerx
        if self.step > 0:
            self.rect.top = plane_rect.buttom
        else:
            self.rect.bottom = plane_rect.top

    def update(self, war):
        """游戏循环"""
        # 子弹移动
        self.rect = self.rect.move(0, self.step)
        # 边界判断
        if self.rect.top < 0 or self.rect.bottom > self.screen.get_height():
            self.remove(self.plane.bullets)
        else:
            # 游戏渲染
            self.screen.blit(self.image, self.rect)
        # 碰撞检测
        targets = pygame.sprite.spritecollide(self, war.enemies, False)
        for target in targets:
            self.kill()  # 子弹消失
            target.hurt(war, self.power)


