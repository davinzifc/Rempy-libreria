# Sonidos de Interfaz (hover y click en botones)

Módulo "copiar y pegar" para proyectos de **Ren'Py**. Hace que los
botones del juego **suenen al pasar el cursor por encima** (hover) y
**al hacer click**: en el menú principal, en las opciones de elección
(`menu:`), en el menú de pausa (guardar, cargar, preferencias...) y en
el menú rápido de abajo.

Se configura una sola vez en `options.rpy` y suena en todos lados; el
jugador puede ajustar el volumen desde Opciones, y además podés
**prenderlo, apagarlo o cambiar los sonidos en cualquier escena**.

No hace falta saber programar para usarlo: seguí los pasos de más abajo.

## Qué hay en esta carpeta

```
sonidos_interfaz/
├── modulo_sonidos_interfaz.rpy   <- el módulo en sí
├── audio/
│   ├── si_hover.mp3              <- sonido de ejemplo al pasar el cursor
│   └── si_click.wav              <- sonido de ejemplo al hacer click
└── README.md                     <- este archivo
```

Todos los archivos van siempre juntos, en la misma carpeta.

## Cómo instalarlo

1. Copiá **toda esta carpeta** (`sonidos_interfaz`, con todo lo que
   tiene adentro) dentro de la carpeta `game/modulos/` de tu proyecto de
   Ren'Py. Si tu proyecto no tiene una carpeta `game/modulos/`, creala
   vos mismo y pegá la carpeta del módulo ahí adentro.

   Al final te tiene que quedar así:

   ```
   tu_proyecto/
   └── game/
       └── modulos/
           └── sonidos_interfaz/
               ├── modulo_sonidos_interfaz.rpy
               ├── audio/
               │   ├── si_hover.mp3
               │   └── si_click.wav
               └── README.md
   ```

