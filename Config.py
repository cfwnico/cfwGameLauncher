# cfw
# 2022.6.25

import json


class Config:
    def __init__(self, conf_filepath) -> None:
        self.conf_filepath = conf_filepath
        with open(self.conf_filepath, "r", encoding="utf-8") as f:
            self.confdata_dict: dict = json.load(f)

    def get_config_dict(self) -> dict:
        return self.confdata_dict

    def save_config(self, key: str, value):
        if key in self.confdata_dict:
            self.confdata_dict[key] = value
        with open(self.conf_filepath, "w", encoding="utf-8") as f:
            json.dump(self.confdata_dict, f, ensure_ascii=False)


class GameData:
    def __init__(self, data_filepath) -> None:
        self.data_filepath = data_filepath
        with open(self.data_filepath, "r", encoding="utf-8") as f:
            self._gamedata_dict: dict = json.load(f)

    def get_game_list(self) -> list:
        game_list = []
        for i in self._gamedata_dict.keys():
            game_list.append(i)
        return game_list

    def get_game_data(self, game_name: str) -> dict:
        if game_name in self._gamedata_dict:
            return self._gamedata_dict[game_name]

    def save_game_data(self, game_name: str, key: str, value: str):
        if game_name in self._gamedata_dict:
            game_data = self._gamedata_dict[game_name]
            game_data[key] = value
            with open(self.data_filepath, "w", encoding="utf-8") as f:
                json.dump(self._gamedata_dict, f, ensure_ascii=False)

    def create_game(self, game_name: str, game_info_dict: dict):
        if game_name in self._gamedata_dict:
            return
        self._gamedata_dict[game_name] = game_info_dict
        with open(self.data_filepath, "w", encoding="utf-8") as f:
            json.dump(self._gamedata_dict, f, ensure_ascii=False)

    def del_game(self, game_name: str):
        self._gamedata_dict.pop(game_name)
        with open(self.data_filepath, "w", encoding="utf-8") as f:
            json.dump(self._gamedata_dict, f, ensure_ascii=False)

    def sort_game(self):
        a1 = sorted(self._gamedata_dict.items(), key=lambda x: x[0])
        self._gamedata_dict = dict(a1)
        print(self._gamedata_dict)
        with open(self.data_filepath, "w", encoding="utf-8") as f:
            json.dump(self._gamedata_dict, f, ensure_ascii=False)
