import os
[os.rename(f, f.replace('txt', 'py')) for f in os.listdir('.') if not f.startswith('.')]