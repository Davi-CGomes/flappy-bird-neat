import os
import neat
from constants import AI_JOGANDO
from jogo import main


def rodar(caminho_config):
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        caminho_config,
    )

    populacao = neat.Population(config)
    populacao.add_reporter(neat.StdOutReporter(True))
    populacao.add_reporter(neat.StatisticsReporter())

    if AI_JOGANDO:
        populacao.run(main, 50)
    else:
        main(None, None)


if __name__ == '__main__':
    caminho = os.path.dirname(__file__)
    caminho_config = os.path.join(caminho, 'config.txt')
    rodar(caminho_config)
