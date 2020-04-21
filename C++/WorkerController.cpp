#include "WorkerController.h"

#include <QDebug>

#include <Python.h>
#include <wchar.h>
#include <string>

#include "PyHelper.h"

Worker::Worker(){
//    initScript();
}

void Worker::initScript(){
    CPyInstance hInstance;

    // Add the path of "control.py" for Python searching
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("import os");
    PyRun_SimpleString("sys.path.append(os.getcwd()+'/../../../Python/')");

    // Import control.py
    CPyObject pName = PyUnicode_FromString("control");
    CPyObject module = PyImport_Import(pName);

    if(module){
        qDebug() << "Load control.py";

        // Init imports and models
        CPyObject pFunc_init = PyObject_GetAttrString(module, "init");
        if(pFunc_init){
            qDebug() << "Load init function";

            PyObject_CallObject(pFunc_init, NULL);

            qDebug() << "init done";
            emit initDone();
        }else{
            qDebug() << "ERROR: Function init()";
        }

        CPyObject pFunc_predict = PyObject_GetAttrString(module, "predict");
        if(!pFunc_predict || !PyCallable_Check(pFunc_predict)){
            qDebug() << "ERROR: Function predict()";
            return;
        }

        while(m_isRunning){
            if(m_isPredicting){
                CPyObject pValue = PyObject_CallFunction(pFunc_predict, "ss", m_imageName.toUtf8().data(), m_classifer.toUtf8().data());
                qDebug() << "Digit: " << PyLong_AsLong(pValue);
                this->thread()->sleep(1);
                emit resultDone(PyLong_AsLong(pValue));
                m_isPredicting = false;
            }
        }

        qDebug() << "Work end";
    }else{
        PyErr_Print();
        qDebug() << "ERROR: Module not imported";
    }
}



WorkerController::WorkerController() {
    m_worker = new Worker;
    m_worker->moveToThread(&m_workerThread);
    connect(&m_workerThread, &QThread::finished, m_worker, &QObject::deleteLater);
    connect(this, &WorkerController::beginInitScript, m_worker, &Worker::initScript);
    connect(m_worker, &Worker::initDone, this, &WorkerController::handleInitDone);
    connect(m_worker, &Worker::resultDone, this, &WorkerController::handleResultsDone);
    m_workerThread.start();

    emit beginInitScript();
}


WorkerController::~WorkerController() {
    m_worker->end();
}

void WorkerController::endThread(){
    m_worker->end();

    m_workerThread.quit();
    m_workerThread.wait();
}


void WorkerController::registerDigitLabel(QLabel* label)
{
    m_digitLabel = label;
}

void WorkerController::handleResultsDone(long value)
{
    if(m_digitLabel){
        emit endPredict();
        m_digitLabel->setText(QString::number(value));
    }
}

void WorkerController::handleInitDone()
{
    emit endInitScript();
}

void WorkerController::predict(const QString& classifer, const QString& imageName)
{
    if(!m_worker->isPredicting()){
        m_worker->setClassifer(classifer);
        m_worker->setImageName(imageName);
        m_worker->predict();
        emit beginPredict();
    }
}
