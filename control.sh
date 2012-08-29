#!/bin/sh

case "$1" in
  off)
    pgrep -f linux-typewriter.py | xargs kill
    notify-send "Typewriter" "Keyboard sounds disabled"
    ;;
  on)
    "$(dirname "$0")/linux-typewriter.py" &
    notify-send "Typewriter" "Keyboard sounds enabled"
    ;;
  toggle)
    if pgrep -f linux-typewriter.py > /dev/null; then
      "$0" off
    else
      "$0" on
    fi
    ;;
  *)
    echo "Usage: $0 (on|off|toggle)"
    ;;
esac
