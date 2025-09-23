

`rsync` is a powerful utility for synchronizing files and directories between two locations, either locally or over a network. It is efficient as it only transfers differences when files are updated.

Here's the command:

```bash
rsync -avzm --dry-run \
    --filter='+ */' \
    --filter='+ */shots_*/' \
    --filter='+ */shots_*/*.mp4' \
    --filter='- *.mp4' \
    --filter='- *' \
    "/home/user/sport-games/" "DEST_USER@DEST_HOST:/path/to/destination_directory/"
```

**Explanation of the command:**

  * `rsync`: The command itself.

  * `-a` (archive): This option is a shortcut for several other options (`-rlptgoD`). It ensures that symbolic links, permissions, timestamps, group, owner, and device files are preserved (where possible). It also implies recursive operation (`-r`).

  * `-v` (verbose): Increases the amount of information you are given during the transfer.

  * `-z` (compress): Compresses file data during the transfer, which can speed up transfers of compressible content over slower networks.

  * `-m` (prune-empty-dirs): This option tells `rsync` to remove empty directory chains from the sender's file list. This means if a directory becomes empty on the source side due to the filtering rules (e.g., a `<game name>/shots_XX/` directory contains no `.mp4` files or only files that are excluded), it won't be created on the destination.

  * `--dry-run` (or `-n`): This is crucial for testing. It makes `rsync` perform a trial run that doesn't make any actual changes but shows you what would be copied. **Remove this option or replace `-n` with the actual options like `-avzm` for the real transfer after verifying the output.**

  * `--filter='RULE'`: This option allows you to specify include/exclude rules. The rules are processed in order for each file and directory. The first rule that matches an item is applied.

      * `--filter='+ */'`: This rule includes all directories at the current level of recursion. For example, under `/home/user/sport-games/`, this includes `<game name>/` directories, allowing `rsync` to descend into them. The `+` means include, and `*/` matches directories.
      * `--filter='+ */shots_*/'`: This rule specifically includes directories whose names start with `shots_` and are located inside the first-level directories (i.e., `<game name>/shots_*/`). This ensures these directories themselves are considered for transfer and `rsync` can look inside them.
      * `--filter='+ */shots_*/*.mp4'`: This is the core inclusion rule for your files. It includes any file ending with `.mp4` that is located inside a `shots_*` directory, which itself is inside a `<game name>` directory.
      * `--filter='- *.mp4'`: This rule excludes any other `.mp4` file that was not explicitly included by the previous rule. This prevents copying `.mp4` files directly under `/home/user/sport-games/` or `/home/user/sport-games/<game name>/`. The `-` means exclude.
      * `--filter='- *'`: This rule excludes all other files and directories not explicitly included by the preceding rules. This is important to ensure only the desired files and their parent directory structure are copied.

  * `"/home/user/sport-games/"`: This is the source directory. The trailing slash (`/`) is important; it means "copy the contents of this directory".

  * `"DEST_USER@DEST_HOST:/path/to/destination_directory/"`: This is the destination.

      * `DEST_USER`: Your username on the remote machine.
      * `DEST_HOST`: The hostname or IP address of the remote machine.
      * `:/path/to/destination_directory/`: The absolute path on the remote machine where the files and their directory structure will be copied. For instance, if a file is `/home/user/sport-games/gameA/shots_01/video.mp4` on the source, it will be copied to `/path/to/destination_directory/gameA/shots_01/video.mp4` on the destination.

**Before running the actual command:**

1.  **Replace placeholders:** Update `DEST_USER`, `DEST_HOST`, and `/path/to/destination_directory/` with your actual remote user, host, and desired target directory.
2.  **Test with `--dry-run`:** Always run the command with the `--dry-run` (or `-n`) option first. This will show you a list of files that would be copied without actually transferring anything.
    ```bash
    rsync -avzmn \
        --filter='+ */' \
        --filter='+ */shots_*/' \
        --filter='+ */shots_*/*.mp4' \
        --filter='- *.mp4' \
        --filter='- *' \
        "/home/user/sport-games/" "DEST_USER@DEST_HOST:/path/to/destination_directory/"
    ```
3.  **Verify the output:** Check the list of files carefully to ensure only the intended files are selected and others are excluded.
4.  **Run the actual command:** If the dry run output is correct, remove `--dry-run` (or replace `-avzmn` with `-avzm`) to perform the actual copy:
    ```bash
    rsync -avzm \
        --filter='+ */' \
        --filter='+ */shots_*/' \
        --filter='+ */shots_*/*.mp4' \
        --filter='- *.mp4' \
        --filter='- *' \
        "/home/user/sport-games/" "DEST_USER@DEST_HOST:/path/to/destination_directory/"
    ```

**SSH Key Authentication:**
For frequent use or in scripts, it's recommended to set up SSH key-based authentication between your local machine and the remote host. This will allow `rsync` to connect without requiring a password each time.

This `rsync` command provides a robust way to achieve your specific file copying requirements while maintaining the desired directory structure and excluding unwanted files.