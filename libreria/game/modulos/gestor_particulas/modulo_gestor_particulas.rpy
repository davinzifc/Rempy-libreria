# ============================================================================
#  MODULO: GESTOR DE PARTICULAS (NIEVE, LLUVIA Y EFECTOS PERSONALIZADOS)
#  Version: 1.0
#  Compatibilidad: Ren'Py 7.x / 8.x
#  Licencia: Uso libre para la comunidad hispanohablante de Ren'Py.
#            Puedes copiar, modificar y redistribuir este archivo sin
#            necesidad de dar credito.
#
#  Para instrucciones de instalacion, ejemplos de uso dentro del guion y
#  mas detalles, abri el archivo "README.md" que viene junto a este
#  script, en esta misma carpeta.
#
#  Resumen rapido de uso (ver el README para mas ejemplos):
#      $ id = gp_crear_particulas(color="#FFFFFF", tamano_min=3, tamano_max=8,
#                                  cantidad=70, angulo_base=90, angulo_variacion=20,
#                                  velocidad_min=30, velocidad_max=80)
#      $ gp_terminar_particulas(id)       # apaga ese efecto en particular
#      $ gp_terminar_todas()              # apaga todos los efectos activos
#
#      $ id_nieve = gp_nieve()            # atajo: nieve ya configurada
#      $ id_lluvia = gp_lluvia()          # atajo: lluvia ya configurada
# ============================================================================


# ============================================================================
#  CONFIGURACION — esto es lo UNICO que normalmente necesitas tocar
# ----------------------------------------------------------------------------
#  No hace falta saber programar para esta parte: cambia el valor que
#  esta despues del signo "=" en cada linea (dejando las comillas si las
#  tiene) y guarda el archivo. Mas abajo, en la seccion "MOTOR", se arman
#  con estos valores los efectos listos para usar "nieve" y "lluvia".
#
#  Si mas adelante queres crear tus propios efectos (hojas, chispas,
#  polvo magico, petalos, etc.) mira la seccion "COMO CREAR TU PROPIO
#  EFECTO" del README.md: no hace falta tocar nada de este archivo para
#  eso, se hace desde tu propio script.rpy.
# ============================================================================

# ----------------------------------------------------------------------------
# --- EFECTO "NIEVE" ---------------------------------------------------------
# ----------------------------------------------------------------------------

# Cuantos copos hay en pantalla al mismo tiempo. Mas cantidad = efecto mas
# denso, pero tambien mas trabajo para la computadora. 50-100 es un buen
# punto de partida.
define GP_NIEVE_CANTIDAD = 150

# Color del copo de nieve, en formato "#RRGGBB" (o "#RRGGBBAA" si le queres
# dar una transparencia fija ademas de la que ya controla la opacidad de
# mas abajo). Solo se usa si GP_NIEVE_IMAGENES esta en None.
define GP_NIEVE_COLOR = "#FFFFFF"

# Lista de imagenes a usar como copos de nieve, por ejemplo:
#     define GP_NIEVE_IMAGENES = ["modulos/gestor_particulas/imagenes/copo.png"]
# Si le pasas mas de una imagen, cada copo elige una al azar. Dejalo en
# None para no usar imagenes: en ese caso los copos se dibujan solos,
# como circulos planos del color de arriba (no hace falta ningun archivo
# de imagen para que la nieve funcione).
define GP_NIEVE_IMAGENES = None

# Rango de tamanio de cada copo, en pixeles (de mas chico a mas grande).
# Cada copo elige un tamanio al azar dentro de este rango. Si queres que
# todos midan exactamente lo mismo, poné el mismo numero en los dos.
define GP_NIEVE_TAMANO_MIN = 3
define GP_NIEVE_TAMANO_MAX = 8

# Angulo de caida, en grados. Sirve para indicar hacia donde "sale" la
# particula:
#     0   = hacia la derecha
#     90  = derecho hacia abajo   (nieve y lluvia normalmente usan esto)
#     180 = hacia la izquierda
#     270 = hacia arriba          (util para chispas de fuego, por ejemplo)
define GP_NIEVE_ANGULO_BASE = 90

# Cuanto puede variar el angulo de cada copo, al azar, para los dos lados
# (por ejemplo, con base 90 y variacion 20, cada copo cae en algun angulo
# entre 70 y 110). Poné 0 si queres que todos caigan en linea exactamente
# igual, sin variacion.
define GP_NIEVE_ANGULO_VARIACION = 20

