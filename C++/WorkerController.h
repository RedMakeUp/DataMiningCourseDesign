#ifndef WORKERCONTROLLER_H
#define WORKERCONTROLLER_H

#include <QObject>
#include <QThread>
#include <QLabel>
#include <QDebug>
#include <QDir>

#include <Python.h>

class Worker: public QObject{
    Q_OBJECT

public:
    Worker();

    void setImageName(const QString& imageName){ m_imageName = imageName;}
    void setClassifer(const QString& classifer){ m_classifer = classifer;}
    bool isPredicting(){return m_isPredicting;}

public slots:
    void initScript();
    void predict(){m_isPredicting = true;}
    void end(){m_isRunning = false;}

signals:
    void initDone();
    void resultDone(long);

private:
    bool m_isPredicting = false;
    bool m_isRunning = true;
    QString m_classifer;
    QString m_imageName;
};

class WorkerController : public QObject
{
    Q_OBJECT

public:
    WorkerController();
    ~WorkerController();

    void registerDigitLabel(QLabel* label);
    void endThread();

public slots:
    void handleResultsDone(long value);
    void handleInitDone();
    void predict(const QString& classifer = "cnn", const QString& imageName = QDir::currentPath() + "/../../temp/digits.png");

signals:
    void beginInitScript();
    void endInitScript();
    void beginPredict();
    void endPredict();

private:
    QThread m_workerThread;
    Worker* m_worker = nullptr;
    QLabel* m_digitLabel = nullptr;
};

#endif // WORKERCONTROLLER_H
