#ifndef DRAWAREA_H
#define DRAWAREA_H

#include <QWidget>
#include <QPaintEvent>
#include <QMouseEvent>
#include <QPaintEvent>
#include <QPoint>
#include <QImage>
#include <QColor>

#include <memory>

//! [0]
class DrawArea : public QWidget
{
    Q_OBJECT

public:
    DrawArea(QWidget* parent = nullptr);

    void initImage();
    void resetImage();
    void saveImage();
    std::shared_ptr<QImage> getImage() const {return m_image;}


protected:
    void paintEvent(QPaintEvent* event) override;
    void mousePressEvent(QMouseEvent *event) override;
    void mouseMoveEvent(QMouseEvent *event) override;
    void mouseReleaseEvent(QMouseEvent *event) override;

private:
    void drawLineTo(const QPoint& endPoint);

private:
    bool m_isDrawing = false;
    std::shared_ptr<QImage> m_image;
    QPoint m_lastPos;
    QColor m_penColor = Qt::white;
    int m_penWidth = 20;
};

#endif // DRAWAREA_H
