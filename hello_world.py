#!/usr/bin/env python3
import sys
if len(sys.argv) == 1: 
	print("Error! Usage: ./hello_world.py <your name>")
else:
	print("Hello, "+sys.argv[1])
