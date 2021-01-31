
colour = 0

with open("test.svg", "w") as vector:

     vector.write('''<svg xmlns="http://www.w3.org/2000/svg" width="4096" height="4096" version="1.1">\n''')

     for x in range(4096):
          for y in range(4096):
               colour += 1
               hex_colour = "#" + hex(colour)[2:].zfill(6)
               vector.write(f'''<rect x="{x}" y="{y}" width="1" height="1" stroke="black" stroke-width="1" fill="{hex_colour}"/>\n''')
   
     vector.write('''</svg>\n''')