2. **Prendelo en `game/options.rpy`.** El módulo viene apagado: la
   configuración global se hace en `options.rpy` (el archivo de
   configuración que trae todo proyecto de Ren'Py). Abrilo y pegá este
   bloque al final, por ejemplo debajo de la sección "Sonidos y música":

   ```renpy
   ## Sonidos de interfaz (módulo sonidos_interfaz) ####################

   define SI_ACTIVADO = True          # los botones suenan en todo el juego
   define SI_CONTROL_USUARIO = True   # el jugador ajusta el volumen en Opciones
   define SI_VOLUMEN_HOVER = 0.5      # volumen con el que arranca el hover
   define SI_VOLUMEN_CLICK = 0.8      # volumen con el que arranca el click
   ```

3. **(Solo si pusiste `SI_CONTROL_USUARIO = True`)** agregá los
   deslizadores a la pantalla de Opciones: ver "Deslizadores de volumen
   en Opciones" más abajo.

4. Abrí el proyecto con el Ren'Py Launcher y ejecutalo. Listo — los
   botones ya suenan en todo el juego.

> **¿Querés ponerlo en otra carpeta** (por ejemplo `game/components/` en
> vez de `game/modulos/`)? Podés hacerlo, pero después tenés que agregar
> en `options.rpy` las líneas `define SI_SONIDO_HOVER = ...` y
> `define SI_SONIDO_CLICK = ...` con la ruta nueva (ver "Usar tus propios
> sonidos").

## Cómo configurarlo (para todo el juego)

Toda la configuración va en **`game/options.rpy`**, con una línea
`define` por opción. No hace falta tocar el archivo del módulo: para
cada opción que no escribas en `options.rpy`, el módulo usa su valor por
defecto (el de la última columna).

| Variable | Para qué sirve | Por defecto |
|---|---|---|
| `SI_ACTIVADO` | `True` = los botones suenan en todo el juego. `False` = módulo apagado (igual se puede prender en una escena con `si_activar()`). | `False` |
| `SI_CONTROL_USUARIO` | `True` = el jugador puede ajustar el volumen del hover y del click desde Opciones. `False` = los deslizadores no aparecen y siempre se usa el volumen de abajo. | `False` |
| `SI_VOLUMEN_HOVER` | Volumen con el que arranca el sonido de hover, de `0.0` (silencio) a `1.0` (máximo). | `0.5` |
| `SI_VOLUMEN_CLICK` | Volumen con el que arranca el sonido de click, de `0.0` (silencio) a `1.0` (máximo). | `0.8` |
| `SI_SONIDO_HOVER` | Sonido al pasar el cursor por un botón. `None` para que no suene. | el `si_hover.mp3` incluido |
| `SI_SONIDO_CLICK` | Sonido al hacer click en un botón. `None` para que no suene. | el `si_click.wav` incluido |
| `SI_MENUS_USAN_CONFIG_GLOBAL` | `True` = lo que apagues en una escena NO afecta al menú principal ni al menú de pausa. `False` = sí los afecta. | `True` |
| `SI_ESTILOS` | Qué tipos de botón suenan. No lo toques si no estás seguro. | `["button", "choice_button", "quick_button"]` |

### Cómo aplicar la configuración en `options.rpy`, paso a paso

1. Abrí el archivo **`game/options.rpy`** de tu proyecto con cualquier
   editor de texto (el Ren'Py Launcher trae uno: botón "Editar archivo"
   → `options.rpy`).
2. Bajá hasta la sección que empieza con
   `## Sonidos y música ####...` y, al final de esa sección (después de
   las líneas de `config.main_menu_music`), pegá el bloque de abajo.
   Cualquier otro lugar del archivo también funciona, siempre que las
   líneas `define` queden **pegadas al margen izquierdo** (sin espacios
   adelante).
3. Cambiá solo el valor que está después del `=` en cada línea y guardá
   el archivo.
4. Cerrá y volvé a abrir el juego (o recargalo con `Shift+R`) para que
   tome los cambios.

**Bloque mínimo** (lo que casi todos van a necesitar):

```renpy
## Sonidos de interfaz (módulo sonidos_interfaz) ####################

define SI_ACTIVADO = True          # True = suenan en todo el juego / False = apagado
define SI_CONTROL_USUARIO = True   # True = el jugador ajusta el volumen en Opciones
define SI_VOLUMEN_HOVER = 0.5      # volumen inicial del hover (0.0 a 1.0)
define SI_VOLUMEN_CLICK = 0.8      # volumen inicial del click (0.0 a 1.0)
```

**Bloque completo** (con todas las opciones, por si querés cambiar algo
más; las líneas que no necesites las podés borrar y el módulo usa su
valor por defecto):

```renpy
## Sonidos de interfaz (módulo sonidos_interfaz) ####################

define SI_ACTIVADO = True
define SI_CONTROL_USUARIO = True
define SI_VOLUMEN_HOVER = 0.5
define SI_VOLUMEN_CLICK = 0.8
define SI_SONIDO_HOVER = "modulos/sonidos_interfaz/audio/si_hover.mp3"
define SI_SONIDO_CLICK = "modulos/sonidos_interfaz/audio/si_click.wav"
define SI_MENUS_USAN_CONFIG_GLOBAL = True
define SI_ESTILOS = ["button", "choice_button", "quick_button"]
```

**Ejemplos de configuraciones comunes:**

- *Que suene solo el click, sin hover:*

  ```renpy
  define SI_ACTIVADO = True
  define SI_SONIDO_HOVER = None
  ```

- *Que suene en todo el juego, pero sin que el jugador pueda cambiar el
  volumen:*

  ```renpy
  define SI_ACTIVADO = True
  define SI_CONTROL_USUARIO = False
  define SI_VOLUMEN_HOVER = 0.3
  define SI_VOLUMEN_CLICK = 0.6
  ```

- *Apagado en todo el juego y prendido solo en algunas escenas* (con
  `si_activar()` en el guion): no escribas nada en `options.rpy`, o
  poné `define SI_ACTIVADO = False`.

> **Importante:** cada nombre (`SI_ACTIVADO`, `SI_VOLUMEN_HOVER`, ...)
> tiene que aparecer **una sola vez** en `options.rpy`. Si ya pegaste el
> bloque y querés cambiar un valor, editá la línea que ya está en vez de
> agregar otra con el mismo nombre.

Los sonidos se reproducen como efectos de sonido normales, así que
además siguen el deslizador **"Volumen sonido"** y el botón **"Silenciar
todo"** de Opciones.

### Deslizadores de volumen en Opciones

Con `define SI_CONTROL_USUARIO = True` en `options.rpy`, el módulo
muestra dos deslizadores, **"Volumen hover"** y **"Volumen click"**,
cada uno con un botón **"Prueba"** para escuchar cómo queda. Para que
aparezcan en la pantalla de Opciones de tu juego hay que agregar una
línea en `screens.rpy`:

1. Abrí `game/screens.rpy` y buscá la pantalla `screen preferences():`.
2. Buscá la parte de `"Volumen sonido"` y, justo debajo de su `hbox`
   (al mismo nivel de sangría que `label _("Volumen sonido")`), agregá
   esta línea:

   ```renpy
                       if config.has_sound:

                           label _("Volumen sonido")

                           hbox:
                               bar value Preference("sound volume")

                               if config.sample_sound:
                                   textbutton _("Prueba") action Play("sound", config.sample_sound)

                           use si_preferencias_volumen    # <- esta línea
   ```

El volumen que elige el jugador se guarda solo (como el resto de las
preferencias de Ren'Py): vale para todas las partidas y se recuerda al
cerrar y volver a abrir el juego. `SI_VOLUMEN_HOVER` y
`SI_VOLUMEN_CLICK` son solo el valor con el que arranca.

Si después cambiás a `SI_CONTROL_USUARIO = False`, no hace falta sacar
la línea de `screens.rpy`: los deslizadores simplemente dejan de
aparecer y se vuelve a usar el volumen de `options.rpy`.

### Usar tus propios sonidos

1. Copiá tus archivos de sonido (`.mp3`, `.ogg` o `.wav`) dentro de la
   carpeta `game/` de tu proyecto (podés crear una carpeta `game/audio/`
   para ordenarlos, por ejemplo). Conviene que sean sonidos **muy
   cortos** (menos de medio segundo).
2. Agregá en `options.rpy` las líneas `SI_SONIDO_HOVER` y
   `SI_SONIDO_CLICK` apuntando a esas rutas, por ejemplo:

   ```
   define SI_SONIDO_HOVER = "audio/mi_hover.ogg"
   define SI_SONIDO_CLICK = "audio/mi_click.ogg"
   ```

## Prenderlo y apagarlo dentro de una escena (`script.rpy`)

En cualquier punto del guion podés escribir una de estas líneas. El
cambio vale **desde ahí en adelante**, hasta que escribas otra.

**A) Apagar los sonidos** (por ejemplo, en una escena tensa donde no
querés que las opciones suenen):

```renpy
$ si_desactivar()           # apaga hover y click
$ si_desactivar("hover")    # apaga solo el sonido al pasar el cursor
$ si_desactivar("click")    # apaga solo el sonido al hacer click
```

**B) Volver a prenderlos:**

```renpy
$ si_activar()              # prende hover y click
$ si_activar("hover")       # prende solo el de pasar el cursor
$ si_activar("click")       # prende solo el de hacer click
```

**C) Usar otros sonidos solo en una parte de la historia** (por ejemplo,
un sonido más oscuro en una escena de terror). El que no escribas queda
como estaba:

