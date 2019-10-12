import sys, pygame
import constants
from game.enemey import SmallEnemyPlane
from game.myplane import MyPlane
from store.result import PlayResult


class War(object):

    READY = 'ready'
    PLAYING = 'playing'
    OVER = 'over'
    # 背景图片
    bg_img = pygame.image.load(constants.BG_IMG)
    bg_over_img = pygame.image.load(constants.BG_OVER_IMG)
    # 标题图片
    title_img = pygame.image.load(constants.IMG_GAME_TITLE)
    # 开始按钮图片
    start_img = pygame.image.load(constants.IMG_GAME_START_BTN)
    # clock对象
    clock = pygame.time.Clock()
    # 游戏字体
    font = None

    @staticmethod
    def start_music():
        """ 背景音乐 """
        pygame.mixer.music.load(constants.BG_MUSIC)
        # 设置音量
        pygame.mixer.music.set_volume(0)
        # 循环播放
        pygame.mixer.music.play(-1)

    def __init__(self, size=constants.SCREEN_SIZE):
        # 游戏状态
        self.state = self.READY
        # 游戏界面
        self.screen = pygame.display.set_mode(size)
        # 我的飞机
        self.plane = MyPlane(self.screen, 20)
        # 敌机
        self.enemies = pygame.sprite.Group()
        # 计数器
        self.times = 0
        # 按下的键盘
        self.down_key = None
        # 游戏结果
        self.result = PlayResult()

    def add_score(self, count):
        self.result.score += count

    def start(self):
        """ 开始游戏 """
        # 游戏初始化
        pygame.init()
        # 背景音乐
        self.start_music()
        # 游戏字体(需要pygame.init())
        self.font = pygame.font.Font(constants.FONT, 32)
        # 循环渲染
        self.update()

    def add_small_enemy(self, num):
        """ 添加小型敌机 """
        for i in range(num):
            self.enemies.add(SmallEnemyPlane(self.screen, 10))

    def bind_event(self):
        """ 事件监听 """
        # 只在一处遍历pygame.event.get()
        for event in pygame.event.get():
            # 与游戏状态无关事件
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.down_key = event.key
            elif event.type == pygame.KEYUP and event.key == self.down_key:
                self.down_key = None
            # 与游戏状态有关事件
            if self.state == self.READY:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.state = self.PLAYING
                    self.add_small_enemy(6)
            elif self.state == self.OVER:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.state = self.READY

    def update(self):
        """ 游戏循环 """
        while True:
            # 设置动画帧数
            self.clock.tick(60)
            # 更新计数器
            self.update_count()
            self.bind_event()
            if self.state == self.READY:
                # 绘制背景图片
                self.screen.blit(self.bg_img, self.screen.get_rect())
                # 渲染标题
                self.screen.blit(self.title_img, self.title_rect)
                # 渲染开始按钮
                self.screen.blit(self.start_img, self.start_rect)
            elif self.state == self.PLAYING:
                # 绘制背景图片
                self.screen.blit(self.bg_img, self.screen.get_rect())
                # 我的飞机刷新
                self.plane.update(self)
                # 敌机刷新
                self.enemies.update(self)
                # 绘制分数
                self.blit_score()
            elif self.state == self.OVER:
                # 绘制背景
                self.screen.blit(self.bg_over_img, self.screen.get_rect())
                # 绘制本地总分
                self.blit_over_score()
                # 绘制游戏最高分
                self.blit_max_score()
            # 刷新界面
            pygame.display.flip()

    @property
    def title_rect(self):
        rect = self.title_img.get_rect()
        width, height = self.screen.get_size()
        rect.centerx = int(width / 2)
        rect.bottom = int(height / 2)
        return rect

    @property
    def start_rect(self):
        rect = self.start_img.get_rect()
        width, height = self.screen.get_size()
        rect.centerx = int(width / 2)
        rect.top = int(height / 2) + 30
        return rect

    def update_count(self):
        """ 更新计数器 """
        self.times += 1
        if self.times > 1000:
            self.times = 0

    def blit_score(self):
        """绘制游戏运行时得分"""
        score_text = self.font.render(
            "得分: {}".format(self.result.score),
            False,
            constants.SCORE_COLOR
        )
        self.screen.blit(score_text, score_text.get_rect())

    def blit_max_score(self):
        """ 绘制游戏最高分 """
        score_text = self.font.render(
            "最高分: {}".format(self.result.max_score()),
            False,
            constants.SCORE_COLOR
        )
        self.screen.blit(score_text, (150, 40))

    def blit_over_score(self):
        """绘制游戏结束时得分"""
        score_text = self.font.render(
            "本次得分: {}".format(self.result.score),
            False,
            constants.SCORE_COLOR
        )
        score_rect = score_text.get_rect()
        width, height = self.screen.get_size()
        score_rect.centerx = int(width / 2)
        score_rect.centery = int(height / 2)
        self.screen.blit(score_text, score_rect)
