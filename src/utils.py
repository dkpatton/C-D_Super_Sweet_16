"""Utility functions for Sweet 16 Retro Game."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

import numpy as np
import pygame


ASSET_DIR = Path(__file__).resolve().parent.parent / "assets"


def load_sprite(name: str) -> pygame.Surface:
    """Load a sprite image.

    If the sprite cannot be found, return a placeholder surface.
    """
    path = ASSET_DIR / "sprites" / name
    if path.is_file():
        return pygame.image.load(path.as_posix()).convert_alpha()

    surface = pygame.Surface((32, 32))
    surface.fill((255, 0, 255))
    return surface


def load_sound(name: str) -> Optional[pygame.mixer.Sound]:
    """Load a sound effect or return a generated beep."""

    path = ASSET_DIR / "audio" / name
    if path.is_file():
        try:
            return pygame.mixer.Sound(path.as_posix())
        except pygame.error:
            pass

    # Fall back to a short generated beep if the file does not exist
    sample_rate = 44100
    duration = 0.25
    freq = 440
    t = np.linspace(0.0, duration, int(sample_rate * duration), False)
    tone = np.sin(freq * t * 2 * np.pi)
    waveform = np.array([tone, tone]).T * 32767
    return pygame.sndarray.make_sound(waveform.astype(np.int16))

