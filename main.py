import sys, os
import windows10_setup
import linux_setup

if "win" in sys.platform():
    windows10_setup.main()

if "linux" in sys.platform():
    linux_setup.main(sys.argv[1])