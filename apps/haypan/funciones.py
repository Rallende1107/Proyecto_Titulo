import os
import json
from .models import Region, Comuna
from django.conf import settings

def cargar_datos_desde_json():
    print("cargar_datos_desde_json")
    try:
        ruta_archivo = os.path.join(settings.BASE_DIR, 'static', 'json', 'regiones.json')
        print(ruta_archivo)

        with open(ruta_archivo, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(data)

        for entry in data:
            region_data = entry.get('region', {})
            comunas_data = entry.get('comunas', [])

            if not region_data or not comunas_data:
                raise ValueError("El formato del JSON es incorrecto")

            region_nombre = region_data.get('nombre', '')
            region_latitud = region_data.get('latitud', '')
            region_longitud = region_data.get('longitud', '')

            # Validar si la Región ya existe
            region, created = Region.objects.get_or_create(nombre=region_nombre, latitud=region_latitud, longitud=region_longitud)
            if not created:
                print(f"La región '{region_nombre}' ya existe")

            for comuna_data in comunas_data:
                comuna_nombre = comuna_data.get('nombre', '')
                comuna_latitud = comuna_data.get('latitud', '')
                comuna_longitud = comuna_data.get('longitud', '')

                # Validar si la Comuna ya existe para esta Región
                comuna, comuna_created = Comuna.objects.get_or_create(nombre=comuna_nombre, latitud=comuna_latitud, longitud=comuna_longitud, region=region)
                if not comuna_created:
                    print(f"La comuna '{comuna_nombre}' ya existe para la región '{region_nombre}'")

        print("Datos cargados exitosamente")
        return {"status": "success", "message": "Datos cargados exitosamente"}

    except FileNotFoundError:
        print("El archivo JSON no se encontró")
        return {"status": "error", "message": "El archivo JSON no se encontró"}
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON")
        return {"status": "error", "message": "Error al decodificar el archivo JSON"}
    except ValueError as ve:
        print(str(ve))
        return {"status": "error", "message": str(ve)}
    except Exception as e:
        print(str(e))
        return {"status": "error", "message": str(e)}
