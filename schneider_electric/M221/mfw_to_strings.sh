now=$(date +"%Y%m%d")
strings "$1" | grep  ^$2 > M221_MFW_Strings-$now.txt
python3 ./se_mfw_firmware_extractor.py M221_MFW_Strings-$now.txt
