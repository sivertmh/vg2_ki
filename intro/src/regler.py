def anbefaling(timer_lekser, fravaer, soevn):
    if fravaer > 12:
        return "Ikke bestått (regler)"
    if timer_lekser > 4 and soevn >= 6:
        return "Bestått (regler)"
    return "Usikkert (regler)"

print(anbefaling(5, 2, 7))
print(anbefaling(1, 15, 5))