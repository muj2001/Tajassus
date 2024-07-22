from manim import *
import numpy as np

class ClassicalMechanics(Scene):
    def construct(self):

        background = ImageMobject("Background.png") 
        
        # Scale the image to fit the screen
        background.set_height(config.frame_height)
        background.set_width(config.frame_width)

        self.add(background)

        my_tex_template = TexTemplate(
            tex_compiler="xelatex",
            output_format='.xdv',
        )
        my_tex_template.add_to_preamble(r"""\usepackage{xcolor} \usepackage{ragged2e} \usepackage{polyglossia} \usepackage{fontspec} \usepackage{etoolbox} \newcommand{\zerodisplayskips}{%
  \setlength{\abovedisplayskip}{0pt}%
  \setlength{\belowdisplayskip}{0pt}%
  \setlength{\abovedisplayshortskip}{0pt}%
  \setlength{\belowdisplayshortskip}{0pt}}
\appto{\normalsize}{\zerodisplayskips}
\appto{\small}{\zerodisplayskips}
\appto{\footnotesize}{\zerodisplayskips} \setmainlanguage{english} \setotherlanguage{urdu} \setmainfont{JameelNooriNastaleeqRegular.ttf}[Path=./fonts/] """)
        
class TestScene(Scene):
    def construct(self):
        # self.play(Write(Text("Hello, World!")))
        # self.wait(1)
        # self.play(FadeOut(Text("Hello, World!")))
        # self.wait(1)
        sq = Square(
            side_length=2, 
            fill_color=BLUE, 
            fill_opacity=0.5
            )
        self.play(Create(sq), run_time = 3)
        self.wait()