#ifndef CONNECTFORM_H
#define CONNECTFORM_H

#include <QWidget>
#include <QPushButton>
#include <QLineEdit>
#include <QSpinBox>

namespace Ui {
class ConnectForm;
}

class ConnectForm : public QWidget
{
    Q_OBJECT

public:
    explicit ConnectForm(QWidget *parent = nullptr);
    ~ConnectForm();
    QPushButton* connectButton();
    QLineEdit* hostName();
    QSpinBox* port();

private slots:
    void on_pushButton_clicked();

private:
    Ui::ConnectForm *ui;
};

#endif // CONNECTFORM_H
