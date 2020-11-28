from manim import *
from manimlib.imports import *
class CascadeStruct(Scene):
    def construct(self):
        example_text = TextMobject(
            " 1) Cascade Structure Realization",
            tex_to_color_map={"text": YELLOW}
        )
     
        group = VGroup(example_text)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.wait()
        self.clear()
        
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
            " Y(z) = S(z) x $H_2$(z) = X(z) x $H_1$(z) x $H_2$(z)",
            tex_to_color_map={"text": YELLOW}
        )
        
        
        square1 = Square(fill_opacity=1)
        square1.to_edge(LEFT, buff = 2.7)
        square2 = Square()
        square2.to_edge(LEFT, buff = 6.7)
        pointer = Arrow(2*RIGHT,4*RIGHT,color=YELLOW)
        pointer.to_edge(LEFT, 1)
        pointer1 = Arrow(2*RIGHT,4*RIGHT,color=YELLOW)
        pointer1.to_edge(LEFT, 5)
        pointer2 = Arrow(2*RIGHT,4*RIGHT,color=YELLOW)
        pointer2.to_edge(LEFT, 9)
        
        text.next_to(pointer, UP, buff = 0.2)
        text1.next_to(pointer1, UP, buff = 0.2)
        text2.next_to(pointer2, UP, buff = 0.2)
        text3.next_to(square1, UP, buff = 0.2)
        text4.next_to(square2, UP, buff = 0.2)
        text5.next_to(pointer1, DOWN, buff = 1)
        text6.next_to(text5, DOWN, buff = 0.2)
        
        self.play(ShowCreation(pointer))
        self.play(Write(text))
        self.play(ShowCreation(square1))
        #self.play(FadeToColor(square1, GREY ))
        self.play(Write(text3))
        self.play(ShowCreation(pointer1))
        self.play(Write(text1))
        self.play(ShowCreation(square2))
        self.play(Write(text4))
        self.play(ShowCreation(pointer2))
        self.play(Write(text2))
        self.play(Write(text5))
        self.play(Write(text6))
          
        self.wait(3)
        self.clear()
        
        example_text2 = TextMobject(
            " 2) Cascade Parallel Structure Realization",
            tex_to_color_map={"text": YELLOW}
        )
     
        group = VGroup(example_text)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text2))
        self.wait()
        self.clear()
        
