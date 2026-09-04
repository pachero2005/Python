from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

# Configuración de tamaño para simular móvil
Window.clearcolor = (0.06, 0.07, 0.1, 1)  # Fondo oscuro #0F111A

class CalculadoraKivy(App):
    def build(self):
        self.expresion = ""
        
        # Contenedor Principal
        layout_principal = BoxLayout(orientation='vertical', padding=15, spacing=10)

        # Pantalla de visualización (Texto)
        self.pantalla = Label(
            text="0", 
            font_size='36sp', 
            halign='right', 
            valign='middle',
            size_hint=(1, 0.25),
            color=(1, 1, 1, 1)
        )
        self.pantalla.bind(size=self.pantalla.setter('text_size'))
        layout_principal.add_widget(self.pantalla)

        # Rejilla para los botones
        grid_botones = GridLayout(cols=4, spacing=8, size_hint=(1, 0.75))

        botones = [
            ('C', (1, 0.32, 0.44, 1)), ('(', (0.16, 0.17, 0.26, 1)), (')', (0.16, 0.17, 0.26, 1)), ('/', (0.53, 0.86, 1, 1)),
            ('7', (0.13, 0.14, 0.2, 1)), ('8', (0.13, 0.14, 0.2, 1)), ('9', (0.13, 0.14, 0.2, 1)), ('*', (0.53, 0.86, 1, 1)),
            ('4', (0.13, 0.14, 0.2, 1)), ('5', (0.13, 0.14, 0.2, 1)), ('6', (0.13, 0.14, 0.2, 1)), ('-', (0.53, 0.86, 1, 1)),
            ('1', (0.13, 0.14, 0.2, 1)), ('2', (0.13, 0.14, 0.2, 1)), ('3', (0.13, 0.14, 0.2, 1)), ('+', (0.53, 0.86, 1, 1)),
            ('0', (0.13, 0.14, 0.2, 1)), ('.', (0.13, 0.14, 0.2, 1)), ('⌫', (0.16, 0.17, 0.26, 1)), ('=', (0.76, 0.91, 0.55, 1))
        ]

        for texto, color_fondo in botones:
            btn = Button(
                text=texto,
                font_size='22sp',
                background_normal='',
                background_color=color_fondo,
                bold=True
            )
            # Determinar color de texto (Oscuro para botones de operaciones, claro para números)
            if texto in ['/', '*', '-', '+', '=']:
                btn.color = (0.06, 0.07, 0.1, 1)
            else:
                btn.color = (1, 1, 1, 1)

            btn.bind(on_press=self.on_click_boton)
            grid_botones.add_widget(btn)

        layout_principal.add_widget(grid_botones)
        return layout_principal

    def on_click_boton(self, instance):
        char = instance.text
        
        if char == 'C':
            self.expresion = ""
        elif char == '⌫':
            self.expresion = self.expresion[:-1]
        elif char == '=':
            try:
                self.expresion = str(eval(self.expresion))
            except Exception:
                self.expresion = "Error"
        else:
            if self.expresion == "Error":
                self.expresion = ""
            self.expresion += char

        self.pantalla.text = self.expresion if self.expresion != "" else "0"

if _name_ == "_main_":
    CalculadoraKivy().run()