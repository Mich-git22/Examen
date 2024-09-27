import tkinter as tk
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
import random


class JuegoMexicanosDijeron:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego 100 Mexicanos Dijeron")
        self.root.geometry("600x400")
        self.root.configure(bg="#4A90E2")  # Color azul
        self.usuario = ""
        self.puntaje = 0
        self.respuestas_seleccionadas = []  # Para almacenar las respuestas seleccionadas
        self.preguntas = self.cargar_preguntas()
        self.nivel = 0  # Inicializar nivel
        self.timer_label = None  # Label del temporizador
        self.timer = None  # Temporizador

        # Interfaz de usuario
        self.lbl_instrucciones = tk.Label(root, text="¡Bienvenido al juego de 100 Mexicanos Dijeron!", bg="#4A90E2",
                                          fg="#FFFFFF", font=("Helvetica", 16))
        self.lbl_instrucciones.pack(pady=20)

        self.btn_ingresar_nombre = tk.Button(root, text="Ingresar Nombre", command=self.ingresar_nombre, bg="#50E3C2",
                                             fg="white", font=("Helvetica", 12))
        self.btn_ingresar_nombre.pack(pady=10)

        self.btn_puntaje = tk.Button(root, text="Ver Puntaje", command=self.abrir_ventana_puntaje, bg="#50E3C2",
                                     fg="white", font=("Helvetica", 12))
        self.btn_puntaje.pack(pady=10)

    def cargar_preguntas(self):
        # Definir preguntas y respuestas
        return {
            "Menciona un lenguaje de programación.": [
                {"respuesta": "Python", "puntos": 100},
                {"respuesta": "Java", "puntos": 80},
                {"respuesta": "JavaScript", "puntos": 70},
                {"respuesta": "C++", "puntos": 50},
                {"respuesta": "Ruby", "puntos": 30}
            ],
            "¿Qué lenguaje se utiliza para el desarrollo web?": [
                {"respuesta": "HTML", "puntos": 100},
                {"respuesta": "CSS", "puntos": 80},
                {"respuesta": "JavaScript", "puntos": 70},
                {"respuesta": "PHP", "puntos": 50},
                {"respuesta": "Python", "puntos": 30}
            ],
            "Menciona un sistema operativo.": [
                {"respuesta": "Windows", "puntos": 100},
                {"respuesta": "Linux", "puntos": 80},
                {"respuesta": "macOS", "puntos": 70},
                {"respuesta": "Ubuntu", "puntos": 50},
                {"respuesta": "Android", "puntos": 30}
            ]
        }

    def ingresar_nombre(self):
        self.usuario = simpledialog.askstring("Nombre del Jugador", "Por favor, ingresa tu nombre:")
        if self.usuario:
            self.lbl_instrucciones.config(text=f"¡Bienvenido, {self.usuario}! ¿Listo para jugar?")
            self.mostrar_instrucciones()  # Mostrar instrucciones después de ingresar el nombre

    def mostrar_instrucciones(self):
        instrucciones = (
            "Instrucciones del Juego:\n"
            "1. El juego consiste en adivinar las respuestas más populares a las preguntas.\n"
            "2. Se te hará una pregunta y deberás ingresar una respuesta.\n"
            "3. Cada respuesta correcta suma puntos según la popularidad de la respuesta.\n"
            "4. Se presentarán varias preguntas y al final se mostrará tu puntaje total.\n"
            "5. Puedes pedir pistas y también hay un límite de tiempo por pregunta."
        )
        messagebox.showinfo("Instrucciones", instrucciones)
        self.jugar()  # Comenzar el juego después de mostrar instrucciones

    def jugar(self):
        self.puntaje = 0
        self.respuestas_seleccionadas = []  # Reiniciar las respuestas seleccionadas
        self.nivel = 0  # Reiniciar el nivel

        # Mezclar preguntas al inicio del juego
        self.lista_preguntas = list(self.preguntas.keys())
        random.shuffle(self.lista_preguntas)

        # Comenzar el juego
        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        if self.nivel < len(self.lista_preguntas):
            pregunta_actual = self.lista_preguntas[self.nivel]
            self.respuestas = self.preguntas[pregunta_actual]

            # Crear ventana para la pregunta
            self.ventana_pregunta = tk.Toplevel(self.root)
            self.ventana_pregunta.title("Pregunta")
            self.ventana_pregunta.configure(bg="#4A90E2")

            # Mostrar pregunta
            lbl_pregunta = tk.Label(self.ventana_pregunta, text=pregunta_actual, bg="#4A90E2", fg="#FFFFFF",
                                    font=("Helvetica", 16))
            lbl_pregunta.pack(pady=20)

            # Botón para pedir pista
            btn_pista = tk.Button(self.ventana_pregunta, text="Pedir Pista", command=self.dar_pista, bg="#50E3C2",
                                  fg="white", font=("Helvetica", 12))
            btn_pista.pack(pady=10)

            # Pedir respuesta al usuario
            self.respuesta_usuario = tk.StringVar()
            entry_respuesta = tk.Entry(self.ventana_pregunta, textvariable=self.respuesta_usuario, bg="#FFFFFF",
                                       font=("Helvetica", 12))
            entry_respuesta.pack(pady=10)

            # Botón para enviar respuesta
            btn_enviar = tk.Button(self.ventana_pregunta, text="Enviar Respuesta", command=self.verificar_respuesta,
                                   bg="#50E3C2", fg="white", font=("Helvetica", 12))
            btn_enviar.pack(pady=10)

            # Temporizador
            self.timer_label = tk.Label(self.ventana_pregunta, text="Tiempo: 10", bg="#4A90E2", fg="#FFFFFF",
                                        font=("Helvetica", 14))
            self.timer_label.pack(pady=10)

            self.start_timer(10)  # Iniciar temporizador de 10 segundos

        else:
            self.mostrar_resultados()  # Mostrar resultados al finalizar

    def start_timer(self, tiempo):
        if tiempo > 0:
            self.timer_label.config(text=f"Tiempo: {tiempo}")
            self.timer = self.root.after(1000, self.start_timer, tiempo - 1)
        else:
            messagebox.showinfo("Tiempo Excedido", "Se acabó el tiempo para esta pregunta.")
            self.ventana_pregunta.destroy()  # Cerrar ventana de pregunta
            self.nivel += 1  # Aumentar nivel
            self.mostrar_pregunta()  # Mostrar la siguiente pregunta

    def dar_pista(self):
        # Proporcionar una pista aleatoria sobre la respuesta
        respuesta_correcta = random.choice(self.respuestas)
        pista = f"La respuesta comienza con la letra: {respuesta_correcta['respuesta'][0]}"
        messagebox.showinfo("Pista", pista)

    def verificar_respuesta(self):
        respuesta_usuario = self.respuesta_usuario.get()
        respuesta_encontrada = False

        for respuesta in self.respuestas:
            if respuesta_usuario and respuesta_usuario.lower() == respuesta['respuesta'].lower():
                self.puntaje += respuesta['puntos']
                self.respuestas_seleccionadas.append(
                    (respuesta['respuesta'], respuesta['puntos']))  # Guardar respuesta y puntaje
                respuesta_encontrada = True

        if not respuesta_encontrada:
            messagebox.showinfo("Respuesta Incorrecta", "Respuesta no válida.")

        self.ventana_pregunta.destroy()  # Cerrar ventana de pregunta
        self.nivel += 1  # Aumentar nivel
        self.start_timer(0)  # Detener temporizador
        self.mostrar_pregunta()  # Mostrar la siguiente pregunta

    def mostrar_resultados(self):
        resultado = f"¡Juego terminado, {self.usuario}! Tu puntaje total es: {self.puntaje} puntos.\n\n"
        resultado += "Respuestas y puntajes obtenidos:\n"
        for respuesta, puntos in self.respuestas_seleccionadas:
            resultado += f"- {respuesta}: {puntos} puntos\n"

        messagebox.showinfo("Resultados", resultado)

    def abrir_ventana_puntaje(self):
        ventana_puntaje = tk.Toplevel(self.root)
        ventana_puntaje.title("Puntaje del Jugador")
        ventana_puntaje.geometry("300x200")
        ventana_puntaje.configure(bg="#4A90E2")  # Color azul de fondo

        lbl_puntaje = tk.Label(ventana_puntaje, text=f"Puntaje Total: {self.puntaje} puntos", font=("Helvetica", 12),
                               bg="#4A90E2", fg="#FFFFFF")
        lbl_puntaje.pack(pady=10)

        lbl_nivel = tk.Label(ventana_puntaje, text=f"Nivel Alcanzado: {self.nivel}", font=("Helvetica", 12),
                             bg="#4A90E2", fg="#FFFFFF")
        lbl_nivel.pack(pady=10)

        btn_cerrar = tk.Button(ventana_puntaje, text="Cerrar", command=ventana_puntaje.destroy, bg="#f44336",
                               fg="white")
        btn_cerrar.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoMexicanosDijeron(root)
    root.mainloop()
