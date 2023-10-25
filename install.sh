# Download Apache Thrift
sudo apt install git
sudo apt install libtool
sudo apt install cmake
git clone https://github.com/apache/thrift.git
cd thrift
./bootstrap.sh
./configure
make
sudo make install
