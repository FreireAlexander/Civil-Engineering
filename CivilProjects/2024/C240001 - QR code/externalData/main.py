import qrcode
import svgwrite

# URL o datos para el QR
url = "https://freirealexander.top"

# Crear el objeto QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # Tamaño de cada cuadro
    border=4,  # Grosor del borde
)
qr.add_data(url)
qr.make(fit=True)

# Crear un archivo SVG usando svgwrite
dwg = svgwrite.Drawing("codigo_qr.svg", profile="tiny")

# Generar el patrón QR
matrix = qr.get_matrix()  # Matriz booleana del QR (True para cuadros negros)
box_size = 10  # Tamaño de cada celda en mm
border = 4 * box_size  # Espaciado alrededor del QR

# Dibujar cada celda negra como un rectángulo en el SVG
for y, row in enumerate(matrix):
    for x, cell in enumerate(row):
        if cell:  # Si es True, dibuja un cuadro negro
            dwg.add(
                dwg.rect(
                    insert=(x * box_size + border, y * box_size + border),
                    size=(box_size, box_size),
                    fill="black",
                )
            )

# Guardar el archivo SVG
dwg.save()

print("Código QR generado y guardado como 'codigo_qr.svg'.")
