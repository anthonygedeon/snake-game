class Window:
    
    def __init__(self, window):
        self.window = window
    
    def get_window_dimension(self):
        return {
            "width": self.window.display.get_surface().get_width(),
            "height": self.window.display.get_surface().get_height()
        }
