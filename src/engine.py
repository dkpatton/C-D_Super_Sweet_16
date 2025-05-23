"""Core game engine for Sweet 16 Retro Game."""

from __future__ import annotations

from enum import Enum, auto

import pygame

from .utils import load_sprite, load_sound


class GameState(Enum):
    """Possible states of the game."""

    MENU = auto()
    PLAYING = auto()
    PAUSED = auto()
    QUIT = auto()


class GameEngine:
    """Main game engine managing the loop and state."""

    WIDTH = 800
    HEIGHT = 600
    FPS = 60

    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Sweet 16 Retro Game")
        self.clock = pygame.time.Clock()

        self.state = GameState.MENU
        self.running = True

        self.font = pygame.font.Font(None, 36)
        self.sprite = load_sprite("player.png")
        self.sound = load_sound("start.wav")

    # ------------------------------------------------------------------
    # Game loop
    # ------------------------------------------------------------------
    def run(self) -> None:
        """Run the main game loop."""

        while self.state != GameState.QUIT:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.FPS)

        pygame.quit()

    # ------------------------------------------------------------------
    # Event handling
    # ------------------------------------------------------------------
    def handle_events(self) -> None:
        """Process input events."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = GameState.QUIT
            elif event.type == pygame.KEYDOWN:
                self._handle_key(event.key)

    def _handle_key(self, key: int) -> None:
        if self.state == GameState.MENU:
            if key in (pygame.K_RETURN, pygame.K_SPACE):
                self.state = GameState.PLAYING
                if self.sound:
                    self.sound.play()
            elif key == pygame.K_ESCAPE:
                self.state = GameState.QUIT

        elif self.state == GameState.PLAYING:
            if key == pygame.K_ESCAPE:
                self.state = GameState.PAUSED
            elif key == pygame.K_q:
                self.state = GameState.QUIT

        elif self.state == GameState.PAUSED:
            if key == pygame.K_ESCAPE:
                self.state = GameState.PLAYING
            elif key == pygame.K_q:
                self.state = GameState.QUIT

    # ------------------------------------------------------------------
    # Update & Render
    # ------------------------------------------------------------------
    def update(self) -> None:
        """Update game state. Placeholder for future logic."""
        pass

    def render(self) -> None:
        """Render the current game state."""

        self.screen.fill((0, 0, 0))

        if self.state == GameState.MENU:
            text = self.font.render("Press Space to Start", True, (255, 255, 255))
            rect = text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
            self.screen.blit(text, rect)
        elif self.state == GameState.PLAYING:
            rect = self.sprite.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
            self.screen.blit(self.sprite, rect)
        elif self.state == GameState.PAUSED:
            pause = self.font.render("Paused - Esc to Resume", True, (255, 255, 255))
            rect = pause.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
            self.screen.blit(pause, rect)

        pygame.display.flip()

