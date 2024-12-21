# TecnoProductos - Back (Python+Django)
Este proyecto tiene como objetivo desarrollar una plataforma digital para la venta de productos electrónicos. Este cuenta tanto con **FrontEnd** y **BackEnd**: En el caso del **Back** esta construido con **Django**, **Django REST Framework** y autenticación mediante **JWT**. Todo esto con el fin de tener una api bien estrucrutada
<br>

![python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
## Tecnologías

- **Backend**: Python 3, Django, Django REST Framework
- **Autenticación**: djangorestframework-simplejwt (JWT)
- **Tests**: Tests integrados con `unittest` y las herramientas nativas de Django + DRF

## Requisitos Previos

- **Python 3.9+** (idealmente)
- Git (opcional)

## Instalación y Configuración

1. **Clonar el repositorio**:
   
   ```bash
   git clone https://github.com/Mayderking/backend_tecno.git
  
2. **Crear y activar entorno virtual (opcional)**:
   
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/Mac
   # venv\Scripts\activate    # Windows
  
3. **Instalar dependencias**:
   
   ```bash
   pip install django 
   ```
   ```bash
     pip install djangorestframework
   ```
   ```bash
   pip install django-cors-headers
   ```
    
> [!Note]
> Recuerda seguir todos los pasos al pie de la letra, para que la instalacion y ejecucion salga bien.

4. **Migrar**:
      
   ```bash
   python manage.py migrat
   ```
5. **Crear un superusuario (opcional)**:
    ```bash
    python manage.py createsuperuser
   
6. **Iniciar el servidor**
   ```bash
    py manage.py runserver
