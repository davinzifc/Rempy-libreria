# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")


# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg room

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show eileen happy

    # Presenta las líneas del diálogo.

    e "Has creado un nuevo juego Ren'Py."

    e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"

    # Ejemplo de uso del módulo "gestor_particulas" (game/modulos/gestor_particulas/):
    # activar un efecto guarda un identificador, que después se usa para
    # desactivar ESE efecto en particular.

    $ id_nieve = gp_nieve()

    e "Mira, empezó a nevar."

    $ gp_terminar_particulas(id_nieve)

    e "Y ahora paró."

    # Ahora, en vez de usar el atajo gp_lluvia(), se arma una lluvia
    # "a mano" con gp_crear_particulas(), pasandole nosotros mismos
    # todos los parametros (ver la clase GP_TipoParticula, en
    # game/modulos/gestor_particulas/modulo_gestor_particulas.rpy, para
    # la lista completa y su explicacion).

    $ id_lluvia = gp_crear_particulas(
        color="#9FC6FF",
        forma="rectangulo",
        tamano_min=14, tamano_max=26,
        ancho_min=1, ancho_max=2,
        cantidad=140,
        angulo_base=100, angulo_variacion=4,
        velocidad_min=650, velocidad_max=950,
        opacidad_min=0.35, opacidad_max=0.7,
    )

    e "Y ahora se largó a llover."

    $ gp_terminar_particulas(id_lluvia)

    e "Listo, ya escampó."

    # Finaliza el juego:

    return
