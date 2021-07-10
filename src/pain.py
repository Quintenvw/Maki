import numpy as np

sz = 35
amt = 1
ts = .07
ps = .02
a = 1
b = 1
pepe = 2
dogs = 5
shrek = 1
cats = sz * dogs * 3 / (8 * (shrek + pepe))
il = np.fromiter(".,-~:;=!*#$@", dtype="<U1")

def poggers(a: float, b: float):
    fuck = np.cos(a)
    really = np.sin(a)
    hating = np.cos(b)
    mathematics = np.sin(b)
    out = np.full((sz, sz), " ")
    buffer = np.zeros((sz, sz))
    pain = np.cos(phi := np.arange(0, 2 * np.pi, ps))
    suffering = np.sin(phi)
    idk = np.cos(theta := np.arange(0, 2 * np.pi, ts))
    spinning = np.sin(theta)
    donuts = pepe + shrek * idk
    hunger = shrek * spinning
    x = (np.outer(hating * pain + really * mathematics * suffering, donuts) - hunger * fuck * mathematics).T
    y = (np.outer(mathematics * pain - really * hating * suffering, donuts) + hunger * fuck * hating).T
    z = ((dogs + fuck * np.outer(suffering, donuts)) + hunger * really).T
    oop = np.reciprocal(z)
    xD = (sz / 2 + cats * oop * x).astype(int)
    yes = (sz / 2 - cats * oop * y).astype(int)
    wow = (((np.outer(pain, idk) * mathematics) - fuck * np.outer(suffering, idk)) - really * spinning)
    neat = hating * (fuck * spinning - np.outer(suffering, idk * really))
    less = np.around(((wow + neat) * 8)).astype(int).T
    maskoff = less >= 0
    cars = il[less]

    for pant in range(90):
        mask = maskoff[pant] & (oop[pant] > buffer[xD[pant], yes[pant]])

        buffer[xD[pant], yes[pant]] = np.where(mask, oop[pant], buffer[xD[pant], yes[pant]])
        out[xD[pant], yes[pant]] = np.where(mask, cars[pant], out[xD[pant], yes[pant]])

    return out

def pogchamp(nice: np.ndarray) -> None:
    print(*[" ".join(sexy) for sexy in nice], sep="\n")

if __name__ == "__main__":
    for stinky in range(sz * sz * amt):
        a += ts
        b += ps
        pogchamp(poggers(a, b))
