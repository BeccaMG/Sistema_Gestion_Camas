Sistema de Gestión de Camas
===========================

Módulo de Gestión de Camas del Sistema de Hospitales desarrollado como MiniProyecto de Desarollo de Software en la Universidad Simón Bolívar para el Centro Médico de Caracas.

===========================
Carpetas y contenidos

	- AM.
	- app_camas:  Archivos relacionados a manejar los pacientes del sistema.
		En el models se encuentran las entidades Ingreso y Habitacion.
	- app_estadisticas: Archivos relacionados a manejar las estadisticas del sistema.
		Actualmente sólo se maneja el termómetro y la matriz de habitaciones.
	- app_paciente: Archivos relacionados a manejar los pacientes del sistema.
		En el models se encuentran la entidad Paciente.
	- app_solicitudes: Archivos relacionados a manejar las solicitudes de camas.
		En el models se encuentran la entidad Solicitud.
	- app_usuario: Archivos relacionados con usuarios del sistema. 
		En el models se encuentran las entidades Médico y Usuario.
	- BD: Archivos relacionados con la base de datos.
	- documentacion: 
		- BD-Documentacion: Se podrá encontrar un diagrama ERE y diccionario de datos de la base de datos del sistema.
		- configuracion: Contiene el archivo settings que deberá ser debidamente modificado y colocado en la carpeta AM.
		- manuales: 
			- Instalación en linux.
			- Instalación en windows. (Versión 1.1)
			- Recomendaciones de modularidad.
		- pantallazosSistema: Imágenes de propuesta para la interfaz del sistema. 
	- static:
		- css: Hojas de estilo del sistema.
		- img: Imágenes utilizadas en el sistema.
		- libs: Librerías utilizadas.
		- scripts: Scripts estáticos para el sistema.
	- templates: Archivos htmls del sistema.

===========================
Bibliografía/enlaces recomendados

	https://www.djangoproject.com/
	http://www.djangobook.com/en/2.0/index.html
	http://aiti.mit.edu/media/programs/mexico-summer-2013/materials/djangobook.pdf

===========================