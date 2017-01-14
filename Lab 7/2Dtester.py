# Create a 2d List
# Let's do this by rows / cols much like a database stores info

COL = 2
temp_ROW = 12 
all_other_ROW = 11


def main():
    # Create the 2d list (table to store info)
    values = [["Fahrenheit", "Celcius"],
                  [-10,-23.33],
                  [" 0",-17.78],
                  [10,-12.22],
                  [20,-6.67],
                  [30,-1.11],
                  [40, 4.44],
                  [50, 10],
                  [60, 15.56],
                  [70, 21.11],
                  [80, 26.67],
                  [90, 32.22],
                  [100,37.78]]
    index = 0
    while index < len(values):
        for c in range(COL):
            for r in range(temp_ROW):
                print(values[r][c], values[r][c+1], sep='       ')
                index +=1
    
             

#Call that sweet main
main() 
