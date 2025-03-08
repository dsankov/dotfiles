# completion.zsh - Completion system configuration

# Initialize the completion system
autoload -U compinit colors
compinit -d "$XDG_CACHE_HOME/zsh/zcompdump-$ZSH_VERSION"
colors

# Options
setopt CORRECT                  # Auto correct mistakes
setopt EXTENDEDGLOB             # Extended globbing. Allows using regular expressions with *
setopt NOCASEGLOB               # Case insensitive globbing
setopt RCEXPANDPARAM            # Array expansion with parameters
setopt NUMERICGLOBSORT          # Sort filenames numerically when it makes sense

# Completion styling
zstyle ':completion:*' matcher-list 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}' # Case insensitive tab completion
zstyle ':completion:*' menu select  # Highlight menu selection

# FZF Tab configuration
zstyle ':fzf-tab:complete:cd:*' fzf-preview 'ls --color $realpath'
zstyle ':fzf-tab:complete:__zoxide_z:*' fzf-preview 'ls --color $realpath'

# Speed up completions
zstyle ':completion:*' accept-exact '*(N)'
zstyle ':completion:*' use-cache on
zstyle ':completion:*' cache-path "$XDG_CACHE_HOME/zsh/zcompcache"
