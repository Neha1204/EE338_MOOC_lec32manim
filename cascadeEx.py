from manimlib.imports import *
from pygments.styles.paraiso_light import YELLOW


class CascadeEx(Scene):
    def construct(self):
        Title_text = TextMobject(
            "Cascade Structure Example",
            tex_to_color_map={"text": YELLOW}
        )
        group = VGroup(Title_text)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(Title_text))
        self.wait()
        self.clear()

        textHz = TexMobject(
            "H(z) = H_1(z)H_2(z)",
        tex_to_color_map = {"text": YELLOW}
        )
        textH1z = TexMobject(
            "H_1(z) = \\frac{1-\\frac{1}{2}z^{-1}}{(1-\\frac{1}{3}z^{-1})^2} = \\frac{1-\\frac{1}{2}z^{-1}}{1-\\frac{2}{3}z^{-1} + \\frac{1}{9}z^{-2}}",
        tex_to_color_map = {"text": YELLOW}
        )
        textH2z = TexMobject(
            "H_2(z) = \\frac{1-\\frac{1}{4}z^{-1}}{1-\\frac{1}{5}z^{-1}}",
        tex_to_color_map = {"text": YELLOW}
        )

        textHz.next_to(textH1z, UP)
        textH2z.next_to(textH1z, DOWN)

        self.play(Write(textHz))
        self.play(Write(textH1z))
        self.play(Write(textH2z))

        self.wait(4)
        self.clear()
