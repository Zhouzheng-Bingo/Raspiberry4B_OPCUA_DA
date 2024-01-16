#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "connectform.h"
#include <QtMqtt/qmqttclient.h>
QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

struct DisMsgInt
{
    int data;
};
struct DisMsgDouble
{
    double data;
};
struct DisMsgQString
{
    //QString data;
    char data[256];
};
struct DisMsgAxisInt
{
    int data[32];
};
struct DisMsgAxisDouble
{
    double data[32];
};
struct DisMsgAxisQString
{
    char data[32][8];
};
struct DisMsgSpindlInt
{
    int data[4];
};
struct DisMsgSpindlDouble
{
    double data[4];
};
struct DisMsgSpindlQString
{
    //QString data[4];
    char data[4][8];
};

struct circleProgramSettingData
{
    int channel;//cnc通道
    int panel; //0:xy  1: yz  2:zx
    int g2;  //0:g02  1:g03
    int orgin; //0:g54 1:g55 ---- 5:g59
    double radius;// 半径
    double feed; //速度
};

struct TappingProgramSettingData
{
    int channel;//cnc通道
    int panel; //0:xy  1: yz  2:zx
    int orgin; //0:g54 1:g55 ---- 5:g59
    int feedAxisIndex;  //0:x  1:y  2:z（几何轴）
    int spindleCW;// 1~999 正转M码
    int spindleStop; //1~999 停止M码
    int sVar;//0-99999  主轴转速s
    int G84Feed;//0-99999  攻丝速度
    double RPos;// R点位置
    double zBottom;//攻丝底部位置
};

struct circleProgramRunData
{
    int channel;      //CNC通道
    char fileName[128];    //程序名
    char fileStr[512];     //程序内容
};
struct TappingProgramRunData
{
    int channel;      //CNC通道
    char fileName[128];    //程序名
    char fileStr[512];     //程序内容
};

struct MotCycleDate
{
    int num;
    unsigned short index[10];
    unsigned int value[10];
};
struct DisMsgPLCXInt
{
    unsigned char data[5];//监控X10.0~X14.7 40个点状态
};
struct DisMsgPLCYInt
{
    unsigned char data[5]; //监控Y8.0~Y12.7 40个点状态
};
struct DisMsgPLCRInt
{
    unsigned char data[5];//监控R450.0~R454.7 40个点状态
};
struct cmdSetPLCBit
{
    int type; //0:Y ; 1:F; 2:R
    int address;//Y:外部IO从Y8.0开始，F信号可用不分通道F230.0~F240.7，R变量可用R0.0~R499.7
    int bit;//0~7
    int On;//On=1:强制信号为1。  On=0:强制型号为0
};
struct cncAlarmQString
{
    char fileName[5][128];    //最多显示5条报警信息
};
struct ProgramRunFileData
{
    char fileName[128];    //程序名 程序名需要全路径，实例："./programs/123.prg"
};


class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    ConnectForm *connectForm;
private slots:
    void on_pushButton_clicked();
    void createNewDiagForm();

    void doConnected();
    void doDisconnected();
    void doDataReceived(const QByteArray& , const QMqttTopicName&);
private:
    Ui::MainWindow *ui;
    QMqttClient *client;
};
#endif // MAINWINDOW_H
