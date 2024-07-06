#Written by Hashim

#Here everything is imported
import pygame

#Here pygame is initialized
pygame.init()

#This class defines a point on the grid
class Point:
  #This method intializes object variables
  #Parameters:
    #screen: Surface
    #position: float[1]
    #size: float[1]
    #value: int (from 0 to 1)
  def __init__(self,screen,position,size,input_value,output_value):
    self.screen = screen
    self.position = position
    self.size = size
    
    self.input_value = input_value
    self.output_value = output_value

  def plot(self):
    colour = [
      255-round(255*self.output_value),
      255-round(255*self.output_value),
      255-round(255*self.output_value)
    ]
    
    pygame.draw.rect(self.screen,(colour),self.position + self.size)