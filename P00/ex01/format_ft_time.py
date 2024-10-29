import time

current = time.time()

formated_curr = f"{current:,.3f}"
scientific_curr = f"{current:,.3e}"
date = time.strftime("%b %d %Y", time.gmtime())


print("Seconds since January 1, 1970:", formated_curr, "or",
      scientific_curr, "in scientific notation")
print(date)
