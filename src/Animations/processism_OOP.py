import sys
sys.path.insert(1, '../AnimationManger/')  # Corrected path

from AnimationManger import *

class CircleCreator:
    def __init__(self, base_circle):
        self.base_circle = base_circle

    def create_circle(self):
        return self.base_circle.copy()

    def create_circles(self):
        circle1 = self.create_circle().to_edge(LEFT).shift(RIGHT, UP)
        circle2 = self.create_circle().next_to(circle1, RIGHT).shift(RIGHT*2)
        circle3 = self.create_circle().next_to(circle2, DOWN).shift(DOWN*2)
        circle4 = self.create_circle().next_to(circle1, DOWN).shift(DOWN*2)

        circles = VGroup(
            circle1,
            circle2,
            circle3,
            circle4,
        )

        return circles

class processism(helpers):
    def construct(self):
        self.camera.background_color = GREY
        self.set_camera_orientation(phi=360 * DEGREES, theta=-90 * DEGREES)
        # Create circles

        circleCreator = CircleCreator(self.create_circle())

        # # Create arrows
        relationArrows = VGroup(
            self.create_arrows(circle1.get_right(), circle2.get_left()),
            self.create_arrows(circle1.get_bottom(), circle4.get_top()),
            self.create_arrows(circle2.get_bottom(), circle3.get_top()),
            self.create_arrows(circle3.get_left(), circle4.get_right()),
            self.create_arrows(circle4.get_right(), circle2.get_left()),
            self.create_arrows(circle3.get_left()+0.1, circle1.get_right()-0.1)
        )


        # Create background
        backGround = Circle(color=GREEN, fill_opacity=0.2).scale(2.7).to_edge(LEFT).shift(DOWN*0.5,UP*0.3,RIGHT,OUT*-2)
        VGroup(circle1, circle2, circle3, circle4, relationArrows).move_to(backGround).shift(OUT*2)
        # Create copies
        copy = VGroup(backGround, *circles, *relationArrows)
        copy1 = copy.copy()
        copy1.to_edge(RIGHT)
        backGround.shift(LEFT*0.3)
        copy1[0].shift(RIGHT*0.3)
        VGroup(copy1,copy).shift(LEFT*0.4)

        # Create relation arrow
        relationArrow7 = self.create_arrows(copy[0].get_right(), copy1[0].get_left(), color=GREEN)

        # Create texts
        entity1 = self.create_tex("An entity").next_to(circles[0], UP)
        relationText = self.create_tex("A relation").next_to(relationArrows[0], UP)
        accumulation = self.create_tex("Accumulation").next_to(relationArrows[0], UP)
        Emergent = self.create_tex("Emergent entity").next_to(backGround, UP)
        topDown, topDownArrows = self.create_top_down(copy[0])
        bottomUp, bottomUpArrows = self.create_bottom_up(copy1[0])

        # Play animations
        self.play_animations(circles, relationArrows, backGround, copy1, relationArrow7, entity1, relationText, accumulation, Emergent, topDown, topDownArrows, bottomUp, bottomUpArrows)
        
    
 # one time function
    def top_down_Arrows(self):
        topDownArrow1 = Arrow3D(start=np.array([-4.2,1.3,0]),end=np.array([-4.2,0.4,1]),color=GREEN).shift(OUT*-2.2).rotate(1,axis=LEFT )
        topDownArrow2 = Arrow3D(start=np.array([-1.8,1.2,0]),end=np.array([-1.8,0,1]), color=GREEN).shift(OUT*-2.2).rotate(1,axis=LEFT )
        topDownArrow3 = Arrow3D(start=np.array([-4,2,0]),end=np.array([-4,1,1]), color=GREEN).shift(OUT*-2.4,UP*2.5).rotate(1,axis=LEFT )
        topDownArrow4 = Arrow3D(start=np.array([-1.4,2.1,0]),end=np.array([-1.4,1,1]), color=GREEN).shift(OUT*-2.4,UP*2.5).rotate(1,axis=LEFT )

        return topDownArrow1, topDownArrow2, topDownArrow3, topDownArrow4
    
    # one time function   
    def create_top_down(self, copy):
        topDown = Text("Top-down",color=BLACK).next_to(copy, OUT).scale(textScale).shift(RIGHT*2,UP*1,OUT*-1.5).rotate(2,axis=LEFT)
        topDownArrows = self.top_down_Arrows()
        return topDown, topDownArrows

    # one time function
    def bottom_up_Arrows(self):
        bottomUpArrow1 = self.create_3d_arrows(end=np.array([4,1.3,0]),start=np.array([4,0.4,1]), color=BLUE).shift(OUT*-2.2,UP*0.6)
        bottomUpArrow2 = self.create_3d_arrows(end=np.array([1.7,1.3,0]),start=np.array([1.7,0.4,1]), color=BLUE).shift(OUT*-2.2,UP*0.6)
        bottomUpArrow3 = self.create_3d_arrows(end=np.array([4.4,1.3,0]),start=np.array([4.4,0.2,1]), color=BLUE).shift(OUT*-2.2,UP*2.5)
        bottomUpArrow4 = self.create_3d_arrows(end=np.array([1.8,1.3,0]),start=np.array([1.8,0.2,1]), color=BLUE).shift(OUT*-2,UP*2.3)

        return bottomUpArrow1, bottomUpArrow2, bottomUpArrow3, bottomUpArrow4
    
    # one time function
    def create_bottom_up(self, copy):
        bottomUp = Text("Bottom-up",color=BLACK).next_to(copy,  OUT).scale(textScale).shift(RIGHT*1.5,UP*1,OUT*-1.5).rotate(2,axis=LEFT)
        bottomUpArrows = self.bottom_up_Arrows()
        
       
        return bottomUp, bottomUpArrows
        

    def play_animations(self, circles, arrow, backGround, copy1, relationArrow7, entity1, relationText, accumulation, Emergent, topDown, topDownArrows, bottomUp, bottomUpArrows):
        self.play(FadeIn(circles[0]))
        self.play(FadeIn(entity1))
        self.wait(1)
        self.play(FadeOut(entity1))
        self.play(FadeIn(circles[1]))
        self.play(FadeIn(arrow[0]))
        self.play(FadeIn(relationText))
        self.wait(1)
        self.play(FadeOut(relationText))
        self.play(FadeIn(circles[2]),FadeIn(circles[3]))
        self.play_fade_in(arrow[1:])
        self.play(FadeIn(accumulation))
        self.wait(1)
        self.play(FadeOut(accumulation))
        self.play(FadeIn(backGround))
        self.play(FadeIn(Emergent))
        self.wait(1)
        self.play(FadeOut(Emergent))
        self.play(FadeIn(copy1))
        self.play(FadeIn(relationArrow7))
        self.move_camera(phi=250 * DEGREES, zoom=1, run_time=2)
        self.play(FadeIn(bottomUp))
        self.play_fade_in(bottomUpArrows) 
    
        self.wait(1)
        self.play(FadeIn(topDown))
        self.play_fade_in(topDownArrows) 
        self.wait(1)