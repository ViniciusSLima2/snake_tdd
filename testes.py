import pytest
from snake import SnakeGame


def test_game_over_on_self_collision():
    """Testa se game_over se torna True ao colidir com o corpo."""
    game = SnakeGame(10, 10)
    # Cobra em forma de 'C'.
    game.snake_body = [(5, 5), (5, 6), (6, 6), (6, 5)]

    # Mude a direção para 's' (baixo) para forçar a colisão com a cauda (6, 5)
    game.direction = 's'
    game.pending_direction = 's'

    assert game.game_over is False
    game.update()
    assert game.game_over is True


def test_snake_stops_moving_after_game_over():
    """Testa se o jogo para de ser atualizado após o game over."""
    game = SnakeGame(10, 10)
    game.snake_body = [(5, 5), (5, 6), (6, 6), (6, 5)]

    # Mude a direção para 's' (baixo) para forçar a colisão
    game.direction = 's'
    game.pending_direction = 's'

    game.update()  # Primeira atualização causa o game over
    assert game.game_over is True

    # Pega o estado do corpo da cobra após o game over
    body_at_game_over = list(game.snake_body)

    game.update()  # Tenta atualizar de novo

    # O corpo da cobra não deve ter mudado
    assert game.snake_body == body_at_game_over