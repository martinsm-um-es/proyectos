import csv
import os

def split_csv(input_file, output_dir, rows_per_file):
    """
    Divide un archivo CSV en múltiples archivos más pequeños.
    
    Args:
        input_file (str): Ruta al archivo CSV de entrada.
        output_dir (str): Carpeta donde se guardarán los archivos divididos.
        rows_per_file (int): Número de filas por cada archivo dividido.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, mode="r", newline="", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        headers = next(reader)  # Leer los encabezados

        file_index = 1
        rows = []
        for row in reader:
            rows.append(row)
            if len(rows) == rows_per_file:
                output_file = os.path.join(output_dir, f"Temperatura_{file_index}.csv")
                with open(output_file, mode="w", newline="", encoding="utf-8") as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow(headers)  # Escribe los encabezados
                    writer.writerows(rows)
                print(f"Archivo creado: {output_file}")
                file_index += 1
                rows = []

        # Guardar cualquier fila restante
        if rows:
            output_file = os.path.join(output_dir, f"Temperatura_{file_index}.csv")
            with open(output_file, mode="w", newline="", encoding="utf-8") as outfile:
                writer = csv.writer(outfile)
                writer.writerow(headers)
                writer.writerows(rows)
            print(f"Archivo creado: {output_file}")

# Parámetros de entrada
input_csv = "./Temperatura.csv"  # Ruta al archivo de entrada
output_directory = "mi_info"  # Carpeta donde guardar los fragmentos
rows_per_split = 40  # Número de filas por archivo

# Ejecutar el programa
split_csv(input_csv, output_directory, rows_per_split)
