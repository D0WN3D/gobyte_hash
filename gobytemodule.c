#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include "gobyte.h"

#if PY_MAJOR_VERSION >= 3 || PY_MAJOR_VERSION == 3 && PY_MINOR_VERSION >= 7
#define SIZE_ARG_TYPE Py_ssize_t
#else
#define SIZE_ARG_TYPE int
#endif

static PyObject *gobyte_getpowhash(PyObject *self, PyObject *args)
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
    gobyte_hash((char *)PyBytes_AsString((PyObject*) input), (int)PyBytes_Size((PyObject*) input), output);
#else
    gobyte_hash((char *)PyString_AsString((PyObject*) input), (int)PyString_Size((PyObject*) input), output);
#endif
    Py_DECREF(input);
#if PY_MAJOR_VERSION >= 3
    value = Py_BuildValue("y#", output, (SIZE_ARG_TYPE)32);
#else
    value = Py_BuildValue("s#", output, 32);
#endif
    PyMem_Free(output);
    return value;
}

static PyMethodDef GoByteMethods[] = {
    { "getPoWHash", gobyte_getpowhash, METH_VARARGS, "Returns the proof of work hash using gobyte hash" },
    { NULL, NULL, 0, NULL }
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef GoByteModule = {
    PyModuleDef_HEAD_INIT,
    "gobyte_hash",
    "...",
    -1,
    GoByteMethods
};

PyMODINIT_FUNC PyInit_gobyte_hash(void) {
    return PyModule_Create(&GoByteModule);
}

#else

PyMODINIT_FUNC initgobyte_hash(void) {
    (void) Py_InitModule("gobyte_hash", GoByteMethods);
}
#endif
