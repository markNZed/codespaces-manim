
from manim import *
scaler = 0.25
textScale = 0.5
stroke_width = 2
class helpers(ThreeDScene):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
    
    
    def create_tex(self, text, color=BLACK):
        return Tex(text).scale(textScale).set_color(color)
    
   

    def create_3d_arrows(self, end,start, color):
        arrow = Arrow3D(end=end, start=start, color=color).rotate(1, axis=LEFT) 
        return arrow


    def create_circle(self,color=BLUE, fill_opacity=1, scaler=0.25):
        return Circle(color=color, fill_opacity=fill_opacity).scale(scaler)


    def create_arrows(self,start, end, buff=0.1, color=BLUE):
        return DoubleArrow(start, end, buff=buff, color=color)
    
    def play_fade_in(self, group):
       return self.play(*[FadeIn(obj) for obj in group])
    
    def play_fade_out(self, group):
         return self.play(*[FadeOut(obj) for obj in group])
    def vgroup_all_mobjects(self):
        return VGroup(*self.mobjects)
    