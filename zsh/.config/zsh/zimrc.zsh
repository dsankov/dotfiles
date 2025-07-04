#
# Modules
#

# Sets sane Zsh built-in environment options.
zmodule environment
# Applies correct bindkeys for input events.
zmodule input
# Utility aliases and functions. Adds colour to ls, grep and less.
zmodule utility

#
# Prompt
#

# Exposes to prompts how long the last command took to execute, used by asciiship.
zmodule duration-info
# Exposes git repository status information to prompts, used by asciiship.
# zmodule git-info
# A heavily reduced, ASCII-only version of the Spaceship and Starship prompts.
# zmodule bira

zmodule fzf
# zmodule direnv
zmodule romkatv/powerlevel10k --use degit

zmodule Aloxaf/fzf-tab
zmodule git
zmodule magic-enter
zmodule ohmyzsh/ohmyzsh --root plugins/sudo

#
# Completion
#

# Additional completion definitions for Zsh.
zmodule zsh-users/zsh-completions --fpath src
# Enables and configures smart and extensive tab completion.
# completion must be sourced after all modules that add completion definitions.
zmodule completion

#
# Modules that must be initialized last
#

# Fish-like syntax highlighting for Zsh.
# zsh-users/zsh-syntax-highlighting must be sourced after completion
zmodule zsh-users/zsh-syntax-highlighting
# Fish-like autosuggestions for Zsh.
zmodule zsh-users/zsh-autosuggestions
