import time

current = time.time()
old_date = time.strftime("%b %d %Y", time.gmtime(0))

formated_curr = f"{current:,.3f}"
scientific_curr = f"{current:,.3e}"
date = time.strftime("%b %d %Y", time.gmtime())


print("Seconds since", old_date, ":", formated_curr, "or",
      scientific_curr, "in scientific notation")
print(date)
