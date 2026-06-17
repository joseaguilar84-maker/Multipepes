import random
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

Window.size = (450, 750)

KV = '''
ScreenManager:
    MenuScreen:
    TablasScreen:
    EstudioScreen:
    JuegoScreen:
    TrofeosScreen:

<MenuScreen>:
    name: 'menu'
    MDFloatLayout:
        md_bg_color: 0.95, 0.92, 0.98, 1
        MDLabel:
            text: "✨ ¡Multipepes! ✨"
            font_style: "H3"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.85}
            theme_text_color: "Custom"
            text_color: 0.5, 0.2, 0.7, 1
            bold: True
        MDLabel:
            id: estrellas_menu
            text: "⭐ Estrellas Totales: 0"
            font_style: "H6"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.76}
            theme_text_color: "Custom"
            text_color: 0.9, 0.6, 0, 1
            bold: True
        MDLabel:
            text: "🦄   ✏️   🎈   🧸"
            font_style: "H2"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.62}
        MDFillRoundFlatIconButton:
            icon: "book-open-variant"
            text: "¡Aprender las Tablas!"
            font_size: "20sp"
            md_bg_color: 0.2, 0.7, 0.3, 1
            pos_hint: {"center_x": 0.5, "center_y": 0.44}
            size_hint: (0.7, 0.08)
            on_release: root.manager.current = 'tablas'
        MDFillRoundFlatIconButton:
            icon: "controller-classic"
            text: "¡Ponerse a Prueba!"
            font_size: "20sp"
            md_bg_color: 0.9, 0.3, 0.5, 1
            pos_hint: {"center_x": 0.5, "center_y": 0.32}
            size_hint: (0.7, 0.08)
            on_release: root.manager.get_screen('juego').iniciar_juego(); root.manager.current = 'juego'
        MDFillRoundFlatIconButton:
            icon: "trophy"
            text: "Mis Trofeos"
            font_size: "20sp"
            md_bg_color: 0.9, 0.7, 0.1, 1
            pos_hint: {"center_x": 0.5, "center_y": 0.20}
            size_hint: (0.7, 0.08)
            on_release: root.manager.get_screen('trofeos').actualizar_pantalla(); root.manager.current = 'trofeos'

<TablasScreen>:
    name: 'tablas'
    MDFloatLayout:
        md_bg_color: 0.9, 0.95, 1, 1
        MDLabel:
            text: "Elige una Tabla 📚"
            font_style: "H4"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.92}
            bold: True
            text_color: 0.1, 0.4, 0.8, 1
            theme_text_color: "Custom"
        MDGridLayout:
            cols: 2
            spacing: "20dp"
            size_hint: (0.85, 0.7)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            MDFillRoundFlatButton:
                text: "Tabla del 1  🐸"
                md_bg_color: 0.4, 0.7, 1, 1
                font_size: "18sp"
                on_release: root.ir_a_tabla(1)
            MDFillRoundFlatButton:
                text: "Tabla del 2  🦊"
                md_bg_color: 1, 0.6, 0.2, 1
                font_size: "18sp"
                on_release: root.ir_a_tabla(2)
            MDFillRoundFlatButton:
                text: "Tabla del 3  🦁"
                md_bg_color: 1, 0.4, 0.4, 1
                font_size: "18sp"
                on_release: root.ir_a_tabla(3)
            MDFillRoundFlatButton:
                text: "Tabla del 4  🐼"
                md_bg_color: 0.3, 0.8, 0.5, 1
                font_size: "18sp"
                on_release: root.ir_a_tabla(4)
            MDFillRoundFlatButton:
                text: "Tabla del 5  🐙"
                md_bg_color: 0.7, 0.4, 0.9, 1
                font_size: "18sp"
                on_release: root.ir_a_tabla(5)
            MDFillRoundFlatButton:
                text: "Tabla del 6  🐷"
                md_bg_color: 1, 0.5, 0.7, 1
                font_size: "18sp"
                on_release: root.ir_a_tabla(6)
            MDFillRoundFlatButton:
                text: "Tabla del 7  🐵"
                md_bg_color: 0.6, 0.4, 0.2, 1
                font_size: "18sp"
                on_release: root.ir_a_tabla(7)
            MDFillRoundFlatButton:
                text: "Tabla del 8  🐥"
                md_bg_color: 0.9, 0.8, 0.1, 1
                font_size: "18sp"
                on_release: root.ir_a_tabla(8)
            MDFillRoundFlatButton:
                text: "Tabla del 9  🐳"
                md_bg_color: 0.1, 0.7, 0.8, 1
                font_size: "18sp"
                on_release: root.ir_a_tabla(9)
            MDFillRoundFlatButton:
                text: "Tabla del 10  🦄"
                md_bg_color: 0.6, 0.2, 0.8, 1
                font_size: "18sp"
                on_release: root.ir_a_tabla(10)
        MDIconButton:
            icon: "arrow-left-bold-circle"
            user_font_size: "50sp"
            pos_hint: {"center_x": 0.15, "center_y": 0.08}
            on_release: root.manager.current = 'menu'

<EstudioScreen>:
    name: 'estudio'
    MDFloatLayout:
        md_bg_color: 0.98, 0.98, 0.92, 1
        MDLabel:
            id: titulo_tabla
            text: "Tabla"
            font_style: "H4"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.92}
            bold: True
            theme_text_color: "Custom"
            text_color: 0.2, 0.6, 0.6, 1
        MDCard:
            size_hint: (0.85, 0.68)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            elevation: 4
            padding: "20dp"
            md_bg_color: 0.15, 0.35, 0.25, 1
            radius:
            ScrollView:
                MDLabel:
                    id: contenido_tabla
                    text: ""
                    font_style: "H4" if self.width > 600 else "H5"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    line_height: 1.3
        MDIconButton:
            icon: "arrow-left-bold-circle"
            user_font_size: "50sp"
            pos_hint: {"center_x": 0.15, "center_y": 0.08}
            on_release: root.manager.current = 'tablas'
'''
KV2 = '''
<JuegoScreen>:
    name: 'juego'
    MDFloatLayout:
        md_bg_color: 0.94, 0.97, 0.94, 1
        MDLabel:
            id: puntaje_label
            text: "⭐ Estrellas: 0"
            font_style: "H4"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.91}
            theme_text_color: "Custom"
            text_color: 0.9, 0.6, 0, 1
            bold: True
        MDLabel:
            id: racha_label
            text: "Progreso Tabla Actual: 0/5"
            font_style: "Subtitle1"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.84}
            theme_text_color: "Secondary"
        MDLabel:
            id: pregunta_label
            text: "¿?"
            font_style: "H2"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.68}
            bold: True
            theme_text_color: "Custom"
            text_color: 0.2, 0.2, 0.5, 1
        MDFillRoundFlatButton:
            id: opcion1
            text: "A"
            font_size: "24sp"
            size_hint: (0.75, 0.09)
            pos_hint: {"center_x": -0.5, "center_y": 0.48}
            md_bg_color: 0.3, 0.6, 0.9, 1
            on_release: root.verificar_respuesta(self.text)
        MDFillRoundFlatButton:
            id: opcion2
            text: "B"
            font_size: "24sp"
            size_hint: (0.75, 0.09)
            pos_hint: {"center_x": 1.5, "center_y": 0.36}
            md_bg_color: 0.9, 0.4, 0.4, 1
            on_release: root.verificar_respuesta(self.text)
        MDFillRoundFlatButton:
            id: opcion3
            text: "C"
            font_size: "24sp"
            size_hint: (0.75, 0.09)
            pos_hint: {"center_x": -0.5, "center_y": 0.24}
            md_bg_color: 0.4, 0.7, 0.4, 1
            on_release: root.verificar_respuesta(self.text)
        MDLabel:
            id: feedback_label
            text: ""
            font_style: "H4"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.13}
            bold: True
        MDIconButton:
            icon: "home-circle"
            user_font_size: "50sp"
            pos_hint: {"center_x": 0.15, "center_y": 0.06}
            on_release: root.al_menu()

<TrofeosScreen>:
    name: 'trofeos'
    MDFloatLayout:
        md_bg_color: 0.98, 0.94, 0.94, 1
        MDLabel:
            text: "🏆 Mis Trofeos Ganados 🏆"
            font_style: "H4"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.90}
            bold: True
            text_color: 0.8, 0.5, 0, 1
            theme_text_color: "Custom"
        ScrollView:
            size_hint: (0.9, 0.72)
            pos_hint: {"center_x": 0.5, "center_y": 0.48}
            MDGridLayout:
                id: contenedor_trofeos
                cols: 2
                spacing: "15dp"
                size_hint_y: None
                height: self.minimum_height
                padding: "10dp"
        MDIconButton:
            icon: "arrow-left-bold-circle"
            user_font_size: "50sp"
            pos_hint: {"center_x": 0.15, "center_y": 0.07}
            on_release: root.manager.current = 'menu'
'''

