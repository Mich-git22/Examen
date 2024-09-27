class Nodo:
    def __init__(self, pregunta=None, respuesta=None):
        self.pregunta = pregunta  # Pregunta del nodo
        self.respuesta = respuesta  # Respuesta si es un nodo hoja
        self.si = None  # Nodo hijo cuando la respuesta es 'sí'
        self.no = None  # Nodo hijo cuando la respuesta es 'no'


class Akinator:
    def __init__(self):
        # Nodo raíz inicial con una pregunta básica
        self.raiz = Nodo(pregunta="¿Es un animal?")
        # Inicializar respuestas básicas para el árbol
        self.raiz.si = Nodo(respuesta="un perro")
        self.raiz.no = Nodo(respuesta="una silla")

    def jugar(self, nodo):
        if nodo.respuesta:  # Si el nodo tiene una respuesta
            respuesta_usuario = input(f"¿Estás pensando en {nodo.respuesta}? (sí/no): ").strip().lower()
            if respuesta_usuario == 'sí':
                print("¡Lo adiviné!")
            else:
                self.aprender(nodo)
        else:  # Si no es un nodo hoja, es una pregunta
            respuesta_usuario = input(nodo.pregunta + " (sí/no): ").strip().lower()
            if respuesta_usuario == 'sí':
                self.jugar(nodo.si)
            else:
                self.jugar(nodo.no)

    def aprender(self, nodo):
        # Pregunta por la respuesta correcta
        respuesta_correcta = input("¿En qué estabas pensando?: ").strip()
        nueva_pregunta = input(f"Haz una pregunta para diferenciar {nodo.respuesta} de {respuesta_correcta}: ").strip()

        # Preguntar si la nueva respuesta sería 'sí' o 'no' para la nueva pregunta
        respuesta_nueva = input(f"Para {respuesta_correcta}, ¿la respuesta sería 'sí' o 'no'? (sí/no): ").strip().lower()

        # Crear nuevos nodos para la respuesta correcta y la respuesta incorrecta
        nodo_si = Nodo(respuesta=respuesta_correcta)
        nodo_no = Nodo(respuesta=nodo.respuesta)

        # Actualizar el nodo actual con la nueva pregunta
        nodo.pregunta = nueva_pregunta
        if respuesta_nueva == 'sí':
            nodo.si = nodo_si
            nodo.no = nodo_no
        else:
            nodo.si = nodo_no
            nodo.no = nodo_si

        # Eliminar la respuesta anterior ya que ahora es una pregunta
        nodo.respuesta = None

    def iniciar_juego(self):
        while True:
            print("\n¡Piensa en algo y trataré de adivinarlo!")
            self.jugar(self.raiz)
            jugar_otra_vez = input("\n¿Quieres jugar otra vez? (sí/no): ").strip().lower()
            if jugar_otra_vez != 'sí':
                print("¡Gracias por jugar!")
                break


# Inicializar y comenzar el juego
if __name__ == "__main__":
    akinator = Akinator()
    akinator.iniciar_juego()
