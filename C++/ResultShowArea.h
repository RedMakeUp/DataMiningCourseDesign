#ifndef RESULTSHOWAREA_H
#define RESULTSHOWAREA_H

#include <QWidget>
#include <QImage>
#include <QPaintEvent>
#include <QPainter>

class ResultShowArea: public QWidget{
    Q_OBJECT

public:
    ResultShowArea(QWidget* parent = nullptr):QWidget(parent){}

    void setImage(std::shared_ptr<QImage> image) {m_image = image; update();}

protected:
    void paintEvent(QPaintEvent* event) override{
        if(!m_image) return;

        auto scaledImage = m_image->scaled(28, 28, Qt::KeepAspectRatio,Qt::SmoothTransformation);

        QPainter painter(this);
//        painter.setRenderHint(QPainter::Antialiasing);
        QRect dirtyRect = event->rect();
        painter.drawImage(dirtyRect, scaledImage, dirtyRect);
    }

private:
    std::shared_ptr<QImage> m_image = nullptr;
};

#endif // RESULTSHOWAREA_H
