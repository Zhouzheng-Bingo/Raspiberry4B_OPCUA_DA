#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_clicked()
{
    this->connectForm = new ConnectForm();
    this->connectForm->show();
    connect(this->connectForm->connectButton(),&QPushButton::clicked,this,&MainWindow::createNewDiagForm);
}

void MainWindow::createNewDiagForm()
{
        qDebug()<<"createNewDiagForm";
    QString key = this->connectForm->hostName()->text();

    client = new QMqttClient();

    client->setHostname(connectForm->hostName()->text());
    client->setPort(connectForm->port()->value());
    client->connectToHost();

    this->connectForm->hide();

    connect(client, SIGNAL(disconnected()), this,SLOT(doDisconnected()));
    connect(client, SIGNAL(connected()), this,SLOT(doConnected()));
    connect(client, SIGNAL(messageReceived(const QByteArray& , const QMqttTopicName &)), this,SLOT(doDataReceived(const QByteArray& , const QMqttTopicName&)));
}
void MainWindow::doConnected()
{
    qDebug()<<"connect ok";
    ui->label->setText("connect ok");

    client->subscribe(QString("mallDis2PC_C0_P1002"), 0);//订阅轴数
    client->subscribe(QString("proDis2PC_C0_P2002"), 0);//订阅模式
    client->subscribe(QString("proDis2PC_C0_P2004"), 0);//订阅轴编程值

    DisMsgInt data;
    data.data = 1;
    QByteArray byteArray;
    byteArray.append((char*)&data, sizeof(data));
    client->publish(QString("mallPC2Dis_C0_cmd"),byteArray);//请求发送非周期数据

    DisMsgInt data2;
    data2.data = 2;
    QByteArray byteArray2;
    byteArray2.append((char*)&data2, sizeof(data2));
    client->publish(QString("mallPC2Dis_C0_cmd"),byteArray2);//请求发送周期数据

}
void MainWindow::doDisconnected()
{
    ui->label->setText("connect error");
}
void MainWindow::doDataReceived(const QByteArray& message, const QMqttTopicName& topicName)
{
    if(topicName.name() == QString("mallDis2PC_C0_P1002")){
        //轴数
        DisMsgInt *tmpGet = (DisMsgInt*)message.data();
        qDebug()<<"axis num="<<tmpGet->data;
        ui->numLabel->setText(QString("%1").arg(tmpGet->data));
    }
    if(topicName.name() == QString("proDis2PC_C0_P2002")){
        //模式
        DisMsgInt *tmpGet = (DisMsgInt*)message.data();
        qDebug()<<"cnc mode ="<<tmpGet->data;
        ui->modeLabel->setText(QString("%1").arg(tmpGet->data));
    }
    if(topicName.name() == QString("proDis2PC_C0_P2004")){
        //模式
        DisMsgAxisDouble *tmpGet = (DisMsgAxisDouble*)message.data();
        qDebug()<<"cnc x var ="<<tmpGet->data[0];
        ui->xvarLabel->setText(QString("%1").arg(tmpGet->data[0]));
    }
}
