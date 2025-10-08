import pytest
from snake import SnakeGame

# Em testes.py da Etapa 3 (CORRIGIDO)
def test_snake_wraps_around_top_edge():
    game = SnakeGame(10, 10)
    game.snake_body = [(0, 5)]
    game.change_direction('w') # <-- Use o método correto
    game.update()
    assert game.snake_body[0] == (9, 5)

def test_snake_wraps_around_right_edge():
    game = SnakeGame(10, 10)
    game.snake_body = [(5, 9)]
    game.change_direction('d') # <-- Use o método correto
    game.update()
    assert game.snake_body[0] == (5, 0)