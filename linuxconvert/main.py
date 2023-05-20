import sys, os

def main():
    sys.path.append("linuxconvert")
    if "win" in sys.platform:
        import windows10_setup
        windows10_setup.main()

    if "linux" in sys.platform:
        import linux_setup
        linux_setup.main(sys.argv[1])

if __name__ == "__main__":
    main()