
def convert(faces):
    return faces.replace(":)", "🙂").replace(":(", "🙁")
   

def main():
    user=input(" ").strip()
    newtxt=convert(user)
    print(newtxt)
if __name__=="__main__":
    main()

