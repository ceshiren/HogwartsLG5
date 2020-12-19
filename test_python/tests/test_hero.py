import unittest
from unittest import TestCase

from test_python.src.hero_factory import HeroFactory


class TestHero(TestCase):
    def test_fight(self):
        chengyaojin = HeroFactory.create_hero('程咬金')
        libai = HeroFactory.create_hero('李白')

        assert chengyaojin.fight(libai) == True

        # chengyaojin = ChengYaoJin()
        # libai = LiBai()
        chengyaojin = HeroFactory.create_hero('程咬金')
        libai = HeroFactory.create_hero('李白')
        assert libai.fight(chengyaojin) == False

    def test_logging(self):
        import logging
        logging.debug('Debugging information')
        logging.info('Informational message')
        logging.warning('Warning:config file %s not found', 'server.conf')
        logging.error('Error occurred')
        logging.critical('Critical error -- shutting down')


if __name__ == '__main__':
    unittest.main()
