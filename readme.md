# Deploy en raspberry pi 4 en Debian 12 (bookworm)

* Descarga la imagen de Debian 12 (bookworm) e instalar usando el raspberry pi imager

https://www.raspberrypi.com/software/operating-systems/  (Raspberry Pi OS (Legacy, 64-bit))
Debian version	12 (bookworm)

## 1. Instalación
```
* Una vez en el escritorio, abre una nueva ventana de terminal y comienza con buenas maneras actualizando y mejorando tu sistema:

$ sudo apt update
$ sudo apt upgrade -y

Descargar conda:

$ wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh

Convertir en un archivo ejecutable con chmod:

$ chmod +x Miniforge3-Linux-aarch64.sh

luego la ejecutaremos:

$ bash Miniforge3-Linux-aarch64.sh

Una vez finalizada la instalación, debemos activar Conda en la ventana de terminal actual:

$ source ~/miniforge3/bin/activate

Ahora vamos a instalar algo llamado solucionador de paquetes libmamba. Esto básicamente mejorará Conda y le permitirá pensar de forma mucho más inteligente sobre cómo resolver e instalar nuestros paquetes complejos; una optimización realmente útil:

$ conda install conda-libmamba-solver -y

Luego le indicaremos a Conda que utilice libmamba por defecto:

$ conda config --set solver libmamba

¡Y eso es todo! Conda ya está configurado y listo para usarse en la instalación de nuestros paquetes!

```

