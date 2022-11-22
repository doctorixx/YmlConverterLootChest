import ruamel.yaml

class YamlAnalyzer:

    def __init__(self, path: str, prefix: str):
        self.prefix = prefix
        self.path = path

        with open(path, "r") as f:
            self.yaml = dict(ruamel.yaml.load(f.read(), Loader=ruamel.yaml.Loader))

    def addChests(self, mode: str, cords_file_path: str):
        pass

    def fixChestSettings(self, main_chest_name: str):
        main_chest = dict(self.yaml["chests"][main_chest_name])

        for chest_name in self.yaml["chests"].keys():
            if chest_name.startswith(self.prefix) and chest_name != main_chest_name:
                chest = self.yaml["chests"][chest_name]

                chest_cords = chest["position"]

                self.yaml["chests"][chest_name] = main_chest.copy()
                self.yaml["chests"][chest_name]["position"] = chest_cords.copy()

        with open("out/" + self.path, "w") as f:
            ruamel.yaml.dump(self.yaml, f)
