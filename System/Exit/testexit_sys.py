
def later():
    import sys
    print("Bye World")
    sys.exit(42)
    print("Never executed")

if __name__ == "__main__":
    later()
