def max_volume_container_with_most_volume(bargraph):
    lp = 0
    hp = len(bargraph) - 1

    maxVolumeSoFar = min(bargraph[hp], bargraph[lp]) * (hp - lp)
    maxhp = hp
    maxlp = 0
    while (lp < hp):
        curVol = min(bargraph[hp], bargraph[lp]) * (hp - lp)
        if (curVol > maxVolumeSoFar):
            maxVolumeSoFar = curVol
            maxhp = hp
            maxlp = lp
        if (bargraph[hp] < bargraph[lp]):
            hp -= 1
        else:
            lp += 1
    print("hp=%d, lp=%d" % (maxhp, maxlp))
    return maxVolumeSoFar
        


print(max_volume_container_with_most_volume([1, 8, 6, 2, 5, 4, 8, 3, 7]))
