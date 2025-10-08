import pytest
from snake import SnakeGame
import random

random.seed(0)


def test_starts_with_one_fruit():
    """O jogo deve começar com uma fruta."""
    game = SnakeGame(20, 20)
    assert len(game.fruits) == 1


def test_spawns_two_fruits_at_length_10():
    """Deve haver duas frutas quando a cobra atinge o tamanho 10."""
    game = SnakeGame(20, 20)
    # Força a cobra a ter tamanho 9
    game.snake_body = [(i, 5) for i in range(9)]

    # Coloca uma fruta na frente para ser comida
    head_y, head_x = game.snake_body[0]
    game.direction = 'w'
    game.pending_direction = 'w'
    game.fruits = [(head_y - 1, head_x)]

    game.update()  # Cobra come e cresce para o tamanho 10

    assert len(game.snake_body) == 10
    assert len(game.fruits) == 2


def test_spawns_three_fruits_at_length_20():
    """Deve haver três frutas quando a cobra atinge o tamanho 20."""
    game = SnakeGame(30, 30)
    game.snake_body = [(i, 5) for i in range(19)]

    head_y, head_x = game.snake_body[0]
    game.direction = 'w'
    game.pending_direction = 'w'
    game.fruits = [(head_y - 1, head_x)]

    game.update()

    assert len(game.snake_body) == 20
    assert len(game.fruits) == 3