# author: george
# date: 2024-10-13
# description: play Roll and Record

print()
print("george")

# roll two dices
import sys
import subprocess
import importlib

def install_and_import(package):
    try:
        importlib.import_module(package)
    except ImportError:
        print(f"{package} not found, installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"{package} installed successfully!")
    finally:
        globals()[package] = importlib.import_module(package)

# Install and import required packages
install_and_import('matplotlib')

import random
from matplotlib import pyplot as plt

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def play_game():
    george_rolls = []
    pete_rolls = []
    turn = 0
    
    while True:
        if turn % 2 == 0:
            george_rolls.append(roll_dice())
            if max(plt.hist(george_rolls, bins=range(2, 14), align='left')[0]) >= 8:
                winner = "George"
                break
        else:
            pete_rolls.append(roll_dice())
            if max(plt.hist(pete_rolls, bins=range(2, 14), align='left')[0]) >= 8:
                winner = "Pete"
                break
        turn += 1
        plt.clf()  # Clear the figure to avoid overlapping histograms
    
    return george_rolls, pete_rolls, winner

def create_histograms(george_rolls, pete_rolls, winner):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle(f'Awesome Dice Game - {winner} Wins!', fontsize=18)
    
    # George's histogram (Red)
    ax1.hist(george_rolls, bins=range(2, 14), align='left', rwidth=0.8, color='red', edgecolor='black')
    ax1.set_title(f'George ({len(george_rolls)} rolls)', fontsize=16, fontweight='bold')
    ax1.set_xlabel('Sum of Dice', fontsize=12)
    ax1.set_ylabel('Frequency', fontsize=12)
    ax1.set_xticks(range(2, 13))
    ax1.set_ylim(0, 10)
    ax1.axhline(y=7.8, color='green', linestyle='--', linewidth=2)
    ax1.grid(axis='y', linestyle='--', alpha=0.7)
    ax1.set_facecolor('#f0f0f0')
    
    # Pete's histogram (Blue)
    ax2.hist(pete_rolls, bins=range(2, 14), align='left', rwidth=0.8, color='blue', edgecolor='black')
    ax2.set_title(f'Pete ({len(pete_rolls)} rolls)', fontsize=16, fontweight='bold')
    ax2.set_xlabel('Sum of Dice', fontsize=12)
    ax2.set_ylabel('Frequency', fontsize=12)
    ax2.set_xticks(range(2, 13))
    ax2.set_ylim(0, 10)
    ax2.axhline(y=7.8, color='green', linestyle='--', linewidth=2)
    ax2.grid(axis='y', linestyle='--', alpha=0.7)
    ax2.set_facecolor('#f0f0f0')
    
    plt.tight_layout()
    plt.savefig('awesome_dice_game_result.png', dpi=300, bbox_inches='tight')
    plt.show()

# Play the game and create histograms
george_rolls, pete_rolls, winner = play_game()
create_histograms(george_rolls, pete_rolls, winner)

print(f"{winner} wins the game!")
print(f"George rolled {len(george_rolls)} times.")
print(f"Pete rolled {len(pete_rolls)} times.")
