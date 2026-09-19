# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")

# Simulacion corta de cambio de variables Ir_por_el_callejon / No_paso_nada_en_el_callejon
default Ir_por_el_callejon = False
default No_paso_nada_en_el_callejon = False

label sim_callejon:

    menu:
        "ruta bus":
            jump sim_titular

        "ruta callejon":
            $ Ir_por_el_callejon = True
            jump sim_callejon_velocidad

label sim_callejon_velocidad:

    menu:
        "callejon rapido":
            $ No_paso_nada_en_el_callejon = True
            jump sim_titular

        "callejon lento":
            $ No_paso_nada_en_el_callejon = False
            jump sim_titular

label sim_titular:

    if Ir_por_el_callejon and not No_paso_nada_en_el_callejon:
        "resultado: titular (algo paso en el callejon)"
    else:
        "resultado: sin titular"

    return


# El juego comienza aquí.

label start:

    jump sim_callejon
