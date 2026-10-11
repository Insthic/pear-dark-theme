# Pear Dark Theme

Tema personal para [Pear Desktop](https://github.com/pear-devs/pear-desktop), con fondo oscuro uniforme, portadas redondeadas, cola y letras con margen interno, y un reproductor con controles más visibles.

La barra de progreso tiene una línea de 8 px, un área de interacción de 28 px y un indicador siempre visible. En Linux, el menú de Pear se integra como un botón de tres puntos en el encabezado de YouTube Music.

Este repositorio contiene solamente CSS y un instalador. **Pear Desktop se instala por separado.** No incluye el perfil de una cuenta de Google, cookies, historial, credenciales ni una copia completa de config.json.

## Instalación

1. Instalá Pear Desktop y abrilo una vez para crear su configuración.
2. Cerrá Pear por completo, incluida la bandeja si está habilitada.
3. Descargá este repositorio como ZIP y extraelo.
4. Desde la carpeta extraída, ejecutá:

```sh
python3 install.py
```

En Windows, con Python instalado:

```powershell
py install.py
```

Podés comprobar el destino antes de instalar:

```sh
python3 install.py --dry-run
```

Si Pear usa otra ubicación, pasá el directorio que contiene su config.json:

```sh
python3 install.py --config-dir "/ruta/al/perfil/YouTube Music"
```

El instalador copia los CSS, genera rutas locales y conserva los demás ajustes de tu perfil. Desactiva Album Color Theme, Ambient Mode, Blur Navigation Bar, Visualizer y Synced Lyrics para usar una apariencia consistente y las letras nativas de YouTube Music. En Linux, activa únicamente In-App Menu para integrar el menú y quitar la barra de título separada.

Si ya importaste CSS con los nombres `pear-dark.css` o `progress-bar.css`, reemplaza esas entradas en la lista de temas por las de este paquete. Los otros temas permanecen registrados; pueden cambiar el resultado visual.

## Compatibilidad

Probado visualmente en Pear Desktop 3.12.0 sobre Linux, con ventanas de 936 y 1920 px de ancho. Windows y macOS no se probaron; conservan el comportamiento de los menús de Pear, y la integración del menú de tres puntos se aplica solamente en Linux.

El estilo de progreso está pensado para el minirreproductor nuevo de YouTube Music. Una cuenta con otro diseño puede necesitar ajustes. Los cambios de YouTube Music pueden requerir actualizar selectores del tema.

Pear aplica el CSS después de cargar la página, por lo que puede verse brevemente la apariencia original al abrirlo. Este paquete no modifica ese mecanismo ni incorpora crossfade o AutoMix.

## Deshacer

El instalador guarda un respaldo **local**, dentro de `pear-dark-backups` en el directorio del perfil. Con Pear cerrado, copiá el config.json del respaldo que quieras recuperar sobre el config.json del perfil y volvé a abrir Pear. Si reemplazaste una versión anterior del paquete, también se guarda su carpeta de temas.

No subas esos respaldos al repositorio: contienen tu configuración personal.

## Archivos públicos

- `themes/pear-dark.css`: apariencia e integración del menú en Linux.
- `themes/progress-bar.css`: barra de progreso ampliada.
- `install.py`: instalador sin dependencias externas ni conexiones de red.
- `PRIVACY.md`: límites del paquete y datos excluidos.

El proyecto no está afiliado a Pear Desktop, YouTube, Google, Spotify ni Tidal.
