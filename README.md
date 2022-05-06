# librarie-robot-ROS
## Requisitos previos a la instalación y ejecución del proyecto
Para poder ejecutar el proyecto es necesario tener una instalacion apropiada de ROS y otros paquetes, la cual se describe a continuacion:


    - Ubuntu 16.04LTS.
    -  Git instalado y credenciales SSH para Github.
    -  Ros kinetic Full desktop install y el simulador BebopS basado en Gazebo.  
    -  Simulador de los rotores.
    -  Paquete Bebop_autonomy.
    -  Paquetes para vitualizar el control .
    -  Espacio de trabajo compilado con los paquetes (El proyecto fue probado con Catkin Make).

Es importante instalar estos paquetes desde la fuente para tener la ultima version disponible para Kinetic, a pesar que en BebopS proporcione una instalación para algunos de estos paquetes es necesario actualizarlos. 

## Instalación del proyecto
Una vez cumplidos los requisitos previos se procedera a obtener el proyecto haciendo un git clone a nuestro repositorio y ejecu.
`git clone git@github.com:Pondigo/librarie-robot-ROS.git` \
`cd librarie-robot-ROS` \
`sudo ./initLibraryBebopProject.sh`
El segundo comando se encarga de descargar los archivos bag, que se leen con los comandos de implementacion escritos en python, usando la API de rosbag.

## Ejecución del proyecto
Una vez se tiene el espacio de trabajo completo y se ha inicializado el proyecto correctamente, se podrá ejecutar tanto la version simulada como la implementación fisica. Para ejecutar la simulación se deberan ejecutar los siguientes comandos reemplazando catkin_workspace\dir por el directorio del workspace donde se instalaron y compilaron los paquetes requeridos.


`source [catkin_workspace_dir]/devel/setup.bas` \
`roslaunch bebop_simulator bebop_without_controller.launch`

Para controlar la simulación que como indica su nombre no contiene un controlador, se requerira ejecutar un nodo de bebop_driver tal y como se puede ver a continuación.

`source [catkin_workspace_dir]/devel/setup.bash` \
`roslaunch bebop_driver bebop_node.launch`

Una vez se ha ejecutado la simulación del bebop y el driver se ejecutara en otra terminal el archivo de implementacion en la simulación, reemplazando instalation_dir por el directorio donde se encuentra librarie−robot−ROS. 

`source [catkin_workspace_dir]/devel/setup.bash ` \
`cd [instalation_dir]` \
`python ./simulation.py`

Con esto la secuencia de arranque y un mapeo lateral se llevara a cabo, en este caso al ser en simulación se obvio el concatenamiento de trayectorias, por lo que solo se ejecutara esto una vez.

En cambio para la implementacion fisica se requerira editar en el archivo ~/.bashrc las variables de entorno ROS_MASTER_URI por http://localhost:11311 y ROS_HOSTNAME por localhost. Para posteriormente conectarse con la red provista por el dron Bebop. Una vez conectado se requerira ejecutar un nodo de bebop_driver como en la terminal 2 de la simulación y luego en otra terminal se ejecutara el archivo que lee la implemetacion fisica tal y como se puede observar en el siguiente codigo.

`source [catkin_workspace_dir]/devel/setup.bash ` \
`cd [instalation_dir]` \
`source ~/.bashrc` \
`python ./implementation_bag.py`

Con esto veremos una ejecución de la implementación del proyecto en el dron bebob, donde en la terminal podremos indicar si queremos seguir mapeando lateralmente (Con "S"), hasta que indiquemos que ya no (Con "N").
