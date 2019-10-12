import pygame


class Plane(pygame.sprite.Sprite):
    # 飞机图片
    images_src = []
    # 飞机被击中图片
    images_hit_src = []
    # 摧毁图片
    destroy_images_src = []
    # 摧毁音效
    destroy_sound_src = None
    # 飞机最大血量
    max_blood = 1

    def __init__(self, screen, speed=10):
        super().__init__()
        # 游戏界面
        self.screen = screen
        # 移动速度
        self.speed = speed
        # 状态
        self.active = True
        # 飞机图片对象
        self.images = list(map(lambda img: pygame.image.load(img), self.images_src))
        # 飞机被击中图片对象
        self.images_hit = list(map(lambda img: pygame.image.load(img), self.images_hit_src))
        # 飞机摧毁图片对象
        self.destroy_images = list(map(lambda img: pygame.image.load(img), self.destroy_images_src))
        # 初始化子弹
        self.bullets = pygame.sprite.Group()
        # 初始化飞机位置
        self.rect = self.images[0].get_rect()
        # 血量
        self.blood = self.max_blood
        # 是否被击中
        self.hit = False
        # 初始化位置信息
        self.init_rect()

    def init_rect(self):
        """ 初始化位置信息 """
        pass

    def reset(self):
        """ 复用 """
        self.active = True
        self.hit = False
        self.blood = self.max_blood
        self.init_rect()

    def get_screen_size(self):
        return self.screen.get_size()

    def hurt(self, war, power=1):
        """ 被伤害 """
        self.hit = True
        self.blood -= power
        if self.blood <= 0:
            self.destroy(war)  # 坠机
            war.result.set_history()  # 记录最高分

    def destroy(self, war):
        """ 坠机 """
        self.active = False
        # 清空子弹
        self.bullets.empty()
        if self.destroy_sound_src:
            sound = pygame.mixer.Sound(self.destroy_sound_src)
            sound.play()
        # 这里是多张爆炸图片在同一帧渲染
        for image in self.destroy_images:
            self.screen.blit(image, self.rect)

    def update(self, war):
        """游戏循环"""
        self.bind_event(war.down_key)  # 绑定事件
        self.render(war)  # 渲染视图
        self.bullets.update(war)  # 更新子弹

    def bind_event(self, down_key):
        """ 绑定事件 """
        pass

    def render(self, war):
        self.screen.blit(self.images[0], self.rect)

    def move_up(self):
        """向上移动"""
        self.rect = self.rect.move(0, -self.speed)
        self.rect.top = max(0, self.rect.top)

    def move_down(self):
        """向下移动"""
        self.rect = self.rect.move(0, self.speed)
        self.rect.bottom = min(self.rect.bottom, self.get_screen_size()[1])

    def move_left(self):
        """ 向左移动 """
        self.rect = self.rect.move(-self.speed, 0)
        self.rect.left = max(0, self.rect.left)

    def move_right(self):
        """ 向右移动 """
        self.rect = self.rect.move(self.speed, 0)
        self.rect.right = min(self.rect.right, self.get_screen_size()[0])




