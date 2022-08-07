import os.path
import pathlib
import shutil

# testfile に testdata 内の全ファイルをコピー ※testfile のファイル名は 000001.jpgから連番になる

pattern = '*.jpg'
cnt = 0
work_dir_name = '/home/lii/PycharmProjects/testfile'
path = pathlib.Path('/home/lii/PycharmProjects/testdata')
sorted_list = sorted( list(path.iterdir()))
for f in sorted_list:
    if f.match(pattern):
        src = f
        cnt += 1
        dest = '{0}/{1:06d}.jpg'.format(work_dir_name, cnt)

        # ディレクトリがない場合、作成
        if not os.path.exists(work_dir_name):
            os.mkdir(work_dir_name)
        # ファイルコピー
        shutil.copyfile(src, dest)