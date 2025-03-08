# aliases.zsh - Command aliases

# Navigation options
setopt AUTO_CD              # Go to folder path without using cd.
setopt AUTO_PUSHD           # Push the old directory onto the stack on cd.
setopt PUSHD_IGNORE_DUPS    # Do not store duplicates in the stack.
setopt PUSHD_SILENT         # Do not print the directory stack after pushd or popd.
setopt CDABLE_VARS          # Change directory to a path stored in a variable.

# Basic aliases
alias cp="cp -i"                 # Confirm before overwriting something
alias df='df -h'                 # Human-readable sizes
alias free='free -m'             # Show sizes in MB

# ls and file listing
alias ls='eza --icons=always'
alias l='eza --icons=always -l -F -g'
alias ll='ls -lahF'
alias lls='ls -lahFtr'
alias la='ls -A'
alias lc='ls -CF'
alias tree="ls --tree"

# zoxide
alias zz='z -'

# git
alias lg="lazygit"
alias gitu='git add . && git commit && git push'