```renpy
$ si_cambiar_sonido(hover="audio/susurro.ogg", click="audio/golpe.ogg")
$ si_cambiar_sonido(click="audio/golpe.ogg")   # cambia solo el click
```

**D) Volver a la configuración global** (deshace todo lo de arriba de
una sola vez):

```renpy
$ si_restaurar()
```

Ejemplo completo:

```renpy
label escena_tensa:
    $ si_desactivar()

    e "No hagas ruido..."

    menu:
        "Esconderse":
            pass
        "Correr":
            pass

    $ si_restaurar()
```

### Cosas que conviene saber

- **Se guarda con la partida.** Si apagás los sonidos y el jugador
  guarda, al cargar esa partida siguen apagados. Lo mismo al volver
  atrás con la rueda del mouse (rollback): los sonidos quedan como
  estaban en ese punto del guion.
- **El menú de pausa no se ve afectado** (con
  `SI_MENUS_USAN_CONFIG_GLOBAL = True`): si apagás los sonidos en una
  escena, las opciones de esa escena no suenan, pero guardar, cargar y
  preferencias siguen sonando normalmente.
- **También desde una pantalla (screen):** podés usar las funciones con
  la acción `Function`, por ejemplo:

  ```renpy
  textbutton "Silenciar botones" action Function(si_desactivar)
  ```

- **Un botón puntual sin sonido:** si querés que un botón en particular
  no suene, ponele `hover_sound None activate_sound None` en su
  definición dentro de la pantalla.
- Este módulo se encarga de las propiedades `hover_sound` y
  `activate_sound` de los estilos listados en `SI_ESTILOS`. Si ya tenías
  sonidos puestos a mano en esos estilos (en `screens.rpy`), el módulo
  los reemplaza.

## Autor

- **Autor:** davinzifc

## Compatibilidad y licencia

- Compatible con Ren'Py 8.x (probado en 8.5.3).
- Licencia **MIT**, Copyright (c) 2026 davinzifc. Podés usar, copiar,
  modificar y redistribuir este módulo, incluso en juegos comerciales,
  **siempre que des crédito al desarrollador**: mantené el aviso de
  copyright y la licencia (ya están en el encabezado del archivo
  `.rpy`) en todas las copias o partes sustanciales que distribuyas, por
  ejemplo en la carpeta de créditos de tu juego. El texto completo está
  en el archivo `LICENSE` de la raíz del repositorio.
