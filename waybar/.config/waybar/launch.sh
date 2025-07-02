#!/bin/sh

killall waybar
waybar -c $HOME/hyprdots/waybar/config1.jsonc &
waybar -c $HOME/hyprdots/waybar/config2.jsonc
