import random
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.utils import get_color_from_hex

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
    canvas.before:
        Color:
            rgba: get_color_from_hex('#F2ECF8')
        Rectangle:
            pos: self.pos
            size: self.size
    
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20
        
        Label:
            text: "✨ ¡Multipepes! ✨"
            font_size: '36sp'
            bold: True
            color: get_color_from_hex('#7E37A6')
            size_hint_y: 0.15

        Label:
            id: estrellas_menu
            text: "⭐ Estrellas Totales: 0"
            font_size: '22sp'
            bold: True
            color: get_color_from_hex('#E59B00')
            size_hint_y: 0.10

        Label:
            text: "🦄   ✏️   🎈   🧸"
            font_size: '50sp'
            size_hint_y: 0.25

        Button:
            text: "¡Aprender las Tablas! 📚"
            font_size: '20sp'
            bold: True
            background_normal: ''
            background_color: get_color_from_hex('#33B249')
            size_hint_y: 0.13
            on_release: root.manager.current = 'tablas'

        Button:
            text: "¡Ponerse a Prueba! 🎮"
            font_size: '20sp'
            bold: True
            background_normal: ''
            background_color: get_color_from_hex('#E64C80')
            size_hint_y: 0.13
            on_release: root.manager.get_screen('juego').iniciar_juego(); root.manager.current = 'juego'

        Button:
            text: "Mis Trofeos 🏆"
            font_size: '20sp'
            bold: True
            background_normal: ''
            background_color: get_color_from_hex('#E5B21A')
            size_hint_y: 0.13
            on_release: root.manager.get_screen('trofeos').actualizar_pantalla(); root.manager.current = 'trofeos'

<TablasScreen>:
    name: 'tablas'
    canvas.before:
        Color:
            rgba: get_color_from_hex('#E6F2FF')
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15

        Label:
            text: "Elige una Tabla 📚"
            font_size: '30sp'
            bold: True
            color: get_color_from_hex('#1A66CC')
            size_hint_y: 0.12

        GridLayout:
            cols: 2
            spacing: 15
            size_hint_y: 0.75
            
            Button:
                text: "Tabla del 1  🐸"
                font_size: '18sp'
                bold: True
                background_normal: ''
                background_color: get_color_from_hex('#66B2FF')
                on_release: root.ir_a_tabla(1)
            Button:
                text: "Tabla del 2  🦊"
                font_size: '18sp'
                bold: True
                background_normal: ''
                background_color: get_color_from_hex('#FF9933')
                on_release: root.ir_a_tabla(2)
            Button:
                text: "Tabla del 3  🦁"
                font_size: '18sp'
                bold: True
                background_normal: ''
                background_color: get_color_from_hex('#FF6666')
                on_release: root.ir_a_tabla(3)
            Button:
                text: "Tabla del 4  🐼"
                font_size: '18sp'
                bold: True
                background_normal: ''
                background_color: get_color_from_hex('#4CD980')
                on_release: root.ir_a_tabla(4)
            Button:
                text: "Tabla del 5  🐙"
                font_size: '18sp'
                bold: True
                background_normal: ''
                background_color: get_color_from_hex('#B266E6')
                on_release: root.ir_a_tabla(5)
            Button:
                text: "Tabla del 6  🐷"
                font_size: '18sp'
                bold: True
                background_normal: ''
                background_color: get_color_from_hex('#FF80B2')
                on_release: root.ir_a_tabla(6)
            Button:
                text: "Tabla del 7  🐵"
                font_size: '18sp'
                bold: True
                background_normal: ''
                background_color: get_color_from_hex('#996633')
                on_release: root.ir_a_tabla(7)
            Button:
                text: "Tabla del 8  🐥"
                font_size: '18sp'
                bold: True
                background_normal: ''
                background_color: get_color_from_hex('#E6CC1A')
                on_release: root.ir_a_tabla(8)
            Button:
                text: "Tabla del 9  🐳"
                font_size: '18sp'
                bold: True
                background_normal: ''
                background_color: get_color_from_hex('#1ACCE6')
                on_release: root.ir_a_tabla(9)
            Button:
                text: "Tabla del 10  🦄"
                font_size: '18sp'
                bold: True
                background_normal: ''
                background_color: get_color_from_hex('#9933CC')
                on_release: root.ir_a_tabla(10)

        Button:
            text: "Volver al Menú"
            font_size: '18sp'
            bold: True
            size_hint: (0.5, 0.1)
            pos_hint: {'center_x': 0.5}
            on_release: root.manager.current = 'menu'
'''
KV2 = '''
<EstudioScreen>:
    name: 'estudio'
    canvas.before:
        Color:
            rgba: get_color_from_hex('#FAFAD2')
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15

        Label:
            id: titulo_tabla
            text: "Tabla"
            font_size: '32sp'
            bold: True
            color: get_color_from_hex('#339999')
            size_hint_y: 0.12

        BoxLayout:
            size_hint_y: 0.75
            padding: 10
            canvas.before:
                Color:
                    rgba: get_color_from_hex('#26593F')
                Rectangle:
                    pos: self.pos
                    size: self.size
            ScrollView:
                Label:
                    id: contenido_tabla
                    text: ""
                    font_size: '26sp'
                    bold: True
                    halign: 'center'
                    size_hint_y: None
                    height: self.texture_size[1] + 20

        Button:
            text: "Atrás"
            font_size: '18sp'
            bold: True
            size_hint: (0.4, 0.1)
            pos_hint: {'center_x': 0.5}
            on_release: root.manager.current = 'tablas'

