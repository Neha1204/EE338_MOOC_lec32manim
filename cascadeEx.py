from manimlib.imports import *


class CascadeEx(Scene):
    def construct(self):
        # File from Cascade.py
        example_text = TextMobject(
            " 1) Cascade Structure Realization",
            tex_to_color_map={"text": YELLOW}
        )

        group = VGroup(example_text)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.wait()
        self.clear()

        CENTER = np.array([0, 0, 0])

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

        square1 = Square()
        square1.to_edge(LEFT, buff=2.7)
        square2 = Square()
        square2.to_edge(LEFT, buff=6.7)
        pointer = Arrow(2 * RIGHT, 4 * RIGHT, color=YELLOW)
        pointer.to_edge(LEFT, 1)
        pointer1 = Arrow(2 * RIGHT, 4 * RIGHT, color=YELLOW)
        pointer1.to_edge(LEFT, 5)
        pointer2 = Arrow(2 * RIGHT, 4 * RIGHT, color=YELLOW)
        pointer2.to_edge(LEFT, 9)

        text.next_to(pointer, UP, buff=0.2)
        text1.next_to(pointer1, UP, buff=0.2)
        text2.next_to(pointer2, UP, buff=0.2)
        text3.next_to(square1, CENTER, buff=0.2)
        text4.next_to(square2, CENTER, buff=0.2)
        text5.next_to(pointer1, DOWN, buff=1)
        text6.next_to(text5, DOWN, buff=0.2)

        self.play(ShowCreation(pointer))
        self.play(Write(text))
        self.play(ShowCreation(square1))
        # self.play(FadeToColor(square1, GREY ))
        self.play(Write(text3))
        self.play(ShowCreation(pointer1))
        self.play(Write(text1))
        self.play(ShowCreation(square2))
        self.play(Write(text4))
        self.play(ShowCreation(pointer2))
        self.play(Write(text2))
        self.play(Write(text5))
        self.play(Write(text6))

        self.wait()
        self.clear()

        # --END--

        Title_text = TextMobject(
            "Cascade Structure Example"
        )
        group = VGroup(Title_text)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(Title_text))
        self.wait()
        self.clear()

        CENTER = np.array([0, 0, 0])


        texHzEq = TexMobject(
            "H(z)", r" =\frac{(1-\frac{1}{2}z^{-1})(1-\frac{1}{4}z^{-1})}{(1-\frac{1}{3}z^{-1})(1-\frac{1}{5}z^{-1})(1-\frac{1}{6}z^{-1})} = H_1(z)H_2(z)"
        )
        texHzEq.set_color_by_tex("H(z)", YELLOW)
        texH1zEq = TexMobject(
            "H_1(z)", r"= \frac{1-\frac{1}{2}z^{-1}}{(1-\frac{1}{3}z^{-1})(1-\frac{1}{6}z^{-1})} = \frac{1-\frac{1}{2}z^{-1}}{1-\frac{1}{2}z^{-1} + \frac{1}{18}z^{-2}}"
        )
        texH1zEq.set_color_by_tex("H_1", YELLOW)

        textH2zEq = TexMobject(
            "H_2(z)",r" = \frac{1-\frac{1}{4}z^{-1}}{1-\frac{1}{5}z^{-1}}"
        )
        textH2zEq.set_color_by_tex("H_2", YELLOW)

        texHzEq.next_to(texH1zEq, UP)
        textH2zEq.next_to(texH1zEq, DOWN)

        self.play(Write(texHzEq))
        self.play(Write(texH1zEq))
        self.play(Write(textH2zEq))

        self.wait(4)
        self.clear()

        texH2z = TexMobject(
            "H_2(z)", color=YELLOW, buff=0
        )
        texH1z = TexMobject("H_1(z)", color=YELLOW)
        texz1 = TexMobject(
            "z^{-1}", color=YELLOW, buff=0
        )
        texz2 = TexMobject(
            "z^{-1}", color=YELLOW, buff=0
        )
        texz3 = TexMobject(
            "z^{-1}", color=YELLOW, buff=0
        )
        texz1.scale(0.7)
        texz2.scale(0.7)
        texz3.scale(0.7)

        texXz = TexMobject(
            "X(z)", color=YELLOW, buff=0
        )
        texYz = TexMobject(
            "Y(z)", color=YELLOW, buff=0
        )
        texXzLo = TexMobject(
            "X(z)", color=YELLOW, buff=0
        )
        texYzLo = TexMobject(
            "Y(z)", color=YELLOW, buff=0
        )

        texXzeq = TexMobject(
            "Y(z)",r"=X(z)\times H_1(z)\times H_2(z)=X(z)\times H(z)",
            buff=0
        )
        texXzeq[0].set_color(YELLOW)

        num5 = TextMobject("1/5", color=YELLOW, buff=0)
        num5.scale(0.7)
        num4 = TextMobject("1/4", color=YELLOW, buff=0)
        num4.scale(0.7)
        num2 = TextMobject("1/2", color=YELLOW, buff=0)
        num2.scale(0.7)
        num2min = TextMobject("-1/2", color=YELLOW, buff=0)
        num2min.scale(0.7)
        num18 = TextMobject("-1/18", color=YELLOW, buff=0)
        num18.scale(0.7)

        arrowHi2Tail = np.array([-1, 2.8, 0])
        arrowHi2 = Arrow(arrowHi2Tail, arrowHi2Tail + 2*RIGHT, buff=0)
        rectH2z = Rectangle(
            width=2,
            height=1.3,
            buff=0
        )
        rectH2z.move_to(arrowHi2Tail + LEFT)
        texH2z.move_to(arrowHi2Tail + LEFT)

        rectH1z = Rectangle(
            width=2,
            height=1.3,
            buff=0
        )
        rectH1z.move_to(arrowHi2Tail + 3*RIGHT)
        texH1z.move_to(arrowHi2Tail + 3*RIGHT)

        arrowHi1Head = arrowHi2Tail + 2*LEFT
        arrowHi1 = Arrow(arrowHi1Head + 2*LEFT, arrowHi1Head, buff=0)
        texXz.move_to(arrowHi1Head + 2.7*LEFT)
        arrowHi3Tail = arrowHi2Tail + 4*RIGHT
        arrowHi3 = Arrow(arrowHi3Tail, arrowHi3Tail + 2*RIGHT, buff=0)
        texYz.move_to(arrowHi3Tail + 2.55*RIGHT)

        texXzeq.next_to(arrowHi2, DOWN*3.4)

        arrowLo2Tail = np.array([-3.75, 0.2, 0])
        arrowLo6Tail = arrowLo2Tail + 1.5*RIGHT
        arrowLo9Tail = arrowLo6Tail + 1.5*RIGHT
        arrowLo10Tail = arrowLo9Tail + 1.5*RIGHT
        arrowLo14Tail = arrowLo10Tail + 1.5*RIGHT
        arrowLo20Tail = arrowLo14Tail + 1.5*RIGHT
        arrowLo11Tail = arrowLo10Tail + 1.5*DOWN
        arrowLo16Tail = arrowLo11Tail + 1.5*RIGHT
        arrowLo4Tail = arrowLo6Tail + 1.5*DOWN

        arrowLo1 = Arrow(arrowLo2Tail + 1.5*LEFT, arrowLo2Tail, buff=0)
        arrowLo2 = Arrow(arrowLo2Tail, arrowLo2Tail + 1.5*RIGHT, buff=0)
        arrowLo3 = Arrow(arrowLo2Tail + 1.5*DOWN, arrowLo2Tail, buff=0)
        arrowLo4 = Arrow(arrowLo4Tail, arrowLo4Tail + 1.5*LEFT, buff=0)
        arrowLo5 = Arrow(arrowLo6Tail, arrowLo4Tail, buff=0)
        arrowLo6 = Arrow(arrowLo6Tail, arrowLo9Tail, buff=0)
        arrowLo7 = Arrow(arrowLo9Tail + 1.5*DOWN, arrowLo9Tail, buff=0)
        arrowLo8 = Arrow(arrowLo4Tail, arrowLo4Tail + 1.5*RIGHT, buff=0)
        arrowLo9 = Arrow(arrowLo9Tail, arrowLo9Tail + 1.5*RIGHT, buff=0)
        arrowLo10 = Arrow(arrowLo10Tail, arrowLo10Tail + 1.5*RIGHT, buff=0)
        arrowLo11 = Arrow(arrowLo10Tail + 1.5*DOWN, arrowLo10Tail, buff=0)
        arrowLo12 = Arrow(arrowLo16Tail, arrowLo16Tail + 1.5*LEFT, buff=0)
        arrowLo13 = Arrow(arrowLo14Tail, arrowLo16Tail, buff=0)
        arrowLo14 = Arrow(arrowLo14Tail, arrowLo20Tail, buff=0)
        arrowLo15 = Arrow(arrowLo16Tail + 1.5*RIGHT, arrowLo20Tail, buff=0)
        arrowLo16 = Arrow(arrowLo16Tail, arrowLo16Tail + 1.5*RIGHT, buff=0)
        arrowLo17 = Arrow(arrowLo16Tail, arrowLo16Tail + 1.5*DOWN, buff=0)
        arrowLo18 = Arrow(arrowLo16Tail + 1.5*DOWN, arrowLo11Tail + 1.5*DOWN, buff=0)
        arrowLo19 = Arrow(arrowLo11Tail + 1.5*DOWN, arrowLo11Tail, buff=0)
        arrowLo20 = Arrow(arrowLo20Tail, arrowLo20Tail + 1.5*RIGHT, buff=0)

        texXzLo.move_to(arrowLo2Tail + 2.2*LEFT)
        texYzLo.move_to(arrowLo20Tail + 2.05*RIGHT)
        num5.next_to(arrowLo4, DOWN*0.15)
        num4.next_to(arrowLo8, DOWN*0.15)
        num2.next_to(arrowLo12, DOWN*0.15)
        num18.next_to(arrowLo18, DOWN*0.15)
        num2min.next_to(arrowLo16, DOWN*0.15)
        texz1.next_to(arrowLo5, RIGHT*0.1)
        texz2.next_to(arrowLo13, RIGHT*0.1)
        texz3.next_to(arrowLo17, RIGHT*0.1)


        self.play(Write(texXz), ShowCreation(arrowHi1))
        self.play(ShowCreation(rectH2z), Write(texH2z))
        self.play(ShowCreation(arrowHi2))
        self.play(ShowCreation(rectH1z), Write(texH1z))
        self.play(ShowCreation(arrowHi3), Write(texYz))

        self.play(Write(texXzeq))

        self.play(ShowCreation(arrowLo1), Write(texXzLo))
        self.play(ShowCreation(arrowLo2))
        self.play(ShowCreation(arrowLo5), ShowCreation(arrowLo4), ShowCreation(arrowLo3), Write(num5), Write(texz1))
        self.play(ShowCreation(arrowLo6), ShowCreation(arrowLo7), ShowCreation(arrowLo8), Write(num4))
        self.play(ShowCreation(arrowLo9))
        self.play(ShowCreation(arrowLo10))
        self.play(ShowCreation(arrowLo11), ShowCreation(arrowLo12), ShowCreation(arrowLo13), Write(num2), Write(texz2))
        self.play(ShowCreation(arrowLo17), ShowCreation(arrowLo18), ShowCreation(arrowLo19), Write(num18), Write(texz3))
        self.play(ShowCreation(arrowLo14), ShowCreation(arrowLo15), ShowCreation(arrowLo16), Write(num2min))
        self.play(ShowCreation(arrowLo20), Write(texYzLo))

        self.wait(4)
        self.clear()

