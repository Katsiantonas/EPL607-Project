# EPL607 - Project Part 1

## Introduction
In this Project, we create a python script which renders a right red triangle and saves it into
a PNG file.

## Members
- Antonis Katsiantonis
- Nikolas Vattis

## Programming Language
For this project, we decided to use the Python language because it's a general purpose language, 
it's easy to work with and provides easy-to-use libraries for the purpose of our Project. 
This way, we can focus on the logical part of the project, and less with the language itself.

## Image Processing Library
For the image processing, we decided to use the Pillow library, because it's one of the more
popular options for image rendering. Also, iit provides a simple interface for drawing shapes, 
such as triangles.

## Rendering Process
In order to draw our first triangle, what we did initially was to define its points. We did this 
by creating a list of 3 tuples, each tuple having the x and y coordinates of a triangle vertex. 
The units of the vertex coordinates are pixels, where (0, 0) starts at the top left.
The vertices are then passed as input to the Pillow library, which then creates a new image 
and draws a triangle using the input points as vertices. 

## Image Result
![Image Result](triangle_image.png "Image Result")
After the rendering process, the Pillow library saves the generated image in a PNG file. We 
have generated a right red triangle with vertices on the top-left, bottom-left and bottom-right
corners (100 pixels away from the image corners).