for i in range(0,10):
    with open(f"table/{i}.txt","w") as f:
        for g in range(0,11):
            f.write(f"{i} X {g} = {i*g}")
            f.write("\n")