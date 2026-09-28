# Ejemplo de uso del modulo "sonidos_interfaz"
# (game/modulos/sonidos_interfaz/).
# Los sonidos de hover y click quedan activos en todos los botones del
# juego (menu principal, opciones de eleccion, menu de pausa...) porque
# game/options.rpy tiene "define SI_ACTIVADO = True". Este ejemplo muestra ademas como
# prenderlos, apagarlos y cambiarlos dentro de una escena.
#
# Este archivo vive en game/vistas/ y NO es parte del modulo: es solo
# una demostracion a la que se llega desde el menu de script.rpy.

label ejemplo_sonidos_interfaz:

    scene bg room

    show eileen happy

    e "Pasa el cursor por las opciones y elegi una: cada boton suena al pasar por encima y al hacer click."

    # ------------------------------------------------------------------
    # 1) CONFIGURACION GLOBAL: no hace falta escribir nada.
    # ------------------------------------------------------------------
    menu:
        "Opcion A (con sonido)":
            pass
        "Opcion B (con sonido)":
            pass

    # ------------------------------------------------------------------
    # 2) APAGAR TODO en la escena con si_desactivar().
    # ------------------------------------------------------------------
    $ si_desactivar()

    e "Ahora apague los sonidos para esta escena. Proba: estas opciones no suenan."

    menu:
        "Opcion silenciosa A":
            pass
        "Opcion silenciosa B":
            pass

    e "Si abris el menu de pausa (Esc o click derecho), vas a ver que ahi SI siguen sonando: SI_MENUS_USAN_CONFIG_GLOBAL esta en True."

    # ------------------------------------------------------------------
    # 3) PRENDER SOLO UNO: aca solo el click, sin hover.
    # ------------------------------------------------------------------
    $ si_activar("click")

    e "Ahora prendi solo el click: pasar el cursor no suena, elegir si."

    menu:
        "Solo click A":
            pass
        "Solo click B":
            pass

    # ------------------------------------------------------------------
    # 4) OTROS SONIDOS solo para esta parte de la historia.
    # ------------------------------------------------------------------
    $ si_activar()
    $ si_cambiar_sonido(
        hover="modulos/efecto_maquina_de_escribir/audio/mme_tecleo.mp3",
        click="modulos/ruleta_rusa/audio/rr_vacio.mp3",
    )

    e "Y ahora cambie los sonidos solo para esta parte: tecleo al pasar el cursor, gatillo al elegir."

    menu:
        "Sonido distinto A":
            pass
        "Sonido distinto B":
            pass

    # ------------------------------------------------------------------
    # 5) VOLVER a la configuracion global con si_restaurar().
    # ------------------------------------------------------------------
    $ si_restaurar()

    e "Y con si_restaurar() todo vuelve a como esta en la configuracion del modulo. Fin del ejemplo."

    return