## 2. Crear enviroment e Instalar librerias
```
Una vez que tengas Conda listo, crea un nuevo archivo .yml en la carpeta de inicio de tu Pi (/home/pi/) y llámalo:

ultralytics-pi5-environment.yml

Dentro de ese archivo, pegue lo siguiente:

name: ultralytics-env
channels:
  - pytorch
  - conda-forge
dependencies:
  - _openmp_mutex=4.5=3_kmp_llvm
  - alsa-lib=1.2.14=h86ecc28_0
  - aom=3.9.1=hcccb83c_0
  - attr=2.5.1=h4e544f5_1
  - brotli=1.1.0=h86ecc28_3
  - brotli-bin=1.1.0=h86ecc28_3
  - brotli-python=1.1.0=py311h89d996e_3
  - bzip2=1.0.8=h68df207_7
  - c-ares=1.34.5=h86ecc28_0
  - ca-certificates=2025.7.14=hbd8a1cb_0
  - cairo=1.18.4=h83712da_0
  - certifi=2025.7.14=pyhd8ed1ab_0
  - cffi=1.17.1=py311h14e8bb7_0
  - charset-normalizer=3.4.2=pyhd8ed1ab_0
  - colorama=0.4.6=pyhd8ed1ab_1
  - contourpy=1.3.2=py311hc07b1fb_0
  - cpuonly=2.0=0
  - cpython=3.11.13=py311hd8ed1ab_0
  - cycler=0.12.1=pyhd8ed1ab_1
  - cyrus-sasl=2.1.28=h6c5dea3_0
  - dav1d=1.2.1=h31becfc_0
  - dbus=1.16.2=heda779d_0
  - double-conversion=3.3.1=h5ad3122_0
  - ffmpeg=7.1.1=gpl_h30b7fc1_906
  - filelock=3.18.0=pyhd8ed1ab_0
  - font-ttf-dejavu-sans-mono=2.37=hab24e00_0
  - font-ttf-inconsolata=3.000=h77eed37_0
  - font-ttf-source-code-pro=2.038=h77eed37_0
  - font-ttf-ubuntu=0.83=h77eed37_3
  - fontconfig=2.15.0=h8dda3cd_1
  - fonts-conda-ecosystem=1=0
  - fonts-conda-forge=1=0
  - fonttools=4.59.0=py311h164a683_0
  - freeglut=3.2.2=h5eeb66e_3
  - freetype=2.13.3=h8af1aa0_1
  - fribidi=1.0.10=hb9de7d4_0
  - fsspec=2025.7.0=pyhd8ed1ab_0
  - gdk-pixbuf=2.42.12=ha61d561_0
  - gettext=0.25.1=h5ad3122_0
  - gettext-tools=0.25.1=h5ad3122_0
  - giflib=5.2.2=h31becfc_0
  - gmp=6.3.0=h0a1ffab_2
  - gmpy2=2.2.1=py311h8dd2ae4_0
  - graphite2=1.3.14=h5ad3122_0
  - h2=4.2.0=pyhd8ed1ab_0
  - harfbuzz=11.2.1=h405b6a2_0
  - hdf5=1.14.6=nompi_h587839b_102
  - hpack=4.1.0=pyhd8ed1ab_0
  - hyperframe=6.1.0=pyhd8ed1ab_0
  - icu=75.1=hf9b3779_0
  - idna=3.10=pyhd8ed1ab_1
  - imath=3.1.12=hf428078_0
  - jasper=4.2.5=h9d5db0e_0
  - jinja2=3.1.6=pyhd8ed1ab_0
  - keyutils=1.6.1=h4e544f5_0
  - kiwisolver=1.4.8=py311h75754e6_1
  - krb5=1.21.3=h50a48e9_0
  - lame=3.100=h4e544f5_1003
  - lcms2=2.17=hc88f144_0
  - ld_impl_linux-aarch64=2.44=h5e2c951_1
  - lerc=4.0.0=hfdc4d58_1
  - libabseil=20250127.1=cxx17_h18dbdb1_0
  - libaec=1.1.4=h1e66f74_0
  - libasprintf=0.25.1=h5e0f5ae_0
  - libasprintf-devel=0.25.1=h5e0f5ae_0
  - libass=0.17.3=h3c9f632_2
  - libavif16=1.3.0=hb72faec_0
  - libblas=3.9.0=32_h1a9f1db_openblas
  - libbrotlicommon=1.1.0=h86ecc28_3
  - libbrotlidec=1.1.0=h86ecc28_3
  - libbrotlienc=1.1.0=h86ecc28_3
  - libcap=2.75=h51d75a7_0
  - libcblas=3.9.0=32_hab92f65_openblas
  - libclang-cpp20.1=20.1.8=default_hf07bfb7_0
  - libclang13=20.1.8=default_h173080d_0
  - libcups=2.3.3=h5cdc715_5
  - libcurl=8.14.1=h6702fde_0
  - libde265=1.0.15=h2a328a1_0
  - libdeflate=1.24=he377734_0
  - libdrm=2.4.125=h86ecc28_0
  - libedit=3.1.20250104=pl5321h976ea20_0
  - libegl=1.7.0=hd24410f_2
  - libev=4.33=h31becfc_2
  - libexpat=2.7.1=hfae3067_0
  - libffi=3.4.6=he21f813_1
  - libflac=1.4.3=h2f0025b_0
  - libfreetype=2.13.3=h8af1aa0_1
  - libfreetype6=2.13.3=he93130f_1
  - libgcc=15.1.0=he277a41_3
  - libgcc-ng=15.1.0=he9431aa_3
  - libgcrypt-lib=1.11.1=h86ecc28_0
  - libgettextpo=0.25.1=h5ad3122_0
  - libgettextpo-devel=0.25.1=h5ad3122_0
  - libgfortran=15.1.0=he9431aa_3
  - libgfortran5=15.1.0=hbc25352_3
  - libgl=1.7.0=hd24410f_2
  - libglib=2.84.2=hc022ef1_0
  - libglu=9.0.3=h5ad3122_1
  - libglvnd=1.7.0=hd24410f_2
  - libglx=1.7.0=hd24410f_2
  - libgomp=15.1.0=he277a41_3
  - libgpg-error=1.55=h5ad3122_0
  - libheif=1.19.7=gpl_hf91bf23_100
  - libhwloc=2.11.2=default_h6f258fa_1002
  - libiconv=1.18=hc99b53d_1
  - libjpeg-turbo=3.1.0=h86ecc28_0
  - liblapack=3.9.0=32_h411afd4_openblas
  - liblapacke=3.9.0=32_hc659ca5_openblas
  - libllvm20=20.1.8=h2b567e5_0
  - liblzma=5.8.1=h86ecc28_2
  - libnghttp2=1.64.0=hc8609a4_0
  - libnsl=2.0.1=h86ecc28_1
  - libntlm=1.4=hf897c2e_1002
  - libogg=1.3.5=h86ecc28_1
  - libopenblas=0.3.30=pthreads_h9d3fd7e_0
  - libopencv=4.12.0=qt6_py311h6b27ceb_600
  - libopengl=1.7.0=hd24410f_2
  - libopenvino=2025.0.0=hd63d6c0_3
  - libopenvino-arm-cpu-plugin=2025.0.0=hd63d6c0_3
  - libopenvino-auto-batch-plugin=2025.0.0=hf15766e_3
  - libopenvino-auto-plugin=2025.0.0=hf15766e_3
  - libopenvino-hetero-plugin=2025.0.0=ha8e9e04_3
  - libopenvino-ir-frontend=2025.0.0=ha8e9e04_3
  - libopenvino-onnx-frontend=2025.0.0=hd8f0270_3
  - libopenvino-paddle-frontend=2025.0.0=hd8f0270_3
  - libopenvino-pytorch-frontend=2025.0.0=h5ad3122_3
  - libopenvino-tensorflow-frontend=2025.0.0=h33e842c_3
  - libopenvino-tensorflow-lite-frontend=2025.0.0=h5ad3122_3
  - libopus=1.5.2=h86ecc28_0
  - libpciaccess=0.18=h86ecc28_0
  - libpng=1.6.50=hec79eb8_0
  - libpq=17.5=hf590da8_0
  - libprotobuf=5.29.3=h4edc36e_1
  - librsvg=2.58.4=h3ac5bce_3
  - libsndfile=1.2.2=h79657aa_1
  - libsqlite=3.50.2=hdbb6186_2
  - libssh2=1.11.1=h18c354c_0
  - libstdcxx=15.1.0=h3f4de04_3
  - libstdcxx-ng=15.1.0=hf1166c9_3
  - libsystemd0=257.7=h2bb824b_0
  - libtiff=4.7.0=h7c15681_5
  - libtorch=2.7.1=cpu_generic_h1028f2b_2
  - libudev1=257.7=h7b9e449_0
  - libunwind=1.8.2=h9e2cd2c_0
  - liburing=2.11=h17cf362_0
  - libusb=1.0.29=h06eaf92_0
  - libuuid=2.38.1=hb4cce97_0
  - libuv=1.51.0=h86ecc28_0
  - libvorbis=1.3.7=h01db608_0
  - libvpx=1.14.1=h0a1ffab_0
  - libwebp-base=1.6.0=ha2e29f5_0
  - libxcb=1.17.0=h262b8f6_0
  - libxcrypt=4.4.36=h31becfc_1
  - libxkbcommon=1.10.0=hbab7b08_0
  - libxml2=2.13.8=he060846_0
  - libzlib=1.3.1=h86ecc28_2
  - llvm-openmp=20.1.8=he40846f_0
  - lz4-c=1.10.0=h5ad3122_1
  - markupsafe=3.0.2=py311ha09ea12_1
  - matplotlib-base=3.10.3=py311h0385ec1_0
  - mpc=1.3.1=h783934e_1
  - mpfr=4.2.1=h2305555_3
  - mpg123=1.32.9=h65af167_0
  - mpmath=1.3.0=pyhd8ed1ab_1
  - munkres=1.1.4=pyhd8ed1ab_1
  - ncurses=6.5=ha32ae93_3
  - networkx=3.4.2=pyh267e887_2
  - nomkl=1.0=h5ca1d4c_0
  - numpy=1.24.2=py311h71ac5a4_0
  - opencv=4.12.0=qt6_py311hc303290_600
  - openexr=3.3.4=h718fb27_0
  - openh264=2.6.0=h0564a2a_0
  - openjpeg=2.5.3=h3f56577_0
  - openldap=2.6.10=h30c48ee_0
  - openssl=3.5.1=hd08dc88_0
  - optree=0.16.0=py311hc07b1fb_0
  - packaging=25.0=pyh29332c3_1
  - pandas=2.3.1=py311hffd966a_0
  - pango=1.56.4=he55ef5b_0
  - patsy=1.0.1=pyhd8ed1ab_1
  - pcre2=10.45=hf4ec17f_0
  - pillow=11.3.0=py311ha4eaa5e_0
  - pip=25.1.1=pyh8b19718_0
  - pixman=0.46.2=h86a87f0_0
  - psutil=7.0.0=py311ha879c10_0
  - pthread-stubs=0.4=h86ecc28_1002
  - pugixml=1.15=h6ef32b0_0
  - pulseaudio-client=17.0=h2f84921_1
  - py-cpuinfo=9.0.0=pyhd8ed1ab_1
  - py-opencv=4.12.0=qt6_py311h01b6c42_600
  - pybind11=3.0.0=pyh9380348_1
  - pybind11-global=3.0.0=pyhf748d72_1
  - pycparser=2.22=pyh29332c3_1
  - pyparsing=3.2.3=pyhd8ed1ab_1
  - pysocks=1.7.1=pyha55dd90_7
  - python=3.11.13=h1683364_0_cpython
  - python-dateutil=2.9.0.post0=pyhe01879c_2
  - python-tzdata=2025.2=pyhd8ed1ab_0
  - python_abi=3.11=7_cp311
  - pytorch=2.7.1=cpu_generic_py311_hcdfc2e8_2
  - pytorch-mutex=1.0=cpu
  - pytz=2025.2=pyhd8ed1ab_0
  - pyyaml=6.0.2=py311h58d527c_2
  - qhull=2020.2=h70be974_5
  - qt6-main=6.9.1=h13135bf_1
  - rav1e=0.7.1=ha3529ed_3
  - readline=8.2=h8382b9d_2
  - requests=2.32.4=pyhd8ed1ab_0
  - scipy=1.15.2=py311h2973cce_0
  - sdl2=2.32.54=h5ad3122_0
  - sdl3=3.2.18=h506f210_0
  - seaborn=0.13.2=hd8ed1ab_3
  - seaborn-base=0.13.2=pyhd8ed1ab_3
  - setuptools=80.9.0=pyhff2d567_0
  - six=1.17.0=pyhd8ed1ab_0
  - sleef=3.8=h8fb0607_0
  - snappy=1.2.1=hd4fb6f5_1
  - statsmodels=0.14.5=py311h8b8d0ce_0
  - svt-av1=3.0.2=h5ad3122_0
  - sympy=1.14.0=pyh2585a3b_105
  - tbb=2022.1.0=hf6e3e71_0
  - tk=8.6.13=noxft_h5688188_102
  - torchvision=0.22.0=cpu_py311_hb1dc043_1
  - torchvision-extra-decoders=0.0.2=py311h4a11f85_3
  - tqdm=4.67.1=pyhd8ed1ab_1
  - typing-extensions=4.14.1=h4440ef1_0
  - typing_extensions=4.14.1=pyhe01879c_0
  - tzdata=2025b=h78e105d_0
  - ultralytics=8.3.167=pyh2a12c56_0
  - unicodedata2=16.0.0=py311ha879c10_0
  - urllib3=2.5.0=pyhd8ed1ab_0
  - wayland=1.24.0=h698ed42_0
  - wheel=0.45.1=pyhd8ed1ab_1
  - x264=1!164.3095=h4e544f5_2
  - x265=3.5=hdd96247_3
  - xcb-util=0.4.1=hca56bd8_2
  - xcb-util-cursor=0.1.5=h86ecc28_0
  - xcb-util-image=0.4.0=h5c728e9_2
  - xcb-util-keysyms=0.4.1=h5c728e9_0
  - xcb-util-renderutil=0.3.10=h5c728e9_0
  - xcb-util-wm=0.4.2=h5c728e9_0
  - xkeyboard-config=2.45=h86ecc28_0
  - xorg-libice=1.1.2=h86ecc28_0
  - xorg-libsm=1.2.6=h0808dbd_0
  - xorg-libx11=1.8.12=hca56bd8_0
  - xorg-libxau=1.0.12=h86ecc28_0
  - xorg-libxcomposite=0.4.6=h86ecc28_2
  - xorg-libxcursor=1.2.3=h86ecc28_0
  - xorg-libxdamage=1.1.6=h86ecc28_0
  - xorg-libxdmcp=1.1.5=h57736b2_0
  - xorg-libxext=1.3.6=h57736b2_0
  - xorg-libxfixes=6.0.1=h57736b2_0
  - xorg-libxi=1.8.2=h57736b2_0
  - xorg-libxrandr=1.5.4=h86ecc28_0
  - xorg-libxrender=0.9.12=h86ecc28_0
  - xorg-libxtst=1.2.5=h57736b2_3
  - xorg-libxxf86vm=1.1.6=h86ecc28_0
  - yaml=0.2.5=hf897c2e_2
  - zstandard=0.23.0=py311ha879c10_2
  - zstd=1.5.7=hbcf94c1_2

Esto crear una enviroment con todas las librerias necesarias, ahi se define la versión de python, versión de ultralytics, pytorch, torchvision etc..

IMPORTANTE: Cambiar la versión de numpy; abre una nueva terminal y ejecuta:

$ python3 -c "import numpy; print(numpy.__version__)"

Copia la versión de numpy que te aparesca y actualizala en el archivo ultralytics-pi5-environment.yml :

numpy=1.24.2=py311h71ac5a4_0

aunque como estamos usando Debian 12 lo mas probable es que tengas la misma versión.

Así, esto es esencialmente una lista de todos los paquetes que Ultralytics necesita instalar y, lo que es más importante, qué versión está instalada. En una ventana de terminal, asegúrese de haber activado Conda y luego cree un nuevo entorno virtual con los paquetes de esa lista con:

$ conda env create -f ultralytics-pi5-environment.yml

Una vez finalizada la instalación, podemos configurar picamera2 con el siguiente comando echo en el enviroment cread:

* Activar enviroment:

$ conda activate NOMBRE_ENVIROMENT

$ echo '/usr/lib/python3/dist-packages' > /home/CAMBIA_NOMBRE_USUARIO/miniforge3/envs/ultralytics-env/lib/python3.11/site-packages/system-packages.pth

Nota: donde dice 'CAMBIA_NOMBRE_USUARIO' agrega el nombre del usuario de tu raspberry pi.


¡Ya tienes listo el paquete Ultralytics YOLO. A partir de aquí, podrás ejecutar código Python para descargar y usar cualquier modelo compatible con Ultralytics!!

```

### Otros:

```
* Listar conda enviroments:

$ conda env list

* Eliminar un enviroment por nombre:

$ conda remove --name NOMBRE_ENVIROMENT --all

* Activar conda para luego activar enviroment x:

$ source ~/miniforge3/bin/activate

$ conda activate NOMBRE_ENVIROMENT

```

## Listar camaras:
```
$ ls /dev/video*
```