# Rango de velocidad de caida, en pixeles por segundo. Cada copo elige una
# velocidad al azar dentro de este rango (los copos mas rapidos dan
# sensacion de estar mas cerca de "camara"). Si queres que todos caigan a
# la misma velocidad, poné el mismo numero en los dos.
define GP_NIEVE_VELOCIDAD_MIN = 30
define GP_NIEVE_VELOCIDAD_MAX = 80

# ¿El movimiento es una linea recta (False) o tiene un vaiven lateral
# como si lo empujara el viento (True)? La nieve real casi nunca cae en
# linea perfectamente recta, por eso este efecto viene activado.
define GP_NIEVE_ONDULADO = True

# Que tan ancho es el vaiven lateral (en pixeles) y que tan rapido se
# repite (en "ondas" por segundo). Solo se usan si GP_NIEVE_ONDULADO es
# True. Numeros mas grandes = vaiven mas exagerado / mas rapido.
define GP_NIEVE_AMPLITUD_ONDULADO = 25
define GP_NIEVE_FRECUENCIA_ONDULADO = 0.6

# ¿Los copos van girando sobre si mismos mientras caen? Con copos
# circulares de color plano casi no se nota, pero si usas una imagen (por
# ejemplo un copo con forma de estrella) le da mucha vida al efecto.
define GP_NIEVE_ROTAR = False

# Rango de opacidad de cada copo (0.0 = invisible, 1.0 = totalmente
# solido). Variar la opacidad entre copos da sensacion de profundidad
# (unos parecen estar mas lejos que otros).
define GP_NIEVE_OPACIDAD_MIN = 0.5
define GP_NIEVE_OPACIDAD_MAX = 1.0

# Orden de dibujado ("zorder") del efecto dentro de su capa. No hace
# falta tocar esto salvo que sepas lo que haces: el valor por defecto ya
# deja la nieve por debajo del cuadro de dialogo. La CAPA en la que se
# muestran los efectos se controla con GP_CAPA_POR_DEFECTO, mas abajo en
# la seccion "MOTOR" (o pasando capa="..." a gp_crear_particulas() /
# gp_nieve() / gp_lluvia()).
define GP_NIEVE_ZORDER = -10


# ----------------------------------------------------------------------------
# --- EFECTO "LLUVIA" ---------------------------------------------------------
# ----------------------------------------------------------------------------

# Cuantas gotas hay en pantalla al mismo tiempo. La lluvia suele
# necesitar mas cantidad que la nieve para verse "tupida".
define GP_LLUVIA_CANTIDAD = 140

# Color de la gota. Un celeste/gris clarito suele verse bien sobre casi
# cualquier fondo. Solo se usa si GP_LLUVIA_IMAGENES esta en None.
define GP_LLUVIA_COLOR = "#9FC6FF"

# Lista de imagenes para la gota (igual que en la nieve). Dejalo en None
# para que la gota se dibuje sola, como un rectangulo (raya) plana del
# color de arriba: es la forma mas comun de representar lluvia y no
# necesita ningun archivo de imagen.
define GP_LLUVIA_IMAGENES = None

# Forma de la particula cuando NO se usa imagen: "circulo" o "rectangulo".
# Para lluvia, "rectangulo" da el clasico efecto de rayas cayendo.
define GP_LLUVIA_FORMA = "rectangulo"

# Rango de largo de cada gota (alto del rectangulo), en pixeles.
define GP_LLUVIA_TAMANO_MIN = 14
define GP_LLUVIA_TAMANO_MAX = 26

# Rango de ancho de cada gota (grosor del rectangulo), en pixeles. Solo
# se usa cuando GP_LLUVIA_FORMA es "rectangulo".
define GP_LLUVIA_ANCHO_MIN = 1
define GP_LLUVIA_ANCHO_MAX = 2

# Angulo de caida (ver la explicacion completa en la seccion de la
# nieve, mas arriba). La lluvia suele caer un poco inclinada en vez de
# derecha, como si la empujara el viento.
define GP_LLUVIA_ANGULO_BASE = 100
define GP_LLUVIA_ANGULO_VARIACION = 4

# Rango de velocidad de caida, en pixeles por segundo. La lluvia cae
# mucho mas rapido que la nieve.
define GP_LLUVIA_VELOCIDAD_MIN = 650
define GP_LLUVIA_VELOCIDAD_MAX = 950

# Rango de opacidad de cada gota (0.0 = invisible, 1.0 = totalmente
# solida).
define GP_LLUVIA_OPACIDAD_MIN = 0.35
define GP_LLUVIA_OPACIDAD_MAX = 0.7

