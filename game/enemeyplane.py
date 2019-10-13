import random

from game.plane import Plane


class EnemyPlane(Plane):

    def init_rect(self):
        self.rect.bottom = random.randint(-self.rect.height * 5, 0)
        self.rect.left = random.randint(0, self.screen.get_width() - self.rect.width)

    def render(self, war):
        """ 渲染视图 """
        self.down_move()
        self.blit_image(war)

    def down_move(self):
        """ 向下移动 """
        self.rect.bottom += self.speed
        if self.rect.top > self.screen.get_height():
            self.reset()

    def blit_image(self, war):
        self.screen.blit(self.images[0], self.rect)

    def destroy(self, war):
        """ 坠毁 """
        super().destroy(war)
        self.reset()
        # 得分
        war.add_score(self.blood * 10)
        # 添加敌机
        war.add_enemy()
