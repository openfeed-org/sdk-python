# build.sh
tmp_dir=$(mktemp -d -t ci-XXXXXXXXXX)

git clone https://github.com/openfeed-org/proto.git $tmp_dir
mv $tmp_dir/*.proto protos

rm -rf $tmp_dir

protoc --proto_path=protos --python_out=openfeed/generated protos/*.proto --pyi_out openfeed/generated
cd openfeed/generated

# https://github.com/protocolbuffers/protobuf/issues/1491#issuecomment-1648982084
# `-i.bak` and `&` behave the same in GNU and BSD (macOS) sed.
sed -i.bak 's/^import.*_pb2/from . &/' *.py
rm -f *.py.bak

cd ../../
python3 setup.py sdist bdist_wheel