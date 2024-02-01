#include "connectform.h"
#include "ui_connectform.h"

ConnectForm::ConnectForm(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::ConnectForm)
{
    ui->setupUi(this);
    this->setWindowFlags(Qt::SubWindow);
}

ConnectForm::~ConnectForm()
{
    delete ui;
}

QPushButton* ConnectForm::connectButton()
{
    return ui->connectButton;
}

QLineEdit* ConnectForm::hostName()
{
    return ui->lineEditHostname;
}

QSpinBox* ConnectForm::port()
{
    return ui->spinBoxPort;
}

void ConnectForm::on_pushButton_clicked()
{
    this->hide();
}
