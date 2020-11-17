set PATH=C:\Apps\cwrsync_6.2.0_x64_free\bin;%PATH%

rsync -avR -e "ssh  -i C:\Users\a\.ssh\id_rsa -o StrictHostKeyChecking=no" ./ ccf@192.168.0.10:/mnt/mfs/data/Wind/./
@pause
REM > output.log 2>&1

ssh -i C:\Users\a\.ssh\id_rsa -o StrictHostKeyChecking=no jaysus@192.168.0.9 "/mnt/mfs/data/Wind/update/import.sh"
@pause
