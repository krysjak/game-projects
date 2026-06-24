import pygame
import random
import math
import sys

# Ініціалізація Pygame
pygame.init()

# Параметри екрану
WIDTH = 1200
HEIGHT = 800
FPS = 60

# Кольори
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (255, 100, 150),      # Рожевий
    (100, 200, 255),      # Блакитний
    (255, 200, 100),      # Оранжевий
    (150, 100, 255),      # Фіолетовий
    (100, 255, 150),      # Зелений
    (255, 100, 100),      # Червоний
    (255, 255, 100),      # Жовтий
    (200, 150, 255),      # Лавандовий
    (100, 255, 255),      # Ціан
    (255, 150, 200),      # Рожевий 2
]

# Структурні точки дерева (невидимі атрактори)
class TreeNode:
    def __init__(self, x, y, depth=0):
        self.x = x
        self.y = y
        self.depth = depth
        self.children = []
        self.strength = 1.0 + depth * 0.1  # Сильніші глибокі вузли

# Клас для точки (людини)
class Point:
    def __init__(self, x, y, wave_number, color):
        self.x = x
        self.y = y
        self.wave = wave_number
        self.vx = random.uniform(-0.5, 0.5)
        self.vy = random.uniform(-0.5, 0.5)
        self.point_size = 4
        self.color = color
        self.trail = []
        self.trail_length = 10
        self.mass = 1
        self.age = 0
        
    def update(self, all_points, tree_nodes):
        self.age += 1
        
        # Притягання до вузлів дерева (ГОЛОВНЕ!)
        for node in tree_nodes:
            dx = node.x - self.x
            dy = node.y - self.y
            distance = math.sqrt(dx**2 + dy**2) + 0.1
            
            if distance > 0.1:
                # Сила залежить від того на якій глибині вузол
                force = (node.strength * 100) / (distance ** 1.5)
                force *= 0.0002
                
                ax = (dx / distance) * force
                ay = (dy / distance) * force
                
                self.vx += ax
                self.vy += ay
        
        # Гравітаційна взаємодія з іншими людьми (слабка)
        for point in all_points:
            if point is self:
                continue
            
            dx = point.x - self.x
            dy = point.y - self.y
            distance = math.sqrt(dx**2 + dy**2) + 0.1
            
            if distance > 0.1 and distance < 200:
                force = (self.mass * point.mass) / (distance ** 2)
                force *= 0.00002
                
                ax = (dx / distance) * force
                ay = (dy / distance) * force
                
                self.vx += ax
                self.vy += ay
        
        # Рух з демпуванням
        self.x += self.vx
        self.y += self.vy
        self.vx *= 0.998
        self.vy *= 0.998
        
        # Обмежуємо екран
        if self.y < -400:
            self.y = -400
            self.vy = 0
        
        # Додаємо до сліду
        self.trail.append((self.x, self.y))
        if len(self.trail) > self.trail_length:
            self.trail.pop(0)
    
    def draw(self, surface, camera_x, camera_y, zoom):
        screen_x = (self.x - camera_x) * zoom + WIDTH // 2
        screen_y = (self.y - camera_y) * zoom + HEIGHT // 2
        
        if -50 > screen_x or screen_x > WIDTH + 50:
            return
        if -50 > screen_y or screen_y > HEIGHT + 50:
            return
        
        # Малюємо слід
        if len(self.trail) > 1:
            for i in range(len(self.trail) - 1):
                x1, y1 = self.trail[i]
                sx1 = (x1 - camera_x) * zoom + WIDTH // 2
                sy1 = (y1 - camera_y) * zoom + HEIGHT // 2
                sx2 = (self.trail[i+1][0] - camera_x) * zoom + WIDTH // 2
                sy2 = (self.trail[i+1][1] - camera_y) * zoom + HEIGHT // 2
                
                pygame.draw.line(surface, self.color, (int(sx1), int(sy1)), (int(sx2), int(sy2)), 1)
        
        # Малюємо точку
        size = max(2, int(self.point_size * zoom))
        pygame.draw.circle(surface, self.color, (int(screen_x), int(screen_y)), size)
        pygame.draw.circle(surface, WHITE, (int(screen_x), int(screen_y)), size, 1)

