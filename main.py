import ast
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import sympy as sp

class MainApp(App):
    def build(self):
        self.title = 'Maple Clone'

        layout = BoxLayout(orientation='vertical')

        # Input field
        self.inputField = TextInput(multiline=True, size_hint_y=None, height=150)
        layout.add_widget(self.inputField)

        # Output display
        self.outputDisplay = TextInput(multiline=True, readonly=True, size_hint_y=None, height=150)
        layout.add_widget(self.outputDisplay)

        # Button for evaluation
        self.evalButton = Button(text='Evaluate', size_hint_y=None, height=50)
        self.evalButton.bind(on_press=self.on_enter)
        layout.add_widget(self.evalButton)

        return layout

    def on_enter(self, instance):
        # Get the text from the input field
        input_text = self.inputField.text

        try:
            # Evaluate the expression using SymPy
            result = sp.sympify(input_text)
        except Exception as e:
            result = f"Error: {e}"

        # Display the result in the output field
        self.outputDisplay.text = str(result)

if __name__ == '__main__':
    MainApp().run()
