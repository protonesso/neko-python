import argparse

def main():
	parser = argparse.ArgumentParser(description="Next generation package manager")

	parser.add_argument("install", metavar="install", type=str, nargs='+')

	parser.add_argument("-c", "--config", type=str, dest="config")
	parser.add_argument("-r", "--rootdir", type=str, dest="rootdir")
	parser.add_argument("-f", "--force", action="store_true", dest="force")

	args = parser.parse_args()

	print(args.config)

	if args.force:
		print("Force mode enabled!");

	args.install.pop(0)
	for i in args.install:
		print(i)

main()