# Orden de dibujado (ver la explicacion en la seccion de la nieve).
define GP_LLUVIA_ZORDER = -10


# ============================================================================
#  A PARTIR DE ACA: EL "MOTOR" DEL MODULO
# ----------------------------------------------------------------------------
#  No necesitas editar nada de lo que sigue para usar el modulo. Si no
#  sabes programar, es mejor que no lo toques. Si queres crear tus
#  propios efectos personalizados (mas alla de nieve y lluvia), no hace
#  falta editar esto: se hace llamando a GP_TipoParticula(...) desde tu
#  propio script.rpy, como se explica en el README.md.
# ============================================================================
init python:

    import random as _gp_random
    import math as _gp_math
    import copy as _gp_copy

    class GP_TipoParticula(object):
        """
        Guarda TODA la configuracion de un efecto de particulas (nieve,
        lluvia, o cualquier efecto propio). No dibuja nada por si sola:
        es simplemente la "receta" que despues usa GestorParticulas para
        crear y animar las particulas.

        Parametros:

            imagenes (list o None):
                Lista de rutas de imagen (dentro de la carpeta "game/")
                para usar como particula. Si hay mas de una, cada
                particula elige una al azar. Si es None, la particula se
                dibuja como una figura de color plano (ver "color" y
                "forma") en vez de una imagen.

            color (str o list):
                Color plano de la particula, en formato "#RRGGBB". Se
                puede pasar una lista de colores (por ejemplo
                ["#FFFFFF", "#DDEEFF"]) para que cada particula elija uno
                al azar. Solo se usa si "imagenes" es None.

            forma ("circulo" o "rectangulo"):
                Forma de la particula de color plano. "circulo" sirve
                para nieve, polvo, chispas, etc. "rectangulo" sirve para
                lluvia o rayas de luz. Solo se usa si "imagenes" es None.

            tamano_min, tamano_max (numeros):
                Rango de tamanio de la particula, en pixeles (para
                imagenes, es el lado mas largo de la imagen ya
                escalada; para rectangulos, es el largo). Cada particula
                elige un tamanio al azar dentro del rango. Usa el mismo
                valor en los dos para que no varie.

            ancho_min, ancho_max (numeros o None):
                Solo para forma "rectangulo": rango de GROSOR del
                rectangulo (distinto del largo, que es "tamano"). Si se
                dejan en None, se usa el mismo valor que tamano_min /
                tamano_max (o sea, la particula queda cuadrada).

            cantidad (int):
                Cuantas particulas hay en pantalla al mismo tiempo.

            angulo_base (grados), angulo_variacion (grados):
                Direccion en la que "salen" las particulas. 0 = derecha,
                90 = abajo, 180 = izquierda, 270 = arriba. Cada
                particula recibe un angulo al azar entre
                (angulo_base - angulo_variacion) y
                (angulo_base + angulo_variacion). Con variacion 0, todas
                las particulas van exactamente en angulo_base.

            velocidad_min, velocidad_max (pixeles por segundo):
                Rango de velocidad de cada particula. Con los dos
                valores iguales, todas las particulas van a la misma
                velocidad (sin aleatoriedad).

            ondulado (bool), amplitud_ondulado (pixeles),
            frecuencia_ondulado (ondas por segundo):
                Si "ondulado" es True, el movimiento deja de ser una
                linea recta y se le suma un vaiven lateral tipo
                "viento" (util para nieve, hojas, polvo). Si es False,
                el movimiento es perfectamente lineal (util para
                lluvia).

            rotar (bool), rotacion_velocidad_min,
            rotacion_velocidad_max (grados por segundo):
                Si "rotar" es True, cada particula gira sobre si misma
                mientras se mueve, a una velocidad de rotacion al azar
                dentro del rango indicado (puede ser negativa, para que
                gire al reves). Solo tiene efecto visible con imagenes o
                con forma "rectangulo".

            opacidad_min, opacidad_max (de 0.0 a 1.0):
                Rango de transparencia de cada particula. Variarla da
                sensacion de profundidad.

            origen ("auto", "arriba", "abajo", "izquierda", "derecha" o
            "toda_pantalla"):
                De que borde de la pantalla "nacen" las particulas
                cuando se reciclan. Con "auto" (recomendado) se calcula
                solo a partir del angulo: si van para abajo nacen
                arriba, si van para arriba nacen abajo, si van para la
                derecha nacen a la izquierda, etc. "toda_pantalla" hace
                que puedan aparecer en cualquier parte (util para
                efectos ambiente como luciernagas o polvo en el aire,
                sobre todo combinado con tiempo_vida_min/max).

            origen_min, origen_max (de 0.0 a 1.0):
                Limita la zona del borde de nacimiento (por ejemplo,
                para que la nieve solo nazca en la mitad izquierda de la
                pantalla). Por defecto es 0.0 a 1.0, o sea, todo el
                borde.

            tiempo_vida_min, tiempo_vida_max (segundos, o None):
                Si se dejan en None (por defecto), cada particula vive
                hasta que sale de la pantalla, momento en el que
                reaparece del otro lado (reciclado infinito: es lo que
                se usa para nieve y lluvia). Si se les pone un numero,
                ademas la particula desaparece y se reinicia despues de
                ese tiempo, haya salido de pantalla o no (util para
                efectos que no dependen de "caer", como chispas que se
                apagan solas).

            zorder (int):
                Orden de dibujado del efecto dentro de su capa. Ver
                gp_crear_particulas() para mas detalle.
        """

        def __init__(
            self,
            imagenes=None,
            color="#FFFFFF",
            forma="circulo",
            tamano_min=6,
            tamano_max=6,
            ancho_min=None,
            ancho_max=None,
            cantidad=60,
            angulo_base=90,
            angulo_variacion=0,
            velocidad_min=60,
            velocidad_max=60,
            ondulado=False,
            amplitud_ondulado=15,
            frecuencia_ondulado=1.0,
            rotar=False,
            rotacion_velocidad_min=-60,
            rotacion_velocidad_max=60,
            opacidad_min=1.0,
            opacidad_max=1.0,
            origen="auto",
            origen_min=0.0,
            origen_max=1.0,
            tiempo_vida_min=None,
            tiempo_vida_max=None,
            zorder=-10,
        ):

            if forma not in ("circulo", "rectangulo"):
                raise Exception("GP_TipoParticula: 'forma' tiene que ser 'circulo' o 'rectangulo' (recibido: %r)" % (forma,))

            if origen not in ("auto", "arriba", "abajo", "izquierda", "derecha", "toda_pantalla"):
                raise Exception("GP_TipoParticula: 'origen' invalido: %r" % (origen,))

            self.imagenes = imagenes
            self.color = color
            self.forma = forma
            self.tamano_min = tamano_min
            self.tamano_max = tamano_max
            self.ancho_min = ancho_min
            self.ancho_max = ancho_max
            self.cantidad = cantidad
            self.angulo_base = angulo_base
            self.angulo_variacion = angulo_variacion
            self.velocidad_min = velocidad_min
            self.velocidad_max = velocidad_max
            self.ondulado = ondulado
            self.amplitud_ondulado = amplitud_ondulado
            self.frecuencia_ondulado = frecuencia_ondulado
            self.rotar = rotar
            self.rotacion_velocidad_min = rotacion_velocidad_min
            self.rotacion_velocidad_max = rotacion_velocidad_max
            self.opacidad_min = opacidad_min
            self.opacidad_max = opacidad_max
            self.origen = origen
            self.origen_min = origen_min
            self.origen_max = origen_max
            self.tiempo_vida_min = tiempo_vida_min
            self.tiempo_vida_max = tiempo_vida_max
            self.zorder = zorder

    def _gp_color_a_rgba(color_hex, opacidad):
        """
        Convierte un color en formato "#RRGGBB" o "#RRGGBBAA" y una
        opacidad (0.0 a 1.0) en una tupla (r, g, b, a) de 0 a 255, lista
        para usar con las funciones de dibujo de Ren'Py.
        """
        color_hex = color_hex.lstrip("#")
        r = int(color_hex[0:2], 16)
        g = int(color_hex[2:4], 16)
        b = int(color_hex[4:6], 16)
        a = int(color_hex[6:8], 16) if len(color_hex) >= 8 else 255
        a = int(a * max(0.0, min(1.0, opacidad)))
        return (r, g, b, a)

    class GestorParticulas(renpy.Displayable):
        """
        Displayable interno que crea, mueve y dibuja las particulas de
        un GP_TipoParticula. No se usa directamente desde el guion: se
        activa y se apaga con gp_crear_particulas() / gp_terminar_particulas(),
        mas abajo.
        """

        def __init__(self, tipo, **kwargs):
            super(GestorParticulas, self).__init__(**kwargs)
            self.tipo = tipo
            self.particulas = None
            self.st_anterior = None
            self.imagenes_resueltas = [renpy.displayable(ruta) for ruta in tipo.imagenes] if tipo.imagenes else []
            # Se completa la primera vez que se renderiza (necesita "st"
            # y "at", que recien estan disponibles en render()).
            self.imagenes_info = None

        def visit(self):
            # Le avisa a Ren'Py que precargue estas imagenes, para que
            # no se note una pausa la primera vez que aparece cada una.
            return list(self.imagenes_resueltas)

        def _elegir_origen(self, vx, vy):
            tipo = self.tipo
            origen = tipo.origen
            if origen == "auto":
                if abs(vy) >= abs(vx):
                    origen = "arriba" if vy >= 0 else "abajo"
                else:
                    origen = "izquierda" if vx >= 0 else "derecha"
            return origen

        def _generar_particula(self, ancho, alto, st, dispersar):
            tipo = self.tipo

            tamano = _gp_random.uniform(tipo.tamano_min, tipo.tamano_max)
            if tipo.ancho_min is not None:
                ancho_particula = _gp_random.uniform(tipo.ancho_min, tipo.ancho_max)
            else:
                ancho_particula = tamano

            angulo = _gp_math.radians(
                tipo.angulo_base + _gp_random.uniform(-tipo.angulo_variacion, tipo.angulo_variacion)
            )
            velocidad = _gp_random.uniform(tipo.velocidad_min, tipo.velocidad_max)
            vx = _gp_math.cos(angulo) * velocidad
            vy = _gp_math.sin(angulo) * velocidad

            origen = self._elegir_origen(vx, vy)
            margen = tamano + ancho_particula

            if dispersar and origen != "toda_pantalla":
                # Al activar el efecto por primera vez, se reparten las
                # particulas por toda la pantalla (no solo en el borde
                # de origen) para que el efecto se vea "en marcha" desde
                # el primer instante, en vez de aparecer todas juntas en
                # una linea.
                x = _gp_random.uniform(0, ancho)
                y = _gp_random.uniform(0, alto)
            elif origen == "toda_pantalla":
                x = _gp_random.uniform(0, ancho)
                y = _gp_random.uniform(0, alto)
            elif origen == "arriba":
                x = _gp_random.uniform(tipo.origen_min * ancho, tipo.origen_max * ancho)
                y = -margen
            elif origen == "abajo":
                x = _gp_random.uniform(tipo.origen_min * ancho, tipo.origen_max * ancho)
                y = alto + margen
            elif origen == "izquierda":
                x = -margen
                y = _gp_random.uniform(tipo.origen_min * alto, tipo.origen_max * alto)
            else:  # "derecha"
                x = ancho + margen
                y = _gp_random.uniform(tipo.origen_min * alto, tipo.origen_max * alto)

            color = tipo.color
            if isinstance(color, list):
                color = _gp_random.choice(color)

            imagen_indice = None
            escala = 1.0
            if self.imagenes_info:
                imagen_indice = _gp_random.randrange(len(self.imagenes_info))
                _disp, ancho_natural, alto_natural = self.imagenes_info[imagen_indice]
                referencia = max(1.0, float(max(ancho_natural, alto_natural)))
                escala = tamano / referencia

            vida = None
            if tipo.tiempo_vida_max is not None:
                vida = _gp_random.uniform(tipo.tiempo_vida_min, tipo.tiempo_vida_max)

            opacidad = _gp_random.uniform(tipo.opacidad_min, tipo.opacidad_max)

            # El color final (en RGBA) y las medidas en pixeles enteros
            # se calculan aca, UNA sola vez por particula, en vez de
            # recalcularlos en cada cuadro dentro de render(): con
            # muchas particulas en pantalla, evitar ese trabajo repetido
            # todo el tiempo es lo que mas ayuda a poder tener mas
            # cantidad sin que se note en el rendimiento.
            color_rgba = None
            radio_px = 0
            ancho_px = 0
            tamano_px = 0
            if imagen_indice is None:
                color_rgba = _gp_color_a_rgba(color, opacidad)
                if tipo.forma == "rectangulo":
                    ancho_px = max(1, int(ancho_particula))
                    tamano_px = max(1, int(tamano))
                else:
                    radio_px = max(1, int(tamano / 2.0))

            return {
                "x": x,
                "y": y,
                "vx": vx,
                "vy": vy,
                "tamano": tamano,
                "ancho": ancho_particula,
                "imagen_indice": imagen_indice,
                "escala": escala,
                "color_rgba": color_rgba,
                "radio_px": radio_px,
                "ancho_px": ancho_px,
                "tamano_px": tamano_px,
                "opacidad": opacidad,
                "rotacion": _gp_random.uniform(0, 360) if tipo.rotar else 0.0,
                "velocidad_rotacion": (
                    _gp_random.uniform(tipo.rotacion_velocidad_min, tipo.rotacion_velocidad_max)
                    if tipo.rotar else 0.0
                ),
                "fase_ondulado": _gp_random.uniform(0, 2 * _gp_math.pi),
                "nacimiento": st,
                "vida": vida,
            }

        def render(self, width, height, st, at):
            tipo = self.tipo

            # La primera vez que se dibuja, se mide el tamanio natural
            # de cada imagen (para poder escalarla despues a "tamano").
            if tipo.imagenes and self.imagenes_info is None:
                self.imagenes_info = []
                for disp in self.imagenes_resueltas:
                    render_natural = renpy.render(disp, width, height, st, at)
                    self.imagenes_info.append((disp, render_natural.width, render_natural.height))

            # La primera vez que se dibuja, se crean todas las
            # particulas de una.
            if self.particulas is None:
                self.particulas = [
                    self._generar_particula(width, height, st, True)
                    for _ in range(tipo.cantidad)
                ]
                self.st_anterior = st

            dt = st - self.st_anterior
            self.st_anterior = st
            # Si el tiempo retrocedio (rollback) o hubo un salto muy
            # grande (por ejemplo, el juego estuvo pausado), se ignora
            # ese instante en vez de mover las particulas de un salto.
            if dt < 0 or dt > 0.25:
                dt = 0.0

            r = renpy.Render(width, height)
            lienzo = r.canvas()
            margen = tipo.tamano_max * 2 + tipo.amplitud_ondulado + 20

            # Se sacan del bucle los valores que no cambian particula a
            # particula (no cambian en todo este render()), para no
            # tener que consultarlos de nuevo en cada vuelta: con
            # cientos de particulas, esa consulta repetida se nota.
            particulas = self.particulas
            rotar = tipo.rotar
            ondulado = tipo.ondulado
            frecuencia_ondulado = tipo.frecuencia_ondulado
            amplitud_ondulado = tipo.amplitud_ondulado
            forma_rectangulo = tipo.forma == "rectangulo"
            imagenes_info = self.imagenes_info

            for indice in range(len(particulas)):
                p = particulas[indice]

                p["x"] += p["vx"] * dt
                p["y"] += p["vy"] * dt
                if rotar:
                    p["rotacion"] = (p["rotacion"] + p["velocidad_rotacion"] * dt) % 360.0

                vencida = p["vida"] is not None and (st - p["nacimiento"]) > p["vida"]
                fuera_de_pantalla = (
                    p["x"] < -margen or p["x"] > width + margen or
                    p["y"] < -margen or p["y"] > height + margen
                )

                if vencida or fuera_de_pantalla:
                    p = self._generar_particula(width, height, st, False)
                    particulas[indice] = p

                x_dibujo = p["x"]
                if ondulado:
                    fase = st * frecuencia_ondulado * 2 * _gp_math.pi + p["fase_ondulado"]
                    x_dibujo += _gp_math.sin(fase) * amplitud_ondulado

                imagen_indice = p["imagen_indice"]
                if imagen_indice is not None:
                    disp, _aw, _ah = imagenes_info[imagen_indice]
                    transformada = Transform(disp, zoom=p["escala"], rotate=p["rotacion"], alpha=p["opacidad"])
                    render_hijo = renpy.render(transformada, width, height, st, at)
                    hw, hh = render_hijo.width, render_hijo.height
                    r.blit(render_hijo, (x_dibujo - hw / 2.0, p["y"] - hh / 2.0))
                elif forma_rectangulo:
                    aw = p["ancho_px"]
                    ah = p["tamano_px"]
                    lienzo.rect(p["color_rgba"], (int(x_dibujo - aw / 2.0), int(p["y"] - ah / 2.0), aw, ah))
                else:
                    lienzo.circle(p["color_rgba"], (int(x_dibujo), int(p["y"])), p["radio_px"])

            # Vuelve a pedir un cuadro nuevo lo antes posible, para que
            # la animacion sea continua.
            renpy.redraw(self, 0)

            return r

    # "Recetas" de nieve y lluvia ya armadas, a partir de las variables
    # de la seccion "CONFIGURACION", arriba del todo de este archivo.
    # Las usan gp_nieve() y gp_lluvia(), mas abajo, pero tambien las
    # podes usar vos directamente: gp_crear_particulas(tipo=GP_NIEVE).
    GP_NIEVE = GP_TipoParticula(
        imagenes=GP_NIEVE_IMAGENES,
        color=GP_NIEVE_COLOR,
        forma="circulo",
        tamano_min=GP_NIEVE_TAMANO_MIN,
        tamano_max=GP_NIEVE_TAMANO_MAX,
        cantidad=GP_NIEVE_CANTIDAD,
        angulo_base=GP_NIEVE_ANGULO_BASE,
        angulo_variacion=GP_NIEVE_ANGULO_VARIACION,
        velocidad_min=GP_NIEVE_VELOCIDAD_MIN,
        velocidad_max=GP_NIEVE_VELOCIDAD_MAX,
        ondulado=GP_NIEVE_ONDULADO,
        amplitud_ondulado=GP_NIEVE_AMPLITUD_ONDULADO,
        frecuencia_ondulado=GP_NIEVE_FRECUENCIA_ONDULADO,
        rotar=GP_NIEVE_ROTAR,
        opacidad_min=GP_NIEVE_OPACIDAD_MIN,
        opacidad_max=GP_NIEVE_OPACIDAD_MAX,
        zorder=GP_NIEVE_ZORDER,
    )

    GP_LLUVIA = GP_TipoParticula(
        imagenes=GP_LLUVIA_IMAGENES,
        color=GP_LLUVIA_COLOR,
        forma=GP_LLUVIA_FORMA,
        tamano_min=GP_LLUVIA_TAMANO_MIN,
        tamano_max=GP_LLUVIA_TAMANO_MAX,
        ancho_min=GP_LLUVIA_ANCHO_MIN,
        ancho_max=GP_LLUVIA_ANCHO_MAX,
        cantidad=GP_LLUVIA_CANTIDAD,
        angulo_base=GP_LLUVIA_ANGULO_BASE,
        angulo_variacion=GP_LLUVIA_ANGULO_VARIACION,
        velocidad_min=GP_LLUVIA_VELOCIDAD_MIN,
        velocidad_max=GP_LLUVIA_VELOCIDAD_MAX,
        ondulado=False,
        opacidad_min=GP_LLUVIA_OPACIDAD_MIN,
        opacidad_max=GP_LLUVIA_OPACIDAD_MAX,
        zorder=GP_LLUVIA_ZORDER,
    )

    # Capa por defecto en la que se muestran los efectos. Se usa
    # "screens" (en vez de "master") para que el efecto NO se borre
    # solo cuando cambies de fondo con la instruccion "scene": se queda
    # prendido hasta que vos lo apagues con gp_terminar_particulas().
    GP_CAPA_POR_DEFECTO = "screens"

    # Contador interno para generar un identificador nuevo cada vez que
    # se crea un efecto con gp_crear_particulas(). Cada efecto activo
    # queda anotado en _gp_activos, con su identificador como clave y
    # la etiqueta/capa de su pantalla como valor (necesario para poder
    # apagarlo despues con gp_terminar_particulas(id)).
    _gp_contador = 0
    _gp_activos = {}

    def gp_crear_particulas(tipo=None, capa=None, **parametros):
        """
        Crea y muestra un efecto de particulas nuevo, armado a partir de
        los parametros que le pases (sin depender de que exista ningun
        efecto predefinido). Devuelve un identificador (un numero) que
        despues usas con gp_terminar_particulas(id) para apagar
        ESE efecto en particular. Podes tener muchos efectos distintos
        activos al mismo tiempo, cada uno con su propio identificador.

        Le podes pasar, con nombre, cualquiera de los parametros que
        recibe GP_TipoParticula (color, imagenes, forma, tamano_min,
        tamano_max, cantidad, angulo_base, angulo_variacion,
        velocidad_min, velocidad_max, ondulado, amplitud_ondulado,
        frecuencia_ondulado, rotar, rotacion_velocidad_min,
        rotacion_velocidad_max, opacidad_min, opacidad_max, origen,
        origen_min, origen_max, tiempo_vida_min, tiempo_vida_max,
        zorder). La explicacion completa de cada uno esta en el
        docstring de la clase GP_TipoParticula, un poco mas arriba en
        este mismo archivo. Los que no le pases quedan con su valor por
        defecto.

        Ejemplo (chispas de fuego, armadas al vuelo, sin ningun efecto
        predefinido ni ninguna imagen):

            $ id_chispas = gp_crear_particulas(
                color=["#FFCC66", "#FF9933", "#FF6600"], forma="circulo",
                tamano_min=2, tamano_max=5, cantidad=25,
                angulo_base=270, angulo_variacion=30,
                velocidad_min=30, velocidad_max=70,
                origen="abajo", tiempo_vida_min=0.8, tiempo_vida_max=1.6,
            )
            ...
            $ gp_terminar_particulas(id_chispas)

        Parametros propios de esta funcion (no de GP_TipoParticula):

            tipo (GP_TipoParticula o None):
                Si ya tenes armado un GP_TipoParticula de antes (por
                ejemplo, uno que queres reutilizar varias veces sin
                escribir todos sus parametros cada vez), se lo podes
                pasar directamente con tipo=...: en ese caso se ignora
                cualquier otro parametro.

            capa (str o None):
                En que capa se muestra el efecto. Si se deja en None,
                se usa GP_CAPA_POR_DEFECTO ("screens").
        """
        if tipo is None:
            tipo = GP_TipoParticula(**parametros)

        if capa is None:
            capa = GP_CAPA_POR_DEFECTO

        global _gp_contador
        _gp_contador += 1
        id_efecto = _gp_contador

        etiqueta = "gp_efecto_%d" % id_efecto
        instancia = GestorParticulas(tipo)
        _gp_activos[id_efecto] = (etiqueta, capa)

        # El zorder se pasa como argumento especial "_zorder" (y no como
        # clausula "zorder" dentro del screen) porque esa clausula se
        # evalua antes de que los parametros del screen (en este caso,
        # "instancia") esten disponibles.
        renpy.show_screen(
            "gp_efecto",
            _tag=etiqueta,
            _layer=capa,
            _zorder=tipo.zorder,
            instancia=instancia,
        )

        return id_efecto

    def gp_terminar_particulas(id_efecto):
        """
        Apaga (oculta) el efecto de particulas creado con
        gp_crear_particulas(), a partir del identificador que devolvio
        esa funcion. Si el identificador no corresponde a ningun efecto
        activo (por ejemplo, porque ya se habia apagado antes), no hace
        nada.
        """
        datos = _gp_activos.pop(id_efecto, None)
        if datos is None:
            return
        etiqueta, capa = datos
        renpy.hide_screen(etiqueta, layer=capa)

    def gp_terminar_todas():
        """Apaga todos los efectos de particulas que esten activos."""
        for id_efecto in list(_gp_activos.keys()):
            gp_terminar_particulas(id_efecto)

    def gp_efecto_activo(id_efecto):
        """Devuelve True si ese identificador corresponde a un efecto todavia activo."""
        return id_efecto in _gp_activos

    def _gp_tipo_con_cambios(tipo_base, cambios):
        """
        Devuelve una copia de "tipo_base" (un GP_TipoParticula) con los
        atributos de "cambios" (un diccionario) sobreescritos. Si
        "cambios" esta vacio, devuelve "tipo_base" tal cual, sin copiar.
        La usan gp_nieve() y gp_lluvia() para permitir ajustar la receta
        de nieve/lluvia sin tener que escribirla de nuevo entera.
        """
        if not cambios:
            return tipo_base
        nuevo = _gp_copy.copy(tipo_base)
        for clave, valor in cambios.items():
            setattr(nuevo, clave, valor)
        return nuevo

    def gp_nieve(capa=None, **cambios):
        """
        Atajo para crear el efecto de nieve ya configurado (ver los
        GP_NIEVE_* de la seccion "CONFIGURACION", arriba del todo del
        archivo). Devuelve un identificador, igual que
        gp_crear_particulas().

        Le podes pasar, con nombre, cualquier parametro de
        GP_TipoParticula para ajustar solo eso puntualmente, sin tocar
        la configuracion general. Por ejemplo, para una nevada mas
        densa solo en esta escena:

            $ id_nieve = gp_nieve(cantidad=150)
        """
        return gp_crear_particulas(tipo=_gp_tipo_con_cambios(GP_NIEVE, cambios), capa=capa)

    def gp_lluvia(capa=None, **cambios):
        """
        Atajo para crear el efecto de lluvia ya configurado (ver los
        GP_LLUVIA_* de la seccion "CONFIGURACION"). Funciona igual que
        gp_nieve(): devuelve un identificador y acepta parametros de
        GP_TipoParticula para ajustar puntualmente esta lluvia.
        """
        return gp_crear_particulas(tipo=_gp_tipo_con_cambios(GP_LLUVIA, cambios), capa=capa)


# Pantalla (screen) interna que efectivamente muestra el efecto en
# pantalla. No se usa directamente: la maneja gp_crear_particulas() /
# gp_terminar_particulas().
screen gp_efecto(instancia):
    add instancia
