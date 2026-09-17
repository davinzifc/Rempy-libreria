# ============================================================================
#  MODULO: EFECTO MAQUINA DE ESCRIBIR (TEXTO LETRA POR LETRA)
#  Version: 1.0
#  Compatibilidad: Ren'Py 7.x / 8.x
#  Licencia: Uso libre para la comunidad hispanohablante de Ren'Py.
#            Puedes copiar, modificar y redistribuir este archivo sin
#            necesidad de dar crédito.
# ============================================================================
#
# QUE HACE ESTE MODULO
# ----------------------------------------------------------------------------
# Hace que el texto de los dialogos aparezca letra por letra, como si un
# personaje lo estuviera escribiendo en tiempo real, en lugar de aparecer
# de golpe. Este comportamiento ya existe dentro del motor de Ren'Py; este
# modulo simplemente lo activa y lo deja configurado y documentado para
# que cualquier persona, sin experiencia previa, pueda usarlo.
#
# COMO INSTALAR ESTE MODULO EN CUALQUIER PROYECTO
# ----------------------------------------------------------------------------
# 1. Copia este archivo (tal cual esta) Y la carpeta "audio" que viene justo
#    a su lado (con el sonido de tecleo de ejemplo) dentro de la carpeta
#    "game" de tu proyecto de Ren'Py, manteniendo la misma posicion
#    relativa entre ambos. Por ejemplo, si este archivo queda en
#    "game/modulos/modulo_efecto_maquina_de_escribir.rpy", la carpeta debe
#    quedar en "game/modulos/audio/". Ren'Py carga TODOS los archivos .rpy
#    que encuentre, sin importar la subcarpeta.
#    Si no te interesa el sonido de tecleo, puedes omitir la carpeta
#    "audio" y simplemente configurar MME_SONIDO_TECLEO = None mas abajo.
# 2. No necesitas tocar ningun otro archivo del proyecto (ni options.rpy,
#    ni script.rpy). El modulo funciona por si solo apenas lo copias.
# 3. Abre el proyecto con el Ren'Py Launcher y ejecutalo. Listo, el efecto
#    ya esta activo en todos los dialogos.
#
# COMO CONFIGURAR LA VELOCIDAD
# ----------------------------------------------------------------------------
# Justo mas abajo, en la seccion "CONFIGURACION", cambia el valor de la
# constante MME_VELOCIDAD_CPS por el numero que prefieras:
#
#   0      = efecto desactivado (el texto aparece de golpe, como viene
#            por defecto en un proyecto nuevo de Ren'Py)
#   1-60   = caracteres por segundo. Valores usuales para dialogos van de
#            20 a 35 (comodo para leer). Numeros mas altos = mas rapido.
#
# COMO USARLO DENTRO DEL GUION (script.rpy)
# ----------------------------------------------------------------------------
# El efecto se aplica automaticamente a todos los dialogos, no hace falta
# escribir nada especial. Pero si quieres mas control, aqui hay 3 formas:
#
# A) Cambiar la velocidad de un personaje especifico (recomendado si un
#    personaje debe hablar siempre distinto al resto, por ejemplo un
#    narrador mas rapido o un personaje nervioso). Se define junto con el
#    personaje, en script.rpy:
#
#        define e = Character("Eileen", cps=25)
#        define n = Character("Narrador", cps=40)
#
# B) Cambiar la velocidad solo en una linea puntual de dialogo, con la
#    etiqueta de texto {cps=...} dentro de las comillas:
#
#        e "Esto se lee normal, pero {cps=5}esto se escribe muy
#        despacio{/cps} y esto vuelve a la velocidad normal."
#
# C) Cambiar la velocidad general para todo lo que siga, usando la
#    funcion que trae este modulo (util para efectos dramaticos):
#
#        $ mme_definir_velocidad(5)      # muy lento
#        e "Esto... se... escribe... despacio..."
#        $ mme_definir_velocidad(25)     # vuelve a la velocidad normal
#
# NOTA PARA EL JUGADOR
# ----------------------------------------------------------------------------
# Mientras el texto se esta "escribiendo", un clic o tecla completa esa
# linea de inmediato; otro clic avanza a la siguiente. Esto ya lo maneja
# Ren'Py automaticamente, no requiere codigo adicional. Ademas, el menu
# estandar de "Preferencias" de Ren'Py ya incluye un control deslizante de
# "Velocidad de texto" que le permite al jugador ajustarlo a su gusto.
#
# COMO CONFIGURAR EL SONIDO DE TECLEO (OPCIONAL)
# ----------------------------------------------------------------------------
# Este modulo puede reproducir un sonido de tecleo mientras el texto se
# esta "escribiendo", como si fuera una maquina de escribir de verdad.
# Ren'Py no avisa cuando aparece cada letra individual, asi que el sonido
# se reproduce en bucle (loop) durante toda la animacion del texto y se
# corta automaticamente en cuanto termina de aparecer (o el jugador hace
# clic para saltarselo). Usa un sonido corto de una sola tecla (como el
# que trae este modulo por defecto) para que el bucle suene como un
# traqueteo continuo. Es opcional:
#
#   - Por defecto viene CONFIGURADO Y ACTIVO, usando el archivo de ejemplo
#     que se incluye junto a este modulo, en la carpeta
#     "game/modulos/audio/mme_tecleo.mp3".
#   - Si prefieres que no suene nada, en la seccion "CONFIGURACION" cambia
#     MME_SONIDO_TECLEO a None:
#
#         define MME_SONIDO_TECLEO = None
#
#   - Si quieres usar otro sonido, copia tu propio archivo de audio
#     (.mp3, .ogg o .wav) dentro de la carpeta "game/" de tu proyecto y
#     apunta la constante a esa ruta, relativa a "game/". Por ejemplo, si
#     pones tu archivo en "game/audio/mi_sonido.ogg":
#
#         define MME_SONIDO_TECLEO = "audio/mi_sonido.ogg"
#
#   - Tambien puedes cambiarlo en tiempo real desde el guion (script.rpy),
#     por ejemplo para que un personaje tenga un tecleo distinto:
#
#         $ MME_SONIDO_TECLEO = "audio/mi_sonido.ogg"
#         e "Este dialogo ya suena con el nuevo sonido de tecleo."
#         $ MME_SONIDO_TECLEO = None
#         e "Y este dialogo vuelve a quedar en silencio."
#
#   - El volumen general de este sonido (independiente del volumen de cada
#     dialogo) se controla con la constante MME_SONIDO_TECLEO_VOLUMEN, en
#     la seccion "CONFIGURACION". Va de 0.0 (silencio) a 1.0 (volumen
#     normal del archivo). Por ejemplo, para que suene mas bajito:
#
#         define MME_SONIDO_TECLEO_VOLUMEN = 0.4
#
#     Ademas, como cualquier otro efecto de sonido, tambien respeta el
#     control deslizante "Sonido" del menu de Preferencias de Ren'Py.
# ============================================================================


