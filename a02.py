### YOUR CODE FOR calculateArea() FUNCTION GOES HERE ###
def calculateArea(length,width):
    area = length * width
    return area
#### End OF MARKER



### YOUR CODE FOR checkTilesFit() FUNCTION GOES HERE ###
def checkTilesFit(plot_width, plot_length, tile_width, tile_length):
    plot_area=int(plot_length)*int(plot_width)
    tile_area=int(tile_length)*int(tile_width)
    if (plot_area%tile_area==0 and plot_length>0 and plot_width>0 and tile_length>0 and tile_width>0) :
        return True
    else:
        return False
#### End OF MARKER



### YOUR CODE FOR calculateTiles() FUNCTION GOES HERE ###
def calculateTiles(plot_width, plot_length, tile_width, tile_length):
    if type(plot_width)==str:
        return ("Invalid Input")
    elif type(plot_length)==str:
        return("Invalid Input")
    elif type(tile_length)==str:
        return ("Invalid Input")
    elif type(tile_width)==str:
        return("Invalid Input")
    elif plot_length==0:
        return None
    elif plot_width==0:
        return None
    elif tile_length==0:
        return None
    elif tile_width==0:
        return None
    plot_area=int(plot_length)*int(plot_width)
    tile_area=int(tile_length)*int(tile_width)
    No_of_tiles=plot_area/tile_area
    
    if checkTilesFit(plot_width, plot_length, tile_width, tile_length)==True:
        return No_of_tiles
    else:
        return "Not Possible"
#### End OF MARKER



