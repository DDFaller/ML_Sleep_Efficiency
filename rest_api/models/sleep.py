from  models import Base
from dataclasses import dataclass

@dataclass
class Sleep():
    Age:str
    Sleep_duration:str
    REM_sleep_percentage:str
    Deep_sleep_percentage:str
    Light_sleep_percentage:str
    Awakenings:str
    Caffeine_consumption:str
    Alcohol_consumption:str
    Exercise_frequency:str
    sex:str
    smoking:str
    Bedhour:str
    Wakehour:str

    def to_list(self):
        return [
            self.age,
            self.gender,
            self.sleep_hours,
            self.wake_ups,
            self.alcohol_consumption,
            self.coffee_consumption,
            self.exercise_frequency,
            self.smoke
        ]
        
    def to_dict(self):
        return {
            'Age':self.Age, 
            'Sleep duration': self.Sleep_duration,
            'REM sleep percentage': self.REM_sleep_percentage,
            'Deep sleep percentage': self.Deep_sleep_percentage,
            'Light sleep percentage': self.Light_sleep_percentage,
            'Awakenings': self.Awakenings,
            'Caffeine consumption': self.Caffeine_consumption,
            'Alcohol consumption': self.Alcohol_consumption,
            'Exercise frequency': self.Exercise_frequency,
            'sex': self.sex,
            'smoking': self.smoking,
            'Bedhour': self.Bedhour,
            'Wakehour': self.Wakehour
        }
