#!/bin/bash

# Define variables
SCRIPT_PATH="/root/pos.py"
SERVICE_PATH="/etc/systemd/system/pos.service"

# Ensure the POS script exists
if [ ! -f "$SCRIPT_PATH" ]; then
    echo "Error: $SCRIPT_PATH not found!"
    exit 1
fi

# Create the systemd service
echo "Creating systemd service..."
cat <<EOF | sudo tee $SERVICE_PATH > /dev/null
[Unit]
Description=POS System
After=network.target

[Service]
ExecStart=/usr/bin/python3 $SCRIPT_PATH
WorkingDirectory=/root
StandardOutput=tty
StandardError=tty
Restart=always
User=root

[Install]
WantedBy=multi-user.target
EOF

# Reload systemd and enable the service
echo "Enabling and starting the POS service..."
sudo systemctl daemon-reload
sudo systemctl enable pos.service
sudo systemctl start pos.service

echo "Setup complete! The POS system will run on boot."
