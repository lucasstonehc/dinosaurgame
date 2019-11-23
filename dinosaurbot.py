# importing above defined libraries to 
# implement the functionalities  
from PIL import ImageGrab, ImageOps 
import pyautogui 
import time 
import numpy as np   
    
class Cordenates(): 
  
    # coordenatas para encontar o button de restart o game.
    screen_x,screen_y =  pyautogui.size()
    replaybutton = (screen_x/2, screen_y/2) 

    dinosaur = (110, 350) 
      
def restartGame(): 
  
    # Usando pyautogui para criar uma insteração sem nenhum usuário humano.   
    pyautogui.click(Cordenates.replaybutton) 
  
def pressSpace():  

    # pressionando a tecla space
    pyautogui.keyDown('space') 
  
    # aguardando um tempo para liberar 
    time.sleep(0.03)   
  
    # liberando a tecla space  
    pyautogui.keyUp('space') 
  
def imageGrab():  
    # definindo a coordenada do box em frente ao dino 
    box = (Cordenates.dinosaur[0]+30, Cordenates.dinosaur[1], 
           Cordenates.dinosaur[0]+120, Cordenates.dinosaur[1]+30) 
  
    # pegando todos os pixel em forma RGB tupples    
    image = ImageGrab.grab(box) 
  
    # convertendo RGB to Grayscale 
    grayImage = ImageOps.grayscale(image) 
  
    # usando o numpy para somar todos os grayscale pixels  
    a = np.array(grayImage.getcolors()) 
  
    # retornado a soma  
    return a.sum() 

def gameOver():

    x = 487
    y = 291
    x2 = 48   
    y2 = 44    

    box = (x, y, x+x2, y+y2)

    image = ImageGrab.grab(box) 
    grayImage = ImageOps.grayscale(image) 
    a = np.array(grayImage.getcolors())
    
    return a.sum()

restartGame() 
while True:  
    if(gameOver() == 4180):
        restartGame() 
    if(imageGrab() != 2955):    
        pressSpace()
        time.sleep(0.1) 