from cx_Freeze import setup, Executable

setup(name = 'POKEMANS', 
      version='3.1.4', 
      description='POKEMANS',
      executables = [Executable(script = 'main.py')])
