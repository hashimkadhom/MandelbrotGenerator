#Written by Hashim Kadhom

#Here everything is imported
import pygame
from point import Point

#Here pygame is initialized
pygame.init()

#Here the window is set up
SCREEN_DIMENSIONS = (600,600)
win = pygame.display.set_mode(SCREEN_DIMENSIONS)

#This is where the code's executed
def main():
  #This checks if the user closes the program

  win.fill((0,0,0))

  ranges = [[-2,2],[-2,2]]
   
  point_list = produce_points(SCREEN_DIMENSIONS,ranges)

  for point in point_list:
    point.output_value = test(point.input_value)
    point.plot()

  print("Done")

  while (True):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

    pygame.display.update()
                                
#Returns a list of 'empty' gridded points
#Parameters:
  #dimensions: float[1]
  #density: float[1]
def produce_points(density,ranges):
  point_list = []
  point_size = [1,1] 
  
  point_change = [
    (ranges[0][1]-ranges[0][0])/density[0],
    (ranges[1][1]-ranges[1][0])/density[1]
  ]

  column_count = 0
  for column in range(density[0]):
    row_count = 0
    for row in range(density[1]):
      
      point_list.append(Point(
        win,
        [column_count*point_size[0],
         row_count*point_size[1]],
        point_size,
        [column_count*point_change[0]+ranges[0][0],
         row_count*point_change[1]+ranges[1][0]],
        0))
      
      row_count += 1
    column_count += 1
  
  return point_list

#Adds two complex numbers together
#Parameters:
  #a: float[1]
  #b: float[1]
def add(a,b):
  return [a[0]+b[0],a[1]+b[1]]
  
#Squares a complex number
#Parameters:
  #a: float[1]
def square(a):
  return [a[0]**2 - a[1]**2,2*a[0]*a[1]]

#Returns a value after testing a point with a mandelbrot algorithm
def test(point):
  iteration_limit = 30
  iteration = 0
  
  holding_point = [0,0]
  
  while iteration < iteration_limit:
    holding_point = add(square(holding_point),point)
    iteration += 1
    if holding_point[0]**2 + holding_point[1]**2 >= 4:
      break

  return iteration/iteration_limit

main()