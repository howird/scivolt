# Search and Replace in Neovim

The general syntax is:

```vim
:[range]s/{pattern}/{replacement}/[flags]
```

Here's a breakdown of each part:

1.  **`:`** Enters Command-line mode.
2.  **`[range]`** (Optional): Specifies the lines where the substitution should occur. Common ranges include:
    * `%`: The entire file (equivalent to `1,$`). This is the most common range for global replacement.
    * `.`: The current line only (default if no range is specified).
    * `$` : The last line.
    * `'<,'>`: The visually selected lines (Vim automatically inserts this when you enter Command-line mode from Visual mode).
    * `10,20`: Lines 10 through 20, inclusive.
    * `.+5`: The current line and the next 5 lines.
    * `/pattern1/,/pattern2/`: Lines between the first occurrence of `pattern1` and the first subsequent occurrence of `pattern2`.
3.  **`s`**: The substitute command.
4.  **`/`**: Delimiter. While `/` is conventional, you can use other non-alphanumeric characters (like `#`, `|`, `_`) if your pattern or replacement contains slashes, avoiding excessive escaping. E.g., `:s#http://#https://#g`.
5.  **`{pattern}`**: The regular expression to search for. Vim uses its own flavor of regex. Key elements:
    * `.`: Matches any single character.
    * `*`: Matches zero or more of the preceding atom.
    * `\+`: Matches one or more of the preceding atom.
    * `\?`: Matches zero or one of the preceding atom.
    * `[]`: Character class (e.g., `[abc]`).
    * `\(\)`: Capturing group.
    * `^`: Start of line.
    * `$`: End of line.
    * `\<`: Start of word.
    * `\>`: End of word.
    * Use `\` to escape special characters (e.g., `\.` to match a literal dot).
6.  **`{replacement}`**: The string to replace the matched pattern with.
    * `&` or `\0`: Represents the entire matched pattern.
    * `\1`, `\2`, ...: Represents the text captured by the 1st, 2nd, ... capturing group `\(\)` in the pattern.
    * `\r`: Represents a newline character (for inserting line breaks).
    * `\t`: Represents a tab character.
    * Use `\` to escape special characters (e.g., `\\` for a literal backslash, `\/` for a literal slash if `/` is the delimiter).
7.  **`[flags]`** (Optional): Modify the behavior of the substitution. Common flags:
    * `g` (global): Replace *all* occurrences in each specified line. Without `g`, only the *first* occurrence on each line is replaced.
    * `c` (confirm): Prompt before each substitution. You can type `y` (yes), `n` (no), `a` (all remaining), `q` (quit), `l` (last - substitute this one and quit), `^E` (scroll up), `^Y` (scroll down).
    * `i` (ignore case): Perform case-insensitive matching for the pattern.
    * `I` (case sensitive): Perform case-sensitive matching (overrides the `'ignorecase'` setting if it's enabled).
    * `n` (count): Report the number of matches without actually performing the substitution. Useful for testing patterns.
    * `e` (error suppression): Suppress error messages if the pattern is not found.

**Examples:**

* Replace the first occurrence of `foo` with `bar` on the current line:
    ```vim
    :s/foo/bar/
    ```
* Replace all occurrences of `foo` with `bar` on the current line:
    ```vim
    :s/foo/bar/g
    ```
* Replace all occurrences of `foo` with `bar` in the entire file:
    ```vim
    :%s/foo/bar/g
    ```
* Replace all occurrences of `foo` with `bar` in the entire file, confirming each change:
    ```vim
    :%s/foo/bar/gc
    ```
* Replace all occurrences of `foo` (case-insensitive) with `bar` in the entire file:
    ```vim
    :%s/foo/bar/gi
    ```
* Replace `(width, height)` with `(height, width)` across the whole file:
    ```vim
    :%s/(\(.*\), \(.*\))/(\2, \1)/g
    ```
    * `\(.*\)`: Captures any sequence of characters into group 1 (`\1`) and group 2 (`\2`).
* Remove trailing whitespace from all lines:
    ```vim
    :%s/\s\+$//e
    ```
    * `\s\+`: Matches one or more whitespace characters.
    * `$`: Matches the end of the line.
    * Replace with nothing (`//`).
    * `e`: Suppress errors for lines without trailing whitespace.
* Use a different delimiter to replace a URL:
    ```vim
    :%s#http://example.com#https://example.com#g
    ```

This covers the fundamental usage. Vim's substitution capabilities are very powerful, allowing for complex pattern matching and replacements.