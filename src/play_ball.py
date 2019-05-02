import pygame

from src.ball import Ball
from src.key_states import KeyStates


pygame.init()


# constants
SCREEN_SIZE = (1500, 600)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BALL_EDGE_WIDTH = 0


# soundz
pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 1024)  # not janky at all :)
splat_sound = pygame.mixer.Sound('../assets/splat.ogg')


def main():
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    ball = Ball(
        x=int(SCREEN_SIZE[0] / 2) - 20,
        y=40,
        speed_x=0,
        speed_y=0,
        color=WHITE
    )
    key_states = KeyStates()
    MIN_X = 0 + ball.width
    MAX_X = SCREEN_SIZE[0] - ball.width
    MAX_Y = SCREEN_SIZE[1] - ball.height
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    key_states.key_states['R'] = True
                if event.key == pygame.K_LEFT:
                    key_states.key_states['L'] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    key_states.key_states['R'] = False
                if event.key == pygame.K_LEFT:
                    key_states.key_states['L'] = False

        screen.fill(BLACK)
        if key_states.key_states['R']:
            ball.update_speed_x(speed_x=ball.speed_x + 1)
        if key_states.key_states['L']:
            ball.update_speed_x(speed_x=ball.speed_x - 1)
        if not key_states.key_states['R'] and ball.speed_x > 0:
            ball.update_speed_x(speed_x=ball.speed_x - 1)
        if not key_states.key_states['L'] and ball.speed_x < 0:
            ball.update_speed_x(speed_x=ball.speed_x + 1)
        if ball.x < MIN_X:
            ball.x = MIN_X
            ball.speed_x *= -1
            splat_sound.play()
        if ball.x > MAX_X:
            ball.x = MAX_X
            ball.speed_x *= -1
            splat_sound.play()
        if ball.y > MAX_Y:
            ball.y = MAX_Y
            ball.speed_y *= -1
        ball.update_speed_y(ball.speed_y + 1)
        ball.update_position()
        pygame.draw.ellipse(
            screen,
            ball.color,
            [ball.x, ball.y, ball.width, ball.height],
            BALL_EDGE_WIDTH
        )
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == '__main__':
    main()
