def main():
    a=dollars_to_float(input("How much was the meal? "))
    b=percentages_to_float(input("What percentage would you like to tip"))
    c=(b/100)*a
    print(f"Leave ${c:.2f}")

def dollars_to_float(d):
    return float(d.strip("$"))
def percentages_to_float(p):
    return float(p.strip("%"))

if __name__ == "__main__":
    main()