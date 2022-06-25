from pathlib import Path

root_dir = Path('files')
file_paths = root_dir.glob("**/*")

for path in file_paths:
  if path.is_file():
    parent_fol = path.parts[-2]
    parent_fol2 = path.parts[-3]
    print(parent_fol2 + "-" + parent_fol)
    new_name = parent_fol2 + "-" + parent_fol + path.name
    path.rename(path.with_name(new_name))