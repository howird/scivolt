---
tags:
  - 'sw/tool'
  - 'guide'
---

# my vim cheatsheet
;
![vim graphical cheatsheet](vim.png)

## Text Editing

### Modes

- normal: `esc`
- visual: `v`
- visual line: `<shft> + v`
- commands: `:`

### Movements

- vertical:
    - `<count> + (h|j|k|l)`: up/down/left/right
    - `<ctrl> + u` / `<ctrl> + d`: Scroll up/down
    
- horizontal:
    - `^`: first non-blank character of the current line
    - `<count: optional> + _`: first non-blank character of the current line or a specified number of lines down
    - `$`: end of line

- `%`: match bracket

### Commands

- basic:
    - `y`: copy
    - `d`: delete

- compound:
    - `(d|y) + (i|a) + `:
-

### Special Commands

-

### Search

- `n` / `<shft> + n`: Search next/previous and keep text centered.

### Primeagen Mods
- Visual Mode `J`: Move selected text block down
- Visual Mode `K`: Move selected text block up
- Normal Mode `J`: Join lines but keep cursor in place
- Visual Mode `<leader> + p`: Paste while preserving the clipboard
- Normal/Visual Mode `<leader> + d`: Delete without affecting clipboard
- Normal/Visual Mode `<leader> + y`: Yank to system clipboard
- Normal Mode `<leader> + <shft> + y`: Yank entire line to system clipboard

### Clipboard & Deletion
- Visual Mode `<leader> + p`: Paste while preserving the clipboard (`[["_dP]]`).
- Normal/Visual Mode `<leader> + d`: Delete without affecting clipboard (`[["_d]]`).
- Normal/Visual Mode `<leader> + y`: Yank to system clipboard (`[["+y]]`).
- Normal Mode `<leader> + <shft> + y`: Yank entire line to system clipboard.

### Insert Mode
- Insert Mode `<ctrl> + c`: Exit insert mode (`<Esc>`).
- Normal Mode `Q`: Disable `Q` (no operation).

### Tmux Integration
- Normal Mode `<ctrl> + f`: Open new Tmux session (`tmux-sessionizer`).

## Window Navigation

- `<ctrl> + w`: is the main control (like `<ctrl> + b` for tmux)
    - `h|j|k|l`: moving cursor to another window
    - `s`: horizontal **s**plit
    - `v`: **v**ertical split
    - `p`: **p**revious window
    - `<shift> + (h|j|k|l)`: moving window location


## Project Navigation

- `<leader> + p + v`: Open the project view

- `p`: preview window
- `%`: create a file
- `R`: rename
- `d`: delete

- `mf`: Marks a file or directory
    - Any action that can be performed on multiple files depend on these marks. So if you want to copy, move or delete files, you need to mark them.
- `mt`: Assign the "target directory" used by the move and copy commands.
- `mc`: Copy the marked files in the target directory
- `mm`: Move the marked files to the target directory
- [source](https://vonheikemen.github.io/devlog/tools/using-netrw-vim-builtin-file-explorer/)

## Tools

### Code Formatting
- Normal Mode `<leader> + f`: Format code using LSP

### Quickfix List Navigation
- Normal Mode `<ctrl> + k`: Go to next item in quickfix list.
- Normal Mode `<ctrl> + j`: Go to previous item in quickfix list.
- Normal Mode `<leader> + k`: Go to next item in location list.
- Normal Mode `<leader> + j`: Go to previous item in location list.

### Search & Replace
- Normal Mode `<leader> + s`: Search and replace current word

### File Permissions
- Normal Mode `<leader> + x`: Make the current file executable

### Git Integration
- Normal Mode `<leader> + g + s`: Open Git interface

### Undo Tree
- Normal Mode `<leader> + u`: Toggle Undo Tree

### Telescope (Fuzzy Finder)
- Normal Mode `<leader> + p + f`: Find files using Telescope
- Normal Mode `<leader> + p + b`: List buffers using Telescope
- Normal Mode `<ctrl> + p`: Search Git-tracked files
- Normal Mode `<leader> + p + s`: Grep for string with input
- Normal Mode `<leader> + v + h`: Search help tags using Telescope

### Harpoon (Quick File Navigation)
- Normal Mode `<leader> + a`: Add current file to Harpoon
- Normal Mode `<ctrl> + e`: Open Harpoon quick menu
- Normal Mode `<ctrl> + (h|j|k|l)`: Navigate to Harpoon file 1/2/3/4

