import pytest
from snake import SnakeGame

def test_snake_wraps_around_top_edge():
    game = SnakeGame(10, 10)
    game.snake_body = [(0, 5)] # No topo
    game.direction = 'w'
    game.update()
    assert game.snake_body[0] == (9, 5) # Deve aparecer na base

def test_snake_wraps_around_right_edge():
    game = SnakeGame(10, 10)
    game.snake_body = [(5, 9)] # Na direita
    game.direction = 'd'
    game.update()
    assert game.snake_body[0] == (5, 0) # Deve aparecer na esquerda