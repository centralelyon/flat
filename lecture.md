# The lecture.json file
This file allows the program to know which files need to be put in the flat and how.
This file can be quite little with only few informations but you can add some layers to better access data.
First of all, I will present you only the mandatory fields then, the other fields that can help you to get visuals in your tools.

Let's start with an example of this file : 
```json
{
    "videos": {
        "type":"include",
        "extension": "mp4"
    },
    "beautiful_image": {
        "type":"list",
        "extension": "jpg|png"
    },
    "perspective": {
        "type": "important",
        "extension": "json"
    },
    "metadata": {
        "type": "string",
        "extension": "json"
    }
}
```
## the keys
The keys of this dictionary will be the keys of the dictionaries of the flat.json file.
Furthermore, these keys needs to be the end part of the files we want to include in the flat.json file.

Each of these keys need to be a dictionary.
**Be aware :** The keys are case sensitive !

## the extension fiels <- Mandatory
This key is here to determine which extensions need to be include.
**Be aware :** This field can not be empty, "" is not authorized.

If you want to include multiple extensions, just add a | between them without adding space. I doesn't work with the type string.

## the type field <- Mandatory
This key is here to determine what type of element will be the key in the flat.json file.
There is four different types : 
- include : create a list with all files with the extension of the extension field.
- list : list the name of all elements ending by `{your_name}.extension`.
- string : create a string of the unique element finishing by `{your_name}.extension`.
- important : create two different fields.
 - One named `all_{your_name}` with all the files ending by `{your_name}.extension`.
 - The second name `validate_{your_name}` with either the file named exactly `{your_name}.extension` or finishing by `__{your_name}.extension`. (doble underscore)