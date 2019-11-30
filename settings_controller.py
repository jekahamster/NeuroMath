import json

class SettingsController():
    DEFAULT_PATH = "settings.json"

    @staticmethod
    def loadFrom(fileName="settings.json"):
        with open(fileName, "r") as file:
            data = json.load(file)

        SettingsController.numbersNetworkPath   = data["NumbersNetworkPath"]
        SettingsController.operatorsNetworkPath = data["OperatorsNetworkPath"]
        SettingsController.canvasImg            = data["CanvasImg"]
        SettingsController.numberLabels         = data["NumberLabels"]
        SettingsController.operatorLabels       = data["OperatorLabels"]
        SettingsController.windowHeight         = data["WindowHeight"]
        SettingsController.windowWidth          = data["WindowWidth"]
        SettingsController.windowResizable      = data["WindowResizable"]
        SettingsController.theme                = data["Theme"]
        SettingsController.primaryPalette       = data["PrimaryPalette"]
        SettingsController.adjustAll            = bool(data["AdjustAll"])
        SettingsController.finderMode           = int(data["FinderMode"])
