from sys import exit
from sources.game import Game

def main():
    game = Game()
    game.run()

try:
    if __name__ == "__main__":
        main()
except SyntaxError as syntax_exception:
    print(f'Oops! Ocorreu um erro de sintaxe no código.\n\
        __class__ = {syntax_exception.__class__}\n\
        __doc__ = {syntax_exception.__doc__}\n\
        args = {syntax_exception.args}')
except (ValueError, ZeroDivisionError) as value_exception:
    print(f'Oops! Ocorreu um erro de valores.\n\
        __class__ = {value_exception.__class__}\n\
        __doc__ = {value_exception.__doc__}\n\
        args = {value_exception.args}')
except TypeError as type_exception:
    print(f'Oops! Ocorreu um erro de conversão de tipo de dados.\n\
        __class__ = {type_exception.__class__}\n\
        __doc__ = {type_exception.__doc__}\n\
        args = {type_exception.args}')
except Exception as general_exception:
    print(f'Oops! Ocorreu um erro não identificado.\n\
        __class__ = {general_exception.__class__}\n\
        __doc__ = {general_exception.__doc__}\n\
        args = {general_exception.args}')
finally:
    exit()
