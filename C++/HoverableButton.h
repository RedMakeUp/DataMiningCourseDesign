#ifndef HOVERABLEBUTTON_H
#define HOVERABLEBUTTON_H

#include <QPushButton>
#include <QEvent>

class HoverableButton:public QPushButton{
    Q_OBJECT

public:
    HoverableButton(QWidget* parent = nullptr):QPushButton(parent){}

    void disable() {m_isEnable = false; this->setDisabled(true);}
    void enable() {m_isEnable = true; this->setDisabled(false);}

signals:
    void mouseEnter();
    void mouseLeave();

protected:
    void enterEvent(QEvent*) override {if(m_isEnable) emit mouseEnter();}
    void leaveEvent(QEvent*) override {if(m_isEnable) emit mouseLeave();}

private:
    bool m_isEnable = false;
};

#endif // HOVERABLEBUTTON_H
