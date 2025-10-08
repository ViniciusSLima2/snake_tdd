import pytest
from snake import SnakeGame  # Importará da versão Green desta etapa
import random

# Forçar uma semente para que os testes sejam previsíveis
random.seed(0)


def test_fruit_spawns_on_creation():
    """Testa se uma fruta é criada quando o jogo começa."""
    game = SnakeGame(20, 20)
    assert game.fruit is not None
    assert isinstance(game.fruit, tuple)


def test_snake_grows_when_eating_fruit():
    """Testa se a cobra cresce ao comer a fruta."""
    game = SnakeGame(10, 10)
    initial_length = len(game.snake_body)

    # Coloca a fruta na frente da cabeça da cobra
    head_y, head_x = game.snake_body[0]
    game.fruit = (head_y - 1, head_x)  # A cobra começa indo para cima ('w')

    game.update()

    new_length = len(game.snake_body)
    assert new_length == initial_length + 1


def test_fruit_respawns_after_being_eaten():
    """Testa se a fruta muda de lugar após ser comida."""
    game = SnakeGame(10, 10)

    # Coloca a fruta na frente da cabeça da cobra
    head_y, head_x = game.snake_body[0]
    eaten_fruit_pos = (head_y - 1, head_x)
    game.fruit = eaten_fruit_pos

    game.update()

    # A nova fruta não deve estar no mesmo lugar da antiga
    assert game.fruit is not None
    assert game.fruit != eaten_fruit_pos