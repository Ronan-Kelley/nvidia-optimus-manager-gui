#!/bin/bash
sudo -v

# make sure that proprietary nvidia drivers are installed
if [ -z $(find /lib/modules/$(uname -r) -type f -name 'nvidia-drm*') ];then
    echo "you need to have nvidia proprietary drivers installed for this to work!"
    doflicky-ui &
    exit 1
fi

cd nvidia-optimus-manager

# blacklist nouveau driver
sudo mkdir -p /etc/modprobe.d
echo "blacklist nouveau" | sudo tee /etc/modprobe.d/blacklist-nouveau.conf

# install dependencies
sudo eopkg it pciutils linux-driver-management python3-tkinter

# install backend
sudo mkdir -p /etc/lightdm/lightdm.conf.d/
sudo cp 99-nvidia.conf /etc/lightdm/lightdm.conf.d
sudo cp nvidia-optimus-autoconfig.service /etc/systemd/system/nvidia-optimus-autoconfig.service
sudo cp nvidia-optimus-manager /usr/bin/nvidia-optimus-manager

# enable backend in systemd
sudo systemctl daemon-reload
sudo systemctl enable nvidia-optimus-autoconfig

# install gui
sudo chmod 777 ../gui/Main.py
sudo cp ../gui/Main.py /bin/optimusGui

echo "please restart for changes to take effect!"
exit 0