colors = ["red", "green", "yellow", "blue", "pink", "purple"]
patterns = ["dotted", "floral", "ditsy", "ikat", "stripes"]

colors.insert(2,"Black") #add
colors.remove("yellow") #remove
colors_index = colors[1:6] #index 1-5
fabric = colors + patterns

print(fabric)
