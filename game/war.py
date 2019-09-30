import sys, pygame
import constants
from game.enemey import SmallEnemyPlane
from game.myplane import MyPlane


class War(object):

    READY = 'ready'
    PLAYING = 'playing'
    OVER = 'over'
    # 背景图片
    bg_img = pygame.image.load(constants.BG_IMG)
    bg_over_img = pygame.image.load(constants.BG_OVER_IMG)
    # clock对象
    clock = pygame.time.Clock()

    def __init__(self, size=constants.SCREEN_SIZE):
        # 游戏状态
        self.state = self.READY
        # 游戏界面
        self.screen = pygame.display.set_mode(size)
        # 我的飞机
        self.plane = MyPlane(self.screen)
        # 敌机
        self.enemies = pygame.sprite.Group()
        # 计数器
        self.times = 0
        # 按下的键盘
        self.down_key = None

    def start(self):
        """ 开始游戏 """
        # 游戏初始化
        pygame.init()
        # 背景音乐
        self.start_music()
        # 循环渲染
        self.update()

    def add_small_enemy(self, num):
        """ 添加小型敌机 """
        for i in range(num):
            self.enemies.add(SmallEnemyPlane(self.screen, 10))

    @staticmethod
    def start_music():
        """ 背景音乐 """
        pygame.mixer.music.load(constants.BG_MUSIC)
        # 设置音量
        pygame.mixer.music.set_volume(0.2)
        # 循环播放
        pygame.mixer.music.play(-1)

    def bind_event(self):
        """ 事件监听 """
        # 只在一处遍历pygame.event.get()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.down_key = event.key
            elif event.type == pygame.KEYUP and event.key == self.down_key:
                self.down_key = None

    def update(self):
        """ 游戏循环 """
        while True:
            # 设置动画帧数
            self.clock.tick(60)
            # 先绑定事件再绘制视图
            self.bind_event()
            # 更新计数器
            self.update_count()
            # 每次循环都要重新添加事件监听
            # 绘制背景图片
            self.screen.blit(self.bg_img, self.screen.get_rect())
            # 我的飞机刷新
            self.plane.update(self)
            # 敌机刷新
            self.enemies.update(self)
            print(self.enemies)
            # 刷新界面
            pygame.display.flip()

    def update_count(self):
        """ 更新计数器 """
        self.times += 1
        if self.times > 1000:
            self.times = 0
