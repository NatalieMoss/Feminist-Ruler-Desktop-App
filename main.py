from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle, Line
from kivy.lang import Builder
from fractions import Fraction

class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.result_label_background = Rectangle(size=(200, 40), pos=(0, 0))  # Adjust the size
        # Set the canvas instructions for the background color and border
        with self.canvas.before:
            Color(0.0157, 0.2863, 0.2667, 1)  # green
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        # Update the rectangle's position and size when the layout is resized
        self.rect.pos = self.pos
        self.rect.size = self.size

    def convert(self):
        feet_text = self.ids.feet_input.text
        inches_text = self.ids.inches_input.text

        try:
            feet = int(feet_text) if feet_text else 0
            inches = float(Fraction(inches_text)) if inches_text else 0
            decimal_feet = feet + (inches / 12)
            result = decimal_feet * 1.207
            self.ids.result_label.text = f"Result: {result:.3f} nefeet"
        except ValueError:
            self.ids.result_label.text = "Invalid input"


class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()  # Directly return the CalculatorLayout as the root widget


if __name__ == "__main__":
    CalculatorApp().run()
