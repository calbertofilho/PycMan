from os import environ as environment, path, getcwd
from sys import exit
import pygame

class Game:
    '''Função de inicialização de todas as bibliotecas do jogo'''
    def __init__(self):
        environment['SDL_VIDEO_CENTERED'] = '1'                                                                     # Centraliza a janela no monitor
        pygame.init()                                                                                               # Inicia a biblioteca PyGame
        pygame.font.init()                                                                                          # Inicia a biblioteca de manipulação de fonts do PyGame
        pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512)                             # Inicia a biblioteca de manipulação de áudio do PyGame
        self.running = True                                                                                         # Flag que sinaliza a execução do jogo
        self.playing = False                                                                                        # Flag que sinaliza se está no play do jogo
        self.UP_KEY      = False                                                                                    # Flag que sinaliza que a tecla ↑ foi pressionada
        self.DOWN_KEY    = False                                                                                    # Flag que sinaliza que a tecla ↓ foi pressionada
        self.LEFT_KEY    = False                                                                                    # Flag que sinaliza que a tecla ← foi pressionada
        self.RIGHT_KEY   = False                                                                                    # Flag que sinaliza que a tecla → foi pressionada
        self.CONFIRM_KEY = False                                                                                    # Flag que sinaliza que a tecla «Enter» foi pressionada
        self.CANCEL_KEY  = False                                                                                    # Flag que sinaliza que a tecla «Esc» foi pressionada
        self.BACK_KEY    = False                                                                                    # Flag que sinaliza que a tecla «Backspace» foi pressionada
        self.JUMP_KEY    = False                                                                                    # Flag que sinaliza que a tecla «Ctrl» foi pressionada
        self.ACTION_KEY  = False                                                                                    # Flag que sinaliza que a tecla «Space» foi pressionada
        self.DISPLAY_WIDTH = 640                                                                                    # Comprimento da janela
        self.DISPLAY_HEIGHT = 480                                                                                   # Altura da janela
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.font_name = ""
        self.display = pygame.Surface((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))                                    # Canvas
        self.window = pygame.display.set_mode(((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT)))                          # Janela
        icon = pygame.image.load(path.join(path.join(getcwd(), 'resources/images'), 'icon.png')).convert_alpha()    # Imagem com o ícone do jogo
        pygame.display.set_icon(icon)                                                                               # Seta como ícone na janela do jogo
        pygame.display.set_caption('PycMan v1.0')                                                                   # Título da janela do jogo

    '''Função que controla o loop do jogo'''
    def game_loop(self):
        while self.playing:
            self.handle_events()
            if self.CONFIRM_KEY:
                self.playing = False
            elif self.CANCEL_KEY:
                self.close_game()
            self.display.fill(self.BLACK)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()

    '''Função que manipula os eventos de teclado'''
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_game()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    self.UP_KEY = True
                if event.key in (pygame.K_DOWN, pygame.K_s):
                    self.DOWN_KEY = True
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    self.LEFT_KEY = True
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    self.RIGHT_KEY = True
                if event.key == pygame.K_RETURN:
                    self.CONFIRM_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.CANCEL_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_SPACE:
                    self.JUMP_KEY = True
                if event.key in (pygame.K_LCTRL, pygame.K_RCTRL):
                    self.ACTION_KEY = True
            if event.type == pygame.KEYUP:
                self.reset_keys()

    '''Função que limpa o estado de todas as teclas do teclado'''
    def reset_keys(self):
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.LEFT_KEY = False
        self.RIGHT_KEY = False
        self.CONFIRM_KEY = False
        self.CANCEL_KEY = False
        self.BACK_KEY = False
        self.JUMP_KEY = False
        self.ACTION_KEY = False

    '''Função que encerra todas as bibliotecas e fecha o jogo'''
    def close_game(self):
        self.running = False
        self.playing = False
        pygame.display.quit()
        pygame.mixer.quit()
        pygame.quit()
        exit()
