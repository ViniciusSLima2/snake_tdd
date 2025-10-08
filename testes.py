import pytest
from snake import SnakeGame  # Irá falhar, pois snake.py não tem SnakeGame ainda


def test_snake_creation_and_initial_position():
    """Testa se a cobra é criada na posição correta."""
    game = SnakeGame(width=10, height=10)
    # Posição inicial esperada no centro
    expected_head_pos = (5, 5)
    assert game.snake_body[0] == expected_head_pos


def test_snake_moves_forward():
    """Testa se a cobra se move um passo para frente."""
    # A direção inicial padrão é 'w' (para cima)
    game = SnakeGame(width=10, height=10)
    initial_pos = game.snake_body[0]  # (5, 5)

    game.update()  # Move a cobra

    new_pos = game.snake_body[0]
    expected_pos = (4, 5)  # Um passo para cima de (5, 5)

    assert new_pos == expected_pos
    assert len(game.snake_body) == 1  # A cobra ainda tem tamanho 1