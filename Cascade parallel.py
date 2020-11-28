import numpy as np
from manimlib.imports import *

class WriteStuff2(Scene):
    def construct(self):
        example_text = TextMobject(
            " 2) Cascade Parallel Structure Realization",
            tex_to_color_map={"text": YELLOW}
        )
     
        group = VGroup(example_text)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.wait()
        self.clear()
        
        CENTER = np.array([0, 0, 0])
        pos = np.array([-4.5,2.5,0])
        
        text = TextMobject(
            " X(z)",
            tex_to_color_map={"text": YELLOW}
        )
        text1 = TextMobject(
            " S(z)",
            tex_to_color_map={"text": YELLOW}
        )
        text2 = TextMobject(
            " Y(z)",
            tex_to_color_map={"text": YELLOW}
        )
        text3 = TextMobject(
            " $H_1$(z)",
            tex_to_color_map={"text": YELLOW}
        )
        text4 = TextMobject(
            " $H_2$(z)",
            tex_to_color_map={"text": YELLOW}
        )
        text5 = TextMobject(
            " S(z) = X(z) x $H_1$(z)",
            tex_to_color_map={"text": YELLOW}
        )
        text6 = TextMobject(
            " H(z) = $H_1$(z) x $H_2$(z) + $H_3$(z)",
            tex_to_color_map={"text": YELLOW}
        )
        text7 = TextMobject(
            " $H_3$(z)",
            tex_to_color_map={"text": YELLOW}
        )
        text8 = TextMobject(
            " Y(z) = X(z) x $H_1$(z) x $H_2$(z) + X(z) x $H_3$(z)",
            tex_to_color_map={"text": YELLOW}
        )
        
        
        pointer = Arrow(2*RIGHT,4*RIGHT,color=YELLOW)
        pointer.move_to(pos)
        square1 = Square()
        square1.move_to(pos+([2,0,0]))
        pointer1 = Arrow(2*RIGHT,4*RIGHT,color=YELLOW)
        pointer1.move_to(pos+([4,0,0]))
        square2 = Square()
        square2.move_to(pos+([6,0,0]))
        pointer2 = Arrow(2*RIGHT,4*RIGHT,color=YELLOW)
        pointer2.move_to(pos+([8,0,0]))
        
        line = Line((-4.5,0,0), (-4.5, 2.5, 0), color = YELLOW)
        line2 = Line((-4.5,0,0), (-1.5, 0, 0), color = YELLOW)
        
        square3 = Square()
        square3.move_to([-0.5,0,0])
        
        line3 = Line((0.5,0,0), (3.3, 0, 0), color = YELLOW)
        line4 = Line((3.3,0,0), (3.3, 2.5, 0), color = YELLOW)
        
        text.next_to(pointer, UP, buff = 0.2)
        text1.next_to(pointer1, UP, buff = 0.2)
        text2.next_to(pointer2, UP, buff = 0.2)
        text3.next_to(square1, CENTER, buff = 0.2)
        text4.next_to(square2, CENTER, buff = 0.2)
        text5.next_to(pointer1, DOWN, buff = 1)
        text7.next_to(square3, CENTER, buff = 0.2)
        text8.next_to(square3, DOWN, buff = 1)
        text6.next_to(text8, DOWN, buff = 0.2)
        
        self.play(ShowCreation(pointer))
        self.play(Write(text))
        self.play(ShowCreation(square1))
        self.play(Write(text3))
        self.play(ShowCreation(pointer1))
        self.play(Write(text1))
        self.play(ShowCreation(square2))
        self.play(Write(text4))
        self.play(ShowCreation(pointer2))
        self.play(Write(text2))
        self.play(ShowCreation(line))
        self.play(ShowCreation(line2))
        self.play(ShowCreation(square3))
        self.play(Write(text7))
        self.play(ShowCreation(line3))
        self.play(ShowCreation(line4))
        self.play(Write(text8))
        self.play(Write(text6))
          
        self.wait()
        self.clear()
        
        
class WriteStuff3(Scene):
    def construct(self):
        example_text = TextMobject(
            "Taking an example for system function",
            tex_to_color_map={"text": YELLOW}
        )
        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
            " H(z) = ",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()
       
        
