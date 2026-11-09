ultrasonidos = 40
infrarrojos = 12
luz = 7
barra_ultrasonidos = "#" * (ultrasonidos // 5)
barra_infrarrojos = "#" * (infrarrojos // 5)
barra_luz = "#" * (luz // 5)
print(f"Ultrasonidos: {ultrasonidos:.1f} {barra_ultrasonidos}")
print(f"Infrarrojos: {infrarrojos:.1f} {barra_infrarrojos}")
print(f"Luz: {luz:.1f} {barra_luz}")