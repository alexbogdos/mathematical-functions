class Geometry:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        
    def center(self, widget_width):
        x = (self.width - widget_width) / 2
        return x

    def anchor_B(self, widget_height, difference):
        y = (self.height - widget_height) - difference
        return y
    
    def anchor_BL(self, widget_size, difference):
        x = difference[0]
        y = (self.height - widget_size[1]) - difference[1]
        return x,y
    
    def anchor_BR(self, widget_size, difference):
        x = (self.width - widget_size[0]) - difference[0]
        y = (self.height - widget_size[1]) - difference[1]
        return x,y