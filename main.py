from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from fractions import Fraction


class CalculatorLayout(BoxLayout):
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
