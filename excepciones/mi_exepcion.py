class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"increible cometiste este error: {err}")

#lanzand mi propia excepcion
#raise MiExcepcion("Jajjajaja, tonto")

#manejandola
try:
    raise MiExcepcion("Jajjajaja, tonto")
except:
    print("Como cometes ese error?")
    