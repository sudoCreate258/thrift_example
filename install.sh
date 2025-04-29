# Download Apache Thrift
sudo apt install git libtool cmake flex bison
git clone https://github.com/apache/thrift.git
cd thrift
./bootstrap.sh
./configure
make
sudo make install
