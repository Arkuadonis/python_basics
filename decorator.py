def enhancement(f):
    def newfuntionality():
        print("we are about to execute a funtion")
        f()
        print("funtion execution completed")
    return newfuntionality

@enhancement
def oldfuntionality():
    print("Hello, World")

oldfuntionality()