from PIL import Image, ImageDraw

image = Image.new("RGB", (1024, 720), "white")

draw = ImageDraw.Draw(image)

triangle_points = [
    (100, 100),
    (100, 720 - 100),
    (1024 - 100, 720 - 100),
]

draw.polygon(triangle_points, outline="red")

image.save("triangle_image.png")