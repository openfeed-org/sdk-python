# build.sh
tmp_dir=$(mktemp -d -t ci-XXXXXXXXXX)

git clone https://github.com/openfeed-org/proto.git $tmp_dir
mv $tmp_dir/*.proto protos

rm -rf $temp

protoc --proto_path=protos --python_out=openfeed/generated protos/*.proto --pyi_out openfeed/generated
cd openfeed/generated

# https://github.com/protocolbuffers/protobuf/issues/1491#issuecomment-1648982084
# note: on mac, install gnu-sed (default is not compat)
sed -i -E 's/^import.*_pb2/from . \0/' *.py

cd ../../
python3 setup.py sdist bdist_wheel