class MenuScreen(Screen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.estrellas_menu.text = f"⭐ Estrellas Totales: {app.datos['estrellas']}"

class TablasScreen(Screen):
    def ir_a_tabla(self, numero_tabla):
        estudio_scr = self.manager.get_screen('estudio')
        estudio_scr.cargar_tabla(numero_tabla)
        self.manager.current = 'estudio'

class EstudioScreen(Screen):
    def cargar_tabla(self, numero):
        self.ids.titulo_tabla.text = f"Tabla del {numero} ✨"
        texto_tabla = ""
        for i in range(1, 11):
            texto_tabla += f"{numero}  x  {i}   =   {numero * i}\n"
        self.ids.contenido_tabla.text = texto_tabla

class JuegoScreen(Screen):
    respuesta_correcta = 0
    tabla_actual = 1
    aciertos_consecutivos = 0

    def iniciar_juego(self):
        app = MDApp.get_running_app()
        self.ids.puntaje_label.text = f"⭐ Estrellas: {app.datos['estrellas']}"
        self.tabla_actual = random.randint(1, 10)
        num2 = random.randint(1, 10)
        self.respuesta_correcta = self.tabla_actual * num2
        self.ids.pregunta_label.text = f"¿Cuánto es {self.tabla_actual} x {num2}? 🤔"
        self.ids.feedback_label.text = ""
        self.ids.racha_label.text = f"Progreso Tabla del {self.tabla_actual}: {self.aciertos_consecutivos}/5"
        opciones = {self.respuesta_correcta}
        while len(opciones) < 3:
            falsa = self.respuesta_correcta + random.randint(-4, 4)
            if falsa > 0 and falsa != self.respuesta_correcta:
                opciones.add(falsa)
        lista_opciones = list(opciones)
        random.shuffle(lista_opciones)
        self.ids.opcion1.text = str(lista_opciones)
        self.ids.opcion2.text = str(lista_opciones)
        self.ids.opcion3.text = str(lista_opciones)
        self.ids.opcion1.pos_hint = {"center_x": -0.5, "center_y": 0.48}
        self.ids.opcion2.pos_hint = {"center_x": 1.5, "center_y": 0.36}
        self.ids.opcion3.pos_hint = {"center_x": -0.5, "center_y": 0.24}
        Animation(pos_hint={"center_x": 0.5, "center_y": 0.48}, d=0.4, t='out_back').start(self.ids.opcion1)
        Animation(pos_hint={"center_x": 0.5, "center_y": 0.36}, d=0.5, t='out_back').start(self.ids.opcion2)
        Animation(pos_hint={"center_x": 0.5, "center_y": 0.24}, d=0.6, t='out_back').start(self.ids.opcion3)

    def verificar_respuesta(self, texto_seleccionado):
        app = MDApp.get_running_app()
        if int(texto_seleccionado) == self.respuesta_correcta:
            app.reproducir_sonido('acierto')
            app.datos['estrellas'] += 1
            self.aciertos_consecutivos += 1
            self.ids.puntaje_label.text = f"⭐ Estrellas: {app.datos['estrellas']}"
            if self.aciertos_consecutivos >= 5:
                tabla_str = str(self.tabla_actual)
                if not app.datos['trofeos'][tabla_str]:
                    app.datos['trofeos'][tabla_str] = True
                    self.ids.feedback_label.text = f"¡NUEVO TROFEO! 🏆 Tabla del {tabla_str}"
                else:
                    self.ids.feedback_label.text = "¡Excelente! 🎉 ¡Sigue así!"
                self.aciertos_consecutivos = 0
            else:
                self.ids.feedback_label.text = "¡Excelente! 🎉"
            self.ids.feedback_label.text_color = (0.2, 0.7, 0.2, 1)
            from kivy.clock import Clock
            Clock.schedule_once(lambda dt: self.iniciar_juego(), 1.6)
        else:
            app.reproducir_sonido('error')
            self.aciertos_consecutivos = 0
            self.ids.feedback_label.text = "¡Casi! Inténtalo de nuevo 💪"
            self.ids.feedback_label.text_color = (0.9, 0.3, 0.3, 1)
            self.ids.racha_label.text = f"Progreso Tabla del {self.tabla_actual}: 0/5"
        anim = Animation(font_size="32sp", duration=0.15) + Animation(font_size="24sp", duration=0.15)
        anim.start(self.ids.feedback_label)

    def al_menu(self):
        self.aciertos_consecutivos = 0
        self.manager.current = 'menu'

class TrofeosScreen(Screen):
    def actualizar_pantalla(self):
        self.ids.contenedor_trofeos.clear_widgets()
        app = MDApp.get_running_app()
        for i in range(1, 11):
            desbloqueado = app.datos['trofeos'][str(i)]
            texto = f"🏆 Tabla del {i}\n¡Dominada!" if desbloqueado else f"🔒 Tabla del {i}\n(5 aciertos)"
            color_fondo = (0.95, 0.85, 0.4, 1) if desbloqueado else (0.8, 0.8, 0.8, 1)
            from kivymd.uix.card import MDCard
            from kivymd.uix.label import MDLabel
            tarjeta = MDCard(orientation='vertical', padding="10dp", size_hint_y=None, height="110dp", md_bg_color=color_fondo, radius=)
            lbl = MDLabel(text=texto, halign="center", bold=True, theme_text_color="Custom", text_color=(0.3, 0.2, 0.1, 1) if desbloqueado else (0.5, 0.5, 0.5, 1))
            tarjeta.add_widget(lbl)
            self.ids.contenedor_trofeos.add_widget(tarjeta)

class MultipepesApp(MDApp):
    datos = {"estrellas": 0, "trofeos": {str(i): False for i in range(1, 11)}}

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Purple"
        completo = KV + KV2
        return Builder.load_string(completo)

    def reproducir_sonido(self, tipo):
        archivo = "acierto.wav" if tipo == 'acierto' else "error.wav"
        sonido = SoundLoader.load(archivo)
        if sonido:
            sonido.volume = 0.6
            sonido.play()

if __name__ == '__main__':
    MultipepesApp().run()
