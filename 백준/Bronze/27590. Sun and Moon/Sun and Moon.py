ds, ys = map(int, input().split())
dm, ym = map(int, input().split())

sun_year = ys - ds
moon_year = ym - dm

while sun_year != moon_year:
    sun_year += ys if sun_year < moon_year else 0
    moon_year += ym if moon_year < sun_year else 0

print(sun_year)
