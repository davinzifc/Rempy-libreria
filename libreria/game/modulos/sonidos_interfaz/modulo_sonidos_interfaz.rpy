# ============================================================================
#  MODULO: SONIDOS DE INTERFAZ (hover y click en botones y opciones)
#  Version: 1.0
#  Compatibilidad: Ren'Py 8.x
#  Autor: davinzifc
#  Licencia: MIT. Copyright (c) 2026 davinzifc.
#            Puedes usar, copiar, modificar y redistribuir este archivo,
#            siempre que mantengas este aviso de copyright y la licencia
#            MIT (ver el archivo LICENSE del repositorio) en las copias.
#            Es decir: hay que dar credito al desarrollador.
#
#  Para instrucciones de instalacion, ejemplos de uso dentro del guion y
#  mas detalles, abri el archivo "README.md" que viene junto a este
#  script, en esta misma carpeta.
#
#  Resumen rapido de uso (ver el README para mas ejemplos):
#      define SI_ACTIVADO = True                 # en options.rpy: prende el modulo en todo el juego
#      define SI_CONTROL_USUARIO = True          # en options.rpy: volumen ajustable en Preferencias
#      $ si_desactivar()                         # apaga hover y click en la escena
#      $ si_desactivar("hover")                  # apaga solo el sonido al pasar el cursor
#      $ si_activar()                            # los vuelve a prender
#      $ si_cambiar_sonido(click="audio/x.ogg")  # otro sonido solo para esta parte
#      $ si_restaurar()                          # vuelve a la configuracion global
# ============================================================================


# ============================================================================
#  CONFIGURACION: SE HACE EN "options.rpy", NO ACA
# ----------------------------------------------------------------------------
#  Este modulo viene APAGADO. Para prenderlo en todo el juego, copia este
#  bloque al final de "game/options.rpy" de tu proyecto y ajusta los
#  valores (ver el README para la explicacion de cada linea):
#
#      ## Sonidos de interfaz (modulo sonidos_interfaz) ####################
#      define SI_ACTIVADO = True
#      define SI_CONTROL_USUARIO = True
#      define SI_VOLUMEN_HOVER = 0.5
#      define SI_VOLUMEN_CLICK = 0.8
#
#  Lo que sigue son solo los valores POR DEFECTO, los que se usan para
#  cada opcion que no escribas en options.rpy. No hace falta tocarlos: si
#  queres cambiar alguno, agrega un "define" con el mismo nombre en
#  options.rpy y ese es el que manda.
# ============================================================================
init -1 python:

    # Prende el modulo en todo el juego (menu principal, opciones de
    # eleccion, menu de pausa...). Apagado por defecto: se activa en
    # options.rpy. Aun apagado, se puede prender en una escena con
    # si_activar().
    SI_ACTIVADO = False

    # Si el jugador puede ajustar el volumen del hover y del click con los
    # deslizadores de Preferencias (pantalla si_preferencias_volumen). Con
    # False no aparecen y siempre se usan SI_VOLUMEN_HOVER/CLICK.
    SI_CONTROL_USUARIO = False

    # Sonido al pasar el cursor y al hacer click: ruta a un archivo dentro
    # de "game/" (.mp3, .ogg o .wav), o None para que no suene.
    SI_SONIDO_HOVER = "modulos/sonidos_interfaz/audio/si_hover.mp3"
    SI_SONIDO_CLICK = "modulos/sonidos_interfaz/audio/si_click.wav"

    # Volumen con el que arranca cada sonido: 0.0 = silencio, 1.0 = el
    # maximo del archivo. Si SI_CONTROL_USUARIO es True, despues lo ajusta
    # el jugador. Ademas ambos siguen el deslizador general "Sonido".
    SI_VOLUMEN_HOVER = 0.5
    SI_VOLUMEN_CLICK = 0.8

    # True = si_desactivar() en una escena NO silencia el menu principal
    # ni el menu de pausa (guardar, cargar, preferencias...). Recomendado.
    SI_MENUS_USAN_CONFIG_GLOBAL = True

    # Estilos de boton que suenan. Con estos tres suenan el menu principal,
    # el menu de pausa, las opciones de eleccion (menu:), el menu rapido y
    # los "textbutton" / "imagebutton" normales.
    SI_ESTILOS = ["button", "choice_button", "quick_button"]


