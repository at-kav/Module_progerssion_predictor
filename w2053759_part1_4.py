# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: 20222066
# Date: 01/12/2023

from graphics import *

def histogram(progress_count: int,trailer_count: int,retriver_count: int,exclude_count: int):
    "To create histogram"

    #variables needed for columns
    top_left_x_coordinate=100
    bottom_right_x_coordinate=225
    mid_value_of_column=165
    gap=0
    mlutiplied_pixel_value=10

    columns=[((progress_count*mlutiplied_pixel_value),'palegreen1'),((trailer_count*mlutiplied_pixel_value),'palegreen3'),((retriver_count*mlutiplied_pixel_value),'darkkhaki'),((exclude_count*mlutiplied_pixel_value),'pink3')]
    column_names=('Progress','Trailer','Retriever','Excluded')
    column_value=[(485-(progress_count*mlutiplied_pixel_value),progress_count),(485-(trailer_count*mlutiplied_pixel_value),trailer_count),(485-(retriver_count*mlutiplied_pixel_value),retriver_count),(485-(exclude_count*mlutiplied_pixel_value),exclude_count)]

    def create_colums(columns,top_left_x_coordinate,bottom_right_x_coordinate,gap):        
        for (progression,colour) in columns:
            Arectangle = Rectangle(Point(top_left_x_coordinate + gap,(500-progression)), Point(bottom_right_x_coordinate + gap,500))
            Arectangle.setFill(colour)
            Arectangle.draw(win)
            gap= gap + 150

    def displaying_column_names(column_names,mid_value_of_column,gap):
        for coulmn_name in column_names:   
            text = Text(Point(mid_value_of_column + gap,520),coulmn_name)
            text.setTextColor('grey')
            text.setSize(14)
            text.setStyle('bold')
            text.setFace('helvetica')
            text.draw(win)
            gap= gap + 150
    
    def displaying_values_of_columns(column_value,mid_value_of_column,gap):
        for (coordinate_y,coulmn_values) in column_value:   
            text = Text(Point(mid_value_of_column + gap,coordinate_y),coulmn_values)
            text.setTextColor('grey')
            text.setSize(12)
            text.setStyle('bold')
            text.setFace('helvetica')
            text.draw(win)
            gap=gap+150

    #Create window
    win = GraphWin('Histogram', 800, 600)
    win.setBackground('white')

    #write Heading
    my_heading = Text(Point(200, 30), 'Histogram Results')
    my_heading.setTextColor('black')
    my_heading.setSize(20)
    my_heading.setStyle('bold')
    my_heading.setFace('helvetica')
    my_heading.draw(win)

    #Draw line
    aLine = Line(Point(50,500), Point(725,500))
    aLine.draw(win)

    #create column
    create_colums(columns,top_left_x_coordinate,bottom_right_x_coordinate,gap)

    #display column names
    displaying_column_names(column_names,mid_value_of_column,gap)

    #displaying column value
    displaying_values_of_columns(column_value,mid_value_of_column,gap)

    #calculate total inputs    
    total = progress_count + trailer_count + retriver_count + exclude_count

    #display total inputs
    text_1 = Text(Point(165,550),f'{total} outcomes in total.')
    text_1.setTextColor('grey')
    text_1.setSize(16)
    text_1.setStyle('bold')
    text_1.setFace('helvetica')
    text_1.draw(win)

    try:
        win.getMouse() # pause for click in window
        win.close()
    except:
        pass
