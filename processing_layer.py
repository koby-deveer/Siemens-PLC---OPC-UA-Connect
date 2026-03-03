from datetime import datetime

class ProcessingLayer:

    @staticmethod
    def evaluate_quality(level, config):
        if level < config["low_alarm_threshold"]:
            return "low_alarm"
        elif level > config["high_alarm_threshold"]:
            return "high_alarm"
        else:
            return "good"

    @staticmethod
    def build_tank_data(level, config):

        quality = ProcessingLayer.evaluate_quality(level, config)

        tank_data = {
            "tank_name": config["tank_name"],
            "level": level,
            "timestamp": datetime.now().isoformat(),
            "quality": quality,
            "tank_config": {
                "location": config["location"],
                "capacity": config["capacity"],
                "min_level": config["min_level"],
                "max_level": config["max_level"],
                "low_alarm_threshold": config["low_alarm_threshold"],
                "high_alarm_threshold": config["high_alarm_threshold"],
                "unit": config["unit"]
            }
        }

        return tank_data