# ============================================================================
#  A PARTIR DE ACA: EL "MOTOR" DEL MODULO
# ----------------------------------------------------------------------------
#  No necesitas editar nada de lo que sigue para usar el modulo. Si no
#  sabes programar, es mejor que no lo toques.
# ============================================================================

# Estado de la escena actual. None significa "usar la configuracion
# global". Al ser "default", se guarda junto con la partida y se deshace
# con el rollback, asi que al cargar o retroceder los sonidos quedan
# exactamente como estaban en ese punto del guion.
default si_hover_activo = None
default si_click_activo = None
default si_sonido_hover = None
default si_sonido_click = None

# Volumen elegido por el jugador en las Preferencias. Es "persistent"
# (igual que el resto de las preferencias de Ren'Py): vale para todas las
# partidas y se recuerda al cerrar y volver a abrir el juego. Se inicializa
# en "init 999" para que ya se hayan leido los valores de options.rpy.
init 999 python:
    if persistent.si_volumen_hover is None:
        persistent.si_volumen_hover = SI_VOLUMEN_HOVER
    if persistent.si_volumen_click is None:
        persistent.si_volumen_click = SI_VOLUMEN_CLICK

init python:

    def si_activar(cual="ambos"):
        """
        Prende los sonidos de los botones a partir de este punto del guion.

        Parametros:
            cual (str): "ambos" (por defecto), "hover" o "click".
        """
        _si_cambiar_estado(cual, True)

    def si_desactivar(cual="ambos"):
        """
        Apaga los sonidos de los botones a partir de este punto del guion.

        Parametros:
            cual (str): "ambos" (por defecto), "hover" o "click".
        """
        _si_cambiar_estado(cual, False)

    def si_cambiar_sonido(hover=None, click=None):
        """
        Usa otros sonidos (en lugar de los de la configuracion) a partir de
        este punto del guion. El que no se pase queda como esta.

        Parametros:
            hover (str): ruta al nuevo sonido al pasar el cursor.
            click (str): ruta al nuevo sonido al hacer click.
        """
        if hover is not None:
            store.si_sonido_hover = hover
        if click is not None:
            store.si_sonido_click = click

    def si_restaurar():
        """
        Descarta todo lo cambiado en la escena (prendido/apagado y sonidos
        propios) y vuelve a la configuracion global (options.rpy).
        """
        store.si_hover_activo = None
        store.si_click_activo = None
        store.si_sonido_hover = None
        store.si_sonido_click = None

    def _si_cambiar_estado(cual, valor):
        if cual not in ("ambos", "hover", "click"):
            raise Exception('sonidos_interfaz: "cual" tiene que ser "ambos", "hover" o "click", no {!r}.'.format(cual))

        if cual in ("ambos", "hover"):
            store.si_hover_activo = valor
        if cual in ("ambos", "click"):
            store.si_click_activo = valor

    def _si_sonido_final(activo_escena, sonido_escena, sonido_global, volumen, en_menu):
        """
        Decide que archivo tiene que sonar (o None) combinando la
        configuracion global con lo que se haya cambiado en la escena.
        """
        if en_menu:
            activo, sonido = SI_ACTIVADO, sonido_global
        else:
            activo = SI_ACTIVADO if activo_escena is None else activo_escena
            sonido = sonido_global if sonido_escena is None else sonido_escena

        if not activo:
            return None
        return _si_con_volumen(sonido, volumen)

    def _si_con_volumen(sonido, volumen):
        """
        Devuelve el archivo listo para reproducir con el volumen pedido, o
        None si no hay sonido o el volumen es cero.
        """
        if not sonido or volumen is None:
            return None

        # Redondeado para que mover el deslizador un pelito no genere un
        # nombre de archivo distinto (y una reconstruccion de estilos) nuevo.
        volumen = round(max(0.0, min(1.0, volumen)), 2)
        if volumen <= 0.0:
            return None

        # "<volume ...>" es la forma que tiene Ren'Py de ajustar el volumen
        # de un archivo puntual sin tocar el canal entero (que es el mismo
        # que usan los demas efectos de sonido del juego).
        if volumen != 1.0:
            return "<volume {}>{}".format(volumen, sonido)
        return sonido

    def _si_volumen(cual):
        """
        Volumen elegido por el jugador en las Preferencias. Si el control
        del jugador esta apagado (SI_CONTROL_USUARIO) o todavia no hay
        valor guardado, usa el de la configuracion.
        """
        if not SI_CONTROL_USUARIO:
            return SI_VOLUMEN_HOVER if cual == "hover" else SI_VOLUMEN_CLICK

        if cual == "hover":
            elegido, inicial = persistent.si_volumen_hover, SI_VOLUMEN_HOVER
        else:
            elegido, inicial = persistent.si_volumen_click, SI_VOLUMEN_CLICK
        return inicial if elegido is None else elegido

    def si_probar(cual):
        """
        Reproduce el sonido de hover o de click con el volumen elegido en
        las Preferencias. La usan los botones "Prueba" de la pantalla
        si_preferencias_volumen.

        Parametros:
            cual (str): "hover" o "click".
        """
        if cual == "hover":
            renpy.play(_si_con_volumen(SI_SONIDO_HOVER, _si_volumen("hover")))
        elif cual == "click":
            renpy.play(_si_con_volumen(SI_SONIDO_CLICK, _si_volumen("click")))
        else:
            raise Exception('sonidos_interfaz: "cual" tiene que ser "hover" o "click", no {!r}.'.format(cual))

    def _si_sonidos_actuales():
        # Durante el arranque los "default" todavia no existen: por eso
        # getattr con None (= usar la configuracion global).
        en_menu = SI_MENUS_USAN_CONFIG_GLOBAL and getattr(store, "_menu", False)

        hover = _si_sonido_final(
            getattr(store, "si_hover_activo", None),
            getattr(store, "si_sonido_hover", None),
            SI_SONIDO_HOVER, _si_volumen("hover"), en_menu,
        )
        click = _si_sonido_final(
            getattr(store, "si_click_activo", None),
            getattr(store, "si_sonido_click", None),
            SI_SONIDO_CLICK, _si_volumen("click"), en_menu,
        )
        return (hover, click)

    # Ultimo par (hover, click) que quedo aplicado en los estilos. Es una
    # lista para poder modificarla desde adentro de las funciones.
    _si_aplicado = [None]

    # Ren'Py reproduce los sonidos de los botones a partir de las
    # propiedades de estilo "hover_sound" y "activate_sound". Esta funcion
    # se engancha a "config.build_styles_callbacks", asi que corre cada
    # vez que Ren'Py arma los estilos (al iniciar el juego y en cada
    # renpy.style.rebuild()). Es el mismo mecanismo que usa Ren'Py para
    # sus propias "style preferences".
    def _si_aplicar_estilos():
        hover, click = _si_sonidos_actuales()

        for nombre in SI_ESTILOS:
            estilo = getattr(style, nombre)
            estilo.hover_sound = hover
            estilo.activate_sound = click

        _si_aplicado[0] = (hover, click)

    # Corre al comienzo de cada interaccion (cada linea de dialogo, cada
    # menu, cada pantalla). Solo reconstruye los estilos si el sonido que
    # corresponde cambio: por ejemplo tras si_desactivar(), al cargar una
    # partida, al hacer rollback, o al entrar/salir del menu de pausa.
    def _si_actualizar():
        if _si_sonidos_actuales() != _si_aplicado[0]:
            renpy.style.rebuild()

    config.build_styles_callbacks.append(_si_aplicar_estilos)
    config.interact_callbacks.append(_si_actualizar)


