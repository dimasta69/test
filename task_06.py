# Произволит проверку на количество заданных пользователей.
# Если их больше двух, возникает исключение.
# Так же возникает исключение при вводе отличительного от одного из параметров R,P,S.
# По итогу возвращает победителя (если одинаковые значения R,P,S выводит первого иргрока).
# Так как дан пример данных, которые будут переданы функции, из которых видна четко переданная структура,
# то к к именам игрока будем обращаться к 0 элементу, а игровой атрибу обращаться к 1 элементу.
class RPSGameError(Exception):
    pass

class WrongNumberOfPlayersError(RPSGameError):
    def __init__(self):
        super().__init__("Wrong number of players. Задано больше двух игроков.")

class NoSuchStrategyError(RPSGameError):
    def __init__(self):
        super().__init__("Invalid strategy. Выбран неправленьный параметр 'R', 'P', 'S'.")

def rps_game_winner(data):
    if len(data) != 2:
        raise WrongNumberOfPlayersError()

    game_attribute = ['R', 'P', 'S']
    for i in data:
        if i[1] not in game_attribute:
            raise NoSuchStrategyError()

    atr_player_1 = data[0][1]
    atr_player_2 = data[1][1]

    player_1_win = ((atr_player_1 == 'R' and atr_player_2 == 'S')
                    or (atr_player_1 == 'P' and atr_player_2 == 'R')
                    or (atr_player_1 == 'S' and atr_player_2 == 'P'))

    if atr_player_1 == atr_player_2:
        return data[0][0], data[0][1]
    elif player_1_win:
        return data[0][0], data[0][1]
    else:
        return data[1][0], data[1][1]
# Проверка
rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]) # => WrongNumberOfPlayersError
rps_game_winner([['player1', 'P'], ['player2', 'A']]) # => NoSuchStrategyError
print(rps_game_winner([['player1', 'P'], ['player2', 'S']])) # => 'player2 S'
print(rps_game_winner([['player1', 'P'], ['player2', 'P']])) # => 'player1 P'
