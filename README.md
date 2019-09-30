## 项目名称
飞机大战
## 代码细节
1. 事件监听放在循环之内
2. event.type表示事件类型，event.key表示哪个键
3. 只在一处遍历事件
  for event in pygame.event.get():
4. 创建一个精灵组
  pygame.sprite.Group()
5. 调用精灵组的update方法，会调用精灵组内每个精灵的update方法
注意:必须是update方法。
6. pygame.sprite.Sprite子类的构造方法需要调用super().__init__() 