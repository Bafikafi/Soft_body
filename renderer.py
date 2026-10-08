import pygame


class renderer:
    @staticmethod
    def render(display: pygame.display, obj):
        pygame.draw.circle(display, color=(255, 0, 0), center=(obj.x, obj.y), radius=5)
