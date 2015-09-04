import os

cwd = os.path.dirname(__file__)
problem = os.path.splitext(os.path.basename(__file__))[0]

if not os.path.exists(os.path.join(cwd, 'support_files', problem)):
    os.makedirs(os.path.join(cwd, 'support_files', problem))

try:
    os.rename(os.path.join(cwd, 'support_files', problem, 'test.txt'),
              os.path.join(cwd, 'support_files', problem, 'tested.txt'))
except WindowsError as e:
    if e.errno == 2:
        fh = open(os.path.join(cwd, 'support_files', problem, 'tested.txt'), 'w')
        fh.write("I am learnnig programming")
        fh.close()

os.rename(os.path.join(cwd, 'support_files', problem, 'tested.txt'),
          os.path.join(cwd, 'support_files', problem, 'TextFile1.txt'))