# ============================================================================
#  DESLIZADORES DE VOLUMEN PARA LAS PREFERENCIAS
# ----------------------------------------------------------------------------
#  Para que el jugador pueda ajustar el volumen del hover y del click,
#  pone "define SI_CONTROL_USUARIO = True" en options.rpy y agrega esta
#  linea dentro de la pantalla "preferences" de tu
#  screens.rpy, debajo de "Volumen sonido" (ver el README):
#
#      use si_preferencias_volumen
#
#  Cada deslizador trae un boton "Prueba" para escuchar como queda.
# ============================================================================
screen si_preferencias_volumen():

    # Solo aparece si SI_CONTROL_USUARIO = True en options.rpy.
    if SI_CONTROL_USUARIO:
        vbox:
            style_prefix "slider"

            if SI_SONIDO_HOVER:
                label _("Volumen hover")

                hbox:
                    bar value FieldValue(persistent, "si_volumen_hover", range=1.0, step=0.05, style="slider")
                    textbutton _("Prueba"):
                        action Function(si_probar, "hover")
                        activate_sound None

            if SI_SONIDO_CLICK:
                label _("Volumen click")

                hbox:
                    bar value FieldValue(persistent, "si_volumen_click", range=1.0, step=0.05, style="slider")
                    textbutton _("Prueba"):
                        action Function(si_probar, "click")
                        activate_sound None
