def main():
    expressions=input("Expression: ").lower().strip()
    def interpreter():
        try:
            parts=expressions.split()
            x=int(parts[0])
            y=(parts[1])
            z=int(parts[2])
        except(IndexError, ValueError):
            print("Invalid format...*interpreter dies*:(")
            return
        if y not in ["+", "-", "/", "*"]:
            print("Invalid operator...*interpreter dies*:(")
            return
        if y=="+":
            print(f"{x+z:.1f}")
        elif y=="-":
            print(f"{x-z:.1f}")
        elif y=="*":
            print(f"{x*z:.1f}")
        else:
            if z==0:
                print("Can't divide by 0...sorry...*interpreter dies*:(")
                return
            else:
                 print(f"{x/z:.1f}")
    interpreter()
if __name__=="__main__":
    main()