# Головна гра
class TreeOfLifeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("ДЕРЕВО ЖИТТЯ 🌳 - Люди Утворюють Форму")
        self.clock = pygame.time.Clock()
        self.font_big = pygame.font.Font(None, 56)
        self.font_small = pygame.font.Font(None, 20)
        self.font_tiny = pygame.font.Font(None, 16)
        
        self.points = []
        self.tree_nodes = []
        self.create_tree_structure()
        
        self.wave = 0
        self.wave_timer = 0
        self.wave_duration = 60 * FPS
        
        self.game_time = 0
        self.running = True
        
        # Камера
        self.camera_x = 0
        self.camera_y = -200
        self.zoom = 1.0
        self.min_zoom = 0.3
        self.max_zoom = 3.0
        
        # Для руху мишею
        self.dragging = False
        self.last_mouse_x = 0
        self.last_mouse_y = 0
        
        # Космос - зірки
        self.stars = self.generate_stars()
        
        self.add_initial_point()
    
    def create_tree_structure(self):
        """Створюємо структуру вузлів дерева (невидима архітектура)"""
        # Коріння (внизу)
        root = TreeNode(0, 200, 0)
        self.tree_nodes.append(root)
        
        # Стовбур (вгору)
        trunk = TreeNode(0, 0, 1)
        self.tree_nodes.append(trunk)
        
        # Великі гілки (розходяться)
        for angle in [-math.pi/4, math.pi/4]:
            branch = TreeNode(150 * math.cos(angle), -150 * math.sin(angle), 2)
            self.tree_nodes.append(branch)
            
            # Малі гілочки від великих гілок
            for sub_angle in [-math.pi/6, math.pi/6]:
                total_angle = angle + sub_angle
                sub_branch = TreeNode(
                    300 * math.cos(total_angle), 
                    -300 * math.sin(total_angle),
                    3
                )
                self.tree_nodes.append(sub_branch)
                
                # Листки (мальюки гілочки)
                for leaf_angle in [-math.pi/8, math.pi/8]:
                    total_leaf_angle = total_angle + leaf_angle
                    leaf = TreeNode(
                        400 * math.cos(total_leaf_angle),
                        -400 * math.sin(total_leaf_angle),
                        4
                    )
                    self.tree_nodes.append(leaf)
    
    def generate_stars(self):
        """Генеруємо зірки"""
        stars = []
        for _ in range(1000):
            x = random.uniform(-3000, 3000)
            y = random.uniform(-2000, 2000)
            brightness = random.randint(50, 200)
            size = random.randint(1, 3)
            stars.append((x, y, brightness, size))
        return stars
    
    def draw_cosmos(self):
        """Малюємо космос"""
        self.screen.fill(BLACK)
        
        for x, y, brightness, size in self.stars:
            screen_x = (x - self.camera_x) * self.zoom + WIDTH // 2
            screen_y = (y - self.camera_y) * self.zoom + HEIGHT // 2
            
            if -50 < screen_x < WIDTH + 50 and -50 < screen_y < HEIGHT + 50:
                color = (brightness, brightness, brightness)
                pygame.draw.circle(self.screen, color, (int(screen_x), int(screen_y)), size)
    
    def add_initial_point(self):
        """Додаємо першу людину"""
        self.wave = 1
        # Випадкова позиція біля екрану
        angle = random.uniform(0, 2 * math.pi)
        radius = 800
        x = math.cos(angle) * radius
        y = -400 + math.sin(angle) * radius
        
        point = Point(x, y, self.wave, random.choice(COLORS))
        self.points.append(point)
    
    def add_wave_points(self):
        """Додаємо нові точки поступово"""
        if self.wave_timer > 0 and self.wave_timer % 60 == 0:
            for _ in range(3):  # 3 точки за секунду
                angle = random.uniform(0, 2 * math.pi)
                radius = random.uniform(600, 1000)
                x = math.cos(angle) * radius
                y = -400 + math.sin(angle) * radius
                
                point = Point(x, y, self.wave, random.choice(COLORS))
                self.points.append(point)
    
    def draw_connections(self):
        """Малюємо лінії між людьми що близько одна до одної"""
        max_distance = 100
        
        for i, point1 in enumerate(self.points):
            for point2 in self.points[i + 1:]:
                dx = point1.x - point2.x
                dy = point1.y - point2.y
                distance = math.sqrt(dx**2 + dy**2)
                
                if distance < max_distance:
                    sx1 = (point1.x - self.camera_x) * self.zoom + WIDTH // 2
                    sy1 = (point1.y - self.camera_y) * self.zoom + HEIGHT // 2
                    sx2 = (point2.x - self.camera_x) * self.zoom + WIDTH // 2
                    sy2 = (point2.y - self.camera_y) * self.zoom + HEIGHT // 2
                    
                    # Золотий колір для лінії
                    alpha = int(100 * (1 - distance / max_distance))
                    color = (min(255, 200 + alpha), min(255, 200 + alpha // 2), 0)
                    
                    pygame.draw.line(self.screen, color, 
                                   (int(sx1), int(sy1)),
                                   (int(sx2), int(sy2)), 1)
    
    def draw_tree_structure(self):
        """Малюємо деревовидну структуру вузлів (для показу)"""
        for node in self.tree_nodes:
            screen_x = (node.x - self.camera_x) * self.zoom + WIDTH // 2
            screen_y = (node.y - self.camera_y) * self.zoom + HEIGHT // 2
            
            # Маленькі світлі точки для вузлів
            size = int(2 + node.depth * 0.5)
            pygame.draw.circle(self.screen, (100, 150, 100), (int(screen_x), int(screen_y)), size)
    
    def draw_info(self):
        """Малюємо інформацію"""
        # Заголовок
        title_text = self.font_big.render("ДЕРЕВО ЖИТТЯ 🌳", True, (0, 200, 50))
        self.screen.blit(title_text, (WIDTH // 2 - 250, 20))
        
        # Статистика
        people_text = self.font_small.render(f"Люди: {len(self.points)}", True, WHITE)
        self.screen.blit(people_text, (20, 100))
        
        # Послання
        msg1 = self.font_small.render("Люди самі утворюють форму дерева! 🌳", True, (100, 200, 255))
        self.screen.blit(msg1, (WIDTH // 2 - 250, HEIGHT - 60))
        
        msg2 = self.font_tiny.render("Вони притягуються невидимою структурою й створюють живе дерево", True, (200, 150, 255))
        self.screen.blit(msg2, (WIDTH // 2 - 350, HEIGHT - 30))
    
    def handle_events(self):
        """Обробка подій"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            
            # Масштабування
            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    self.zoom *= 1.1
                    self.zoom = min(self.max_zoom, self.zoom)
                elif event.y < 0:
                    self.zoom *= 0.9
                    self.zoom = max(self.min_zoom, self.zoom)
            
            # ПКМ - рух камери
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    self.dragging = True
                    self.last_mouse_x, self.last_mouse_y = event.pos
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    self.dragging = False
            
            if event.type == pygame.MOUSEMOTION:
                if self.dragging:
                    mouse_x, mouse_y = event.pos
                    dx = (mouse_x - self.last_mouse_x) / self.zoom
                    dy = (mouse_y - self.last_mouse_y) / self.zoom
                    
                    self.camera_x -= dx
                    self.camera_y -= dy
                    
                    self.last_mouse_x = mouse_x
                    self.last_mouse_y = mouse_y
    
    def update(self):
        """Оновлення логіки"""
        self.game_time += 1
        self.wave_timer += 1
        
        # Додаємо нові люди
        self.add_wave_points()
        
        # Оновляємо людей - вони притягуються до вузлів дерева!
        for point in self.points:
            point.update(self.points, self.tree_nodes)
        
        # Нова хвиля
        if self.wave_timer >= self.wave_duration:
            self.wave += 1
            self.wave_timer = 0
    
    def draw(self):
        """Малюємо все"""
        self.draw_cosmos()
        
        # Малюємо невидимої деревовидну структуру (крім точок)
        # self.draw_tree_structure()  # Закоментовано для прихованої архітектури
        
        # Малюємо лінії між близькими людьми
        self.draw_connections()
        
        # Малюємо людей (вони САМИ утворюють дерево!)
        for point in self.points:
            point.draw(self.screen, self.camera_x, self.camera_y, self.zoom)
        
        # Малюємо інформацію
        self.draw_info()
        
        pygame.display.flip()
    
    def run(self):
        """Головний цикл"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

# Запуск гри
if __name__ == "__main__":
    game = TreeOfLifeGame()
    game.run()
