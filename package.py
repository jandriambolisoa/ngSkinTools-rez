name = "ngskintools2"

version = "2.1.6"

authors = [
    "Viktoras Makauskas",
    "Jeremy Andriambolisoa",
]

description = \
    """
    ngSkinTools is a skinning plugin for Autodesk Maya, introducing new concepts
    to character skinning such as layers, any-pose-mirroring, enhanced paint
    brushes, true smoothing, and more.
    """


requires = [
    "python-3+",
    "maya-2025+"
]

uuid = "ngskintools.ngskintools2"

build_command = 'python {root}/build.py {install}'

def commands():
    env.MAYA_PLUG_IN_PATH.append("{root}/python/ngskintools2/Contents/plug-ins/2025")
    env.PYTHONPATH.append("{root}/python/ngskintools2/Contents/scripts")
    