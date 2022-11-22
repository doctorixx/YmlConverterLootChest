import sys

from messages import USAGE_MSG
from newYamlAnalyzer import YamlAnalyzer

args = sys.argv[1:]

try:
    analyzer = YamlAnalyzer(args[0], "yamlC_")

    if args[1] == "add":

        mode = args[2]  # (VALUES) del or save
        cords_file = args[3]

        if mode not in ["del", "save"]:
            raise AttributeError("Mode attr error")

        analyzer.addChests()

    elif args[1] == "fix":

        main_chest = "chest"

        if len(args) >= 3:
            main_chest = args[2]

        analyzer.fixChestSettings(main_chest)

except Exception as e:
    print(e)
    print(USAGE_MSG)
