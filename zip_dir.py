import os
import zipfile


# Not relevant to judges
IGNORE = [
    '.git',
    '.gitignore',
    'LICENSE',
    'Makefile',
    'README.md',
    'hashcode21.zip',
    'zip_dir.py',
]


def zip_directory(zf):
    for root, _, files in os.walk('./'):
        for file in files:
            if file in IGNORE:
                continue

            zf.write(
                os.path.join(root, file),
                os.path.relpath(os.path.join(root, file),
                os.path.join('./', '..'))
            )


if __name__ == '__main__':
    zf = zipfile.ZipFile('hashcode21.zip', 'w', zipfile.ZIP_DEFLATED)
    zip_directory(zf)
    zf.close()
