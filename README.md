# Flat JSON Array for Directory Structure

The goal of this project is provide a flat array to nested, hierarchical directory strucures. This flat array will be saved in a file named `flat.json` as the root of the directory, to be used programmatically. This array will contain various informations on:

- the directory hierarchical structure
- directories and files properties
- other

Given the following directory structure:

```
├── dir1
│   ├── file1.txt
└── file3.txt
```

It will generate the following flat array as a JSON file:

```
[
    {
        "name": "dir1",
        "type": "directory",
        "path": "/"
    },
    {
        "name": "file1.txt",
        "type": "file",
        "path": "/dir1/"
    }, 
    {
        "name": "file3.txt",
        "type": "file",
        "path": "/"
    }
]
````

## Examples of use

- Provide access to a file system using a single index file
- Create index with custom attributes and access control


## How does it work?

It relies upon json file to configurate the programs, so you will find a Markdown file for each config files to better understand how to use this program. Those markdown files will be named the same way of the config files.

The json file created by this program is a list of dictionaries that can represent either a file or a directory.

## How to automatically generalte and deploy?

Automatic generation:

- Cron-based
- Webhooks
- Observing file changes

Automatic deploy:

- Webhooks that update and run

Error management:

## Error management

Errors may occur and are managed as follows

- Default value is provided in attributes
- 

## TODO

- Do more tests with asserts.
- Add more data when you do the flat at the file level.
- Be capable of managing well sub directories.

# Similar projets and alternatives

- 