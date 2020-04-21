#include "DrawArea.h"

#include <QPainter>
#include <QPen>
#include <QDebug>
#include <QRandomGenerator>
#include <QDir>

#include <iostream>

int roundUp(double value){
    return static_cast<int>(value + 0.5);
}

DrawArea::DrawArea(QWidget* parent)
    :QWidget(parent)
{
    // Use style sheet for color, border and etc
    this->setAttribute(Qt::WA_StyledBackground, true);
}

void DrawArea::initImage()
{
    m_image = std::make_shared<QImage>(width(), height(), QImage::Format_RGB32);
    m_image->fill(QColor(0, 0, 0));
    update();
}

void DrawArea::resetImage()
{
    m_image->fill(QColor(0, 0, 0));
    update();
}

void DrawArea::saveImage()
{
    m_image->scaled(28, 28, Qt::KeepAspectRatio,Qt::SmoothTransformation)
            .convertToFormat(QImage::Format_Grayscale8)
            .save(QDir::currentPath() + "/../../temp/digits.png", "png", 100);
}

void DrawArea::paintEvent(QPaintEvent* event)
{
    QPainter painter(this);
//    painter.setRenderHint(QPainter::Antialiasing);
    QRect dirtyRect = event->rect();
    painter.drawImage(dirtyRect, *m_image, dirtyRect);
}

void DrawArea::mousePressEvent(QMouseEvent* event)
{
    if (event->button() == Qt::LeftButton) {
        m_isDrawing = true;
        m_lastPos = event->pos();
    }
}

void DrawArea::mouseMoveEvent(QMouseEvent* event)
{
    if((event->buttons() & Qt::LeftButton) && m_isDrawing){
        drawLineTo(event->pos());
    }
}

void DrawArea::mouseReleaseEvent(QMouseEvent* event)
{
    if (event->button() == Qt::LeftButton && m_isDrawing) {
        drawLineTo(event->pos());
        m_isDrawing = false;
    }
}

void DrawArea::drawLineTo(const QPoint& endPoint)
{
    QPainter painter(m_image.get());
//    painter.setRenderHint(QPainter::Antialiasing);
    painter.setPen(QPen(m_penColor, m_penWidth, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));

    double randomValue1 = QRandomGenerator::global()->generateDouble();
    int dx = roundUp(randomValue1 * 4 - 2.0);
    double randomValue2 = QRandomGenerator::global()->generateDouble();
    int dy = roundUp(randomValue2 * 4 - 2.0);
    QPoint randomPoint(endPoint.x() + dx, endPoint.y() + dy);
    painter.drawLine(m_lastPos, randomPoint);

    int rad = (m_penWidth / 2) + 2;
    update(QRect(m_lastPos, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad));

    m_lastPos = endPoint;
}

