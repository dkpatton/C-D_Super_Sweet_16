# Sweet 16 Retro Game

A retro-style 8-bit game built in Python to celebrate Dave and Christine’s 16th anniversary. Traverse eight milestone-based levels—each inspired by a moment in their relationship—and face the final ‘Homeschooling Chaos’ boss.

---

## Table of Contents

1. [Features](#features)
2. [Levels](#levels)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Contributing](#contributing)
7. [License](#license)

---

## Features

* **Retro 8-bit Graphics:** Pixel-art aesthetic reminiscent of NES/SNES era.
* **Python-Powered:** Built using [Pygame](https://www.pygame.org/) (or [Arcade](https://api.arcade.academy/)) for simplicity.
* **Diverse Gameplay:** Stealth, platforming, puzzles, time-management, and mini-games.
* **Nostalgic Soundtrack:** Chiptune tracks matching each level’s theme.

---

## Levels

### Level 1

1. **MySpace & AIM Chat**: Reconstruct chat logs to progress.
2. **DMB Concert Sneak**: Stealth through a crowd to reach front row.
3. **Halloween Night (Saw Theme)**: Solve memory riddles in a puzzle escape.

### Level 2

4. **Moving to Long Beach**: Side-scrolling drive through a storm and desert detour, ending back home.
5. **College in Sacramento**: Time-management or maze mini-game simulating college life.
6. **Wedding at Muir Beach**: Platform/puzzle assembly of wedding decor and vows.

### Level 3

7. **Buying First House**: Tetris-like furniture fitting and negotiation puzzles.
8. **Family & Homeschool**: Rhythm parenting mini-game and tower-defense-style learning challenges.

**Final Boss:** ‘Homeschooling Chaos’—cross rivers, dodge interruptions, and defeat the Chaos Beast of schedules and pop quizzes.

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/sweet-16-retro-game.git
   cd sweet-16-retro-game
   ```
2. (Optional) Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   * Requirements include `pygame` (or `arcade`), `numpy`, and any audio libraries.

---

## Usage

```bash
python main.py
```

* Navigate menus with arrow keys.
* Player movement: arrow keys; action/interact: Z or spacebar; cancel/menu back: X or Esc.

---

## Project Structure

```
├── assets/             # Sprites, tiles, audio
├── src/                # Python source modules
│   ├── levels/         # Level-specific logic
│   ├── engine.py       # Core game loop & renderer
│   └── utils.py        # Helpers (input, collision, etc.)
├── README.md           # Project overview (you are here)
├── requirements.txt    # Python dependencies
└── main.py             # Entry point
```

---

## Contributing

1. Fork the repo.
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit changes & push.
4. Open a Pull Request.

Please adhere to the existing code style and include tests where appropriate.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
