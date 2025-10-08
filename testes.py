import pytest
from snake import SnakeGame  # Importará da versão Green desta etapa


def test_change_direction():
    """Testa se a direção da cobra pode ser alterada."""
    game = SnakeGame(10, 10)
    game.change_direction('d')  # Direita
    game.update()

    # Posição inicial é (5,5), movendo para 'd' deve ser (5,6)
    assert game.snake_body[0] == (5, 6)


def test_cannot_reverse_direction():
    """Testa se a cobra não pode inverter sua direção."""
    game = SnakeGame(10, 10)
    game.snake_body = [(5, 5), (6, 5)]  # Cobra com 2 segmentos, indo para cima
    game.direction = 'w'

    # Tenta ir para baixo ('s'), que é o oposto de 'w'
    game.change_direction('s')

    # A direção não deve mudar
    assert game.direction == 'w'

    # Tenta ir para o lado, o que é permitido
    game.change_direction('a')
    assert game.direction == 'a'