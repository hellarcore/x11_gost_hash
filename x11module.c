#include <Python.h>

#include "x11hash.h"

static PyObject *x11_gost_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
#if PY_MAJOR_VERSION >= 3
    PyBytesObject *input;
#else
    PyStringObject *input;
#endif
    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);

#if PY_MAJOR_VERSION >= 3
    x11_gost_hash((char *)PyBytes_AsString((PyObject*) input), output);
#else
    x11_gost_hash((char *)PyString_AsString((PyObject*) input), output);
#endif
    Py_DECREF(input);
#if PY_MAJOR_VERSION >= 3
    value = Py_BuildValue("y#", output, 32);
#else
    value = Py_BuildValue("s#", output, 32);
#endif
    PyMem_Free(output);
    return value;
}

static PyMethodDef X11GostMethods[] = {
    { "getPoWHash", x11_gost_getpowhash, METH_VARARGS, "Returns the proof of work hash using x11gost hash" },
    { NULL, NULL, 0, NULL }
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef X11GostModule = {
    PyModuleDef_HEAD_INIT,
    "x11_gost_hash",
    "...",
    -1,
    X11GostMethods
};

PyMODINIT_FUNC PyInit_x11_gost_hash(void) {
    return PyModule_Create(&X11GostModule);
}

#else

PyMODINIT_FUNC initx11_gost_hash(void) {
    (void) Py_InitModule("x11_gost_hash", X11GostMethods);
}
#endif
