# Flat JSON Array for Files and Directory Index

The goal of this project is provide a flat array that captures fiels and directories properties and structure. As those usually are hierarchical, the flat array provides a more usuable and readable way to filter, agregate and rank, while capturing the structure. This flat array will be saved in a file named `flat.json` at the root of the main directory. This array will contain various informations on:

- The directory hierarchical structure
- Directories and files properties
- Other meta-data

Given the following directory structure:

```
├── dir_1
│   ├── file_1.txt
└── file_2.txt
```

It will generate the following flat array as a JSON file:

```
[
    {
        "name": "dir_1",
        "type": "directory",
        "path": "/"
    },
    {
        "name": "file_1.txt",
        "type": "file",
        "path": "/dir_1/"
    }, 
    {
        "name": "file_2.txt",
        "type": "file",
        "path": "/"
    }
]
````

It is fully customizable and can be used to:

- Provide access to a file system using a single index file
- Create index with custom attributes and access control
- Keep files that are needed and ignore files like dot files (e.g. DS_Store)

## How does it work?

It relies upon json file to configurate the programs, so you will find a Markdown file for each config files to better understand how to use this program. Those markdown files will be named the same way of the config files.

The json file created by this program is a list of dictionaries that can represent either a file or a directory.

A set of rules enables:
- To calculate and store files attributes
- Capture the structure (depth, path)
- Extract meta-data from videos 

## Attributes types


### .txt

- Number of characters

## How to automatically generalte and deploy?

Automatic generation:

- Cron-based
- Webhooks
- Observing file changes

Automatic deploy:

- Webhooks that update and run the script

Error management:

- Default value if attribute cannot be calculated
- ..

## Similar projets and alternatives

- 

## TODO and Roadmap

- Do more tests with asserts.
- Add more data when you do the flat at the file level.
- Be capable of managing well sub directories.
- Write rules to ignore files.
- Support other languages (e.g. JavaScript).
- Optimize to only update the file that have changed.