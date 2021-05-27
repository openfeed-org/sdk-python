# build.sh
tmp_dir=$(mktemp -d -t ci-XXXXXXXXXX)

git clone https://github.com/openfeed-org/proto.git $tmp_dir
mv $tmp_dir/*.proto protos -f

rm -rf $temp

protoc --proto_path=protos --python_out=openfeed/generated protos/*.proto
cd openfeed/generated
sed -i -E 's/^import.*_pb2/from . \0/' *.py

cd ../../
python3 setup.py sdist bdist_wheel