<JuegoScreen>:
    name: 'juego'
    canvas.before:
        Color:
            rgba: get_color_from_hex('#F0F7F0')
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15

        Label:
            id: puntaje_label
            text: "⭐ Estrellas: 0"
            font_size: '30sp'
            bold: True
            color: get_color_from_hex('#E59B00')
            size_hint_y: 0.10

        Label:
            id: racha_label
            text: "Progreso: 0/5"
            font_size: '18sp'
            color: get_color_from_hex('#666666')
            size_hint_y: 0.08

        Label:
            id: pregunta_label
            text: "¿?"
            font_size: '48sp'
            bold: True
            color: get_color_from_hex('#333380')
            size_hint_y: 0.22

        BoxLayout:
            orientation: 'vertical'
            spacing: 15
            size_hint_y: 0.50
            
            Button:
                id: opcion1
                text: "A"
                font_size: '24sp'
                bold: True
                background_normal: ''
                background_color: get_color_from_hex('#4D99E6')
                on_release: root.verificar_respuesta(self.text)
            Button:
                id: opcion2
                text: "B"
                font_size: '24sp'
                bold: True
                background_normal: ''
                background_color: get_color_from_hex('#E66666')
                on_release: root.verificar_respuesta(self.text)
            Button:
                id: opcion3
                text: "C"
                font_size: '24sp'
                bold: True
                background_normal: ''
                background_color: get_color_from_hex('#66B266')
                on_release: root.verificar_respuesta(self.text)

        Label:
            id: feedback_label
            text: ""
            font_size: '24sp'
            bold: True
            size_hint_y: 0.10

        Button:
            text: "Menú Principal"
            font_size: '16sp'
            bold: True
            size_hint: (0.4, 0.08)
            pos_hint: {'center_x': 0.5}
            on_release: root.al_menu()

<TrofeosScreen>:
    name: 'trofeos'
    canvas.before:
        Color:
            rgba: get_color_from_hex('#FAF0F0')
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15

        Label:
            text: "🏆 Mis Trofeos Ganados 🏆"
            font_size: '28sp'
            bold: True
            color: get_color_from_hex('#CC8000')
            size_hint_y: 0.12

        ScrollView:
            size_hint_y: 0.76
            GridLayout:
                id: contenedor_trofeos
                cols: 2
                spacing: 15
                size_hint_y: None
                height: self.minimum_height
                padding: 10

        Button:
            text: "Menú Principal"
            font_size: '18sp'
            bold: True
            size_hint: (0.4, 0.1)
            pos_hint: {'center_x': 0.5}
            on_release: root.manager.current = 'menu'
'''

class MenuScreen(Screen):
    def on_enter(self):
        app = App.get_running_app()
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
            texto_tabla += f"{numero}  x  {i}   =   {numero * i}\\n\\n"
        self.ids.contenido_tabla.text = texto_tabla

class JuegoScreen(Screen):
    respuesta_correcta = 0
    tabla_actual = 1
    aciertos_consecutivos = 0

    def iniciar_juego(self):
        app = App.get_running_app()
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
        self.ids.opcion1.text = str(lista_opciones[0])
        self.ids.opcion2.text = str(lista_opciones[1])
        self.ids.opcion3.text = str(lista_opciones[2])

    def verificar_respuesta(self, texto_seleccionado):
        app = App.get_running_app()
        if int(texto_seleccionado) == self.respuesta_correcta:
            app.reproducir_sonido('acierto')
            app.datos['estrellas'] += 1
            self.aciertos_consecutivos += 1
            self.ids.puntaje_label.text = f"⭐ Estrellas: {app.datos['estrellas']}"
            
            if self.aciertos_consecutivos >= 5:
                tabla_str = str(self.tabla_actual)
                if not app.datos['trofeos'][tabla_str]:
                    app.datos['trofeos'][tabla_str] = True
                    self.ids.feedback_label.text = f"🏆 ¡NUEVO TROFEO TABLA DEL {tabla_str}! 🏆"
                else:
                    self.ids.feedback_label.text = "🎉 ¡Excelente! ¡Sigue así! 🎉"
                self.aciertos_consecutivos = 0
            else:
                self.ids.feedback_label.text = "🎉 ¡Excelente! 🎉"
            self.ids.feedback_label.color = get_color_from_hex('#339933')
            
            from kivy.clock import Clock
            Clock.schedule_once(lambda dt: self.iniciar_juego(), 1.5)
        else:
            app.reproducir_sonido('error')
            self.aciertos_consecutivos = 0
            self.ids.feedback_label.text = "💪 ¡Casi! Inténtalo otra vez 💪"
            self.ids.feedback_label.color = get_color_from_hex('#CC3333')
            self.ids.racha_label.text = f"Progreso Tabla del {self.tabla_actual}: 0/5"

    def al_menu(self):
        self.aciertos_consecutivos = 0
        self.manager.current = 'menu'

class TrofeosScreen(Screen):
    def actualizar_pantalla(self):
        self.ids.contenedor_trofeos.clear_widgets()
        app = App.get_running_app()
        from kivy.uix.label import Label
        
        for i in range(1, 11):
            desbloqueado = app.datos['trofeos'][str(i)]
            texto = f"🏆 Tabla del {i}\\n¡Dominada!" if desbloqueado else f"🔒 Tabla del {i}\\n(5 aciertos)"
            color_txt = get_color_from_hex('#805500') if desbloqueado else get_color_from_hex('#777777')
            
            lbl = Label(
                text=texto,
                halign='center',
                bold=True,
                color=color_txt,
                size_hint_y=None,
                height=100
            )
            self.ids.contenedor_trofeos.add_widget(lbl)

class MultipepesApp(App):
    datos = {"estrellas": 0, "trofeos": {str(i): False for i in range(1, 11)}}

    def build(self):
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
