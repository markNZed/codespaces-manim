from manim import *
class DoubleArrow3D(Line3D):
    def __init__(
            self,
            start: np.ndarray = LEFT,
            end: np.ndarray = RIGHT,
            thickness: float = 0.02,
            height: float = 0.3,
            base_radius: float = 0.08,
            
            color: ParsableManimColor = WHITE,
            **kwargs,
        ) -> None:
            super().__init__(
                start=start, end=end, thickness=thickness, color=color, **kwargs,
            )

            self.length = np.linalg.norm(self.vect)
      
            self.set_start_and_end_attrs(
                self.start - (height+0.1) * -self.direction,
                self.end - (height+0.1) * self.direction,
                **kwargs,
            )
       
            self.cone = Cone(
                direction=self.direction, base_radius=base_radius, height=height, **kwargs
            )
            self.cone2 = Cone(
                 direction=-self.direction, base_radius=base_radius, height=height, **kwargs
 
            )
            self.cone.shift(self.end + (height-0.2) * self.direction)
            self.cone2.shift(self.start + (height-0.2) * -self.direction)
            self.add(self.cone, self.cone2)
            self.set_color(color)
    
