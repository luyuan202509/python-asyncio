from pathlib import Path
path = Path(__file__).with_name("programming.txt")

contents = "I love createing new games.\n"
contents += "I also love finding meaning in large datasets."
path.write_text(contents)
print(path.read_text())

