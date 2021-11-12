available_colors = ['red', 'yellow', 'green', 'white', 'black']

requested_colors = ['red', 'yellow' ]

for requested_color in requested_colors:
    if requested_color in available_colors:
        colors_exist = 'Requested colors are exist!'
    else:
        colors_no_exist = 'Requested colors are no exist!'

if colors_no_exist:
    print(colors_no_exist)
else:
    print(colors_exist)