# ----------------------------------------------------------------------------
# CONFIGURACION (el unico bloque que normalmente necesitas editar)
# ----------------------------------------------------------------------------
define MME_VELOCIDAD_CPS = 25

# Ruta (relativa a la carpeta "game/") del sonido que se reproduce por cada
# letra que aparece en el dialogo. Dejalo en None para que no suene nada.
define MME_SONIDO_TECLEO = "modulos/audio/mme_tecleo.mp3"

# Volumen del sonido de tecleo: 0.0 = silencio, 1.0 = volumen normal del
# archivo. Bajalo si el sonido de ejemplo (u otro que pongas) suena
# demasiado fuerte en comparacion con el resto del audio del juego.
define MME_SONIDO_TECLEO_VOLUMEN = 0.2


# ----------------------------------------------------------------------------
# LOGICA DEL MODULO (no es necesario editar nada de aqui en adelante)
# ----------------------------------------------------------------------------
init python:

    def mme_definir_velocidad(cps):
        """
        Cambia la velocidad de escritura (en caracteres por segundo) para
        todo el dialogo que se muestre a partir de este punto del guion.

        Parametros:
            cps (int): caracteres por segundo.
                0 = instantaneo (efecto desactivado)
                1 a 60 = velocidad tipica de dialogo (20-35 recomendado)
        """
        preferences.text_cps = cps

    # Aplica la velocidad configurada arriba como punto de partida del
    # juego. Se usa una asignacion directa (no "default") para que este
    # modulo funcione sin importar lo que ya tenga definido options.rpy
    # en el proyecto donde se copie.
    preferences.text_cps = MME_VELOCIDAD_CPS

    # Canal de audio propio para el sonido de tecleo, separado del canal
    # "sound" general, para que no interrumpa (ni sea interrumpido por)
    # otros efectos de sonido del juego. Usa el mixer "sound" para que el
    # jugador lo controle con el control deslizante "Sonido" de siempre.
    renpy.music.register_channel("mme_teclado", mixer="sound", loop=False, tight=True)

    # "config.character_callback" es UNA sola funcion (no una lista). Si el
    # proyecto donde se copia este modulo ya tenia una propia configurada,
    # la guardamos para seguir llamandola y no romper lo que ya existia.
    _mme_callback_previo = config.character_callback

    # Ren'Py no ofrece un evento por cada letra individual, asi que este
    # sonido se reproduce en bucle (loop) mientras el texto se esta
    # "escribiendo" y se corta apenas termina de aparecer (o el jugador lo
    # salta con un clic). Con un sonido corto de una sola tecla, el bucle
    # suena como un traqueteo continuo.
    def mme_sonido_de_tecleo(event, **kwargs):
        """
        "show" marca el instante en que aparece el cuadro de dialogo
        (arranca el bucle); "slow_done" marca cuando termina la animacion
        letra por letra (corta el bucle); "end" es un respaldo por si
        "slow_done" no llega a dispararse (por ejemplo con el texto
        instantaneo o en modo "saltar"). Si MME_SONIDO_TECLEO esta en None,
        no hace nada.
        """
        if _mme_callback_previo is not None:
            _mme_callback_previo(event, **kwargs)

        if not MME_SONIDO_TECLEO:
            return

        # "interact" viene en False en casos donde el dialogo no genera una
        # interaccion real (por ejemplo durante un rollback); en esos casos
        # no queremos reproducir sonido.
        if not kwargs.get("interact", True):
            return

        if event == "show" and preferences.text_cps != 0:
            renpy.sound.set_volume(MME_SONIDO_TECLEO_VOLUMEN, channel="mme_teclado")
            renpy.sound.play(MME_SONIDO_TECLEO, channel="mme_teclado", loop=True)
        elif event in ("slow_done", "end"):
            renpy.sound.stop(channel="mme_teclado")

    # Se registra como el callback global de personaje para que el sonido
    # suene en TODOS los dialogos, sin tener que modificar cada Character()
    # del proyecto donde se copie este modulo.
    config.character_callback = mme_sonido_de_tecleo
