import json
import os
import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

# Configuración de rutas
DATA_DIR = '../data' 
IMAGES_DIR = os.path.join(DATA_DIR, 'images')

JSON_FILES = {
    'train': os.path.join(DATA_DIR, 'mvtec_screws_train.json'),
    'val':   os.path.join(DATA_DIR, 'mvtec_screws_val.json'),
    'test':  os.path.join(DATA_DIR, 'mvtec_screws_test.json')
}

# Función para cargar y mapear datos de JSON
def get_global_image_map(json_files):
    """
    Carga todos los JSONs y devuelve un diccionario.
    CORRECCIÓN: Usa una clave única (source + id) para evitar mezclar 
    cajas de train con test si los IDs se repiten.
    """
    global_annotations = {}
    global_categories = {}
    
    for name, path in json_files.items():
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    data = json.load(f)
            except Exception as e:
                print(f"Error al cargar {name} JSON: {e}")
                continue

            # Mapear categorías (solo una vez)
            if not global_categories:
                 global_categories = {cat['id']: cat['name'] for cat in data['categories']}

            # Mapa local de IDs -> Nombres de archivo
            image_filename_map = {img['id']: img['file_name'] for img in data['images']}

            for ann in data['annotations']:
                img_id = ann['image_id']
                
                # GENERAR CLAVE ÚNICA
                # Evita colisión si 'train' y 'test' tienen ambos una imagen con ID=1
                unique_key = f"{name}_{img_id}" 
                
                if unique_key not in global_annotations:
                    global_annotations[unique_key] = {
                        'filename': image_filename_map[img_id],
                        'source': name, # Guardamos de qué JSON vino
                        'original_id': img_id,
                        'bboxes': []
                    }
                
                # Solo añadimos la caja a su entrada única correspondiente
                global_annotations[unique_key]['bboxes'].append(ann['bbox'])

    return global_annotations, global_categories

def calculate_ratio_for_bboxes(bboxes):
    """Calcula el ratio Max/Min usando la diagonal."""
    objects_data = []
    
    for bbox in bboxes:
        # Nota: Si el formato es [col, row, w, h, phi], ajusta aquí. 
        # COCO estándar es [x, y, w, h]. MVTec rotado suele ser [y, x, w, h, phi] o [x, y, w, h, phi]
        # Asumimos que width y height son índices 2 y 3.
        width = bbox[2]
        height = bbox[3]
        
        float_width = float(width)
        float_height = float(height)
        longitud_diagonal = math.sqrt(float_width**2 + float_height**2)
        objects_data.append({'size': longitud_diagonal})

    if len(objects_data) < 2:
        return 0.0 
    
    objects_data.sort(key=lambda x: x['size'])
    obj_min_size = objects_data[0]['size']
    obj_max_size = objects_data[-1]['size']
    
    if obj_min_size == 0: return 0.0
    return obj_max_size / obj_min_size

def visualize_best_case(image_data, global_categories):
    """Visualiza la imagen ganadora con correcciones de dibujo."""
    target_filename = image_data['filename']
    target_image_path = os.path.join(IMAGES_DIR, target_filename)
    bboxes = image_data['bboxes']
    
    if not os.path.exists(target_image_path):
        print(f"Error: No se encuentra la imagen {target_image_path}")
        return

    # 1. Recalcular datos para visualización
    objects_data = []
    for bbox in bboxes:
        row, col, width, height, phi = bbox # Asumiendo formato estándar del JSON
        
        float_width = float(width)
        float_height = float(height)
        longitud_diagonal = math.sqrt(float_width**2 + float_height**2)

        center = (float(col), float(row))
        size = (float_width, float_height)
        angle_deg = math.degrees(-float(phi))

        rect = (center, size, angle_deg)
        box_points = cv2.boxPoints(rect)
        box_points = np.intp(box_points) 

        objects_data.append({
            'size': longitud_diagonal,
            'box': box_points,
            'center': (int(col), int(row))
        })
        
    objects_data.sort(key=lambda x: x['size'])
    obj_min = objects_data[0]
    obj_max = objects_data[-1]
    ratio = obj_max['size'] / obj_min['size']

    # 2. Dibujar
    img = cv2.imread(target_image_path)
    
    # Dibujar todos en azul
    for obj in objects_data:
        cv2.drawContours(img, [obj['box']], 0, (255, 0, 0), 2)
        
    # MÍNIMO (Amarillo)
    cv2.drawContours(img, [obj_min['box']], 0, (0, 255, 255), 4) 
    cv2.putText(img, f"MIN: {obj_min['size']:.1f}", 
                (obj_min['center'][0] - 50, obj_min['center'][1] + 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 3)

    # MÁXIMO (Verde)
    cv2.drawContours(img, [obj_max['box']], 0, (0, 255, 0), 4)
    cv2.putText(img, f"MAX: {obj_max['size']:.1f}", 
                (obj_max['center'][0] - 50, obj_max['center'][1] - 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 3)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    plt.figure(figsize=(12, 8))
    plt.imshow(img_rgb)
    plt.title(f"Imagen con mayor ratio entre tamaño de piezas\n"
              f"Set: {image_data['source']} | Imagen: {target_filename}\n"
              f"Ratio = {ratio:.2f}", 
              fontsize=16, fontweight='bold')
    plt.axis('off')
    plt.show()

# BLOQUE PRINCIPAL
global_annotations, global_categories = get_global_image_map(JSON_FILES)

best_ratio = 0.0
best_unique_key = None

print(f"Total de entradas únicas procesadas: {len(global_annotations)}")

for unique_key, data in global_annotations.items():
    ratio = calculate_ratio_for_bboxes(data['bboxes'])
    
    if ratio > best_ratio:
        best_ratio = ratio
        best_unique_key = unique_key
        

print("\n-------------------------------------------------------------")

if best_unique_key is not None:
    best_data = global_annotations[best_unique_key]
    
    print(f"ANÁLISIS FINALIZADO:")
    print(f"   Imagen con peor ratio: {best_data['filename']}")
    print(f"   Origen: {best_data['source']}")
    print(f"   Ratio máximo: {best_ratio:.2f}")
    
    visualize_best_case(best_data, global_categories)
else:
    print("No se encontraron datos válidos.")