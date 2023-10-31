import pygame
import random
import math

pygame.init()

BACKGROUND_COLOR = (135, 206, 250)
PARTICLE_COLOR = (65, 105, 225, 100)  # Semi-transparent blue particles
PARTICLE_RADIUS = 5
NUM_PARTICLES = 100
PARTICLE_SPEED = 2
INTERACTION_RADIUS = 2 * PARTICLE_RADIUS  # Interaction radius is twice the particle radius

scrn_wd = 800
scrn_h = 600
screen = pygame.display.set_mode((scrn_wd, scrn_h))
pygame.display.set_caption("Ideal Gas simulator")

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-PARTICLE_SPEED, PARTICLE_SPEED)
        self.vy = random.uniform(-PARTICLE_SPEED, PARTICLE_SPEED)

    def update(self):
        self.x += self.vx
        self.y += self.vy

        if self.x < 0 or self.x > scrn_wd:
            self.vx *= -1

        if self.y < 0 or self.y > scrn_h:
            self.vy *= -1

    def draw(self):
        pygame.draw.circle(screen, PARTICLE_COLOR, (int(self.x), int(self.y)), PARTICLE_RADIUS)

def elastic_collision(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    distance = math.sqrt(dx**2 + dy**2)

    if distance < INTERACTION_RADIUS:
        angle = math.atan2(dy, dx)
        v1 = math.sqrt(p1.vx**2 + p1.vy**2)
        v2 = math.sqrt(p2.vx**2 + p2.vy**2)
        phi1 = math.atan2(p1.vy, p1.vx)
        phi2 = math.atan2(p2.vy, p2.vx)

        new_v1 = (v1 * math.cos(phi1 - angle) * (1 - 1) + 2 * 1 * v2 * math.cos(phi2 - angle)) / (1 + 1)
        new_v2 = (v2 * math.cos(phi2 - angle) * (1 - 1) + 2 * 1 * v1 * math.cos(phi1 - angle)) / (1 + 1)

        p1.vx = new_v1 * math.cos(angle) + v1 * math.sin(phi1 - angle) * math.cos(angle + math.pi / 2)
        p1.vy = new_v1 * math.sin(angle) + v1 * math.sin(phi1 - angle) * math.sin(angle + math.pi / 2)
        p2.vx = new_v2 * math.cos(angle) + v2 * math.sin(phi2 - angle) * math.cos(angle + math.pi / 2)
        p2.vy = new_v2 * math.sin(angle) + v2 * math.sin(phi2 - angle) * math.sin(angle + math.pi / 2)

particles = [Particle(random.randint(0, scrn_wd), random.randint(0, scrn_h)) for _ in range(NUM_PARTICLES)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(NUM_PARTICLES):
        for j in range(i + 1, NUM_PARTICLES):
            elastic_collision(particles[i], particles[j])

    screen.fill(BACKGROUND_COLOR)

    for particle in particles:
        particle.update()
        particle.draw()

    pygame.display.update()

pygame.quit()

