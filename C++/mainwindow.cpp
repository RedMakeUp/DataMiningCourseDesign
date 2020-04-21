#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QDebug>

#include "HoverableButton.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    const QString promptHolder = "Please choose a classifer";

    ui->pushButton_simpleANN->setToolTip("Simple ANN");
    ui->pushButton_simpleANN->disable();
    connect(ui->pushButton_simpleANN, &HoverableButton::mouseEnter, this, [this](){
        ui->label_prompt->setText("Simple Neural Network");
    });
    connect(ui->pushButton_simpleANN, &HoverableButton::mouseLeave, this, [this, promptHolder](){
        ui->label_prompt->setText(promptHolder);
    });

    ui->pushButton_cnn->setToolTip("CNN");
    ui->pushButton_cnn->disable();
    connect(ui->pushButton_cnn, &HoverableButton::mouseEnter, this, [this](){
        ui->label_prompt->setText("Convolutional Neural Network(VGG)");
    });
    connect(ui->pushButton_cnn, &HoverableButton::mouseLeave, this, [this, promptHolder](){
        ui->label_prompt->setText(promptHolder);
    });

    ui->pushButton_svm->setToolTip("SVM");
    ui->pushButton_svm->disable();
    connect(ui->pushButton_svm, &HoverableButton::mouseEnter, this, [this](){
        ui->label_prompt->setText("Support Vector Machine");
    });
    connect(ui->pushButton_svm, &HoverableButton::mouseLeave, this, [this, promptHolder](){
        ui->label_prompt->setText(promptHolder);
    });

    ui->pushButton_decisionTree->setToolTip("Decision Tree");
    ui->pushButton_decisionTree->disable();
    connect(ui->pushButton_decisionTree, &HoverableButton::mouseEnter, this, [this](){
        ui->label_prompt->setText("Decision Tree(CART)");
    });
    connect(ui->pushButton_decisionTree, &HoverableButton::mouseLeave, this, [this, promptHolder](){
        ui->label_prompt->setText(promptHolder);
    });


    ui->progressBar->setRange(0, 0);
    ui->progressBar->hide();

    m_workController.registerDigitLabel(ui->digit_label);
    connect(&m_workController, &WorkerController::beginPredict,this,[this](){
        ui->progressBar->show();
    });
    connect(&m_workController, &WorkerController::endPredict,this,[this](){
        ui->progressBar->hide();
    });
    connect(&m_workController, &WorkerController::endInitScript,this,[this](){
        ui->pushButton_simpleANN->enable();
        ui->pushButton_svm->enable();
        ui->pushButton_decisionTree->enable();
        ui->pushButton_cnn->enable();
    });

    ui->draw_area->initImage();
    ui->show_area->setImage(ui->draw_area->getImage());
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::closeEvent(QCloseEvent *event)
{
    m_workController.endThread();

    event->accept();
}


void MainWindow::onSaveButtonClicked()
{
    ui->show_area->update();
    ui->draw_area->saveImage();

    qDebug() << "Save";
}

void MainWindow::onResetButtonClicked()
{
    ui->draw_area->resetImage();
    ui->draw_area->update();
    ui->show_area->update();
}

void MainWindow::onSimpleAnnButtonClicked()
{
    m_workController.predict("simple_ann");
}

void MainWindow::onSvmButtonClicked()
{
    m_workController.predict("svm");
}

void MainWindow::onCnnButtonClicked()
{
    m_workController.predict("cnn");
}

void MainWindow::onDecisionTreeButtonClicked()
{
    m_workController.predict("decision_tree");
}

void MainWindow::onClosed()
{

}
