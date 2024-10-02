def cantidad_leds(num):
    map_leds = [6,2,5,5,4,5,6,3,7,6]
    num = str(num)
    leds = 0
    for numero in num:
        leds += map_leds[int(numero)]
    return leds

n = input("Digite el numero para hacer con LEDs: ")
print(f"{n} Se necesita {cantidad_leds(n)} LEDs")

    