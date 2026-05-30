def hex_string_to_RGB(hex_color):
    hex_color = hex_color[1:]
    
    r_hex = hex_color[0:2]
    g_hex = hex_color[2:4]
    b_hex = hex_color[4:6]
    
    r = int(r_hex, 16)
    g = int(g_hex, 16)
    b = int(b_hex, 16)
    
    return {"r": r, "g": g, "b": b}
