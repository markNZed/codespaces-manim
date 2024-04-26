class processism(helpers):
    def setup(self):
        self.camera.background_color = GREY
        self.set_camera_orientation(phi=360 * DEGREES, theta=-90 * DEGREES)
        self.renderer.camera.light_source.move_to(3 *UP + 5 *LEFT)
        self.renderer.camera.ambient_light = 1.0 # Increase ambient light for less shadow
        
    def construct(self):
       

        entity_circle1 = self.create_circle().to_edge(LEFT).shift(RIGHT, UP)
        entity_circle2 = self.create_circle().next_to(entity_circle1, RIGHT).shift(RIGHT*2)
        entity_circle3 = self.create_circle().next_to(entity_circle2, DOWN).shift(DOWN*2)
        entity_circle4 = self.create_circle().next_to(entity_circle1, DOWN).shift(DOWN*2)

        circles = VGroup(
            entity_circle1,
            entity_circle2,
            entity_circle3,
            entity_circle4,
        )


        # # Create arrows
        relation_arrows = VGroup(
            self.create_3D_double_arrow(entity_circle1.get_right(), entity_circle2.get_left()),
            self.create_3D_double_arrow(entity_circle1.get_bottom(), entity_circle4.get_top()),
            self.create_3D_double_arrow(entity_circle2.get_bottom(), entity_circle3.get_top()),
            self.create_3D_double_arrow(entity_circle3.get_left(), entity_circle4.get_right()),
            self.create_3D_double_arrow(entity_circle4.get_right(), entity_circle2.get_left()),
            self.create_3D_double_arrow(entity_circle3.get_left()+0.1, entity_circle1.get_right()-0.1)
        )


        # Create emergent_entity
        emergent_entity = Circle(color=GREEN, fill_opacity=0.2).scale(2.7).to_edge(LEFT).shift(DOWN*0.5,UP*0.3,RIGHT,OUT*-2)
        VGroup(entity_circle1, entity_circle2, entity_circle3, entity_circle4, relation_arrows).move_to(emergent_entity).shift(OUT*2)
        # Create copies
        top_down_elements = VGroup(emergent_entity, entity_circle1,entity_circle2,entity_circle3,entity_circle4, *relation_arrows)
        bottom_up_elements = top_down_elements.copy()
        bottom_up_elements.to_edge(RIGHT)
        emergent_entity.shift(LEFT*0.3)
        bottom_up_elements[0].shift(RIGHT*0.3)
        VGroup(bottom_up_elements,top_down_elements).shift(LEFT*0.4)

        # Create relation arrow
        relationArrow7 = self.create_3D_double_arrow(top_down_elements[0].get_right(), bottom_up_elements[0].get_left(), color=GREEN)

        # Create texts
        entity1 = self.create_tex("An entity").next_to(circles[0], UP)
        relationText = self.create_tex("A relation").next_to(relation_arrows[0], UP)
        accumulation = self.create_tex("Accumulation").next_to(relation_arrows[0], UP)
        Emergent = self.create_tex("Emergent entity").next_to(emergent_entity, UP)
        topDown, topDownArrows = self.create_top_down(top_down_elements[0],top_down_elements)
        bottomUp, bottomUpArrows = self.create_bottom_up(bottom_up_elements[0],bottom_up_elements)

        # Play animations
        self.play_animations(circles, relation_arrows, emergent_entity, bottom_up_elements, relationArrow7, entity1, relationText, accumulation, Emergent, topDown, topDownArrows, bottomUp, bottomUpArrows)
        
    
 # one time function
    def top_down_Arrows(self, group):
        arrows = []
        for i in range(1, 5):
            center = group[i].get_center()
            end = self.create_end(center)
            start = self.create_start(center)
            arrow = Arrow(start=end, end=start, color=GREEN)
            arrows.append(arrow)
        return tuple(arrows)
    
    # one time function   
    def create_top_down(self, copy, group):
        topDown = Text("Top-down",color=BLACK).next_to(copy,  OUT).scale(textScale).shift(RIGHT*1.5,UP*1,OUT*-1.5).rotate(2,axis=LEFT)
        topDownArrows = self.top_down_Arrows(group)
        return topDown, topDownArrows

    # one time function
    def bottom_up_Arrows(self, group):
        
        arrows = []
        for i in range(1, 5):
            center = group[i].get_center()
            end = self.create_end(center)
            start = self.create_start(center)
            arrow = Arrow(end=end, start=start, color=BLUE)
            arrows.append(arrow)
        return tuple(arrows)
        
    # one time function
    def create_bottom_up(self, copy, group):
        bottomUp = Text("Bottom-up",color=BLACK).next_to(copy,  OUT).scale(textScale).shift(RIGHT*1.5,UP*1,OUT*-1.5).rotate(2,axis=LEFT)
        # bottomUpArrows = self.bottom_up_Arrows(group)
        bottomUp_arrow = self.bottom_up_Arrows(group)
        return bottomUp, bottomUp_arrow
        

    def play_animations(self, circles, arrow, emergent_entity, bottom_up_elements, relationArrow7, entity1, relationText, accumulation, Emergent, topDown, topDownArrows, bottomUp, bottomUpArrows):
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
        self.play(FadeIn(emergent_entity))
        self.play(FadeIn(Emergent))
        self.wait(1)
        self.play(FadeOut(Emergent))
        self.play(FadeIn(bottom_up_elements))
        self.play(FadeIn(relationArrow7))
        self.move_camera(phi=250 * DEGREES, zoom=1, run_time=2)
        self.play(FadeIn(bottomUp))
        self.play_fade_in(bottomUpArrows) 
    
        self.wait(1)
        self.play(FadeIn(topDown))
        self.play_fade_in(topDownArrows) 
        self.wait(1)