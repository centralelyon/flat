# The directory.json file
This file is usefull to know at which depth the directory structure need to be flatened.
This json only have two possible fields and only one is mandatory.

Here is an example of this file : 
```json
{
    "directory":"competition_name/match_name/",
    "exclude": {
        "competition_name": [
            "test/*"
        ],
        "match_name": [
            "test/*",
            "test*",
            "testing.png"
        ]
    }
}
```

## Directory <- Mandatory
The directory is used to know the depth needed to be flatened.
To flatened only a directory composed of sub-directories of 1 depth, it needs only one name followed by a trailing slash.
So, `name/` for instance.

If you want to go to the file, which means to have a dictionary for each files, you need to add `file` at the end of the program.
So, `name/file` for instance.

If you want to go to the file for each files even in intermediate depth, you need to add `files` at the end of the program.
So, `dir_name/sub_dir_name/sub_sub_dir_name/files`.

**Attention :** In all cases, no files from the root folder will be read.

Now arose the question : what the sense of the generic name I put to my directory ?
The name used before each trailing slash will be the key containing the value of the directory.

## exclude <- optional
Used to know which files or directories to exclude, usefull if we have test files that you don't want to appear in our applications.
The key of the dictionary should be the names put, you can include only some.
The way the exclude function is the following : **Be aware** it is case insensitive.
- `name` : exclude all named files this way.
- `name.json` : exclude named file with this extension.
- `name/` : exclude named directories.
- `name*` : exclude all files starting with `name`.
- `name/*` : exclude all directories strating with `name.