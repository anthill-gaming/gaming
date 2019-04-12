#!/usr/bin/env bash
# bash -c "$(curl -sL https://raw.githubusercontent.com/iepathos/reqs/master/download.sh)"

OS=${OSTYPE//[0-9.-]*/}
python="/usr/bin/env python3"

case "$OS" in
    darwin|linux)
        echo "Starting installation script...";;
    *)
        echo "Unknown operating system $OSTYPE"
        exit 1
esac

if [[ "$OS" == "darwin" ]]; then
    if [[ $EUID -eq 0 ]]; then
        echo "Do not run this script as root." 2>&1
        exit 1
    fi
fi

# General setup
source anthill/framework/setup.sh
source anthill/platform/setup.sh

# Services setup
source admin/setup.sh
source apigw/setup.sh
source backup/setup.sh
source bot/setup.sh
source config/setup.sh
source discovery/setup.sh
source dlc/setup.sh
source environment/setup.sh
source event/setup.sh
source exec/setup.sh
source game_controller/setup.sh
source game_master/setup.sh
source leaderboard/setup.sh
source log/setup.sh
source login/setup.sh
source media/setup.sh
source message/setup.sh
source moderation/setup.sh
source blog/setup.sh
source profile/setup.sh
source promo/setup.sh
source report/setup.sh
source social/setup.sh
source store/setup.sh

echo
echo "Updating geoip databases..."
eval ${python} "manage.py mmdb_update"

echo
echo "Installation completed."
