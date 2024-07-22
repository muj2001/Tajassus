from manim import *
import numpy as np
    
class TestScene(Scene):
    def construct(self):
        self.play(Write(Text("Hello, World!")))
        self.wait(4)
        background = ImageMobject("./important_media/background/Background.png") 
        
        # Scale the image to fit the screen
        background.set_height(config.frame_height)
        background.set_width(config.frame_width)

        self.add(background)

        sq = Square(
            side_length=2, 
            fill_color=BLUE, 
            fill_opacity=0.5
            )
        self.play(Create(sq), run_time = 3)
        self.wait()
