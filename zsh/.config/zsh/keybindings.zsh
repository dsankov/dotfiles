# # keybindings.zsh - Key bindings configuration
#
# bindkey -e  # Use emacs key bindings
#
# # Home/End keys
# # bindkey '^[[7~' beginning-of-line
# # bindkey '^[[H' beginning-of-line
# # bindkey '^[[8~' end-of-line
# # bindkey '^[[F' end-of-line
# if [[ "${terminfo[khome]}" != "" ]]; then
#   bindkey "${terminfo[khome]}" beginning-of-line
# fi
# if [[ "${terminfo[kend]}" != "" ]]; then
#   bindkey "${terminfo[kend]}" end-of-line
# fi
#
# # Insert/Delete keys
# bindkey '^[[2~' overwrite-mode
# bindkey '^[[3~' delete-char
# #
# # # Navigation keys
# # bindkey '^[[C'  forward-char
# # bindkey '^[[D'  backward-char
# # bindkey '^[[5~' history-beginning-search-backward
# # bindkey '^[[6~' history-beginning-search-forward
# #
# # Navigate words with ctrl+arrow keys
# bindkey '^[Oc' forward-word
# bindkey '^[Od' backward-word
# bindkey '^[[1;5D' backward-word
# bindkey '^[[1;5C' forward-word
# bindkey '^H' backward-kill-word  # delete previous word with ctrl+backspace
# bindkey '^[[Z' undo              # Shift+tab undo last action
#
# bindkey '^[[1;2D' backward-char
# bindkey '^[[1;2D' beginning-of-line     # Shift + Arrow Left
# bindkey '^[[1;2C' end-of-line           # Shift + Arrow Right
# # bindkey '^[[1;2A' beginning-of-buffer   # Shift + Arrow Up
# # bindkey '^
