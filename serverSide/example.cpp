class YourClassName
{
private:
    int mNum;
public:
    int getmNum();
    void setmNum(int value);
    YourClassName();
    YourClassName(int value);
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

YourClassName::YourClassName(int value)
{

}

YourClassName::~YourClassName()
{

}
