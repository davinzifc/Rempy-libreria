# Librería de Módulos para Ren'Py

Proyecto **gratuito y de código abierto para la comunidad de Ren'Py**.
Acá vas a encontrar módulos "copiar y pegar": cada uno agrega una
funcionalidad a tu juego (por ejemplo, un efecto de texto) sin que
tengas que programarla desde cero. Están pensados para poder usarse
aunque no sepas programar.

Este proyecto existe gracias a la comunidad de **[Venus Tuto](https://www.youtube.com/@VenusTuto)**,
un canal de YouTube dedicado a enseñar Ren'Py. 💜

## Índice de módulos

| Módulo | Qué hace |
|---|---|
| [Efecto Máquina de Escribir](libreria/game/modulos/efecto_maquina_de_escribir/README.md) | El texto de los diálogos aparece letra por letra, con un sonido de tecleo opcional y configurable. |

*(A medida que se agreguen más módulos, van a aparecer acá.)*

## Cómo usar un módulo

1. Entrá a la carpeta del módulo que te interese (link en el índice de
   arriba) y leé su propio `README.md`: ahí están los pasos exactos de
   instalación y configuración de ESE módulo en particular.
2. En general, la idea es siempre la misma: copiás la carpeta completa
   del módulo dentro de `game/modulos/` en tu propio proyecto de Ren'Py,
   y listo — no hace falta tocar ningún otro archivo.

## Estructura del proyecto

```
libreria/                          <- proyecto de Ren'Py (podés abrirlo con el Launcher)
└── game/
    └── modulos/
        └── efecto_maquina_de_escribir/   <- un módulo, autocontenido en su carpeta
            ├── modulo_efecto_maquina_de_escribir.rpy
            ├── audio/
            └── README.md
```

Cada módulo vive en su propia carpeta, con todo lo que necesita adentro
(script, sonidos u otros archivos, y su propio `README.md`), para que
copiarlo a otro proyecto sea tan simple como copiar esa carpeta.

## Licencia

Uso libre para la comunidad de Ren'Py: podés copiar, modificar y
redistribuir cualquiera de estos módulos, en proyectos personales o
comerciales, sin necesidad de dar crédito (aunque siempre se agradece).
