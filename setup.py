# setup.py
from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        name="reyplot.scatter_plot",          # <--- updated
        sources=["reyplot/scatter_plot.pyx"], # <--- updated
        language="c",
    )
]

setup(
    name="reyplot",
    version="0.1.0",
    packages=["reyplot"],
    ext_modules=cythonize(
        extensions,
        compiler_directives={
            "language_level": "3",
            "boundscheck": False,
            "wraparound": False,
            "cdivision": True,
        }
    ),
)
