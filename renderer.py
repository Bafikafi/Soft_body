import pygame


class renderer:
    @staticmethod
    def render_debug(display: pygame.display, objs):
        if type(objs) != list:
            pygame.draw.circle(
                display, color=(255, 0, 0), center=(objs.x, objs.y), radius=5
            )
            return

        for obj in objs:
            pygame.draw.circle(
                display, color=(255, 0, 0), center=(obj.x, obj.y), radius=5
            )

    @staticmethod
    def redner_edge_debug(display: pygame.display, objs):
        if type(objs) != list:
            a_position = (objs.vertex_a.x, objs.vertex_a.y)
            b_position = (objs.vertex_b.x, objs.vertex_b.y)
            pygame.draw.line(display, (0, 255, 0), a_position, b_position)
# helo