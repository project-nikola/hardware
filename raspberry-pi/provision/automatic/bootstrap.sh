#!/bin/bash
#
# Bootstrap the client/server.

setup_server_static_ip() {
  local ip_addr="$1"
  local ssh_alias="$2"

  local netmask=$(ssh "$ssh_alias" <<EOF | tail -n 1
sudo ifconfig wlan0 |
  sed -ne 's/^.*Mask://p'
EOF
)

  local network="$ip_addr"
  local broadcast=$(ssh "$ssh_alias" <<EOF | tail -n 1
sudo ifconfig wlan0 |
  sed -nr 's/^.*Bcast:(([0-9]{1,3}\.){3}[0-9]{1,3}).*$/\1/p'
EOF
)

  local gateway=$(ssh "$ssh_alias" /sbin/ip route | awk '/default/ { print $3 }')

  python networking.py "$ip_addr" "$netmask" "$network" "$broadcast" "$gateway" |
    ssh "$ssh_alias" 'sudo tee /etc/network/interfaces'
}

setup_client_ssh_config() {
  local user="$1"
  local ip_addr="$2"
  local host_name="$3"

  # Add to server authorized_keys
  ssh "$user"@"$ip_addr" 'mkdir -p .ssh'
  scp ~/.ssh/id_rsa.pub "$user@$ip_addr:.ssh/authorized_keys"

  # Add to client SSH config
  cat <<EOF >>~/.ssh/config

Host $host_name
  HostName $ip_addr
  User $user
  IdentityFile ~/.ssh/id_rsa
EOF
}

update_server_dev_tools() {
  local ssh_alias="$1"

  ssh "$ssh_alias" <<EOF
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install tmux -y
EOF
}

main() {
  if [[ "$#" -ne 3 ]]; then
      echo 'usage: ./bootstrap.sh PI_USER PI_IP SSH_ALIAS'
      exit 1
  fi

  setup_client_ssh_config "$1" "$2" "$3"
  setup_server_static_ip "$2" "$3"
  update_server_dev_tools "$3"
}

main "$@"
