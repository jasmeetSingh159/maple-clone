from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.core.text import LabelBase
from core.evaluator import evaluate_expression

class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 5  # Add some space between widgets
        self.padding = [10, 10, 10, 10]  # Padding around the layout
        Window.clearcolor = (1, 1, 1, 1)  # White background

        # Register the custom font
        LabelBase.register(name='TimesNewRoman', fn_regular='assets/fonts/times_new_roman.ttf')

        # Add the first input field
        self.add_input_field()

    def add_input_field(self):
        input_field = TextInput(multiline=False, font_name='TimesNewRoman', font_size=32, size_hint_y=None, height=40)
        input_field.bind(on_text_validate=self.on_enter)
        self.add_widget(input_field)

    def on_enter(self, instance):
        # Evaluate the expression
        input_text = instance.text.strip()
        result = evaluate_expression(input_text)

        # Display the result in a new read-only TextInput below the input field
        result_display = TextInput(text=(input_text + " = " + str(result)), readonly=True, font_name='TimesNewRoman', font_size=32, size_hint_y=None, height=40)
        self.add_widget(result_display)

        # Disable the current input field
        instance.readonly = True

        # Add a new input field for further inputs
        self.add_input_field()