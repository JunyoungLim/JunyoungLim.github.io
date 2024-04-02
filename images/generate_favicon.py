import os
import shutil
import subprocess
import sys


def _validate_dim(dim):
    print(dim)
    dim_splitted = dim.split('x')
    if len(dim_splitted) != 2:
        return False
    d1, d2 = dim_splitted
    print(d1)
    if int(d1) != int(d2):
        return False
    return True


def _get_validated_dim(filename):
    img_name, dim = filename.rsplit('-', 1)
    if not _validate_dim(dim):
        return False
    return dim


def _is_png(filepath):
    return extension == '.png'


def _generate(source, src_dir, dst_dir):
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for filepath in os.listdir(src_dir):
        filename, extension = os.path.splitext(filepath)
        if extension == '.png':
            dim = _get_validated_dim(filename)
            if dim:
                subprocess.run(['convert', source, '-resize', dim, os.path.join(dst_dir, filepath)])
            else:
                subprocess.run(['convert', source, '-resize', '192x192', os.path.join(dst_dir, filepath)])
        elif extension == '.ico':
                subprocess.run(['convert', source, '-resize', '32x32', os.path.join(dst_dir, filepath)])
        else:
            shutil.copy(os.path.join(src_dir, filepath), os.path.join(dst_dir, filepath))


if __name__ == '__main__':
    source = sys.argv[1]
    print(source)
    src_dir = sys.argv[2]
    dst_dir = sys.argv[3]
    _generate(source, src_dir, dst_dir)


