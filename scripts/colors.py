import json
from logging import exception
"""
Themes:
  light
  dark
"""

try:
    with open('assets/config.json', 'r') as file:
        data = json.load(file)
    theme = data["theme"]
except:
    print("load theme: failed")
    theme = "light"

class Colors:
    test = '#222222'
    
    def change_theme():
        global theme
        if theme == "dark": 
            theme = "light"
        else:
            theme = "dark"
            
        try:
            with open('assets/config.json', 'r') as file:
                data = json.load(file)
            data["theme"] = theme
            with open('assets/config.json', 'w') as f:
                json.dump(data, f)
                
        except(exception):
            print("Save theme: failed")
            print(exception)
        
    def get_theme():
        return theme
        
    def bg(theme=theme):
        if theme == "dark":
            return '#133B31'
        else:
            return '#F6EEE0'
        
    def fg(theme=theme):
        if theme == "dark":
            return '#DBEBE7'
        else:
            return '#B8380F'
        
    def bg_entry(theme=theme):
        if theme == "dark":
            return '#0B5542' #DBEBE7
        else:
            return '#CEA79B'
    
    def fg_entry(theme=theme):
        if theme == "dark":
            return '#DBEBE7'
        else:
            return '#FFFFFF'