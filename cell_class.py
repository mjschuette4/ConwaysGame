import pygame, random

class Cell:
    def __init__(self, surface, grid_x, grid_y):
        self.alive = False
        self.surface = surface
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.image = pygame.Surface((20, 20))
        self.rect = self.image.get_rect()
        self.neighbors = []

    def update(self):
        self.rect.topleft = (self.grid_x*20, self.grid_y*20)

    def draw(self):
        if self.alive:
            self.image.fill((0, 0, 0))
        else:
            self.image.fill((0, 0, 0))
            pygame.draw.rect(self.image, (255, 255, 255), (1, 1, 16, 16))
        self.surface.blit(self.image, (self.grid_x*20, self.grid_y*20))

    def get_neighbors(self, grid):
        neighbor_list = [[1,1],[-1,-1],[1,-1],[0,-1],[1,0],[-1,0]]
        for neighbor in neighbor_list:
            neighbor[0] += self.grid_x
            neighbor[1] += self.grid_y
        for neighbor in neighbor_list:
            if neighbor[0] < 0:
                neighbor[0] += 30
            if neighbor[1] < 0:
                neighbor[1] += 30
            if neighbor[1] > 29:
                neighbor[1] -= 30
            if neighbor[0] > 29:
                neighbor[0] -= 30
        for neighbor in neighbor_list:
            try:
                self.neighbors.append(grid[neighbor[1]][neighbor[0]])
            except:
                print(neighbor)
                


