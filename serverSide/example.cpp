#include <map>
class YourClassName
{
private:
    int mNum;
    std::map<char, char> mDictionary;
    char mString;
    int mList;
    bool mBool;
    int* mNull;
public:
    
    int getmNum();
    void setmNum(int value);
    YourClassName();
    YourClassName(int value,  std::map<char,char> value2, char value3, int value4, bool value5, int* value6);
    ~YourClassName();
};

int YourClassName::getmNum(){
    return mNum;
}
void YourClassName::setmNum(int value){
    mNum = value;
}

YourClassName::YourClassName()
{

}

YourClassName::YourClassName(int value,  std::map<char,char> value2, char value3, int value4, bool value5, int* value6)
{
    mNum = value;
    mDictionary = value2;
    mString = value3;
    mList = value4;
    mBool = value5;
    mNull = value6;

}

YourClassName::~YourClassName()
{

}
