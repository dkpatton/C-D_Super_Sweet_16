"""Entry point for Sweet 16 Retro Game."""

from src.engine import GameEngine


def main() -> None:
    """Run the main game loop."""
    engine = GameEngine()
    engine.run()


if __name__ == "__main__":
    main()
