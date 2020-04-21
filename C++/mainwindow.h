#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QCloseEvent>

#include "WorkerController.h"

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget* parent = nullptr);
    ~MainWindow();

protected:
    void closeEvent(QCloseEvent* event) override;

private slots:
    void onSaveButtonClicked();
    void onResetButtonClicked();
    void onSimpleAnnButtonClicked();
    void onSvmButtonClicked();
    void onCnnButtonClicked();
    void onDecisionTreeButtonClicked();
    void onClosed();

private:
    Ui::MainWindow* ui;
    WorkerController m_workController;
};
#endif // MAINWINDOW_H
